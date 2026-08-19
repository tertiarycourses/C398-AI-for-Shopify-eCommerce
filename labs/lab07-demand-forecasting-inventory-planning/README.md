# Lab 7 — Demand Forecasting and Inventory Planning with AI

**Topic 02 — Applying AI to Retail Operations and Customer Experience**  |  **Duration:** 40 minutes  |  **Tools:** ChatGPT or Claude, a spreadsheet, labs/resources/sales_history_monthly.csv, labs/resources/products.csv

## Goal

Turn sales history into a demand forecast, reorder quantities and a slow-mover list.

A forecast is only useful when it ends in a buying decision. You will take two years of Bloom & Brew monthly sales, have AI identify trend and seasonality by category, forecast the next three months for the top SKUs, then convert that into reorder points with lead time and safety stock - and check one of them by hand before anyone raises a purchase order.

## What you'll build

A three-month demand forecast, reorder quantities with safety stock, and a slow-mover list ready for the buying meeting.

## Prerequisites

- labs/resources/sales_history_monthly.csv and products.csv downloaded
- A spreadsheet open for checking the arithmetic

**Starts from:** `labs/resources/sales_history_monthly.csv`

## Steps

1. **Open sales_history_monthly.csv and check what you have: 24 months of units by SKU, category and month.** Open sales_history_monthly.csv and get oriented before you prompt: which SKUs, which categories, which 24 months, and whether any SKU has gaps. A forecast built on a file you have not looked at is a guess with a table around it. Note the categories with obvious seasonality - coffee and home fragrance behave very differently through the year.

2. **Ask for the pattern first - trend, seasonality and anomalies by category - before asking for any forecast.** Ask for the pattern before the numbers. If the assistant describes a peak in November and December for gifting categories and a summer trough for hot drinks, it has read your data; if it describes a pattern that is not there, you have found that out before building a purchase order on top of it. The constraint about 24 months being short matters - two years gives you two observations of each season, which is enough to see a pattern and not enough to be certain of it.

```text
Role: you are a demand planner for Bloom & Brew.
Context: the attached sales_history_monthly.csv holds 24 months of unit sales by SKU, category and month.
Task: describe the demand pattern for each category - underlying trend, seasonal peaks and troughs, and any month that looks like an anomaly rather than a pattern.
Format: a table of category, trend direction, peak months, trough months, and a one-line note on anomalies.
Constraints: base every statement on the data in the file; state clearly where 24 months is too short to be confident.
```

3. **Forecast the next three months for the top ten SKUs by volume, with the method stated.** Now the forecast. Three requirements make it usable: the method stated in one line (so you can judge it), a low and high case (so the buyer sees the range, not a false-precision single number), and the exclusion of SKUs with too little history (so new products do not get a confident forecast built on three data points). Read the stated seasonal uplift and ask yourself whether you agree with it.

```text
Task: forecast units for the next three months for the ten highest-volume SKUs.
Format: a table of SKU, category, last three months actual, forecast for each of the next three months, and the method used in one line.
Constraints: state the seasonal uplift you applied and why; give a low and high case as well as the base case; do not forecast SKUs with fewer than six months of history - list those separately.
```

4. **Convert the forecast into a reorder decision using lead time and safety stock.** This is the step that turns analysis into a decision. Reorder point = expected demand over the lead time plus safety stock; order when stock on hand falls below it. Asking for a formula column is not a formality - it is how you find out that the assistant used 6 weeks as 1.5 months in one row and 2 months in another. Check that the lead-time demand column is consistent before you look at the order quantities.

```text
Task: convert the base-case forecast into a reorder plan.
Context: supplier lead time is 6 weeks; we hold 2 weeks of safety stock; current stock on hand is in products.csv.
Format: a table of SKU, forecast monthly demand, lead-time demand, safety stock, reorder point, stock on hand, and order now yes/no with the quantity.
Constraints: show the arithmetic for each reorder point in a formula column so I can check it.
```

5. **Find the cash problem at the other end: the slow movers and the overstocks.** Overstock is the expensive half of inventory planning and the half that gets ignored, because nothing goes wrong visibly. Months of cover and cash at cost are the two numbers that make it visible - a total at the bottom of that table is usually the most persuasive line in a buying meeting. Match each slow mover to an action rather than listing them: markdown, bundle with a fast seller, return to supplier, or discontinue.

```text
Task: list the SKUs where stock on hand exceeds six months of forecast demand, and the SKUs with no sales in the last three months.
Format: a table of SKU, category, stock on hand, months of cover, value at cost, and a recommended action - markdown, bundle, return to supplier or discontinue.
Constraints: use cost_price from products.csv for the value column; total the cash tied up at the bottom.
```

6. **Recompute one reorder point by hand in the spreadsheet before the plan goes anywhere near a supplier.** Take one SKU and recompute its reorder point in the spreadsheet from the raw numbers: monthly forecast divided by 4.33 to get a weekly rate, times 6 weeks of lead time, plus 2 weeks of safety stock. Compare with the assistant's figure. If they differ by more than rounding, the assumption it used was different from the one you stated - find it before the order goes out, because a wrong reorder point either runs you out of stock or ties up cash for a season.

## Test it

Recompute one reorder point by hand: (monthly forecast / 4.33) x 6 weeks lead time, plus 2 weeks of safety stock at the same weekly rate. The AI's number must match yours within rounding. If it does not, ask it to show the assumption it used for that row - the mismatch is always in the units, not the maths.

## Troubleshooting

| Symptom | Fix |
|---|---|
| The forecast ignores the seasonal peak you can see in the data. | It averaged across the year. Ask explicitly for a month-of-year seasonal index per category and for the forecast to apply it. |
| Reorder points look implausibly large. | Lead time was applied in months where the data is monthly and the lead time is in weeks. Restate both in the same unit and regenerate. |
| Different totals each time you ask. | Arithmetic over long tables is where models drift. Move the arithmetic into the spreadsheet and use the assistant for the method and the narrative. |

## Challenge

Re-run the reorder plan with the lead time increased from 6 to 10 weeks, and quantify how much extra stock the same service level now requires. That number is the cost of an unreliable supplier.

## Reflection

Where in this lab would a wrong AI number have cost you real money, and what check would catch it in your own buying process?

---

*AI for Retail · Course Code C398 · Tertiary Infotech Academy Pte Ltd (UEN 201200696W)*  
*© 2026 Tertiary Infotech Academy Pte Ltd. Version v1.0 · 17 August 2026.*
