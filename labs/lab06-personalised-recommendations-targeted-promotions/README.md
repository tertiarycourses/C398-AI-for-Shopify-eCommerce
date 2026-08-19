# Lab 6 — Personalised Recommendations and Targeted Promotions

**Topic 02 — Applying AI to Retail Operations and Customer Experience**  |  **Duration:** 35 minutes  |  **Tools:** ChatGPT or Claude, a spreadsheet, labs/resources/transactions.csv, labs/resources/products.csv

## Goal

Segment customers from transaction data and build targeted offers and next-best-product recommendations.

Personalisation starts with segmentation, not with a clever message. You will group the Bloom & Brew customers by how recently, how often and how much they buy, define four segments with a targeted offer and channel for each, then build next-best-product recommendations for three individual customers and check that the maths behind each offer still leaves a margin.

## What you'll build

Four customer segments with a targeted offer, channel and message for each, plus next-best-product recommendations for three named customers.

## Prerequisites

- Lab 4 complete - you are working from the anonymised extract, not the raw file
- labs/resources/products.csv for cost and retail prices

**Starts from:** `the anonymised transaction extract you built in Lab 4`

## Steps

1. **Use the anonymised extract from Lab 4, not the raw customer file - the same rule applies to your own store data.** Attach the anonymised extract you produced in Lab 4 - the version with no names, emails or phone numbers and with customer_ref in place of customer_id. Everything in this lab works exactly the same on anonymised data, which is the point: personalisation does not require handing a public AI tool your customer list.

2. **Ask for a recency, frequency and value summary per customer, and a proposed set of four segments.** Send the segmentation prompt. Recency, frequency and value is the workhorse segmentation in retail because all three come straight out of a transaction file. The critical constraint is the reproducibility one: if the assistant states each segment as an explicit rule ('last order within 3 months AND 3 or more orders'), you can rebuild the segments in a spreadsheet next month without asking it again.

```text
Role: you are a CRM analyst for Bloom & Brew.
Context: the attached file is an anonymised transaction extract. Columns: order_id, order_month, customer_ref, sku, qty, unit_price, channel, store.
Task: summarise each customer by recency (months since last order), frequency (orders in the period) and value (total spend), then propose four segments that cover every customer with no overlap.
Format: (1) a table of the four segments with their rule, customer count and share of total revenue; (2) the ten highest-value customers with their recency, frequency and value.
Constraints: state the exact rule for each segment so I can reproduce it in a spreadsheet; flag any customer the rules do not capture.
```

3. **Sanity-check the segments in the spreadsheet before you build offers on top of them.** Before you build campaigns on the segments, check them. In the spreadsheet, count how many customers fall into each segment using the stated rules and compare with the assistant's counts. Language models do arithmetic unreliably over long tables - the segmentation logic is usually sound, the counts are what drift. If the numbers do not match, trust your spreadsheet and tell the assistant the corrected counts.

4. **Design the offer, channel and message for each segment in one pass.** Now design the campaigns. The constraint that stops the most common personalisation mistake is 'do not discount to customers who are already buying at full price' - untargeted discounting spends margin on people who would have bought anyway. Different objectives per segment (reactivate, increase basket size, reward, win back) are what make this personalisation rather than a mailshot with four subject lines.

```text
Task: for each of the four segments, design the next campaign.
Format: a table with columns - segment, objective, offer, channel, subject line or opening line (max 45 characters), and the one metric that tells us it worked.
Constraints: a different objective per segment - do not discount to customers who are already buying at full price; every offer must name a product category that exists in products.csv.
```

5. **Build next-best-product recommendations for three individual customers from their own purchase history.** Pick three customer references from different segments and ask for two next-best products each. The 'reason a store colleague could say out loud' column is the useful one - it turns an algorithmic recommendation into something a person can use at the counter. The constraint that the customer must not already own the product catches the most obvious failure of naive recommendation logic.

```text
Task: for customer_ref <C0xx>, <C0yy> and <C0zz>, recommend the next TWO products each.
Format: a table of customer_ref, what they have bought, recommended SKU, and the one-sentence reason a store colleague could say out loud.
Constraints: recommend only SKUs in products.csv that the customer has not already bought; no recommendation may rely on a product attribute that is not in the file.
```

6. **Check the margin: price the deepest offer against cost in products.csv before anyone approves it.** Finally, price the deepest offer. Take the segment offer with the biggest discount, look up cost_price and retail_price for that category in products.csv, and work out the margin that survives the discount. If a 30% offer takes a 42% margin to 17%, that is a decision for a person with a budget, not something to approve because the AI suggested it. Recommendations are cheap; margin is not.

## Test it

Take one next-best-product recommendation and check it against that customer's own rows in the extract: the recommended SKU must be a product they have NOT bought, and the stated reason must match what they actually purchased. If the reason cites a purchase that is not in their history, the recommendation was invented - re-run it with the customer's rows pasted directly into the prompt.

## Troubleshooting

| Symptom | Fix |
|---|---|
| The segment customer counts do not add up to the total. | The rules overlap or leave gaps. Ask for mutually exclusive and collectively exhaustive rules, then re-check the counts in your spreadsheet. |
| The assistant recommends products the customer already owns. | Paste that customer's purchase rows directly into the prompt rather than relying on it to search the whole file, and repeat the exclusion constraint. |
| Total spend figures differ from your spreadsheet. | Recompute in the spreadsheet and use those numbers. Use the assistant for the segmentation logic, the spreadsheet for the arithmetic. |

## Challenge

Add a fifth segment for customers who buy only on promotion, and design a campaign whose objective is to move them to at least one full-price purchase. Then estimate what that segment currently costs in margin.

## Reflection

Which segment would you actually run first with a limited budget, and what number would tell you within two weeks whether it worked?

---

*AI for Retail · Course Code C398 · Tertiary Infotech Academy Pte Ltd (UEN 201200696W)*  
*© 2026 Tertiary Infotech Academy Pte Ltd. Version v1.0 · 17 August 2026.*
