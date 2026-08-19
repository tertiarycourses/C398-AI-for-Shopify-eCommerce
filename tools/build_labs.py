#!/usr/bin/env python3
"""Generate labs/lab0N-<slug>/README.md and the labs/README.md index.

Driven by the SAME data_domainN.py files that build the slide deck, the Lesson
Plan and the Learner Guide, so the labs cannot drift from the other artifacts.
The `## Steps` section is written in the exact shape build_learner_guide.py
parses (`N. **instruction** <detail prose>` + a fenced prompt block), which is
what makes the Learner Guide the detailed mirror of these files.

Alignment is enforced mechanically: len(step_details) must equal len(steps) for
every lab, and lab numbers must be contiguous from 1.

Run:  python tools/build_labs.py
"""
import os, sys, glob, importlib, re

HERE  = os.path.dirname(os.path.abspath(__file__))
REPO  = os.path.dirname(HERE)
BUILD = os.path.join(REPO, ".claude", "skills", "non-wsq-courseware-build", "build")
sys.path.insert(0, BUILD)
import course_data as C

def load_domains():
    acts = []
    for f in sorted(glob.glob(os.path.join(BUILD, "data_domain[0-9]*.py")),
                    key=lambda q: int("".join(c for c in os.path.basename(q) if c.isdigit()) or 0)):
        n = "".join(c for c in os.path.basename(f) if c.isdigit())
        acts += getattr(importlib.import_module(os.path.basename(f)[:-3]), f"DOMAIN{n}", [])
    return acts

ACT    = load_domains()
TOPICS = {t["num"]: t for t in C.TOPICS}
LABDIR = os.path.join(REPO, "labs")

STOP = {"a","an","the","and","or","for","with","to","of","in","on","like","your","from","by"}
def slug(s):
    words = [w for w in re.sub(r"[^a-z0-9]+", " ", s.lower()).split() if w not in STOP]
    return "-".join(words[:4])

# ---- alignment guards: fail the build rather than ship misaligned labs -------
for i, a in enumerate(ACT, 1):
    if a["num"] != i:
        raise SystemExit(f"Lab numbering is not contiguous: expected {i}, got {a['num']}")
    if len(a.get("step_details", [])) != len(a["steps"]):
        raise SystemExit(f"Lab {a['num']}: {len(a['steps'])} steps but "
                         f"{len(a.get('step_details', []))} step_details - they must match")
    if a["topic"] not in TOPICS:
        raise SystemExit(f"Lab {a['num']}: topic {a['topic']} is not in course_data.TOPICS")

FOOT = (f"---\n\n*{C.TITLE} · Course Code {C.COURSE_CODE} · {C.ORG} "
        f"({C.UEN.replace('UEN: ', 'UEN ')})*  \n"
        f"*© 2026 Tertiary Infotech Academy Pte Ltd. Version {C.VERSION} · {C.VERSION_DATE}.*\n")

