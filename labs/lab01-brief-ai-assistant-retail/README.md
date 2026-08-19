# Lab 1 — Brief an AI Assistant Like a Retail Manager

**Topic 01 — Introduction to AI for Retail**  |  **Duration:** 20 minutes  |  **Tools:** ChatGPT, Claude, Microsoft Copilot or Google Gemini, labs/resources/products.csv

## Goal

Brief an AI assistant with the five-part prompt pattern and choose the right assistant for a retail task.

Three AI assistants, one retail brief. You will send a deliberately vague request, see what comes back, then rewrite it with the five-part pattern - role, context, task, format, constraints - and run the improved brief across ChatGPT, Claude and Copilot or Gemini. You finish with a house prompt template you will reuse in every later lab.

## What you'll build

A reusable five-part house prompt template, plus a scored comparison of three AI assistants on the same retail brief.

## Prerequisites

- A free ChatGPT account and a free Claude account
- Access to Microsoft Copilot or Google Gemini
- labs/resources/products.csv open in a spreadsheet

**Starts from:** `labs/resources/products.csv`

## Steps

1. **Open ChatGPT, Claude and either Microsoft Copilot or Google Gemini in three browser tabs and sign in to each.** Open ChatGPT (chatgpt.com), Claude (claude.ai) and either Microsoft Copilot (copilot.microsoft.com) or Google Gemini (gemini.google.com) in three separate browser tabs and sign in to each. Keep all three open for the whole lab - the point of this lab is the comparison, not any one answer. Free accounts are enough.

2. **Send this deliberately vague one-line brief to ChatGPT, and read the answer critically.** In ChatGPT, start a new chat and send the vague brief exactly as written. Read what comes back and note three things: the length is arbitrary, the tone is generic, and it has invented details - a colour, a material or an origin story that you never supplied. This is what a one-line prompt buys you, and it is why AI output has a reputation for needing a rewrite.

```text
Write a product description for a coffee mug.
```

3. **Rewrite the same request with the five-part pattern and send it again in a NEW chat.** Start a NEW chat - do not continue the previous one, or the vague answer will contaminate the next. Paste the five-part prompt. Each line does a specific job: Role sets the voice, Context supplies the only facts the model is allowed to use, Task states one instruction, Format fixes the shape of the answer, and Constraints rule out what you do not want. Compare this output against the first one - same model, same product, a different result.

```text
Role: you are a senior retail copywriter for Bloom & Brew, a specialty home, gift and coffee retailer.
Context: the product is SKU BB-DRK-014, a 350ml double-walled stoneware mug, matte glaze, dishwasher safe, retail SGD 32.
Task: write the web product description.
Format: 60 words of body copy, then exactly five feature bullets of no more than 8 words each.
Constraints: British English, warm but not cute, no superlatives, no claims that are not in the context above.
```

4. **Send that identical five-part prompt to Claude and to Copilot or Gemini, without changing a single word.** Copy the same five-part prompt into Claude and into Copilot or Gemini. Change nothing, not even the spacing: if you edit the prompt between assistants you are comparing prompts, not assistants. Line the three outputs up side by side in a document or a spreadsheet so you can read them together.

5. **Score the three outputs 1-5 on brand fit, factual accuracy, format compliance and how long you would spend editing.** Score each assistant 1-5 on four criteria and record the scores in a table: brand fit (does it sound like the store?), factual accuracy (did it stay inside the context you gave?), format compliance (60 words and exactly five bullets, or not?), and edit time (how many minutes to publish-ready?). Total the scores. The winner is the assistant you will reach for first in the labs after this one - and different assistants may well win for copy, for analysis and for spreadsheets.

6. **Save your five-part prompt as a house template with placeholders, ready to reuse for any product.** Replace the Bloom & Brew specifics with placeholders in angle brackets and save the result somewhere you will find it again - a note, a document, or a pinned chat. This template is your house prompt. Every later lab in this course starts from it, and every prompt you keep from today goes in the same place. A prompt library that you actually reuse is the single biggest time saver in this course.

```text
Role: you are a senior retail copywriter for <YOUR STORE NAME>, a <YOUR CATEGORY> retailer.
Context: the product is <SKU>, <KEY SPECS>, retail <PRICE>.
Task: <THE ONE THING YOU WANT DONE>.
Format: <EXACT SHAPE OF THE ANSWER - length, sections, table columns>.
Constraints: <BRAND VOICE>, no claims outside the context above, say so if information is missing.
```

## Test it

Open a fresh chat, paste your house template, and fill the placeholders with a DIFFERENT product from products.csv. The answer must come back in exactly the format you specified - the right length and the right number of bullets - with no correction needed from you. If you had to fix the shape of the answer, your Format and Constraints lines are still too loose: tighten them and run it again.

## Troubleshooting

| Symptom | Fix |
|---|---|
| The assistant still invents a material, colour or origin. | Your Constraints line is missing the hard rule. Add: 'Use only the facts in the Context above; if something is missing, write MISSING rather than inventing it.' |
| The output ignores the word count. | Word counts are approximate for language models. Ask for '55-65 words' rather than '60 words', and put the count in the Format line, not buried in the prose. |
| Copilot or Gemini answers in a different structure to the others. | That is a real finding, not a fault - record it in your scoring table. If you need identical structure, add an example of the exact output shape to the Format line. |

## Challenge

Run the same five-part prompt a fourth time with one line removed - drop Constraints, then drop Format - and record what breaks each time. You will be able to say precisely which line is doing which job.

## Reflection

Which of the five parts made the biggest difference to the output you got, and which retail task in your own store would benefit most from being briefed this way?

---

*AI for Retail · Course Code C398 · Tertiary Infotech Academy Pte Ltd (UEN 201200696W)*  
*© 2026 Tertiary Infotech Academy Pte Ltd. Version v1.0 · 17 August 2026.*
