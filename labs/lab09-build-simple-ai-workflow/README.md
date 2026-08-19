# Lab 9 — Build a Simple AI Workflow for a Daily Retail Task

**Topic 02 — Applying AI to Retail Operations and Customer Experience**  |  **Duration:** 45 minutes  |  **Tools:** Google Sheets or Excel, ChatGPT or Claude, labs/resources/transactions.csv, labs/resources/customer_feedback.csv

## Goal

Build and document a repeatable no-code AI workflow with a human check for a daily retail task.

The last step is turning today's prompting into something that runs tomorrow without you. You will build a no-code daily workflow in a spreadsheet - trigger, data, AI step, output, human check - that produces the Bloom & Brew daily sales summary and drafts replies to overnight customer reviews, then document it as a one-page SOP and prove it repeats on a second day of data.

## What you'll build

A working no-code daily-summary workflow - trigger, data, AI step, output, human check - documented as a one-page SOP your team can run.

## Prerequisites

- Labs 5-8 complete - you have a grounded assistant and working analysis prompts
- A Google account for Google Sheets, or Excel

**Starts from:** `labs/resources/transactions.csv and labs/resources/customer_feedback.csv`

## Steps

1. **Define the workflow on paper first: trigger, data in, AI step, output, human check - five boxes, one line each.** Before touching a tool, write the five boxes down. Trigger: 9am each day. Data in: yesterday's transactions and overnight feedback. AI step: the fixed summary prompt. Output: the daily summary and draft replies. Human check: the duty manager approves before anything is sent. Every no-code AI workflow is these five boxes - a workflow that goes wrong is almost always missing the fifth.

2. **Set up the sheet: one tab for the day's transactions, one for overnight feedback, one for the output.** Create a spreadsheet with three tabs: Data (paste the day's transaction rows), Feedback (paste overnight reviews from customer_feedback.csv), and Output (where the finished summary is pasted back). Filter transactions.csv to a single day for the Data tab. The sheet is deliberately the simplest possible plumbing - the point of this lab is the repeatable pattern, not the tooling, and the same five boxes carry over to any automation platform you adopt later.

3. **Write the AI step as a fixed, reusable prompt with the day's data as the only thing that changes.** Write the AI step as a fixed prompt. The only thing that changes between runs is the pasted data - if the prompt itself changes daily, you have not built a workflow, you have just done the task again. Two constraints do the heavy lifting: 'NOT AVAILABLE' for anything not calculable stops invented numbers, and the ban on promising refunds keeps a draft reply from committing the store to something before a person has seen it.

```text
Role: you are the duty manager writing the Bloom & Brew daily trading summary.
Context: below are yesterday's transaction rows and yesterday's customer feedback. Nothing else.
Task: write the daily summary.
Format: (1) five bullets - revenue, units, best category, worst category, one thing that stands out; (2) any stock or service issue that needs attention today; (3) a draft reply to each piece of feedback rated 3 stars or below, maximum 60 words each, in our house tone.
Constraints: use only the rows below; if a number cannot be calculated from them, write NOT AVAILABLE; never promise a refund or a discount in a draft reply - offer to have a colleague make contact.
```

4. **Run the workflow end to end on one day of data and time how long it takes.** Run it: paste the day's rows and the feedback into the prompt, send it, paste the result into the Output tab. Time it. Compare that with how long the same summary takes by hand today. That number is what you take back to your manager, and it is also the honest test of whether the workflow is worth keeping.

5. **Add the human check that has to happen before anything is sent, and name who does it.** Write the human check into the sheet as a literal step with a name against it: who reads the summary, who approves each draft reply, and what they check (numbers against the Data tab, replies against store policy). An approval step that is not written down is not a control - it is a hope.

6. **Document the workflow as a one-page SOP so someone else can run it tomorrow.** Finally, have the assistant write the SOP, then read it as if you had never seen the workflow. Can a duty manager follow it on their first morning? Does it include the exact prompt to paste and what to do when the output looks wrong? Save the SOP with the sheet - the workflow that survives is the one someone else can run without you.

```text
Task: turn the workflow I have just built into a one-page standard operating procedure.
Format: purpose, when it runs, who runs it, the numbered steps with the exact prompt to paste, what to check before sending, and what to do when the output looks wrong.
Constraints: written for a duty manager who has never used AI before; maximum one page; no jargon.
```

## Test it

Run the whole workflow again on a SECOND day of data without changing a word of the prompt. If the output comes back in the same format, with the numbers matching what the Data tab shows and no invented figures, the workflow is repeatable and ready for your team. If you had to adjust the prompt to make day two work, it is still a manual task - fix the prompt, not the day.

## Troubleshooting

| Symptom | Fix |
|---|---|
| The summary invents a revenue figure. | It was asked to total more rows than it can handle reliably. Total revenue and units in the spreadsheet and paste those two figures in as context, leaving the AI to write the narrative. |
| Draft replies promise refunds despite the constraint. | Move that rule to its own line at the end of the prompt and make it explicit: 'Never state or imply a refund, discount or goodwill gesture.' Rules buried mid-paragraph get diluted. |
| Day two comes back in a different format. | The Format line is not specific enough. Include a short worked example of the exact output shape in the prompt itself. |

## Challenge

Extend the workflow with a weekly variant: same five boxes, seven days of data, and one extra section comparing this week with last. Note what you had to change - that is the difference between a task and a process.

## Reflection

How many minutes a day does this workflow save, and what is the one failure that would make you switch it off tomorrow?

---

*AI for Retail · Course Code C398 · Tertiary Infotech Academy Pte Ltd (UEN 201200696W)*  
*© 2026 Tertiary Infotech Academy Pte Ltd. Version v1.0 · 17 August 2026.*
