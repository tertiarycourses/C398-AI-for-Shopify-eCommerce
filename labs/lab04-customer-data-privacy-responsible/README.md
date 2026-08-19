# Lab 4 — Customer Data Privacy and Responsible AI

**Topic 01 — Introduction to AI for Retail**  |  **Duration:** 45 minutes  |  **Tools:** ChatGPT or Claude, a spreadsheet, labs/resources/customers.csv, labs/resources/transactions.csv

## Goal

Anonymise retail customer data before AI use and set the store's responsible-AI rules.

Before AI touches customer data, someone has to decide what it may see. You will classify the columns in the Bloom & Brew customer and transaction files, build an anonymised extract that is safe to paste into a public AI tool, draft a one-page AI usage policy for the store team, then red-team that policy to find what it fails to cover.

## What you'll build

An anonymised data extract that is safe to use with a public AI tool, plus a one-page AI usage policy for your store team.

## Prerequisites

- Lab 1 complete - you have the five-part house prompt template
- customers.csv and transactions.csv open in a spreadsheet

**Starts from:** `labs/resources/customers.csv and labs/resources/transactions.csv`

## Steps

1. **Open customers.csv and transactions.csv and mark every column that could identify a real person.** Open both files and go through the headers column by column. Mark the obvious identifiers first - full_name, email, phone. Then look for the less obvious ones: a postal code plus a join date plus a loyalty tier can identify one person in a small customer base, and customer_id links a transaction row straight back to the named record. Re-identification is usually a combination problem, not a single-column problem.

2. **Ask the assistant to classify the columns - paste only the header row, never the customer data itself.** Send the classification prompt. Note what it contains: headers only, and an explicit statement that no data was pasted. That is the habit worth building - you can get useful advice about a dataset without exposing the dataset. Compare the assistant's classification with the marks you made in step 1, and pay attention to any column it flagged that you did not.

```text
Role: you are a data protection adviser to a retail business in Singapore.
Context: these are the column headers of two customer files. I have deliberately not pasted any data.
customers.csv: customer_id, full_name, email, phone, postal_code, join_date, loyalty_tier, marketing_optin
transactions.csv: order_id, order_date, customer_id, sku, qty, unit_price, channel, store
Task: classify every column as SAFE, IDENTIFYING or SENSITIVE for use with a public AI tool.
Format: a table of column, classification, one-line reason, and the action to take before any AI use.
Constraints: be conservative - if a column could re-identify someone in combination with another, say so.
```

3. **In the spreadsheet, build the anonymised extract: delete the identifying columns, renumber the customers and keep only the month.** Now do the work in the spreadsheet, not in the AI tool. Delete full_name, email and phone entirely. Replace customer_id with a plain running number (C001, C002, ...) in both files so the two still join but no longer point back to the source record. Truncate order_date and join_date to the month (2026-03 rather than 2026-03-14). Cut postal_code to its first two digits or delete it. Save the result as a new file - never overwrite the original - and use only that file for the rest of the day.

4. **Draft the store's one-page AI usage policy from your own classification work.** A policy that no one can follow protects nobody. Send the policy prompt and read the result as a shop-floor supervisor would: is each rule something you could check in ten seconds? The four sections matter more than the wording - what is banned outright, what needs anonymising first, what needs approval, and who to ask. Edit the draft to name real roles in your own business rather than generic ones.

```text
Role: you are writing an internal policy for a six-outlet specialty retailer.
Context: staff use public AI assistants for product copy, customer replies and sales analysis. The column classification above is our starting point.
Task: write a one-page AI usage policy the store team will actually follow.
Format: sections for (1) what may never be pasted into an AI tool, (2) what must be anonymised first, (3) which outputs need human approval before use, (4) who to ask when unsure. Bullet points, plain English, no legal jargon.
Constraints: maximum 400 words; every rule must be checkable by a shop-floor supervisor.
```

5. **Red-team the policy: ask the assistant to find the realistic ways a busy team would breach it.** Red-teaming your own policy is faster than waiting for the breach. The scenarios that come back are the realistic ones - a rushed reply pasted with the customer's full email still in it, a screenshot of a sales report with names visible, a supplier price list pasted into a public tool. Take the fixes that are small enough to survive contact with a busy Saturday and fold them into the policy.

```text
You are a sceptical store manager under time pressure.
Task: list the five most likely ways this policy gets broken in a real store on a busy Saturday, and the smallest change to the policy that would prevent each one.
Format: a table of scenario, why it happens, policy fix.
Constraints: realistic retail scenarios only - no hypothetical attackers.
```

6. **Add the human-in-the-loop rule: name who approves AI output before it reaches a customer, a price or an order.** Finish by writing the rule the AI cannot write for you: the named person or role who approves AI output before it reaches a customer, a price tag or a purchase order. Responsible AI in retail is not a technology control; it is an accountable human at the point where the output becomes a commitment to a customer.

## Test it

Search your anonymised extract for '@', for a phone-number pattern and for any full name from the original file. All three searches must return zero hits - that is what makes the extract safe to paste into a public AI tool. If anything is still found, your column list in step 3 was incomplete; fix it and search again.

## Troubleshooting

| Symptom | Fix |
|---|---|
| The two files no longer join after renumbering. | Renumber customer_id in customers.csv first, then use a lookup to apply the same new number to transactions.csv. Renumbering the files independently breaks the link. |
| The policy reads like a legal document. | Add 'written for a shop-floor supervisor, not a lawyer; maximum 12 words per rule' to the Constraints line and regenerate. |
| The assistant refuses to discuss the customer data at all. | You pasted actual rows. Start a new chat with headers only - the refusal is the guardrail working as intended. |

## Challenge

Take the anonymised extract and try to re-identify one customer using only the columns you kept, plus any public information. Whatever you manage tells you which column to remove next.

## Reflection

Which single column in these files would cause the most damage if it were pasted into a public AI tool, and what stops that happening in your store today?

---

*AI for Retail · Course Code C398 · Tertiary Infotech Academy Pte Ltd (UEN 201200696W)*  
*© 2026 Tertiary Infotech Academy Pte Ltd. Version v1.0 · 17 August 2026.*
