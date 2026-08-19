# Lab 2 — Generate a Product Catalogue with AI

**Topic 01 — Introduction to AI for Retail**  |  **Duration:** 25 minutes  |  **Tools:** ChatGPT or Claude, labs/resources/products.csv, labs/resources/brand_voice.md

## Goal

Produce on-brand product descriptions, feature bullets and SEO metadata from a product data file.

Turn a row of a spreadsheet into web-ready product content. You will ground the assistant in the Bloom & Brew catalogue and brand voice guide, generate descriptions, feature bullets and SEO metadata for five SKUs in a single pass, then fact-check every claim back to the source file and fix the tone in one correction prompt rather than by hand.

## What you'll build

Web-ready descriptions, feature bullets, SEO titles and meta descriptions for five SKUs, in brand voice, as a table you can paste into a product feed.

## Prerequisites

- Lab 1 complete - you have your five-part house prompt template
- labs/resources/products.csv and labs/resources/brand_voice.md downloaded

**Starts from:** `labs/resources/products.csv and labs/resources/brand_voice.md`

## Steps

1. **Open products.csv and brand_voice.md, and choose five SKUs from at least three different categories.** Open labs/resources/products.csv in a spreadsheet and labs/resources/brand_voice.md in a text editor or browser. Read the brand voice guide first - it is short, and it is the standard the output gets judged against. Pick five SKUs spread across at least three categories (for example one drinkware, one home fragrance, one coffee, one gift set, one homeware) so you can see whether the assistant holds the voice across different product types.

2. **Attach both files to a new chat so the assistant writes from your catalogue instead of from guesswork.** Start a new chat and attach both files (ChatGPT: the paperclip; Claude: the attachment button, or a Project with both files added). If your account cannot attach files, paste the five product rows and the full brand voice guide into the chat instead. This is grounding: the assistant now writes from your catalogue, and every claim it makes becomes checkable against a row you can point to.

3. **Ask for description, bullets and SEO metadata for all five SKUs in one table, in one pass.** Send the prompt with your five SKU codes filled in. Note the two things that make this a batch job rather than five separate ones: one table for all five SKUs, and a Format line precise enough that the columns come back ready to paste. The 'if a fact is missing write MISSING' constraint is the important one - it gives the model a legal way out, which is what stops it inventing a material or an origin to fill the gap.

```text
Role: you are a senior retail copywriter for Bloom & Brew.
Context: use the attached products.csv for the facts and brand_voice.md for the tone. Nothing else.
Task: write web copy for these five SKUs: <SKU1>, <SKU2>, <SKU3>, <SKU4>, <SKU5>.
Format: one markdown table. Columns: SKU | Description (55-65 words) | Five feature bullets | SEO title (max 60 characters) | Meta description (max 155 characters).
Constraints: British English; use only facts present in products.csv; no invented materials, origins or awards; no superlatives; if a fact is missing write MISSING.
```

4. **Fact-check every claim: read each description against the SKU's row and strike out anything the file does not support.** Now do the part that cannot be delegated. Take each description and read it against that SKU's row in products.csv. Every material, capacity, origin, certification and price claim must trace back to a column in the file. Strike out anything that does not - a 'hand-thrown in Portugal' that appears nowhere in the data is exactly the kind of claim that becomes a customer complaint. Count the hallucinations you find; that count is your reason for keeping a human check in the process.

5. **Correct the tone in one pass by naming what is wrong, instead of rewriting the copy yourself.** Rather than rewriting the weak rows yourself, tell the assistant precisely what is wrong and what to preserve. Naming the fault ('superlatives and exclamation marks', 'drifts from brand_voice.md') and fixing the scope ('only those two descriptions', 'keep the word count and metadata unchanged') is what makes a correction prompt cheap. Asking it to 'make it better' is what makes it expensive.

```text
Rows 2 and 4 drift from the brand voice guide: they use superlatives and exclamation marks.
Rewrite ONLY those two descriptions to match brand_voice.md. Keep the word count, the bullets and the metadata unchanged.
Return the corrected rows only, in the same table format.
```

6. **Paste the finished table into your product sheet, and save the prompt that produced it into your prompt library.** Copy the finished table into your product sheet or CMS export. Then save the prompt itself - with the placeholders back in - into the prompt library you started in Lab 1. Next month's catalogue update should be a paste and a fact-check, not a rewrite.

## Test it

Pick one finished description and trace every claim in it to a column in products.csv. If a claim has no column behind it, the copy is not publishable - delete or correct it, then add the missing rule to your Constraints line so the next batch does not repeat it. A clean pass means every sentence is supported by data.

## Troubleshooting

| Symptom | Fix |
|---|---|
| The assistant will not read the attached CSV. | Convert it to a plain table pasted directly into the chat, or upload as .txt. Very large files may also be truncated - send only the five rows you need. |
| SEO titles come back over 60 characters. | Ask it to count: 'Return the character count in brackets after each SEO title, and rewrite any that exceed the limit.' Models are poor at silent counting but reliable when made to show it. |
| Every description sounds the same. | Add a constraint: 'Do not reuse the opening construction between rows.' Batch prompts converge on one pattern unless told not to. |

## Challenge

Add a sixth column for a 25-word marketplace short description with a different character limit, and regenerate. Then ask for the same table translated for a second market, keeping the SEO titles in English.

## Reflection

How many claims did you have to strike out, and what does that number tell you about publishing AI product copy without a human check?

---

*AI for Retail · Course Code C398 · Tertiary Infotech Academy Pte Ltd (UEN 201200696W)*  
*© 2026 Tertiary Infotech Academy Pte Ltd. Version v1.0 · 17 August 2026.*
