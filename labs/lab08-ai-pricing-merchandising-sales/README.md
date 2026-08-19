# Lab 8 — AI for Pricing, Merchandising and Sales Analytics

**Topic 02 — Applying AI to Retail Operations and Customer Experience**  |  **Duration:** 35 minutes  |  **Tools:** ChatGPT or Claude, a spreadsheet, labs/resources/products.csv, labs/resources/transactions.csv

## Goal

Analyse margin, model a markdown scenario and produce a KPI summary with recommended actions.

The margin question a retailer actually asks is which products to mark down, which to leave alone, and what it costs. You will build a margin picture by SKU and category, identify markdown and price-increase candidates, model what a 15% markdown does to profit, then produce a one-page KPI summary with three recommended actions - verifying the headline number yourself.

## What you'll build

A margin and markdown review with a modelled price scenario, and a one-page sales KPI summary with three recommended actions.

## Prerequisites

- Lab 7 complete - you know which SKUs are slow movers
- products.csv (cost and retail price) and the anonymised transaction extract

**Starts from:** `labs/resources/products.csv and the anonymised transaction extract from Lab 4`

## Steps

1. **Attach products.csv and the anonymised transaction extract, and ask for the margin picture by SKU and category.** Attach both files and send the margin prompt. The formula is stated in the prompt on purpose - margin can be calculated on cost or on retail, and the two give different answers, so fixing the definition up front prevents an argument later. Asking it to flag any SKU where cost exceeds retail catches data errors that would otherwise propagate through every table after this one.

```text
Role: you are a category manager for Bloom & Brew.
Context: products.csv holds cost_price, retail_price and stock_on_hand; the transaction extract holds units sold by SKU.
Task: build the margin picture.
Format: (1) a table by category of revenue, gross margin percent and gross margin value, sorted by margin value; (2) the ten SKUs contributing the most margin and the ten contributing the least.
Constraints: gross margin percent = (retail_price - cost_price) / retail_price; show the formula you used for each aggregate; flag any SKU where cost exceeds retail.
```

2. **Ask for markdown candidates and price-increase candidates, each with the reason from the data.** Markdown and price-increase candidates are the same analysis in two directions, which is why they are asked for together. The constraints encode real merchandising judgement: a slow seller with plenty of stock is a markdown candidate, a fast seller earning below its category average is a price-increase candidate, and neither call should be made on a handful of units. Read the reasons, not just the SKU list - a reason you disagree with is how you find the assumption behind it.

```text
Task: identify (a) five markdown candidates and (b) five price-increase candidates.
Format: a table of SKU, category, current margin percent, units sold, months of cover, recommendation and the one-line reason from the data.
Constraints: a markdown candidate must have both high cover and low velocity; a price-increase candidate must have strong velocity and below-category margin; do not recommend a price change on a SKU with fewer than 20 units sold.
```

3. **Model the money: what a 15% markdown does to margin, and how many extra units it must sell to break even.** This is the step that stops a markdown being approved on gut feel. The break-even uplift is the number that matters: if a 15% markdown needs 40% more units just to stand still, the question is whether that is realistic for this product. The constraint about elasticity is deliberate - the model has no data on how your customers respond to price, so any elasticity it volunteers is fabricated, and asking it not to invent one keeps the output honest.

```text
Task: model a 15% markdown on the five markdown candidates.
Format: a table of SKU, current price, marked-down price, current margin percent, new margin percent, margin value lost per unit, and the extra units needed to hold total margin flat.
Constraints: state the break-even uplift as a percentage of current units; show the arithmetic; do not assume any demand elasticity you have not been given.
```

4. **Write the category review narrative a merchant would actually read.** Numbers do not persuade on their own. The category review turns the tables into something a merchant reads in two minutes: what is working, what is not, the opportunity and the risk of inaction. The 'every claim must cite a number' constraint is what keeps it from producing plausible retail advice that would be equally true of any store in any year.

```text
Task: write the category review for the two largest categories by revenue.
Format: for each category - what is working, what is not, the single biggest opportunity, and the risk if we do nothing. Maximum 120 words per category.
Constraints: every claim must cite a number from the analysis above; no generic retail advice.
```

5. **Produce the one-page KPI summary for management, ending in three actions with an owner and a date.** The KPI summary is the artifact that leaves the room. Three parts make it actionable: headline KPIs with direction, three actions each with an impact, an owner role and a date, and one risk flagged. Actions without an owner and a date are observations. Edit the draft so the owner roles match real roles in your business.

```text
Task: write a one-page sales KPI summary for the monthly management meeting.
Format: (1) five headline KPIs with the number and the direction; (2) three recommended actions, each with the expected impact, a suggested owner role and a by-when; (3) one risk to flag.
Constraints: maximum 350 words; plain English; no recommendation without a number behind it.
```

6. **Verify the headline number yourself before the summary is circulated.** Before circulating anything, verify the headline. Pick the single number the summary leads with - total gross margin, or the margin percentage for the biggest category - and recompute it in the spreadsheet from the source columns. Circulating an AI-generated number you have not checked is how a management meeting ends up making a decision on a hallucinated figure.

## Test it

Verify the gross margin the AI reports for one SKU: (retail_price - cost_price) / retail_price from products.csv, worked out in the spreadsheet. It must match to one decimal place. Then recompute the total margin value for the largest category the same way. If either differs, the aggregation is wrong and every table built on it needs re-running from the corrected figures.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Margin percentages look too high across the board. | It calculated margin on cost (mark-up) rather than on retail. Restate the formula explicitly and regenerate the whole table. |
| The break-even uplift is missing or vague. | Ask for it as a single percentage per SKU with the arithmetic shown - 'margin value lost per unit divided by new margin value per unit'. |
| Category totals do not match your spreadsheet. | Aggregation over many rows is unreliable. Do the totals in the spreadsheet and give the assistant the corrected figures for the narrative. |

## Challenge

Model a 10% markdown alongside the 15% and compare the break-even uplift for each. Then decide which SKUs you would mark down at all, and write the one-line reason you would give your buyer.

## Reflection

Which of the three recommended actions would you take to your management meeting tomorrow, and which number in it would you want to have checked twice?

---

*AI for Retail · Course Code C398 · Tertiary Infotech Academy Pte Ltd (UEN 201200696W)*  
*© 2026 Tertiary Infotech Academy Pte Ltd. Version v1.0 · 17 August 2026.*
