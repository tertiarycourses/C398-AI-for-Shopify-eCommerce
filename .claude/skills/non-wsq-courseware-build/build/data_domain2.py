"""
Topic 2 - Applying AI to Retail Operations and Customer Experience. Labs 5-9.

Same field contract as data_domain1.py. Lab numbering continues contiguously
from Topic 1 (Labs 1-4), so the deck, Learner Guide, Lesson Plan and labs/
folder all agree on lab numbers.
"""

DOMAIN2 = [

 # ------------------------------------------------------------------ Lab 5
 dict(
  num=5, topic=2,
  title="Build a Grounded Store Service Assistant",
  objective="deploy an AI customer-service assistant grounded in your own policies, FAQ and product data",
  desc=("An assistant that has read your returns policy answers correctly; one that has not will invent a "
        "policy you then have to honour. You will build a Bloom & Brew service assistant grounded in the "
        "store policies, FAQ and product catalogue, give it tone and escalation rules, then test it against "
        "real customer enquiries - including one your policy does not cover."),
  build="A store customer-service assistant grounded in your own policies and FAQ, with a tested escalation rule for anything it cannot answer.",
  services="ChatGPT Projects or Custom GPTs, or Claude Projects; labs/resources/store_policies.md, faq.md, products.csv, customer_feedback.csv",
  duration=40,
  starts_from="labs/resources/store_policies.md, faq.md and products.csv",
  prereq=["Lab 4 complete - you know what data may and may not be used",
          "A ChatGPT or Claude account that supports Projects or Custom GPTs"],
  steps=[
   ("Create a new Project (Claude) or Custom GPT (ChatGPT) named 'Bloom & Brew Service Assistant'.",""),
   ("Add store_policies.md, faq.md and products.csv as the assistant's knowledge - this is what grounds it.",""),
   ("Write the system instructions: role, tone, the grounding rule and the escalation rule.",
    "You are the customer service assistant for Bloom & Brew, a specialty home, gift and coffee retailer with six outlets and an online store.\n"
    "Answer ONLY from the attached store policies, FAQ and product catalogue.\n"
    "If the answer is not in those documents, say: 'I'll pass this to a store colleague who can help' and state what information the colleague will need.\n"
    "Never invent a policy, a price, a delivery date or a stock level.\n"
    "Tone: warm, direct, British English, no more than 120 words per reply, no exclamation marks.\n"
    "Always end a reply about a return, refund or exchange with the exact policy line it is based on."),
   ("Test it on six real enquiries taken from customer_feedback.csv, one at a time.",
    "A customer bought the ceramic pour-over set 26 days ago, has the receipt, and wants to exchange it for a different colour. What do I tell them?"),
   ("Test the escalation path with a question your policy deliberately does not cover.",
    "A customer is asking whether you will price-match a competitor's website. What do I tell them?"),
   ("Tighten one weak answer by fixing the instructions, not by correcting the reply in the chat.",""),
  ],
  step_details=[
   ("In ChatGPT, go to Explore GPTs and create a new GPT (or start a new Project); in Claude, create a new Project. "
    "Name it 'Bloom & Brew Service Assistant'. The reason to use a Project or Custom GPT rather than a plain chat is "
    "persistence: the knowledge files and the instructions stay attached to every future conversation, so the assistant "
    "does not have to be re-briefed each morning."),
   ("Upload store_policies.md, faq.md and products.csv into the project knowledge. This is grounding, and it is the "
    "whole difference between an assistant that answers your returns policy and one that answers a generic returns "
    "policy it learned from the internet. Add nothing else - every extra document is another source it can quote at a "
    "customer, so keep the knowledge base small and authoritative."),
   ("Paste the instructions into the system prompt or project instructions field. Read the lines in order: the role "
    "sets who it is, the grounding rule restricts where answers come from, the escalation line gives it a scripted way "
    "to fail safely, the 'never invent' line closes the most expensive failure mode, and the tone rules keep replies "
    "usable without editing. The last line - quoting the policy line behind any returns answer - is what makes the "
    "assistant auditable when a customer disputes the outcome."),
   ("Open customer_feedback.csv and take six real enquiries from it - a returns question, a delivery question, a "
    "product-suitability question, a loyalty question, a complaint and an out-of-scope one. Send them one at a time in "
    "separate messages, as a customer would. Check each answer against store_policies.md yourself: the assistant "
    "quoting a policy line is only useful if the line it quoted is the right one."),
   ("Now send the question your policy does not answer. This is the most important test in the lab. A grounded "
    "assistant should say it cannot answer and hand over; an ungrounded one will confidently invent a price-match "
    "policy that your staff will then have to honour at the counter. If yours invents an answer, the grounding rule "
    "in your instructions is too weak - strengthen it and test again."),
   ("Pick the weakest of the seven answers and resist the urge to correct it in the chat. Fix the instructions instead: "
    "add the missing rule, tighten the tone line, or add the policy document it needed. Then re-run that same enquiry "
    "in a fresh conversation. Correcting a chat fixes one reply; correcting the instructions fixes every reply from "
    "now on."),
  ],
  test=("Ask the assistant a question your store policies genuinely do not cover - competitor price matching, or a "
        "return at 45 days. It must decline, use your escalation wording and state what the colleague will need. If it "
        "invents a policy instead, it is not ready to face a customer: strengthen the grounding rule and re-test."),
  troubleshooting=[
   ("The assistant answers from general knowledge instead of your files.",
    "Add 'If the documents do not contain the answer, do not use your own knowledge' as its own line, and confirm the files actually uploaded to the project knowledge."),
   ("Replies are far longer than 120 words.",
    "Put the length rule in its own line rather than in a sentence with other rules, and add 'Hard limit - do not exceed under any circumstances.'"),
   ("It quotes the wrong policy line.",
    "Your policy document has ambiguous headings. Add clear section headers to store_policies.md and re-upload - grounding quality is document quality."),
  ],
  challenge=("Add a second knowledge file containing your five most common complaint scenarios with the approved "
             "resolution for each, then re-test the complaint enquiry and compare the answer with the earlier one."),
  reflection=("What would it have cost your store if the ungrounded answer to the price-match question had been given "
              "to a real customer at the counter?"),
 ),

 # ------------------------------------------------------------------ Lab 6
 dict(
  num=6, topic=2,
  title="Personalised Recommendations and Targeted Promotions",
  objective="segment customers from transaction data and build targeted offers and next-best-product recommendations",
  desc=("Personalisation starts with segmentation, not with a clever message. You will group the Bloom & Brew "
        "customers by how recently, how often and how much they buy, define four segments with a targeted "
        "offer and channel for each, then build next-best-product recommendations for three individual "
        "customers and check that the maths behind each offer still leaves a margin."),
  build="Four customer segments with a targeted offer, channel and message for each, plus next-best-product recommendations for three named customers.",
  services="ChatGPT or Claude, a spreadsheet, labs/resources/transactions.csv, labs/resources/products.csv",
  duration=35,
  starts_from="the anonymised transaction extract you built in Lab 4",
  prereq=["Lab 4 complete - you are working from the anonymised extract, not the raw file",
          "labs/resources/products.csv for cost and retail prices"],
  steps=[
   ("Use the anonymised extract from Lab 4, not the raw customer file - the same rule applies to your own store data.",""),
   ("Ask for a recency, frequency and value summary per customer, and a proposed set of four segments.",
    "Role: you are a CRM analyst for Bloom & Brew.\n"
    "Context: the attached file is an anonymised transaction extract. Columns: order_id, order_month, customer_ref, sku, qty, unit_price, channel, store.\n"
    "Task: summarise each customer by recency (months since last order), frequency (orders in the period) and value (total spend), then propose four segments that cover every customer with no overlap.\n"
    "Format: (1) a table of the four segments with their rule, customer count and share of total revenue; (2) the ten highest-value customers with their recency, frequency and value.\n"
    "Constraints: state the exact rule for each segment so I can reproduce it in a spreadsheet; flag any customer the rules do not capture."),
   ("Sanity-check the segments in the spreadsheet before you build offers on top of them.",""),
   ("Design the offer, channel and message for each segment in one pass.",
    "Task: for each of the four segments, design the next campaign.\n"
    "Format: a table with columns - segment, objective, offer, channel, subject line or opening line (max 45 characters), and the one metric that tells us it worked.\n"
    "Constraints: a different objective per segment - do not discount to customers who are already buying at full price; every offer must name a product category that exists in products.csv."),
   ("Build next-best-product recommendations for three individual customers from their own purchase history.",
    "Task: for customer_ref <C0xx>, <C0yy> and <C0zz>, recommend the next TWO products each.\n"
    "Format: a table of customer_ref, what they have bought, recommended SKU, and the one-sentence reason a store colleague could say out loud.\n"
    "Constraints: recommend only SKUs in products.csv that the customer has not already bought; no recommendation may rely on a product attribute that is not in the file."),
   ("Check the margin: price the deepest offer against cost in products.csv before anyone approves it.",""),
  ],
  step_details=[
   ("Attach the anonymised extract you produced in Lab 4 - the version with no names, emails or phone numbers and with "
    "customer_ref in place of customer_id. Everything in this lab works exactly the same on anonymised data, which is "
    "the point: personalisation does not require handing a public AI tool your customer list."),
   ("Send the segmentation prompt. Recency, frequency and value is the workhorse segmentation in retail because all "
    "three come straight out of a transaction file. The critical constraint is the reproducibility one: if the "
    "assistant states each segment as an explicit rule ('last order within 3 months AND 3 or more orders'), you can "
    "rebuild the segments in a spreadsheet next month without asking it again."),
   ("Before you build campaigns on the segments, check them. In the spreadsheet, count how many customers fall into "
    "each segment using the stated rules and compare with the assistant's counts. Language models do arithmetic "
    "unreliably over long tables - the segmentation logic is usually sound, the counts are what drift. If the numbers "
    "do not match, trust your spreadsheet and tell the assistant the corrected counts."),
   ("Now design the campaigns. The constraint that stops the most common personalisation mistake is 'do not discount "
    "to customers who are already buying at full price' - untargeted discounting spends margin on people who would "
    "have bought anyway. Different objectives per segment (reactivate, increase basket size, reward, win back) are "
    "what make this personalisation rather than a mailshot with four subject lines."),
   ("Pick three customer references from different segments and ask for two next-best products each. The 'reason a "
    "store colleague could say out loud' column is the useful one - it turns an algorithmic recommendation into "
    "something a person can use at the counter. The constraint that the customer must not already own the product "
    "catches the most obvious failure of naive recommendation logic."),
   ("Finally, price the deepest offer. Take the segment offer with the biggest discount, look up cost_price and "
    "retail_price for that category in products.csv, and work out the margin that survives the discount. If a 30% "
    "offer takes a 42% margin to 17%, that is a decision for a person with a budget, not something to approve because "
    "the AI suggested it. Recommendations are cheap; margin is not."),
  ],
  test=("Take one next-best-product recommendation and check it against that customer's own rows in the extract: the "
        "recommended SKU must be a product they have NOT bought, and the stated reason must match what they actually "
        "purchased. If the reason cites a purchase that is not in their history, the recommendation was invented - "
        "re-run it with the customer's rows pasted directly into the prompt."),
  troubleshooting=[
   ("The segment customer counts do not add up to the total.",
    "The rules overlap or leave gaps. Ask for mutually exclusive and collectively exhaustive rules, then re-check the counts in your spreadsheet."),
   ("The assistant recommends products the customer already owns.",
    "Paste that customer's purchase rows directly into the prompt rather than relying on it to search the whole file, and repeat the exclusion constraint."),
   ("Total spend figures differ from your spreadsheet.",
    "Recompute in the spreadsheet and use those numbers. Use the assistant for the segmentation logic, the spreadsheet for the arithmetic."),
  ],
  challenge=("Add a fifth segment for customers who buy only on promotion, and design a campaign whose objective is to "
             "move them to at least one full-price purchase. Then estimate what that segment currently costs in margin."),
  reflection=("Which segment would you actually run first with a limited budget, and what number would tell you within "
              "two weeks whether it worked?"),
 ),

 # ------------------------------------------------------------------ Lab 7
 dict(
  num=7, topic=2,
  title="Demand Forecasting and Inventory Planning with AI",
  objective="turn sales history into a demand forecast, reorder quantities and a slow-mover list",
  desc=("A forecast is only useful when it ends in a buying decision. You will take two years of Bloom & Brew "
        "monthly sales, have AI identify trend and seasonality by category, forecast the next three months "
        "for the top SKUs, then convert that into reorder points with lead time and safety stock - and check "
        "one of them by hand before anyone raises a purchase order."),
  build="A three-month demand forecast, reorder quantities with safety stock, and a slow-mover list ready for the buying meeting.",
  services="ChatGPT or Claude, a spreadsheet, labs/resources/sales_history_monthly.csv, labs/resources/products.csv",
  duration=40,
  starts_from="labs/resources/sales_history_monthly.csv",
  prereq=["labs/resources/sales_history_monthly.csv and products.csv downloaded",
          "A spreadsheet open for checking the arithmetic"],
  steps=[
   ("Open sales_history_monthly.csv and check what you have: 24 months of units by SKU, category and month.",""),
   ("Ask for the pattern first - trend, seasonality and anomalies by category - before asking for any forecast.",
    "Role: you are a demand planner for Bloom & Brew.\n"
    "Context: the attached sales_history_monthly.csv holds 24 months of unit sales by SKU, category and month.\n"
    "Task: describe the demand pattern for each category - underlying trend, seasonal peaks and troughs, and any month that looks like an anomaly rather than a pattern.\n"
    "Format: a table of category, trend direction, peak months, trough months, and a one-line note on anomalies.\n"
    "Constraints: base every statement on the data in the file; state clearly where 24 months is too short to be confident."),
   ("Forecast the next three months for the top ten SKUs by volume, with the method stated.",
    "Task: forecast units for the next three months for the ten highest-volume SKUs.\n"
    "Format: a table of SKU, category, last three months actual, forecast for each of the next three months, and the method used in one line.\n"
    "Constraints: state the seasonal uplift you applied and why; give a low and high case as well as the base case; do not forecast SKUs with fewer than six months of history - list those separately."),
   ("Convert the forecast into a reorder decision using lead time and safety stock.",
    "Task: convert the base-case forecast into a reorder plan.\n"
    "Context: supplier lead time is 6 weeks; we hold 2 weeks of safety stock; current stock on hand is in products.csv.\n"
    "Format: a table of SKU, forecast monthly demand, lead-time demand, safety stock, reorder point, stock on hand, and order now yes/no with the quantity.\n"
    "Constraints: show the arithmetic for each reorder point in a formula column so I can check it."),
   ("Find the cash problem at the other end: the slow movers and the overstocks.",
    "Task: list the SKUs where stock on hand exceeds six months of forecast demand, and the SKUs with no sales in the last three months.\n"
    "Format: a table of SKU, category, stock on hand, months of cover, value at cost, and a recommended action - markdown, bundle, return to supplier or discontinue.\n"
    "Constraints: use cost_price from products.csv for the value column; total the cash tied up at the bottom."),
   ("Recompute one reorder point by hand in the spreadsheet before the plan goes anywhere near a supplier.",""),
  ],
  step_details=[
   ("Open sales_history_monthly.csv and get oriented before you prompt: which SKUs, which categories, which 24 months, "
    "and whether any SKU has gaps. A forecast built on a file you have not looked at is a guess with a table around "
    "it. Note the categories with obvious seasonality - coffee and home fragrance behave very differently through the "
    "year."),
   ("Ask for the pattern before the numbers. If the assistant describes a peak in November and December for gifting "
    "categories and a summer trough for hot drinks, it has read your data; if it describes a pattern that is not "
    "there, you have found that out before building a purchase order on top of it. The constraint about 24 months "
    "being short matters - two years gives you two observations of each season, which is enough to see a pattern and "
    "not enough to be certain of it."),
   ("Now the forecast. Three requirements make it usable: the method stated in one line (so you can judge it), a low "
    "and high case (so the buyer sees the range, not a false-precision single number), and the exclusion of SKUs with "
    "too little history (so new products do not get a confident forecast built on three data points). Read the stated "
    "seasonal uplift and ask yourself whether you agree with it."),
   ("This is the step that turns analysis into a decision. Reorder point = expected demand over the lead time plus "
    "safety stock; order when stock on hand falls below it. Asking for a formula column is not a formality - it is how "
    "you find out that the assistant used 6 weeks as 1.5 months in one row and 2 months in another. Check that the "
    "lead-time demand column is consistent before you look at the order quantities."),
   ("Overstock is the expensive half of inventory planning and the half that gets ignored, because nothing goes wrong "
    "visibly. Months of cover and cash at cost are the two numbers that make it visible - a total at the bottom of "
    "that table is usually the most persuasive line in a buying meeting. Match each slow mover to an action rather "
    "than listing them: markdown, bundle with a fast seller, return to supplier, or discontinue."),
   ("Take one SKU and recompute its reorder point in the spreadsheet from the raw numbers: monthly forecast divided by "
    "4.33 to get a weekly rate, times 6 weeks of lead time, plus 2 weeks of safety stock. Compare with the assistant's "
    "figure. If they differ by more than rounding, the assumption it used was different from the one you stated - find "
    "it before the order goes out, because a wrong reorder point either runs you out of stock or ties up cash for a "
    "season."),
  ],
  test=("Recompute one reorder point by hand: (monthly forecast / 4.33) x 6 weeks lead time, plus 2 weeks of safety "
        "stock at the same weekly rate. The AI's number must match yours within rounding. If it does not, ask it to "
        "show the assumption it used for that row - the mismatch is always in the units, not the maths."),
  troubleshooting=[
   ("The forecast ignores the seasonal peak you can see in the data.",
    "It averaged across the year. Ask explicitly for a month-of-year seasonal index per category and for the forecast to apply it."),
   ("Reorder points look implausibly large.",
    "Lead time was applied in months where the data is monthly and the lead time is in weeks. Restate both in the same unit and regenerate."),
   ("Different totals each time you ask.",
    "Arithmetic over long tables is where models drift. Move the arithmetic into the spreadsheet and use the assistant for the method and the narrative."),
  ],
  challenge=("Re-run the reorder plan with the lead time increased from 6 to 10 weeks, and quantify how much extra "
             "stock the same service level now requires. That number is the cost of an unreliable supplier."),
  reflection=("Where in this lab would a wrong AI number have cost you real money, and what check would catch it in "
              "your own buying process?"),
 ),

 # ------------------------------------------------------------------ Lab 8
 dict(
  num=8, topic=2,
  title="AI for Pricing, Merchandising and Sales Analytics",
  objective="analyse margin, model a markdown scenario and produce a KPI summary with recommended actions",
  desc=("The margin question a retailer actually asks is which products to mark down, which to leave alone, "
        "and what it costs. You will build a margin picture by SKU and category, identify markdown and "
        "price-increase candidates, model what a 15% markdown does to profit, then produce a one-page KPI "
        "summary with three recommended actions - verifying the headline number yourself."),
  build="A margin and markdown review with a modelled price scenario, and a one-page sales KPI summary with three recommended actions.",
  services="ChatGPT or Claude, a spreadsheet, labs/resources/products.csv, labs/resources/transactions.csv",
  duration=35,
  starts_from="labs/resources/products.csv and the anonymised transaction extract from Lab 4",
  prereq=["Lab 7 complete - you know which SKUs are slow movers",
          "products.csv (cost and retail price) and the anonymised transaction extract"],
  steps=[
   ("Attach products.csv and the anonymised transaction extract, and ask for the margin picture by SKU and category.",
    "Role: you are a category manager for Bloom & Brew.\n"
    "Context: products.csv holds cost_price, retail_price and stock_on_hand; the transaction extract holds units sold by SKU.\n"
    "Task: build the margin picture.\n"
    "Format: (1) a table by category of revenue, gross margin percent and gross margin value, sorted by margin value; (2) the ten SKUs contributing the most margin and the ten contributing the least.\n"
    "Constraints: gross margin percent = (retail_price - cost_price) / retail_price; show the formula you used for each aggregate; flag any SKU where cost exceeds retail."),
   ("Ask for markdown candidates and price-increase candidates, each with the reason from the data.",
    "Task: identify (a) five markdown candidates and (b) five price-increase candidates.\n"
    "Format: a table of SKU, category, current margin percent, units sold, months of cover, recommendation and the one-line reason from the data.\n"
    "Constraints: a markdown candidate must have both high cover and low velocity; a price-increase candidate must have strong velocity and below-category margin; do not recommend a price change on a SKU with fewer than 20 units sold."),
   ("Model the money: what a 15% markdown does to margin, and how many extra units it must sell to break even.",
    "Task: model a 15% markdown on the five markdown candidates.\n"
    "Format: a table of SKU, current price, marked-down price, current margin percent, new margin percent, margin value lost per unit, and the extra units needed to hold total margin flat.\n"
    "Constraints: state the break-even uplift as a percentage of current units; show the arithmetic; do not assume any demand elasticity you have not been given."),
   ("Write the category review narrative a merchant would actually read.",
    "Task: write the category review for the two largest categories by revenue.\n"
    "Format: for each category - what is working, what is not, the single biggest opportunity, and the risk if we do nothing. Maximum 120 words per category.\n"
    "Constraints: every claim must cite a number from the analysis above; no generic retail advice."),
   ("Produce the one-page KPI summary for management, ending in three actions with an owner and a date.",
    "Task: write a one-page sales KPI summary for the monthly management meeting.\n"
    "Format: (1) five headline KPIs with the number and the direction; (2) three recommended actions, each with the expected impact, a suggested owner role and a by-when; (3) one risk to flag.\n"
    "Constraints: maximum 350 words; plain English; no recommendation without a number behind it."),
   ("Verify the headline number yourself before the summary is circulated.",""),
  ],
  step_details=[
   ("Attach both files and send the margin prompt. The formula is stated in the prompt on purpose - margin can be "
    "calculated on cost or on retail, and the two give different answers, so fixing the definition up front prevents "
    "an argument later. Asking it to flag any SKU where cost exceeds retail catches data errors that would otherwise "
    "propagate through every table after this one."),
   ("Markdown and price-increase candidates are the same analysis in two directions, which is why they are asked for "
    "together. The constraints encode real merchandising judgement: a slow seller with plenty of stock is a markdown "
    "candidate, a fast seller earning below its category average is a price-increase candidate, and neither call "
    "should be made on a handful of units. Read the reasons, not just the SKU list - a reason you disagree with is "
    "how you find the assumption behind it."),
   ("This is the step that stops a markdown being approved on gut feel. The break-even uplift is the number that "
    "matters: if a 15% markdown needs 40% more units just to stand still, the question is whether that is realistic "
    "for this product. The constraint about elasticity is deliberate - the model has no data on how your customers "
    "respond to price, so any elasticity it volunteers is fabricated, and asking it not to invent one keeps the "
    "output honest."),
   ("Numbers do not persuade on their own. The category review turns the tables into something a merchant reads in "
    "two minutes: what is working, what is not, the opportunity and the risk of inaction. The 'every claim must cite "
    "a number' constraint is what keeps it from producing plausible retail advice that would be equally true of any "
    "store in any year."),
   ("The KPI summary is the artifact that leaves the room. Three parts make it actionable: headline KPIs with "
    "direction, three actions each with an impact, an owner role and a date, and one risk flagged. Actions without an "
    "owner and a date are observations. Edit the draft so the owner roles match real roles in your business."),
   ("Before circulating anything, verify the headline. Pick the single number the summary leads with - total gross "
    "margin, or the margin percentage for the biggest category - and recompute it in the spreadsheet from the source "
    "columns. Circulating an AI-generated number you have not checked is how a management meeting ends up making a "
    "decision on a hallucinated figure."),
  ],
  test=("Verify the gross margin the AI reports for one SKU: (retail_price - cost_price) / retail_price from "
        "products.csv, worked out in the spreadsheet. It must match to one decimal place. Then recompute the total "
        "margin value for the largest category the same way. If either differs, the aggregation is wrong and every "
        "table built on it needs re-running from the corrected figures."),
  troubleshooting=[
   ("Margin percentages look too high across the board.",
    "It calculated margin on cost (mark-up) rather than on retail. Restate the formula explicitly and regenerate the whole table."),
   ("The break-even uplift is missing or vague.",
    "Ask for it as a single percentage per SKU with the arithmetic shown - 'margin value lost per unit divided by new margin value per unit'."),
   ("Category totals do not match your spreadsheet.",
    "Aggregation over many rows is unreliable. Do the totals in the spreadsheet and give the assistant the corrected figures for the narrative."),
  ],
  challenge=("Model a 10% markdown alongside the 15% and compare the break-even uplift for each. Then decide which "
             "SKUs you would mark down at all, and write the one-line reason you would give your buyer."),
  reflection=("Which of the three recommended actions would you take to your management meeting tomorrow, and which "
              "number in it would you want to have checked twice?"),
 ),

 # ------------------------------------------------------------------ Lab 9
 dict(
  num=9, topic=2,
  title="Build a Simple AI Workflow for a Daily Retail Task",
  objective="build and document a repeatable no-code AI workflow with a human check for a daily retail task",
  desc=("The last step is turning today's prompting into something that runs tomorrow without you. You will "
        "build a no-code daily workflow in a spreadsheet - trigger, data, AI step, output, human check - that "
        "produces the Bloom & Brew daily sales summary and drafts replies to overnight customer reviews, then "
        "document it as a one-page SOP and prove it repeats on a second day of data."),
  build="A working no-code daily-summary workflow - trigger, data, AI step, output, human check - documented as a one-page SOP your team can run.",
  services="Google Sheets or Excel, ChatGPT or Claude, labs/resources/transactions.csv, labs/resources/customer_feedback.csv",
  duration=45,
  starts_from="labs/resources/transactions.csv and labs/resources/customer_feedback.csv",
  prereq=["Labs 5-8 complete - you have a grounded assistant and working analysis prompts",
          "A Google account for Google Sheets, or Excel"],
  steps=[
   ("Define the workflow on paper first: trigger, data in, AI step, output, human check - five boxes, one line each.",""),
   ("Set up the sheet: one tab for the day's transactions, one for overnight feedback, one for the output.",""),
   ("Write the AI step as a fixed, reusable prompt with the day's data as the only thing that changes.",
    "Role: you are the duty manager writing the Bloom & Brew daily trading summary.\n"
    "Context: below are yesterday's transaction rows and yesterday's customer feedback. Nothing else.\n"
    "Task: write the daily summary.\n"
    "Format: (1) five bullets - revenue, units, best category, worst category, one thing that stands out; (2) any stock or service issue that needs attention today; (3) a draft reply to each piece of feedback rated 3 stars or below, maximum 60 words each, in our house tone.\n"
    "Constraints: use only the rows below; if a number cannot be calculated from them, write NOT AVAILABLE; never promise a refund or a discount in a draft reply - offer to have a colleague make contact."),
   ("Run the workflow end to end on one day of data and time how long it takes.",""),
   ("Add the human check that has to happen before anything is sent, and name who does it.",""),
   ("Document the workflow as a one-page SOP so someone else can run it tomorrow.",
    "Task: turn the workflow I have just built into a one-page standard operating procedure.\n"
    "Format: purpose, when it runs, who runs it, the numbered steps with the exact prompt to paste, what to check before sending, and what to do when the output looks wrong.\n"
    "Constraints: written for a duty manager who has never used AI before; maximum one page; no jargon."),
  ],
  step_details=[
   ("Before touching a tool, write the five boxes down. Trigger: 9am each day. Data in: yesterday's transactions and "
    "overnight feedback. AI step: the fixed summary prompt. Output: the daily summary and draft replies. Human check: "
    "the duty manager approves before anything is sent. Every no-code AI workflow is these five boxes - a workflow "
    "that goes wrong is almost always missing the fifth."),
   ("Create a spreadsheet with three tabs: Data (paste the day's transaction rows), Feedback (paste overnight reviews "
    "from customer_feedback.csv), and Output (where the finished summary is pasted back). Filter transactions.csv to a "
    "single day for the Data tab. The sheet is deliberately the simplest possible plumbing - the point of this lab is "
    "the repeatable pattern, not the tooling, and the same five boxes carry over to any automation platform you adopt "
    "later."),
   ("Write the AI step as a fixed prompt. The only thing that changes between runs is the pasted data - if the prompt "
    "itself changes daily, you have not built a workflow, you have just done the task again. Two constraints do the "
    "heavy lifting: 'NOT AVAILABLE' for anything not calculable stops invented numbers, and the ban on promising "
    "refunds keeps a draft reply from committing the store to something before a person has seen it."),
   ("Run it: paste the day's rows and the feedback into the prompt, send it, paste the result into the Output tab. "
    "Time it. Compare that with how long the same summary takes by hand today. That number is what you take back to "
    "your manager, and it is also the honest test of whether the workflow is worth keeping."),
   ("Write the human check into the sheet as a literal step with a name against it: who reads the summary, who "
    "approves each draft reply, and what they check (numbers against the Data tab, replies against store policy). An "
    "approval step that is not written down is not a control - it is a hope."),
   ("Finally, have the assistant write the SOP, then read it as if you had never seen the workflow. Can a duty manager "
    "follow it on their first morning? Does it include the exact prompt to paste and what to do when the output looks "
    "wrong? Save the SOP with the sheet - the workflow that survives is the one someone else can run without you."),
  ],
  test=("Run the whole workflow again on a SECOND day of data without changing a word of the prompt. If the output "
        "comes back in the same format, with the numbers matching what the Data tab shows and no invented figures, the "
        "workflow is repeatable and ready for your team. If you had to adjust the prompt to make day two work, it is "
        "still a manual task - fix the prompt, not the day."),
  troubleshooting=[
   ("The summary invents a revenue figure.",
    "It was asked to total more rows than it can handle reliably. Total revenue and units in the spreadsheet and paste those two figures in as context, leaving the AI to write the narrative."),
   ("Draft replies promise refunds despite the constraint.",
    "Move that rule to its own line at the end of the prompt and make it explicit: 'Never state or imply a refund, discount or goodwill gesture.' Rules buried mid-paragraph get diluted."),
   ("Day two comes back in a different format.",
    "The Format line is not specific enough. Include a short worked example of the exact output shape in the prompt itself."),
  ],
  challenge=("Extend the workflow with a weekly variant: same five boxes, seven days of data, and one extra section "
             "comparing this week with last. Note what you had to change - that is the difference between a task and "
             "a process."),
  reflection=("How many minutes a day does this workflow save, and what is the one failure that would make you switch "
              "it off tomorrow?"),
 ),
]