dirs = {}
for a in ACT:
    t = TOPICS[a["topic"]]
    d = os.path.join(LABDIR, f"lab{a['num']:02d}-{slug(a['title'])}")
    os.makedirs(d, exist_ok=True)
    dirs[a["num"]] = os.path.basename(d)

    L = []
    L.append(f"# Lab {a['num']} — {a['title']}\n")
    L.append(f"**Topic {t['code']} — {t['title']}**  |  **Duration:** {a['duration']} minutes  |  "
             f"**Tools:** {a['services']}\n")
    L.append("## Goal\n")
    L.append(f"{a['objective'][0].upper()}{a['objective'][1:]}.\n")
    L.append(f"{a['desc']}\n")
    L.append("## What you'll build\n")
    L.append(f"{a['build']}\n")
    L.append("## Prerequisites\n")
    for p in a["prereq"]:
        L.append(f"- {p}")
    L.append(f"\n**Starts from:** `{a['starts_from']}`\n")
    L.append("## Steps\n")
    for i, ((instr, cmd), detail) in enumerate(zip(a["steps"], a["step_details"]), 1):
        L.append(f"{i}. **{instr}** {detail}\n")
        if cmd:
            L.append("```text")
            L.append(cmd)
            L.append("```\n")
    L.append("## Test it\n")
    L.append(f"{a['test']}\n")
    L.append("## Troubleshooting\n")
    L.append("| Symptom | Fix |")
    L.append("|---|---|")
    for sym, fix in a["troubleshooting"]:
        L.append(f"| {sym} | {fix} |")
    L.append("")
    L.append("## Challenge\n")
    L.append(f"{a['challenge']}\n")
    L.append("## Reflection\n")
    L.append(f"{a['reflection']}\n")
    L.append(FOOT)
    with open(os.path.join(d, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print(f"  labs/{os.path.basename(d)}/README.md")

# ------------------------------------------------------------------ index
I = []
I.append(f"# {C.TITLE} — Hands-On Labs\n")
I.append(f"**Course Code:** {C.COURSE_CODE}  |  **{C.DAYS} day, {C.HOURS_PER_DAY:g} instructional hours**  |  "
         f"**{len(ACT)} labs**  |  **Version {C.VERSION}**\n")
I.append("All labs run on one connected scenario: **Bloom & Brew**, a fictional specialty home, gift and "
         "coffee retailer with six outlets and an online store. The synthetic data in "
         "[`resources/`](resources/) carries through the whole day, so each lab builds on the one before "
         "it. No programming is required — every lab is done in a browser with an AI assistant and a "
         "spreadsheet.\n")
I.append("## Labs\n")
I.append("| # | Lab | Topic | Minutes | Starts from |")
I.append("|---|---|---|---|---|")
for a in ACT:
    I.append(f"| {a['num']} | [{a['title']}]({dirs[a['num']]}/README.md) | {a['topic']} | "
             f"{a['duration']} | `{a['starts_from']}` |")
I.append("")
for t in C.TOPICS:
    labs = [a for a in ACT if a["topic"] == t["num"]]
    I.append(f"**Topic {t['code']} — {t['title']}:** Labs {labs[0]['num']}–{labs[-1]['num']} "
             f"({sum(a['duration'] for a in labs)} minutes)  ")
I.append("")
I.append("## Data files\n")
I.append("Everything in [`resources/`](resources/) is **synthetic** — generated by "
         "[`tools/make_sample_data.py`](../tools/make_sample_data.py) with a fixed seed, so every learner "
         "gets identical files and the verification steps always hold. There is no real customer, payment "
         "or employee data anywhere in this repository.\n")
I.append("| File | What it is | Used by |")
I.append("|---|---|---|")
I.append("| `products.csv` | 24 SKUs with material, size, origin, care, certification, cost, retail and stock | Labs 2, 3, 5, 6, 7, 8 |")
I.append("| `customers.csv` | 60 customers **with** names, emails and phone numbers | Lab 4 |")
I.append("| `transactions.csv` | 591 order lines over the last 6 months | Labs 4, 6, 8, 9 |")
I.append("| `sales_history_monthly.csv` | 24 months of unit sales by SKU and category | Lab 7 |")
I.append("| `customer_feedback.csv` | 30 enquiries, reviews and complaints | Labs 5, 9 |")
I.append("| `store_policies.md` | Returns, delivery, loyalty, care and privacy policy | Lab 5 |")
I.append("| `faq.md` | 20 customer FAQs, consistent with the policy | Lab 5 |")
I.append("| `brand_voice.md` | Tone of voice rules the copy is judged against | Labs 2, 3 |")
I.append("")
I.append("`transactions.csv` and `sales_history_monthly.csv` reconcile exactly over the last six months, "
         "so a number checked in one file can be verified against the other.\n")
I.append("## How to use a lab\n")
I.append("Each lab README carries the same structure: **Goal**, **What you'll build**, **Prerequisites**, "
         "numbered **Steps** with the exact prompt to paste, **Test it**, **Troubleshooting**, a "
         "**Challenge** for fast finishers and a **Reflection** question. Work through them in order. If "
         "you fall behind, every lab states the file it starts from, so you can rejoin at any lab.\n")
I.append("> **Note:** " + C.LAB_NOTE + "\n")
I.append(FOOT)
with open(os.path.join(LABDIR, "README.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(I))
print(f"  labs/README.md")
print(f"Generated {len(ACT)} labs, {sum(a['duration'] for a in ACT)} minutes of lab time")
