# Lab 3 — Campaign Copy and AI Product Visuals

**Topic 01 — Introduction to AI for Retail**  |  **Duration:** 45 minutes  |  **Tools:** ChatGPT or Claude, an image model (ChatGPT image generation, Gemini or Copilot Designer), labs/resources/products.csv

## Goal

Generate a complete promotional campaign and an AI product visual, then run a pre-publication check.

Build one seasonal promotion end to end. You will brief the campaign from the Bloom & Brew catalogue, generate email subject lines and body copy, three social captions and an in-store poster headline, then create a product visual with an image model and iterate it one variable at a time. The lab ends with the pre-publication check every AI-assisted campaign needs.

## What you'll build

A complete mini-campaign - email, three social captions, a poster headline and an AI-generated product visual - for one seasonal promotion.

## Prerequisites

- Lab 2 complete - you have on-brand product copy and the brand voice guide
- An assistant with image generation available

**Starts from:** `labs/resources/products.csv and the copy you produced in Lab 2`

## Steps

1. **Choose the promotion: pick one category from products.csv, set the offer and the dates, and name the audience.** Open products.csv and pick one category with enough SKUs to promote - the coffee or home fragrance ranges work well. Decide the offer (for example 20% off the range, or a bundle price), the exact start and end dates, and who it is aimed at (existing loyalty customers, lapsed customers, gift buyers). Write these four facts down before you prompt: a campaign brief with a vague offer produces assets that contradict each other.

2. **Brief the whole campaign in one prompt so every asset shares the same offer and voice.** Attach products.csv and brand_voice.md, then send the campaign prompt with your four facts filled in. Asking for the whole kit in one prompt is deliberate - subject lines, body, captions and poster generated together share one offer, one voice and one call to action. Generated separately, they drift, and you spend the saved time reconciling them.

```text
Role: you are a retail marketing lead for Bloom & Brew.
Context: promotion is <OFFER> on <CATEGORY>, running <START DATE> to <END DATE>, aimed at <AUDIENCE>. Product facts come from the attached products.csv; tone from brand_voice.md.
Task: produce the full campaign kit.
Format: (1) three email subject lines, each max 45 characters; (2) one email body of 120-150 words with a single call to action; (3) three social captions, each under 220 characters with two hashtags; (4) one in-store poster headline of no more than six words.
Constraints: state the offer and the end date in every asset; no superlatives; no claims outside products.csv; British English.
```

3. **Push the subject lines further by asking for distinct angles rather than more variants.** Three variants of the same idea are not three options. Asking for three distinct angles - urgency, benefit, curiosity - gives you something to actually choose between, and the bracketed character counts let you check the 45-character limit without counting by hand. Pick one and note why: that reasoning is what you reuse next campaign.

```text
Rewrite the three subject lines so each takes a DIFFERENT angle: one urgency, one benefit, one curiosity.
Keep each under 45 characters and include the character count in brackets after each line.
```

4. **Generate the product visual with an image prompt that names the subject, setting, light and framing.** Move to your image model (ChatGPT image generation, Gemini, or Copilot Designer). A usable image prompt names four things: subject, setting, light and framing. The constraints matter as much: 'no text' avoids the garbled lettering image models produce, 'no logos or brand marks' avoids generating someone else's trademark, and reserving negative space at the top means your headline has somewhere to sit.

```text
Create a photorealistic lifestyle image for a retail promotion.
Subject: a <PRODUCT> on a pale oak table, styled with a linen napkin and dried eucalyptus.
Setting: a bright Scandinavian-style cafe corner, soft morning light from the left, shallow depth of field.
Framing: 4:5 portrait, product in the lower third, clean negative space at the top for a headline.
Constraints: no text, no logos, no human faces, no brand marks on the product.
```

5. **Iterate the image by changing ONE variable at a time - light, angle, styling or crop - never all at once.** Change exactly one variable and regenerate. Then change one more. Iterating one variable at a time is what turns image generation from a slot machine into a controllable process - you learn which words move the result, and you can get back to a version you liked. Keep the prompt that produced your best image; it is a template for the next campaign, not a one-off.

```text
Keep everything the same, change only the light: warm late-afternoon light from the right instead of morning light from the left.
```

6. **Run the pre-publication check on the whole kit before anything goes live.** Paste the full kit back into the assistant and ask for the check as a fix list. Note what this prompt does NOT ask for: a rewrite. You want the issues surfaced so a person decides what to change. Pay particular attention to the fourth item - if the visual is AI-generated and shows a product a customer will receive, check your platform's and your market's disclosure expectations before publishing, and never present a generated image as a photograph of the actual item.

```text
Check this campaign kit and list every issue as a numbered fix list:
1. Any claim not supported by products.csv.
2. Any price, discount or date that is inconsistent between assets.
3. Any line that breaks brand_voice.md.
4. Anything that would need a disclosure because the image is AI-generated.
Return only the issues and the fix for each - do not rewrite the campaign.
```

## Test it

Read the campaign aloud as a customer would meet it: subject line, then email, then a social caption, then the poster. The offer, the discount and the end date must be identical in all four, and every product claim must trace to products.csv. One inconsistency between assets means the kit is not ready to schedule.

## Troubleshooting

| Symptom | Fix |
|---|---|
| The image has garbled text on the packaging. | Image models cannot spell reliably. Add 'no text, no labels, no packaging copy' to the constraints and add any wording afterwards in a design tool. |
| Every regeneration returns a completely different scene. | You changed more than one variable, or started a new chat. Iterate in the same conversation and change one element per request. |
| The captions repeat the email body word for word. | Add 'each asset must use different wording from the others; do not reuse sentences across assets' to the Constraints line. |

## Challenge

Produce a second version of the whole kit for a different audience - gift buyers instead of loyalty customers - reusing the same offer, then list what actually changed between the two versions.

## Reflection

Which asset needed the most human correction, and what does that tell you about where to keep a person in your campaign process?

---

*AI for Retail · Course Code C398 · Tertiary Infotech Academy Pte Ltd (UEN 201200696W)*  
*© 2026 Tertiary Infotech Academy Pte Ltd. Version v1.0 · 17 August 2026.*
