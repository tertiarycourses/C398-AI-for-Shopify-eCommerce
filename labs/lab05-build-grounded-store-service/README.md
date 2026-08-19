# Lab 5 — Build a Grounded Store Service Assistant

**Topic 02 — Applying AI to Retail Operations and Customer Experience**  |  **Duration:** 40 minutes  |  **Tools:** ChatGPT Projects or Custom GPTs, or Claude Projects; labs/resources/store_policies.md, faq.md, products.csv, customer_feedback.csv

## Goal

Deploy an AI customer-service assistant grounded in your own policies, FAQ and product data.

An assistant that has read your returns policy answers correctly; one that has not will invent a policy you then have to honour. You will build a Bloom & Brew service assistant grounded in the store policies, FAQ and product catalogue, give it tone and escalation rules, then test it against real customer enquiries - including one your policy does not cover.

## What you'll build

A store customer-service assistant grounded in your own policies and FAQ, with a tested escalation rule for anything it cannot answer.

## Prerequisites

- Lab 4 complete - you know what data may and may not be used
- A ChatGPT or Claude account that supports Projects or Custom GPTs

**Starts from:** `labs/resources/store_policies.md, faq.md and products.csv`

## Steps

1. **Create a new Project (Claude) or Custom GPT (ChatGPT) named 'Bloom & Brew Service Assistant'.** In ChatGPT, go to Explore GPTs and create a new GPT (or start a new Project); in Claude, create a new Project. Name it 'Bloom & Brew Service Assistant'. The reason to use a Project or Custom GPT rather than a plain chat is persistence: the knowledge files and the instructions stay attached to every future conversation, so the assistant does not have to be re-briefed each morning.

2. **Add store_policies.md, faq.md and products.csv as the assistant's knowledge - this is what grounds it.** Upload store_policies.md, faq.md and products.csv into the project knowledge. This is grounding, and it is the whole difference between an assistant that answers your returns policy and one that answers a generic returns policy it learned from the internet. Add nothing else - every extra document is another source it can quote at a customer, so keep the knowledge base small and authoritative.

3. **Write the system instructions: role, tone, the grounding rule and the escalation rule.** Paste the instructions into the system prompt or project instructions field. Read the lines in order: the role sets who it is, the grounding rule restricts where answers come from, the escalation line gives it a scripted way to fail safely, the 'never invent' line closes the most expensive failure mode, and the tone rules keep replies usable without editing. The last line - quoting the policy line behind any returns answer - is what makes the assistant auditable when a customer disputes the outcome.

```text
You are the customer service assistant for Bloom & Brew, a specialty home, gift and coffee retailer with six outlets and an online store.
Answer ONLY from the attached store policies, FAQ and product catalogue.
If the answer is not in those documents, say: 'I'll pass this to a store colleague who can help' and state what information the colleague will need.
Never invent a policy, a price, a delivery date or a stock level.
Tone: warm, direct, British English, no more than 120 words per reply, no exclamation marks.
Always end a reply about a return, refund or exchange with the exact policy line it is based on.
```

4. **Test it on six real enquiries taken from customer_feedback.csv, one at a time.** Open customer_feedback.csv and take six real enquiries from it - a returns question, a delivery question, a product-suitability question, a loyalty question, a complaint and an out-of-scope one. Send them one at a time in separate messages, as a customer would. Check each answer against store_policies.md yourself: the assistant quoting a policy line is only useful if the line it quoted is the right one.

```text
A customer bought the ceramic pour-over set 26 days ago, has the receipt, and wants to exchange it for a different colour. What do I tell them?
```

5. **Test the escalation path with a question your policy deliberately does not cover.** Now send the question your policy does not answer. This is the most important test in the lab. A grounded assistant should say it cannot answer and hand over; an ungrounded one will confidently invent a price-match policy that your staff will then have to honour at the counter. If yours invents an answer, the grounding rule in your instructions is too weak - strengthen it and test again.

```text
A customer is asking whether you will price-match a competitor's website. What do I tell them?
```

6. **Tighten one weak answer by fixing the instructions, not by correcting the reply in the chat.** Pick the weakest of the seven answers and resist the urge to correct it in the chat. Fix the instructions instead: add the missing rule, tighten the tone line, or add the policy document it needed. Then re-run that same enquiry in a fresh conversation. Correcting a chat fixes one reply; correcting the instructions fixes every reply from now on.

## Test it

Ask the assistant a question your store policies genuinely do not cover - competitor price matching, or a return at 45 days. It must decline, use your escalation wording and state what the colleague will need. If it invents a policy instead, it is not ready to face a customer: strengthen the grounding rule and re-test.

## Troubleshooting

| Symptom | Fix |
|---|---|
| The assistant answers from general knowledge instead of your files. | Add 'If the documents do not contain the answer, do not use your own knowledge' as its own line, and confirm the files actually uploaded to the project knowledge. |
| Replies are far longer than 120 words. | Put the length rule in its own line rather than in a sentence with other rules, and add 'Hard limit - do not exceed under any circumstances.' |
| It quotes the wrong policy line. | Your policy document has ambiguous headings. Add clear section headers to store_policies.md and re-upload - grounding quality is document quality. |

## Challenge

Add a second knowledge file containing your five most common complaint scenarios with the approved resolution for each, then re-test the complaint enquiry and compare the answer with the earlier one.

## Reflection

What would it have cost your store if the ungrounded answer to the price-match question had been given to a real customer at the counter?

---

*AI for Retail · Course Code C398 · Tertiary Infotech Academy Pte Ltd (UEN 201200696W)*  
*© 2026 Tertiary Infotech Academy Pte Ltd. Version v1.0 · 17 August 2026.*
