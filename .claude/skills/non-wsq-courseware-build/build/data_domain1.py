"""
Topic 1 - Introduction to AI for Retail. Labs 1-4.

Single source for these labs: the slide deck, the Learner Guide, the Lesson Plan
schedule and the labs/lab0N-*/README.md files are ALL generated from this list,
so they cannot drift apart.

Field contract (the engine reads the first nine; build_labs.py reads the rest):
  num, topic, title, objective, desc, build, services, steps, test
  duration        - minutes, must add up to the lab blocks in course_data.SCHEDULE
  starts_from     - the file/artifact this lab begins with, so a learner can rejoin
  prereq          - list of prerequisites (earlier labs, accounts, files)
  step_details    - one expanded paragraph per step, SAME length as steps
  troubleshooting - list of (symptom, fix)
  challenge       - independent extension for fast finishers
  reflection      - one question tying the lab back to its learning outcome
"""

DOMAIN1 = [

 # ------------------------------------------------------------------ Lab 1
 dict(
  num=1, topic=1,
  title="Brief an AI Assistant Like a Retail Manager",
  objective="brief an AI assistant with the five-part prompt pattern and choose the right assistant for a retail task",
  desc=("Three AI assistants, one retail brief. You will send a deliberately vague request, see what comes "
        "back, then rewrite it with the five-part pattern - role, context, task, format, constraints - and "
        "run the improved brief across ChatGPT, Claude and Copilot or Gemini. You finish with a house prompt "
        "template you will reuse in every later lab."),
  build="A reusable five-part house prompt template, plus a scored comparison of three AI assistants on the same retail brief.",
  services="ChatGPT, Claude, Microsoft Copilot or Google Gemini, labs/resources/products.csv",
  duration=20,
  starts_from="labs/resources/products.csv",
  prereq=["A free ChatGPT account and a free Claude account",
          "Access to Microsoft Copilot or Google Gemini",
          "labs/resources/products.csv open in a spreadsheet"],
  steps=[
   ("Open ChatGPT, Claude and either Microsoft Copilot or Google Gemini in three browser tabs and sign in to each.",""),
   ("Send this deliberately vague one-line brief to ChatGPT, and read the answer critically.",
    "Write a product description for a coffee mug."),
   ("Rewrite the same request with the five-part pattern and send it again in a NEW chat.",
    "Role: you are a senior retail copywriter for Bloom & Brew, a specialty home, gift and coffee retailer.\n"
    "Context: the product is SKU BB-DRK-014, a 350ml double-walled stoneware mug, matte glaze, dishwasher safe, retail SGD 32.\n"
    "Task: write the web product description.\n"
    "Format: 60 words of body copy, then exactly five feature bullets of no more than 8 words each.\n"
    "Constraints: British English, warm but not cute, no superlatives, no claims that are not in the context above."),
   ("Send that identical five-part prompt to Claude and to Copilot or Gemini, without changing a single word.",""),
   ("Score the three outputs 1-5 on brand fit, factual accuracy, format compliance and how long you would spend editing.",""),
   ("Save your five-part prompt as a house template with placeholders, ready to reuse for any product.",
    "Role: you are a senior retail copywriter for <YOUR STORE NAME>, a <YOUR CATEGORY> retailer.\n"
    "Context: the product is <SKU>, <KEY SPECS>, retail <PRICE>.\n"
    "Task: <THE ONE THING YOU WANT DONE>.\n"
    "Format: <EXACT SHAPE OF THE ANSWER - length, sections, table columns>.\n"
    "Constraints: <BRAND VOICE>, no claims outside the context above, say so if information is missing."),
  ],
  step_details=[
   ("Open ChatGPT (chatgpt.com), Claude (claude.ai) and either Microsoft Copilot (copilot.microsoft.com) or "
    "Google Gemini (gemini.google.com) in three separate browser tabs and sign in to each. Keep all three open "
    "for the whole lab - the point of this lab is the comparison, not any one answer. Free accounts are enough."),
   ("In ChatGPT, start a new chat and send the vague brief exactly as written. Read what comes back and note three "
    "things: the length is arbitrary, the tone is generic, and it has invented details - a colour, a material or "
    "an origin story that you never supplied. This is what a one-line prompt buys you, and it is why AI output has "
    "a reputation for needing a rewrite."),
   ("Start a NEW chat - do not continue the previous one, or the vague answer will contaminate the next. Paste the "
    "five-part prompt. Each line does a specific job: Role sets the voice, Context supplies the only facts the model "
    "is allowed to use, Task states one instruction, Format fixes the shape of the answer, and Constraints rule out "
    "what you do not want. Compare this output against the first one - same model, same product, a different result."),
   ("Copy the same five-part prompt into Claude and into Copilot or Gemini. Change nothing, not even the spacing: if "
    "you edit the prompt between assistants you are comparing prompts, not assistants. Line the three outputs up "
    "side by side in a document or a spreadsheet so you can read them together."),
   ("Score each assistant 1-5 on four criteria and record the scores in a table: brand fit (does it sound like the "
    "store?), factual accuracy (did it stay inside the context you gave?), format compliance (60 words and exactly "
    "five bullets, or not?), and edit time (how many minutes to publish-ready?). Total the scores. The winner is "
    "the assistant you will reach for first in the labs after this one - and different assistants may well win for "
    "copy, for analysis and for spreadsheets."),
   ("Replace the Bloom & Brew specifics with placeholders in angle brackets and save the result somewhere you will "
    "find it again - a note, a document, or a pinned chat. This template is your house prompt. Every later lab in "
    "this course starts from it, and every prompt you keep from today goes in the same place. A prompt library that "
    "you actually reuse is the single biggest time saver in this course."),
  ],
  test=("Open a fresh chat, paste your house template, and fill the placeholders with a DIFFERENT product from "
        "products.csv. The answer must come back in exactly the format you specified - the right length and the "
        "right number of bullets - with no correction needed from you. If you had to fix the shape of the answer, "
        "your Format and Constraints lines are still too loose: tighten them and run it again."),
  troubleshooting=[
   ("The assistant still invents a material, colour or origin.",
    "Your Constraints line is missing the hard rule. Add: 'Use only the facts in the Context above; if something is missing, write MISSING rather than inventing it.'"),
   ("The output ignores the word count.",
    "Word counts are approximate for language models. Ask for '55-65 words' rather than '60 words', and put the count in the Format line, not buried in the prose."),
   ("Copilot or Gemini answers in a different structure to the others.",
    "That is a real finding, not a fault - record it in your scoring table. If you need identical structure, add an example of the exact output shape to the Format line."),
  ],
  challenge=("Run the same five-part prompt a fourth time with one line removed - drop Constraints, then drop Format - "
             "and record what breaks each time. You will be able to say precisely which line is doing which job."),
  reflection=("Which of the five parts made the biggest difference to the output you got, and which retail task in your "
              "own store would benefit most from being briefed this way?"),
 ),

 # ------------------------------------------------------------------ Lab 2
 dict(
  num=2, topic=1,
  title="Generate a Product Catalogue with AI",
  objective="produce on-brand product descriptions, feature bullets and SEO metadata from a product data file",
  desc=("Turn a row of a spreadsheet into web-ready product content. You will ground the assistant in the "
        "Bloom & Brew catalogue and brand voice guide, generate descriptions, feature bullets and SEO "
        "metadata for five SKUs in a single pass, then fact-check every claim back to the source file and "
        "fix the tone in one correction prompt rather than by hand."),
  build="Web-ready descriptions, feature bullets, SEO titles and meta descriptions for five SKUs, in brand voice, as a table you can paste into a product feed.",
  services="ChatGPT or Claude, labs/resources/products.csv, labs/resources/brand_voice.md",
  duration=25,
  starts_from="labs/resources/products.csv and labs/resources/brand_voice.md",
  prereq=["Lab 1 complete - you have your five-part house prompt template",
          "labs/resources/products.csv and labs/resources/brand_voice.md downloaded"],
  steps=[
   ("Open products.csv and brand_voice.md, and choose five SKUs from at least three different categories.",""),
   ("Attach both files to a new chat so the assistant writes from your catalogue instead of from guesswork.",""),
   ("Ask for description, bullets and SEO metadata for all five SKUs in one table, in one pass.",
    "Role: you are a senior retail copywriter for Bloom & Brew.\n"
    "Context: use the attached products.csv for the facts and brand_voice.md for the tone. Nothing else.\n"
    "Task: write web copy for these five SKUs: <SKU1>, <SKU2>, <SKU3>, <SKU4>, <SKU5>.\n"
    "Format: one markdown table. Columns: SKU | Description (55-65 words) | Five feature bullets | SEO title (max 60 characters) | Meta description (max 155 characters).\n"
    "Constraints: British English; use only facts present in products.csv; no invented materials, origins or awards; no superlatives; if a fact is missing write MISSING."),
   ("Fact-check every claim: read each description against the SKU's row and strike out anything the file does not support.",""),
   ("Correct the tone in one pass by naming what is wrong, instead of rewriting the copy yourself.",
    "Rows 2 and 4 drift from the brand voice guide: they use superlatives and exclamation marks.\n"
    "Rewrite ONLY those two descriptions to match brand_voice.md. Keep the word count, the bullets and the metadata unchanged.\n"
    "Return the corrected rows only, in the same table format."),
   ("Paste the finished table into your product sheet, and save the prompt that produced it into your prompt library.",""),
  ],
  step_details=[
   ("Open labs/resources/products.csv in a spreadsheet and labs/resources/brand_voice.md in a text editor or browser. "
    "Read the brand voice guide first - it is short, and it is the standard the output gets judged against. Pick five "
    "SKUs spread across at least three categories (for example one drinkware, one home fragrance, one coffee, one gift "
    "set, one homeware) so you can see whether the assistant holds the voice across different product types."),
   ("Start a new chat and attach both files (ChatGPT: the paperclip; Claude: the attachment button, or a Project with "
    "both files added). If your account cannot attach files, paste the five product rows and the full brand voice guide "
    "into the chat instead. This is grounding: the assistant now writes from your catalogue, and every claim it makes "
    "becomes checkable against a row you can point to."),
   ("Send the prompt with your five SKU codes filled in. Note the two things that make this a batch job rather than five "
    "separate ones: one table for all five SKUs, and a Format line precise enough that the columns come back ready to "
    "paste. The 'if a fact is missing write MISSING' constraint is the important one - it gives the model a legal way "
    "out, which is what stops it inventing a material or an origin to fill the gap."),
   ("Now do the part that cannot be delegated. Take each description and read it against that SKU's row in products.csv. "
    "Every material, capacity, origin, certification and price claim must trace back to a column in the file. Strike out "
    "anything that does not - a 'hand-thrown in Portugal' that appears nowhere in the data is exactly the kind of claim "
    "that becomes a customer complaint. Count the hallucinations you find; that count is your reason for keeping a human "
    "check in the process."),
   ("Rather than rewriting the weak rows yourself, tell the assistant precisely what is wrong and what to preserve. "
    "Naming the fault ('superlatives and exclamation marks', 'drifts from brand_voice.md') and fixing the scope ('only "
    "those two descriptions', 'keep the word count and metadata unchanged') is what makes a correction prompt cheap. "
    "Asking it to 'make it better' is what makes it expensive."),
   ("Copy the finished table into your product sheet or CMS export. Then save the prompt itself - with the placeholders "
    "back in - into the prompt library you started in Lab 1. Next month's catalogue update should be a paste and a "
    "fact-check, not a rewrite."),
  ],
  test=("Pick one finished description and trace every claim in it to a column in products.csv. If a claim has no "
        "column behind it, the copy is not publishable - delete or correct it, then add the missing rule to your "
        "Constraints line so the next batch does not repeat it. A clean pass means every sentence is supported by data."),
  troubleshooting=[
   ("The assistant will not read the attached CSV.",
    "Convert it to a plain table pasted directly into the chat, or upload as .txt. Very large files may also be truncated - send only the five rows you need."),
   ("SEO titles come back over 60 characters.",
    "Ask it to count: 'Return the character count in brackets after each SEO title, and rewrite any that exceed the limit.' Models are poor at silent counting but reliable when made to show it."),
   ("Every description sounds the same.",
    "Add a constraint: 'Do not reuse the opening construction between rows.' Batch prompts converge on one pattern unless told not to."),
  ],
  challenge=("Add a sixth column for a 25-word marketplace short description with a different character limit, and "
             "regenerate. Then ask for the same table translated for a second market, keeping the SEO titles in English."),
  reflection=("How many claims did you have to strike out, and what does that number tell you about publishing AI "
              "product copy without a human check?"),
 ),

 # ------------------------------------------------------------------ Lab 3
 dict(
  num=3, topic=1,
  title="Campaign Copy and AI Product Visuals",
  objective="generate a complete promotional campaign and an AI product visual, then run a pre-publication check",
  desc=("Build one seasonal promotion end to end. You will brief the campaign from the Bloom & Brew catalogue, "
        "generate email subject lines and body copy, three social captions and an in-store poster headline, "
        "then create a product visual with an image model and iterate it one variable at a time. The lab ends "
        "with the pre-publication check every AI-assisted campaign needs."),
  build="A complete mini-campaign - email, three social captions, a poster headline and an AI-generated product visual - for one seasonal promotion.",
  services="ChatGPT or Claude, an image model (ChatGPT image generation, Gemini or Copilot Designer), labs/resources/products.csv",
  duration=45,
  starts_from="labs/resources/products.csv and the copy you produced in Lab 2",
  prereq=["Lab 2 complete - you have on-brand product copy and the brand voice guide",
          "An assistant with image generation available"],
  steps=[
   ("Choose the promotion: pick one category from products.csv, set the offer and the dates, and name the audience.",""),
   ("Brief the whole campaign in one prompt so every asset shares the same offer and voice.",
    "Role: you are a retail marketing lead for Bloom & Brew.\n"
    "Context: promotion is <OFFER> on <CATEGORY>, running <START DATE> to <END DATE>, aimed at <AUDIENCE>. Product facts come from the attached products.csv; tone from brand_voice.md.\n"
    "Task: produce the full campaign kit.\n"
    "Format: (1) three email subject lines, each max 45 characters; (2) one email body of 120-150 words with a single call to action; (3) three social captions, each under 220 characters with two hashtags; (4) one in-store poster headline of no more than six words.\n"
    "Constraints: state the offer and the end date in every asset; no superlatives; no claims outside products.csv; British English."),
   ("Push the subject lines further by asking for distinct angles rather than more variants.",
    "Rewrite the three subject lines so each takes a DIFFERENT angle: one urgency, one benefit, one curiosity.\n"
    "Keep each under 45 characters and include the character count in brackets after each line."),
   ("Generate the product visual with an image prompt that names the subject, setting, light and framing.",
    "Create a photorealistic lifestyle image for a retail promotion.\n"
    "Subject: a <PRODUCT> on a pale oak table, styled with a linen napkin and dried eucalyptus.\n"
    "Setting: a bright Scandinavian-style cafe corner, soft morning light from the left, shallow depth of field.\n"
    "Framing: 4:5 portrait, product in the lower third, clean negative space at the top for a headline.\n"
    "Constraints: no text, no logos, no human faces, no brand marks on the product."),
   ("Iterate the image by changing ONE variable at a time - light, angle, styling or crop - never all at once.",
    "Keep everything the same, change only the light: warm late-afternoon light from the right instead of morning light from the left."),
   ("Run the pre-publication check on the whole kit before anything goes live.",
    "Check this campaign kit and list every issue as a numbered fix list:\n"
    "1. Any claim not supported by products.csv.\n"
    "2. Any price, discount or date that is inconsistent between assets.\n"
    "3. Any line that breaks brand_voice.md.\n"
    "4. Anything that would need a disclosure because the image is AI-generated.\n"
    "Return only the issues and the fix for each - do not rewrite the campaign."),
  ],
  step_details=[
   ("Open products.csv and pick one category with enough SKUs to promote - the coffee or home fragrance ranges work "
    "well. Decide the offer (for example 20% off the range, or a bundle price), the exact start and end dates, and who "
    "it is aimed at (existing loyalty customers, lapsed customers, gift buyers). Write these four facts down before you "
    "prompt: a campaign brief with a vague offer produces assets that contradict each other."),
   ("Attach products.csv and brand_voice.md, then send the campaign prompt with your four facts filled in. Asking for "
    "the whole kit in one prompt is deliberate - subject lines, body, captions and poster generated together share one "
    "offer, one voice and one call to action. Generated separately, they drift, and you spend the saved time "
    "reconciling them."),
   ("Three variants of the same idea are not three options. Asking for three distinct angles - urgency, benefit, "
    "curiosity - gives you something to actually choose between, and the bracketed character counts let you check the "
    "45-character limit without counting by hand. Pick one and note why: that reasoning is what you reuse next campaign."),
   ("Move to your image model (ChatGPT image generation, Gemini, or Copilot Designer). A usable image prompt names four "
    "things: subject, setting, light and framing. The constraints matter as much: 'no text' avoids the garbled lettering "
    "image models produce, 'no logos or brand marks' avoids generating someone else's trademark, and reserving negative "
    "space at the top means your headline has somewhere to sit."),
   ("Change exactly one variable and regenerate. Then change one more. Iterating one variable at a time is what turns "
    "image generation from a slot machine into a controllable process - you learn which words move the result, and you "
    "can get back to a version you liked. Keep the prompt that produced your best image; it is a template for the next "
    "campaign, not a one-off."),
   ("Paste the full kit back into the assistant and ask for the check as a fix list. Note what this prompt does NOT ask "
    "for: a rewrite. You want the issues surfaced so a person decides what to change. Pay particular attention to the "
    "fourth item - if the visual is AI-generated and shows a product a customer will receive, check your platform's and "
    "your market's disclosure expectations before publishing, and never present a generated image as a photograph of the "
    "actual item."),
  ],
  test=("Read the campaign aloud as a customer would meet it: subject line, then email, then a social caption, then the "
        "poster. The offer, the discount and the end date must be identical in all four, and every product claim must "
        "trace to products.csv. One inconsistency between assets means the kit is not ready to schedule."),
  troubleshooting=[
   ("The image has garbled text on the packaging.",
    "Image models cannot spell reliably. Add 'no text, no labels, no packaging copy' to the constraints and add any wording afterwards in a design tool."),
   ("Every regeneration returns a completely different scene.",
    "You changed more than one variable, or started a new chat. Iterate in the same conversation and change one element per request."),
   ("The captions repeat the email body word for word.",
    "Add 'each asset must use different wording from the others; do not reuse sentences across assets' to the Constraints line."),
  ],
  challenge=("Produce a second version of the whole kit for a different audience - gift buyers instead of loyalty "
             "customers - reusing the same offer, then list what actually changed between the two versions."),
  reflection=("Which asset needed the most human correction, and what does that tell you about where to keep a person "
              "in your campaign process?"),
 ),

 # ------------------------------------------------------------------ Lab 4
 dict(
  num=4, topic=1,
  title="Customer Data Privacy and Responsible AI",
  objective="anonymise retail customer data before AI use and set the store's responsible-AI rules",
  desc=("Before AI touches customer data, someone has to decide what it may see. You will classify the columns "
        "in the Bloom & Brew customer and transaction files, build an anonymised extract that is safe to paste "
        "into a public AI tool, draft a one-page AI usage policy for the store team, then red-team that policy "
        "to find what it fails to cover."),
  build="An anonymised data extract that is safe to use with a public AI tool, plus a one-page AI usage policy for your store team.",
  services="ChatGPT or Claude, a spreadsheet, labs/resources/customers.csv, labs/resources/transactions.csv",
  duration=45,
  starts_from="labs/resources/customers.csv and labs/resources/transactions.csv",
  prereq=["Lab 1 complete - you have the five-part house prompt template",
          "customers.csv and transactions.csv open in a spreadsheet"],
  steps=[
   ("Open customers.csv and transactions.csv and mark every column that could identify a real person.",""),
   ("Ask the assistant to classify the columns - paste only the header row, never the customer data itself.",
    "Role: you are a data protection adviser to a retail business in Singapore.\n"
    "Context: these are the column headers of two customer files. I have deliberately not pasted any data.\n"
    "customers.csv: customer_id, full_name, email, phone, postal_code, join_date, loyalty_tier, marketing_optin\n"
    "transactions.csv: order_id, order_date, customer_id, sku, qty, unit_price, channel, store\n"
    "Task: classify every column as SAFE, IDENTIFYING or SENSITIVE for use with a public AI tool.\n"
    "Format: a table of column, classification, one-line reason, and the action to take before any AI use.\n"
    "Constraints: be conservative - if a column could re-identify someone in combination with another, say so."),
   ("In the spreadsheet, build the anonymised extract: delete the identifying columns, renumber the customers and keep only the month.",""),
   ("Draft the store's one-page AI usage policy from your own classification work.",
    "Role: you are writing an internal policy for a six-outlet specialty retailer.\n"
    "Context: staff use public AI assistants for product copy, customer replies and sales analysis. The column classification above is our starting point.\n"
    "Task: write a one-page AI usage policy the store team will actually follow.\n"
    "Format: sections for (1) what may never be pasted into an AI tool, (2) what must be anonymised first, (3) which outputs need human approval before use, (4) who to ask when unsure. Bullet points, plain English, no legal jargon.\n"
    "Constraints: maximum 400 words; every rule must be checkable by a shop-floor supervisor."),
   ("Red-team the policy: ask the assistant to find the realistic ways a busy team would breach it.",
    "You are a sceptical store manager under time pressure.\n"
    "Task: list the five most likely ways this policy gets broken in a real store on a busy Saturday, and the smallest change to the policy that would prevent each one.\n"
    "Format: a table of scenario, why it happens, policy fix.\n"
    "Constraints: realistic retail scenarios only - no hypothetical attackers."),
   ("Add the human-in-the-loop rule: name who approves AI output before it reaches a customer, a price or an order.",""),
  ],
  step_details=[
   ("Open both files and go through the headers column by column. Mark the obvious identifiers first - full_name, "
    "email, phone. Then look for the less obvious ones: a postal code plus a join date plus a loyalty tier can identify "
    "one person in a small customer base, and customer_id links a transaction row straight back to the named record. "
    "Re-identification is usually a combination problem, not a single-column problem."),
   ("Send the classification prompt. Note what it contains: headers only, and an explicit statement that no data was "
    "pasted. That is the habit worth building - you can get useful advice about a dataset without exposing the dataset. "
    "Compare the assistant's classification with the marks you made in step 1, and pay attention to any column it "
    "flagged that you did not."),
   ("Now do the work in the spreadsheet, not in the AI tool. Delete full_name, email and phone entirely. Replace "
    "customer_id with a plain running number (C001, C002, ...) in both files so the two still join but no longer point "
    "back to the source record. Truncate order_date and join_date to the month (2026-03 rather than 2026-03-14). Cut "
    "postal_code to its first two digits or delete it. Save the result as a new file - never overwrite the original - "
    "and use only that file for the rest of the day."),
   ("A policy that no one can follow protects nobody. Send the policy prompt and read the result as a shop-floor "
    "supervisor would: is each rule something you could check in ten seconds? The four sections matter more than the "
    "wording - what is banned outright, what needs anonymising first, what needs approval, and who to ask. Edit the "
    "draft to name real roles in your own business rather than generic ones."),
   ("Red-teaming your own policy is faster than waiting for the breach. The scenarios that come back are the realistic "
    "ones - a rushed reply pasted with the customer's full email still in it, a screenshot of a sales report with names "
    "visible, a supplier price list pasted into a public tool. Take the fixes that are small enough to survive contact "
    "with a busy Saturday and fold them into the policy."),
   ("Finish by writing the rule the AI cannot write for you: the named person or role who approves AI output before it "
    "reaches a customer, a price tag or a purchase order. Responsible AI in retail is not a technology control; it is "
    "an accountable human at the point where the output becomes a commitment to a customer."),
  ],
  test=("Search your anonymised extract for '@', for a phone-number pattern and for any full name from the original "
        "file. All three searches must return zero hits - that is what makes the extract safe to paste into a public "
        "AI tool. If anything is still found, your column list in step 3 was incomplete; fix it and search again."),
  troubleshooting=[
   ("The two files no longer join after renumbering.",
    "Renumber customer_id in customers.csv first, then use a lookup to apply the same new number to transactions.csv. Renumbering the files independently breaks the link."),
   ("The policy reads like a legal document.",
    "Add 'written for a shop-floor supervisor, not a lawyer; maximum 12 words per rule' to the Constraints line and regenerate."),
   ("The assistant refuses to discuss the customer data at all.",
    "You pasted actual rows. Start a new chat with headers only - the refusal is the guardrail working as intended."),
  ],
  challenge=("Take the anonymised extract and try to re-identify one customer using only the columns you kept, plus any "
             "public information. Whatever you manage tells you which column to remove next."),
  reflection=("Which single column in these files would cause the most damage if it were pasted into a public AI tool, "
              "and what stops that happening in your store today?"),
 ),
]
