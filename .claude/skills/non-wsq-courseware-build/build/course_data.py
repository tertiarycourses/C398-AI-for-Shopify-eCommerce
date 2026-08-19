"""
SINGLE SOURCE OF TRUTH - C398 AI for Retail (non-WSQ).

Every artifact (PPT, Lesson Plan, Learner Guide, LG.md and the lab READMEs) is
generated from this module + data_domain1.py / data_domain2.py, so the four
deliverables stay 100% aligned by construction.

COURSE SHAPE
------------
  * 1 day, 7.5 instructional hours (9:30am-6:30pm, 1-hour lunch, tea within).
  * 2 topics, mirroring the published outline at
    https://www.tertiarycourses.com.sg/ai-for-retail.html
  * 9 hands-on labs, contiguous numbering: Topic 1 = Labs 1-4, Topic 2 = Labs 5-9.
  * No-code throughout - browser-based AI assistants and a spreadsheet only.

NON-WSQ RULES (enforced by the engine and the QA scan - never reintroduce)
--------------------------------------------------------------------------
  * NO assessment of any kind (no written assessment, no practical performance,
    no case study, no marking guide, no answer key). Labs verify, they do not
    assess.
  * NO SSG / SkillsFuture / WSQ funding or subsidy content.
  * NO TRAQOM survey, NO digital attendance, NO 75% attendance rule.
  * NO TGS- course reference - this course carries the plain code C398.

CONNECTED SCENARIO
------------------
All nine labs run on ONE fictional retailer, "Bloom & Brew" - a specialty home,
gift and coffee retailer with six outlets and an online store. The synthetic
data in labs/resources/ grows across the labs: the product catalogue feeds the
copywriting labs, the transactions feed segmentation and analytics, the sales
history feeds forecasting, and the policies and FAQ ground the service
assistant. A learner who falls behind can rejoin at any lab because each lab
states the file it starts from.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "AI for Retail"
SHORT_TITLE  = "AI for Retail"
COURSE_CODE  = "C398"                      # non-WSQ code - never a TGS- ref
VERSION      = "v1.0"
VERSION_DATE = "17 August 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 1
MODE         = "Instructor-led, hands-on practical labs (no programming required)"

DARK_THEME = False

# Deck/LP timing - read by build_slides.py instead of a hard-coded literal.
HOURS_PER_DAY = 7.5
DAILY_TIMING  = "9:30am-6:30pm  ·  1-hour lunch  ·  tea breaks within training time"

# This is a chat-AI course: step "commands" are prompts to paste, not shell
# commands, so the step slides caption the code box accordingly.
PROMPT_CAPTION = "PROMPT  ·  paste into your AI assistant"
# Fenced blocks in the LG Markdown mirror hold prompts, not shell commands.
MD_FENCE = "text"

TRAINER_CERT     = "ACLP-certified trainer; delivers applied AI and data courses for business teams."
TRAINER_DELIVERS = "Practical, no-code AI courses for retail, marketing, operations and analytics roles."

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Describe the AI landscape from generative AI to AI agents, and identify high-value AI use cases across the retail value chain.",
    "LO2: Use AI assistants such as ChatGPT, Claude, Microsoft Copilot and Google Gemini to complete everyday retail tasks with well-structured prompts.",
    "LO3: Generate on-brand product descriptions, marketing copy and product visuals with AI, and check them before they reach a customer.",
    "LO4: Apply customer data privacy, governance and responsible-AI practices when using AI tools on retail data.",
    "LO5: Deploy AI for customer service, personalised recommendations and targeted promotions in a retail setting.",
    "LO6: Apply AI to demand forecasting, inventory planning, pricing, merchandising and sales analytics, and build simple AI workflows for daily retail tasks.",
]
LO_TITLES = [
    "AI Landscape",
    "AI Assistants",
    "Content & Visuals",
    "Responsible AI",
    "Service & Personalisation",
    "Analytics & Workflows",
]

# ------------------------------------------------------------------ topics
TOPICS = [
    dict(num=1, code="01",
         title="Introduction to AI for Retail",
         subtitle="The AI landscape  ·  use cases across the retail value chain  ·  hands-on with ChatGPT, Claude and Copilot  ·  AI-generated product and marketing content  ·  customer data privacy and responsible AI",
         concepts=[
            "Generative AI creates new content - text, images, copy - from a prompt. An AI agent goes further: it plans and carries out a multi-step task using tools and data.",
            "Every stage of the retail value chain has an AI use case: sourcing, merchandising, pricing, marketing, store operations, e-commerce, service and after-sales.",
            "An AI assistant is only as good as the brief. Role, context, task, format and constraints turn a vague answer into copy you can actually publish.",
            "ChatGPT, Claude, Microsoft Copilot and Google Gemini answer the same brief differently. Comparing them on your own task is how you choose the right one.",
            "AI cuts content production from hours to minutes for descriptions, campaigns and visuals - but every output needs a human check before a customer sees it.",
            "Customer data is personal data. Anonymise before you paste, keep payment and identity data out of public AI tools, and keep a person accountable for the decision.",
         ]),
    dict(num=2, code="02",
         title="Applying AI to Retail Operations and Customer Experience",
         subtitle="AI-powered customer service  ·  personalised recommendations and promotions  ·  demand forecasting and inventory planning  ·  pricing, merchandising and sales analytics  ·  everyday AI workflows",
         concepts=[
            "A service assistant grounded in your own FAQ, returns policy and product data answers accurately. An ungrounded one invents policy you will have to honour.",
            "Personalisation starts with segmentation: group customers by how recently, how often and how much they buy, then let AI write the offer for each segment.",
            "Demand forecasting turns sales history into a buying decision. AI is fastest at spotting trend, seasonality and the slow movers quietly tying up cash.",
            "Pricing and markdown calls need margin maths plus judgement. AI surfaces the candidates and the trade-offs; the merchant still makes the decision.",
            "Sales analytics with AI is conversational: ask in plain English, then verify the number against the source data before you act on it.",
            "A simple AI workflow is four parts - trigger, data, AI step, output - plus a human check. That is enough to automate a daily retail task with no code.",
         ]),
]

# ------------------------------------------------------------------ day theme
DAY_THEMES = {
    1: "AI foundations for retail, then AI applied across operations and customer experience",
}

# ------------------------------------------------------------------ schedule
# kind: admin | topic | lab | break | lunch | recap   (NEVER "assess")
# The day must total exactly 480 minutes excluding lunch:
# 450 instructional (7.5 hours) + 30 minutes of tea breaks.
def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:30","9:50",20,"admin","Welcome, course introduction, ice-breaker and ground rules"),
        ("9:50","10:30",40,"topic","Topic 1 - "+TOPICS[0]["title"]+": the AI landscape, retail use cases and the five-part prompt pattern (concepts + trainer demo)"),
        ("10:30","11:15",45,"lab","Hands-on: "+lab_titles([1,2])),
        ("11:15","11:30",15,"break","Tea break"),
        ("11:30","13:00",90,"lab","Hands-on: "+lab_titles([3,4])),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","14:30",30,"topic","Topic 2 - "+TOPICS[1]["title"]+": grounding, segmentation, forecasting and no-code AI workflows (concepts + trainer demo)"),
        ("14:30","15:45",75,"lab","Hands-on: "+lab_titles([5,6])),
        ("15:45","16:00",15,"break","Tea break"),
        ("16:00","18:00",120,"lab","Hands-on: "+lab_titles([7,8,9])),
        ("18:00","18:30",30,"recap","Course recap against the learning outcomes, next steps and Q&A"),
     ]),
    }

# ------------------------------------------------------------------ deck: core concepts section
COURSE_OVERVIEW = dict(
    section_title="AI Foundations for Retail",
    concepts_title="Key Concepts",
    concepts=[
        ("Generative AI", "Creates new text, images and copy from a prompt. The engine behind product descriptions and campaign content."),
        ("AI Assistant", "A chat interface - ChatGPT, Claude, Copilot, Gemini - that you brief in plain English to do a retail task."),
        ("AI Agent", "Goes beyond answering: plans and carries out a multi-step task using tools and your data."),
        ("Grounding", "Giving the AI your own FAQ, policies and product data so answers come from your store, not from the open internet."),
        ("Prompt Pattern", "Role, context, task, format, constraints - the five-part brief that makes AI output usable first time."),
        ("Human in the Loop", "A person checks and approves every AI output that reaches a customer, a price or a purchase order."),
    ],
    framework_title="The Retail AI Value Chain",
    framework=[
        ("Source & Buy", "Supplier research, spec comparison and negotiation prep."),
        ("Merchandise & Price", "Assortment reviews, markdown candidates, category narratives."),
        ("Market & Sell", "Product copy, campaign assets, social captions, email."),
        ("Serve", "FAQ assistants, returns handling, review replies, tone control."),
        ("Plan & Forecast", "Demand forecasts, reorder points, slow-mover and stock-risk reports."),
        ("Analyse", "Plain-English sales analytics, KPI summaries and action lists."),
    ],
    statement=dict(
        headline="AI does not replace the retailer's judgement - it removes the hours before the judgement.",
        body="Every lab today produces something you could use in your store tomorrow: product copy, a service assistant, a forecast, a pricing review, a working workflow.",
        kicker="WHY THIS COURSE"),
    pillars_title="What You'll Build",
    pillars=[
        ("Content & Brand", [
            "A reusable five-part house prompt template",
            "AI product descriptions and SEO metadata for a catalogue",
            "Campaign copy and an AI-generated product visual"]),
        ("Customer Experience", [
            "A store service assistant grounded in your own policies",
            "Four customer segments with a targeted offer each",
            "Next-best-product recommendations for named customers"]),
        ("Operations & Analytics", [
            "A three-month demand forecast and reorder plan",
            "A margin, markdown and category review",
            "A no-code daily sales-summary workflow"]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Start from a real retail artifact - a product sheet, a sales export, a customer enquiry.",
        "Brief the AI with the five-part prompt pattern instead of a one-line question.",
        "Generate a first draft, then challenge it: check the numbers, the policy and the tone.",
        "Verify with the lab's 'Test it' step so you know the output is fit to use.",
        "Save the working prompt into your own prompt library so the next run takes minutes.",
    ],
)

ICE_BREAKER = [
    "Your name, your store or organisation, and your role.",
    "What you sell, and how many outlets or channels you run.",
    "Which AI tools you have already tried at work, if any.",
    "The one retail task you would most like to hand to AI by this evening.",
]

NEXT_STEPS = dict(title="Continuing Your Journey", items=[
    "Pick the single lab that saves you the most time and run it on your own store data next week.",
    "Build your prompt library: every prompt that worked today, saved with the output format it produced.",
    "Agree an AI usage policy with your team before AI touches customer data or pricing.",
    "Explore the follow-on courses in AI, data analytics and automation at www.tertiarycourses.com.sg.",
])

THANK_YOU = dict(
    kicker="THANK YOU FOR ATTENDING",
    body="You have briefed, grounded, verified and shipped AI output across nine retail tasks today - keep applying the same pattern to your own store.")

# Optional per-lab screenshots (courseware/assets/screenshots/). None for this course.
LAB_SHOTS = {}

# ------------------------------------------------------------------ Learner Guide content
LG_INTRO = ("This Learner Guide accompanies the course AI for Retail (C398), conducted by Tertiary Infotech "
            "Academy Pte Ltd. It provides step-by-step instructions for all nine hands-on labs, organised "
            "into the two topics that follow the course slides and Lesson Plan. No programming experience "
            "is required - every lab is done in a browser with an AI assistant and a spreadsheet.")
LG_INTRO2 = ("All nine labs run on one fictional retailer, Bloom & Brew - a specialty home, gift and coffee "
             "retailer with six outlets and an online store. The synthetic data files in labs/resources/ "
             "carry through the whole day, so each lab builds on the one before it. Work through the labs "
             "in order; if you fall behind, each lab states the file it starts from so you can rejoin.")

LG_SETUP = dict(
    needs=[
        "A laptop with a modern browser (Chrome or Edge) and a stable internet connection.",
        "A free ChatGPT account (chatgpt.com) - the assistant used in most labs.",
        "A free Claude account (claude.ai) and access to Microsoft Copilot (copilot.microsoft.com) or Google Gemini (gemini.google.com) for the comparison lab.",
        "A Google account for Google Sheets, used in the analytics and workflow labs.",
        "The synthetic Bloom & Brew data from the course repository: labs/resources/ (product catalogue, transactions, customers, sales history, feedback, store policies, FAQ and brand voice guide).",
        "No programming experience and no software installation is required.",
    ],
    verify_text=("Before you start, open each AI assistant you plan to use and send the message "
                 "'Reply with OK if you can read this.' If each one replies, you are ready. Then download "
                 "the labs/resources/ folder and open products.csv in a spreadsheet to confirm the files "
                 "opened correctly."),
    verify_code="",
    conventions=[
        "Text shown in a PROMPT block is meant to be copied and pasted into the AI assistant named in that step.",
        "Placeholders such as <YOUR STORE NAME> or <YOUR CATEGORY> are replaced with your own values before you send the prompt.",
        "All data in labs/resources/ is synthetic - it contains no real customer, payment or employee data.",
        "Never paste real customer, payment or employee data into a public AI tool during this course.",
        "AI output varies between runs, so your wording will differ from the trainer's. Judge the output against the lab's 'Test it' step, not against the trainer's exact wording.",
    ],
)

LAB_NOTE = ("Use only the synthetic data supplied and accounts you are authorised to use. Never paste real "
            "customer, payment or employee data into a public AI tool.")

LG_WRAPUP = dict(
    title="Wrap-Up - Putting AI to Work in Your Store",
    intro=("You have now taken AI through a full retail day: briefing an assistant, producing catalogue and "
           "campaign content, protecting customer data, grounding a service assistant, personalising offers, "
           "forecasting demand, reviewing pricing and automating a daily task. The pattern is the same every "
           "time - brief it properly, ground it in your own data, verify the output, then keep the prompt."),
    sections=[
        dict(title="The five-part prompt pattern, once more",
             bullets=[
                "Role: who the AI is being asked to be (a retail copywriter, a category manager, a demand planner).",
                "Context: the store, the customer, the season, the constraint - plus the data file if there is one.",
                "Task: the single thing you want done, stated as an instruction, not a question.",
                "Format: the exact shape of the answer - a table, 60 words, five bullets, a subject line.",
                "Constraints: brand voice, what it must not claim, what it must do if it does not know.",
             ]),
        dict(title="What must always stay human",
             bullets=[
                "Any claim about a product that a customer could rely on.",
                "Any price, markdown or purchase-order quantity.",
                "Any reply that commits the store to a refund, exchange or goodwill gesture.",
                "Any decision that uses customer data - and the decision about what data is used at all.",
             ]),
        dict(title="Where the time savings actually come from",
             bullets=[
                "Reuse: a saved prompt that works is worth more than a one-off good answer.",
                "Grounding: attaching your own policy, FAQ and product data removes most of the correction work.",
                "Format discipline: asking for a table you can paste beats asking for prose you must retype.",
                "Batching: doing five SKUs in one prompt costs barely more time than doing one.",
             ]),
    ],
)

LG_NEXT_STEPS = [
    "First pass: complete every lab yourself, following the steps in this guide and the lab READMEs.",
    "Second pass: re-run the labs on your own product, sales and customer data instead of the Bloom & Brew files.",
    "Assemble your prompt library - each working prompt saved with the output format it produced.",
    "Agree your store's AI usage policy (Lab 4) with your team before AI touches customer data or pricing.",
    "Pick one daily task and put the Lab 9 workflow into live use, with the human check kept in place.",
]

LG_GLOSSARY = [
    ("Generative AI", "AI that produces new content - text, images, audio, code - in response to a prompt, rather than only classifying or predicting."),
    ("Large Language Model (LLM)", "The model behind an AI assistant. It predicts text, which is why it is fluent but can also be confidently wrong."),
    ("AI Assistant", "A chat product built on an LLM - ChatGPT, Claude, Microsoft Copilot, Google Gemini - that you brief in plain English."),
    ("AI Agent", "An AI that plans and carries out a multi-step task using tools, files or systems, rather than only answering a single question."),
    ("Prompt", "The instruction you give an AI assistant. The five-part pattern used in this course is role, context, task, format, constraints."),
    ("Grounding", "Supplying the AI with your own documents or data so its answers come from your store's facts instead of general internet knowledge."),
    ("Hallucination", "A fluent, confident output that is factually wrong - an invented product feature, policy or number. The reason every output is checked."),
    ("Human in the Loop", "A named person who reviews and approves AI output before it reaches a customer, a price tag or a purchase order."),
    ("Personal Data", "Any data that identifies a customer - name, email, phone, address, payment details. Removed before data is used with a public AI tool."),
    ("Anonymisation", "Removing or replacing identifying fields so a data extract can no longer be traced to an individual customer."),
    ("Segmentation", "Grouping customers by behaviour - typically how recently, how often and how much they buy - so offers can be targeted."),
    ("Next-Best-Product", "The product a specific customer is most likely to buy next, inferred from their purchase history and that of similar customers."),
    ("Demand Forecast", "A projection of future unit sales for a product or category, used to decide what and when to reorder."),
    ("Reorder Point", "The stock level that triggers a new order: expected demand over the supplier lead time, plus safety stock."),
    ("Safety Stock", "Extra stock held to absorb demand spikes and late deliveries without going out of stock."),
    ("Gross Margin", "(Retail price minus cost price) divided by retail price, as a percentage. The core profitability measure in the pricing lab."),
    ("Markdown", "A permanent or promotional price reduction used to clear stock, at the cost of margin."),
    ("Slow Mover", "A product selling far below the assortment average, tying up cash and shelf space."),
    ("AI Workflow", "A repeatable sequence - trigger, data, AI step, output, human check - that automates a recurring task without code."),
    ("Brand Voice", "The documented tone and language rules that keep every piece of customer-facing content sounding like the same store."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial release. Two topics, nine hands-on labs, one connected Bloom & Brew retail scenario.", TRAINER),
]
