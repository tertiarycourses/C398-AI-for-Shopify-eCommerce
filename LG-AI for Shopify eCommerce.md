# AI for Shopify eCommerce — Learner Guide

**Course Code:** C398  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 28 September 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Environment Setup](#before-you-start--environment-setup)
- [Topic 01 — Getting Started on Shopify](#topic-01--getting-started-on-shopify)
  - [Lab 1 — Set Up Your Shopify Store](#lab-1--set-up-your-shopify-store)
- [Topic 02 — Setting Up Products](#topic-02--setting-up-products)
  - [Lab 2 — Create Products with Variants](#lab-2--create-products-with-variants)
- [Topic 03 — Customizing Theme](#topic-03--customizing-theme)
  - [Lab 3 — Install and Customize a Theme](#lab-3--install-and-customize-a-theme)
  - [Lab 4 — Create a Collection and a Contact Us Page](#lab-4--create-a-collection-and-a-contact-us-page)
- [Topic 04 — Managing Orders](#topic-04--managing-orders)
  - [Lab 5 — Process, Fulfill and Refund an Order](#lab-5--process-fulfill-and-refund-an-order)
- [Topic 05 — Payment and Shipping](#topic-05--payment-and-shipping)
  - [Lab 6 — Set Up Payment Methods](#lab-6--set-up-payment-methods)
  - [Lab 7 — Configure Shipping Rates and Taxes](#lab-7--configure-shipping-rates-and-taxes)
- [Topic 06 — Marketing and Performance](#topic-06--marketing-and-performance)
  - [Lab 8 — Create Discounts and a Marketing Plan](#lab-8--create-discounts-and-a-marketing-plan)
  - [Lab 9 — Set Up SEO, Analytics and Newsletter](#lab-9--set-up-seo-analytics-and-newsletter)
- [Running the Store After Class — Your Weekly Routine](#running-the-store-after-class--your-weekly-routine)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies the course AI for Shopify eCommerce (C398), conducted by Tertiary Infotech Academy Pte Ltd. It provides detailed step-by-step instructions for all 9 hands-on labs, organised by the six course topics. Every lab is completed on your own live Shopify trial store, so by the end of the course you will have built, configured and marketed a working eCommerce store.

Use this guide alongside the course slides: the slides carry the concepts and each lab's overview, while this guide carries the full click-by-click steps. Keep this guide open in every lab.


## Course Learning Outcomes

- LO1: Setup Shopify eCommerce store and CMS
- LO2: Curate product and web content on Shopify store
- LO3: Improve customer experience by customising Shopify theme
- LO4: Manage orders on Shopify store
- LO5: Manage payment and shipping issues on Shopify store
- LO6: Develop and review Shopify store marketing and site performance


## Before You Start — Environment Setup

**What you need**

- A laptop with a modern web browser (Chrome, Edge, Firefox or Safari).
- An email address you can access in class — it becomes your Shopify login and your store's PayPal identity.
- A Shopify free trial store — created step-by-step in Lab 1 at https://www.shopify.com.sg/ (no credit card needed to start).
- The mock product catalog labs/data/mock-products.csv from the course repository — 6 ready-made products (with variants and prices) that you bulk-import in Lab 2 so your store starts with a working catalog.
- A few product images (or use free stock images from burst.shopify.com / unsplash.com).
- Optional: a PayPal account and a Google account (for Google Analytics in Lab 9).

**Working in the Shopify admin**

Everything in this course happens in the Shopify admin — the back office of your store at your-store.myshopify.com/admin. The left sidebar is your map: Orders, Products, Customers, Marketing, Discounts, Analytics, Online Store (under Sales channels) and Settings (bottom-left).

**Conventions used in every lab**

- Menu paths are written like: Settings → General → Standards and formats.
- Names in examples (store names, products, prices) are examples — use your own.
- Each lab ends with a 'Test it' check — do not move on until it passes.
- The storefront is what customers see; the admin is what you see. Keep both open in separate tabs.


## Topic 01 — Getting Started on Shopify

Overview of Shopify eCommerce · Basic store configuration

**Key concepts**

- Shopify is one of the most popular hosted eCommerce platforms — anyone can set up an online store and sell products without managing servers or code.
- Understand your goals before you build: what products you sell, who your target audience is, which sales channels you need and which pricing plan fits.
- Basic store configuration covers the store name, legal business address, time zone, billing, currency, weight unit, shipping, taxes and your domain.
- Store policies, staff permissions and content guidelines govern who may publish and change content on the store (content management policies).
- Home page metadata (title + meta description) is what shoppers see on the search results page — unique, descriptive metadata attracts clicks.
- Order IDs default to #1001, #1002 … — you can brand them with a custom prefix or suffix in Settings → General.


### Lab 1 — Set Up Your Shopify Store

Learning outcome: LO1 — Setup Shopify eCommerce store and CMS.

Goal: Create your own Shopify trial store and complete the basic store configuration — store details, address, time zone, currency, weight unit, home page metadata and a branded order ID prefix.

**What you'll build**

A live Shopify trial store with correct store details, standards and formats, home page metadata and a custom order ID format.   (Tools: Shopify admin, Shopify free trial, web browser.)

**Step-by-step**

1. Set up your Shopify account: go to https://www.shopify.com.sg/ and click Start free trial (no credit card is needed to start).
2. Answer the short setup questions — what you plan to sell and where you plan to sell it — or click 'Skip all' to answer later.
3. Create your login: sign up with your email address (or continue with Google / Apple) and set a password. Use an email you can access in class — it is also used for order notifications and PayPal.
4. Enter a unique store name when prompted — Shopify creates your free your-store-name.myshopify.com address. Choose Singapore as the business location, then wait a moment while Shopify builds the store and drops you into the admin.
5. Take a tour of the Shopify admin: the left sidebar holds Orders, Products, Customers, Marketing, Discounts, Analytics and the Online Store sales channel; Settings is at the bottom-left. The storefront preview is behind the eye icon next to Online Store.
6. On later days, log back in at https://www.shopify.com/login — enter your store domain, email and password.
7. From your Shopify admin, go to Settings → General.

   ```
   Shopify admin → Settings → General
   ```

8. In the Store details section, enter the name of your store in the Store name field.
9. In the Store address section, fill in your legal business name and address — this appears on invoices and is used for shipping calculations.
10. In the Standards and formats section, set the Time zone to (GMT+08:00) Singapore, the Currency to SGD, and the Default weight unit to kg. Click Save.
11. Go to Online Store → Preferences. In the Title and meta description section, enter a Homepage title (up to 70 characters) and a Homepage meta description (up to 320 characters) that describe your store for search engines. Click Save.

   ```
   Shopify admin → Online Store → Preferences
   ```

12. Go back to Settings → General. In the Standards and formats section, edit the Order ID Prefix — replace # with your own brand prefix (e.g. SG-). Click Save.
13. Review your remaining setup checklist: billing information, payment gateways, shipping and taxes — you will complete these in Topics 5.

**Test it**

Open Settings → General and confirm the store name, Singapore time zone, SGD currency and your custom order ID prefix are saved. Open your storefront preview and confirm the store loads with your store name in the browser tab.

> **Note:** A lab summary is in labs/lab-01-*.md. If the Shopify admin looks different from these steps, Shopify has updated its UI — the setting names stay the same; use the admin search bar to find them.

---


## Topic 02 — Setting Up Products

Add products · Product details · Search engine metas · Variants

**Key concepts**

- Products are the goods, digital downloads, services and gift cards you sell — each with a title, description, media, pricing, inventory and shipping details.
- A well-curated product page pairs quality images with benefit-led descriptions — it is your 24/7 salesperson.
- The search engine listing (page title ≤ 55 chars, meta description, URL handle) controls how the product appears on Google.
- Tags are searchable keywords that help customers find products and power automated collections.
- Variants capture every combination of options (size, colour, style) — up to 3 options and 100 variants per product, each with its own price, SKU and image.
- Publish each product to the right sales channels (online store, POS, social) from the product availability panel.


### Lab 2 — Create Products with Variants

Learning outcome: LO2 — Curate product and web content on Shopify store.

Goal: Stock the store two ways: bulk-import the course's mock product catalog (labs/data/mock-products.csv — 6 ready-made products with variants), then add a shirt product manually with a complete product page — title, description, images, pricing, inventory, Colour and Size variants, search engine listing, tags and sales channels.

**What you'll build**

A stocked store: 6 imported mock products plus a fully-curated shirt with Colour/Size variants, SEO listing, tags and sales channels.   (Tools: Shopify admin — Products, CSV product import, product images, SEO listing editor.)

**Step-by-step**

1. Get the mock product catalog mock-products.csv from the labs/data folder of the course repository (also in the Activities folder on the course Drive). It contains 6 ready-made products — shirts, yoga gear and a virtual class package — in Shopify's product CSV format.

   ```
   labs/data/mock-products.csv
   ```

2. From your Shopify admin, go to Products and click Import. Click Add file, select mock-products.csv, then click Upload and preview.

   ```
   Shopify admin → Products → Import
   ```

3. Review the preview (it shows the first product) and click Import products. Shopify emails you when the import completes — refresh the Products page to see all 6 mock products with their variants and prices.
4. Spot-check an imported product (e.g. Pro Yoga Mat): open it and confirm the Colour/Length variants, prices and stock came in. If a product image failed to download from the image URL, add one manually from burst.shopify.com or unsplash.com.
5. Now add a product manually: go to Products → All products and click Add product.

   ```
   Shopify admin → Products → Add product
   ```

6. Enter a product Title (e.g. Classic Cotton Shirt) and a benefit-led Description that tells the customer why they want it, not just what it is.
7. In the Media section, upload at least three product images (front, back, detail). Add descriptive ALT text to each image for SEO and accessibility.
8. In the Pricing section, set the Price (e.g. $39). Optionally set a Compare-at price (e.g. $59) to show a markdown, and Cost per item to track margin.
9. In the Inventory section, enter a SKU, tick Track quantity and set the available Quantity. In the Shipping section, tick This is a physical product and enter the weight (e.g. 0.3 kg).
10. In the Variants section, click Add options like size or color. Enter Option name Color with values Black, White; then Add another option — Size with values S, M, L. Untick any combination you do not sell.
11. Open each variant and assign the matching image, price, SKU and quantity — a different image for each colour.
12. In the Search engine listing section, click Edit website SEO. Enter a Page title (≤ 55 characters), a compelling Meta description and check the URL handle. Click Save.
13. In the Organization panel, set Product type (Shirt), Vendor, and add Tags such as cotton, unisex, classic — separated by commas.
14. In the Publishing/Sales channels panel, click Manage and make the product available on the Online Store channel. Click Save.
15. Time-saver: to create a similar product, open the product and click Duplicate, then rename the duplicate.

**Test it**

The Products page must list the 6 imported mock products plus your shirt. On the storefront, the shirt's Colour and Size selectors must switch price and image per variant, and the Google preview in Edit website SEO must show your custom title and description.

> **Note:** A lab summary is in labs/lab-02-*.md. If the Shopify admin looks different from these steps, Shopify has updated its UI — the setting names stay the same; use the admin search bar to find them.

---


## Topic 03 — Customizing Theme

Choose · Publish · Structure · Theme settings · Code · Collections · Pages

**Key concepts**

- A theme defines the look and feel of your store — spa products want relaxed and luxurious; electronics want energetic and sleek.
- The Shopify Theme Store offers free and paid themes, filterable by industry and collection; you can hold up to 20 themes but publish only one.
- Every theme shares a common structure — page elements (header, body, footer, navigation) and page types (home, collection, product, cart, blog, customer).
- The theme editor customises content, layout, typography and colours with zero code; edit Liquid/HTML/CSS only when a setting does not exist.
- Collections group products for browsing — an automated 'All' collection controls the order of your catalog page.
- Standard pages such as Contact Us use built-in templates (page.contact) so every store gets a working contact form.


### Lab 3 — Install and Customize a Theme

Learning outcome: LO3 — Improve customer experience by customising Shopify theme.

Goal: Browse the Shopify Theme Store, install a new theme, publish it, then use the theme editor to brand the store — logo, banner, colours, fonts and social media links — without touching code, and peek at the theme code editor.

**What you'll build**

A published, branded theme with your own logo, hero banner, colour scheme, typography and social media links.   (Tools: Shopify Theme Store (themes.shopify.com), theme editor, theme code editor.)

**Step-by-step**

1. Go to https://themes.shopify.com/. Click Collections or Industries and pick a category that fits your store. Use the sidebar filters to refine the results.
2. From your Shopify admin, go to Online Store → Themes. In the Theme library section, click Add theme → Visit Theme Store and install a free theme (e.g. Dawn, Craft or Sense).

   ```
   Shopify admin → Online Store → Themes
   ```

3. In the Theme library, find the new theme and click Actions → Publish, then confirm Publish. Your previous theme moves to the library — nothing is lost.
4. On the published theme, click Customize to open the theme editor.
5. In Theme settings → Logo, upload your store logo and set its width.
6. Select the Image banner section on the home page and upload a hero banner image; edit the heading and button text to a clear call-to-action.
7. In Theme settings → Colors, choose a colour scheme that matches your brand; in Theme settings → Typography, pick heading and body fonts.
8. In Theme settings → Social media, paste your Facebook / Instagram / TikTok links so the icons appear in the footer. Click Save.
9. Optional — view the code: from Online Store → Themes click Actions → Edit code to see the theme structure (layout, templates, sections, snippets, assets). Do not change anything yet — close without saving.

**Test it**

Open the storefront preview: your logo, banner, brand colours, fonts and social icons must all be live on the published theme.

> **Note:** A lab summary is in labs/lab-03-*.md. If the Shopify admin looks different from these steps, Shopify has updated its UI — the setting names stay the same; use the admin search bar to find them.

---


### Lab 4 — Create a Collection and a Contact Us Page

Learning outcome: LO3 — Improve customer experience by customising Shopify theme.

Goal: Control the catalog page with an automated 'All' collection, then add a Contact Us page using the built-in page.contact template so customers can reach you.

**What you'll build**

An automated All collection ordering your catalog page, plus a working Contact Us page with a built-in contact form.   (Tools: Shopify admin — Collections, Pages, page.contact template.)

**Step-by-step**

1. From your Shopify admin, go to Products → Collections and click Create collection.

   ```
   Shopify admin → Products → Collections
   ```

2. Give the collection the title All. In the Collection type section, select Automated.
3. Set the condition Product price is greater than 0. Optional: to hide sold-out products, add Inventory stock is greater than 0. Click Save.
4. Visit your-store.myshopify.com/collections/all and note the catalog page order now follows your All collection.
5. Go to Online Store → Pages and click Add page.

   ```
   Shopify admin → Online Store → Pages → Add page
   ```

6. In the Title box type Contact Us. In the Content box add a short welcome line such as 'We would love to hear from you.'
7. In the Template section (Theme template), choose contact (page.contact) from the drop-down. Click Save.
8. Go to Online Store → Navigation, open the Main menu, click Add menu item, name it Contact Us and link it to your new page. Click Save menu.

**Test it**

Open the storefront: the Contact Us link must appear in the main menu and the page must show a working contact form (Name, Email, Message). Submit a test message to yourself.

> **Note:** A lab summary is in labs/lab-04-*.md. If the Shopify admin looks different from these steps, Shopify has updated its UI — the setting names stay the same; use the admin search bar to find them.

---


## Topic 04 — Managing Orders

View · Fulfill · Manage · Refund and cancel

**Key concepts**

- When a customer places an order you get an email notification, the order appears on the Orders page, and the customer receives a confirmation email.
- Fulfillment = picking and packing the products, labelling the shipment and handing it to a carrier — Shopify tracks the status end to end.
- The order Timeline records every event — payments, fulfillments, notes — and is your first stop when troubleshooting a failed capture or refund.
- Day-to-day order management: tags and notes, contacting the customer, resending notifications, push notifications and archiving fulfilled orders.
- Refunds can be full or partial, with optional restocking and customer notification — cancellations reverse the order entirely.
- Consistent, timely order handling keeps the store content and inventory accurate and maintains customer trust.


### Lab 5 — Process, Fulfill and Refund an Order

Learning outcome: LO4 — Manage orders on Shopify store.

Goal: Place a trial order on your own store using a manual payment method, then work the full order lifecycle in the admin — view the order and its Timeline, fulfill it, and process a partial refund.

**What you'll build**

A completed order lifecycle: a test order that has been viewed, paid, fulfilled and refunded, with the Timeline recording every event.   (Tools: Shopify admin — Orders, order Timeline, fulfillment, refunds.)

**Step-by-step**

1. On your storefront, add your shirt product to the cart and check out as a customer. Choose the manual payment method (e.g. Bank Deposit — set up in Lab 6, or Cash on Delivery) and complete the order.
2. From your Shopify admin, go to Orders — the new order appears with a yellow Payment pending / Unfulfilled badge. Click the order number to open it.

   ```
   Shopify admin → Orders
   ```

3. Scroll to the Timeline section and expand the events — order placed, confirmation email sent. The Timeline is your audit trail for troubleshooting payments and refunds.
4. Click Collect payment → Mark as paid to record receipt of the manual payment.
5. Click Fulfill item(s). Optionally add a tracking number, tick Send shipment details to your customer now, then click Fulfill items — the order is now marked Fulfilled.
6. Add a Tag (e.g. test-order) and a Note (e.g. staff training order) in the right panel so the order is searchable.
7. Click Refund. Enter the quantity to refund — Shopify recalculates the Refund total. Untick Restock items if stock did not come back; keep Send a notification to the customer ticked. Click Refund.
8. Back on the Orders page, select the order and choose Archive to remove it from your open orders list.

**Test it**

The order page must show Paid → Fulfilled → Refunded events on the Timeline, and the customer email inbox must have the confirmation, shipment and refund notifications.

> **Note:** A lab summary is in labs/lab-05-*.md. If the Shopify admin looks different from these steps, Shopify has updated its UI — the setting names stay the same; use the admin search bar to find them.

---


## Topic 05 — Payment and Shipping

Payments · PayPal · Manual methods · Fraud · Taxes · Shipping · Dropshipping

**Key concepts**

- Customers pay with any method you enable under Settings → Payments — Shopify Payments, PayPal, credit cards, wallets and manual methods.
- PayPal Express Checkout is created automatically with your store email — activate it to start receiving PayPal payments immediately.
- Manual payment methods (bank deposit, cash on delivery, custom) suit local markets — orders stay pending until you mark them paid.
- Shopify's built-in fraud analysis flags suspicious orders — verify the IP, phone and email, match billing and shipping addresses, review high-value orders.
- Configure taxes for every country and region you ship to; Singapore stores charge GST where registered.
- Shipping strategy is a business decision: free shipping, exact carrier rates or flat rates — supported by product weights and default packaging.
- Dropshipping and fulfillment services ship on your behalf — you price shipping by their fees, not the carrier's.


### Lab 6 — Set Up Payment Methods

Learning outcome: LO5 — Manage payment and shipping issues on Shopify store.

Goal: Configure how your store gets paid: activate PayPal, add a manual Bank Deposit method with customer instructions, set automatic payment capture and review Shopify's fraud analysis indicators.

**What you'll build**

A store that accepts PayPal and Bank Deposit, captures card payments automatically, and a fraud-check routine for suspicious orders.   (Tools: Shopify admin — Settings → Payments, PayPal, manual payment methods.)

**Step-by-step**

1. From your Shopify admin, go to Settings → Payments.

   ```
   Shopify admin → Settings → Payments
   ```

2. In the PayPal section, select your PayPal account type and click Activate. Enter the email address and password for your PayPal account, click I Give Permission, then Go back to Shopify. (No PayPal account yet? Shopify created a PayPal Express Checkout entry for your store email — sign up with the same email.)
3. In the Manual payment methods section, click Add manual payment method → Bank Deposit.
4. In Additional details, enter what the customer sees at checkout (e.g. 'Pay by PayNow/bank transfer within 24 hours'). In Payment instructions, enter your bank account / PayNow details shown on the order confirmation page. Click Activate.
5. In the Payment capture section, choose Automatically capture payment for orders. Click Save.
6. Review fraud prevention practice for every suspicious order: verify the IP address, call the phone number, search the email address, check that billing and shipping addresses match, and review high-value orders before fulfilling.
7. Place a test checkout on your storefront and confirm both PayPal and Bank Deposit appear as payment options.

**Test it**

Your checkout must offer PayPal and Bank Deposit; the Bank Deposit order confirmation page must show your payment instructions; Settings → Payments must show automatic capture enabled.

> **Note:** A lab summary is in labs/lab-06-*.md. If the Shopify admin looks different from these steps, Shopify has updated its UI — the setting names stay the same; use the admin search bar to find them.

---


### Lab 7 — Configure Shipping Rates and Taxes

Learning outcome: LO5 — Manage payment and shipping issues on Shopify store.

Goal: Plan your shipping strategy and implement it: add product weights, create a Singapore shipping zone with a flat rate, add free shipping for orders above $200, and review tax settings for the regions you sell to.

**What you'll build**

A working shipping setup — Singapore zone with a flat rate plus free shipping over $200 — and taxes configured for your selling regions.   (Tools: Shopify admin — Settings → Shipping and delivery, Settings → Taxes and duties.)

**Step-by-step**

1. Decide your strategy first: free shipping (build cost into price), exact carrier rates, or flat rates. Flat rate + free-above-threshold is the common starter combination — it also lifts average order value.
2. Confirm every physical product has a weight (Products → your product → Shipping section) so rates based on weight work correctly.
3. From your Shopify admin, go to Settings → Shipping and delivery. In General shipping rates, click the General profile to edit it.

   ```
   Shopify admin → Settings → Shipping and delivery
   ```

4. Click Create shipping zone, name it Singapore and select Singapore. Click Done.
5. In the Singapore zone, click Add rate → Use flat rate. Name it Standard Delivery, price $5. Click Done.
6. Click Add rate again. Name it Free Shipping, price $0, then click Add conditions → Based on order price → Minimum price $200. Click Done, then Save.
7. Go to Settings → Taxes and duties, open Singapore and review the GST treatment for your store (charge GST only if your business is GST-registered).
8. Run a test checkout: a cart under $200 must offer Standard Delivery $5; add items past $200 and Free Shipping must appear.

**Test it**

Checkout shows Standard Delivery ($5) below $200 and Free Shipping at/above $200 for a Singapore address; product weights and tax regions are in place.

> **Note:** A lab summary is in labs/lab-07-*.md. If the Shopify admin looks different from these steps, Shopify has updated its UI — the setting names stay the same; use the admin search bar to find them.

---


## Topic 06 — Marketing and Performance

Marketing plan · SEO · Discounts · Analytics · Pixels · Newsletter

**Key concepts**

- After launch, the job is traffic and conversion — a marketing plan chooses the tactics that fit your store and budget.
- The 7-step marketing plan: define your message, understand customers, choose tactics, set goals, choose channels, analyse impact, repeat.
- SEO raises your ranking for shoppers already searching for your products — keywords in page titles, meta descriptions, ALT text and body content.
- Shopify automates canonical tags, sitemap.xml, robots.txt and social sharing; you optimise titles, descriptions, URLs and image ALT text.
- Discount codes and automatic discounts (percentage, fixed, free shipping) drive promotions — with usage limits and active dates.
- Store analytics measure performance: sessions, conversion funnel, top traffic sources and locations, sales attributed to marketing.
- Google Analytics, Facebook Pixel and Google Ads conversion tags track campaigns; a newsletter app builds a repeat-customer email list.


### Lab 8 — Create Discounts and a Marketing Plan

Learning outcome: LO6 — Develop and review Shopify store marketing and site performance.

Goal: Draft a one-page marketing plan for your store using the 7-step framework, then implement your first promotion: a discount code and an automatic discount with usage limits and active dates.

**What you'll build**

A one-page marketing plan plus two live promotions — a LAUNCH10 discount code and an automatic spend-more discount.   (Tools: Shopify admin — Discounts, Marketing page, marketing plan worksheet.)

**Step-by-step**

1. Draft your marketing plan (one page): 1 define your message — what makes your store special; 2 understand your customers; 3 choose tactics (content, email, ads, promotions); 4 set a goal (e.g. 250 new customers in 6 months); 5 choose channels; 6 decide how you will analyse impact; 7 review and repeat.
2. From your Shopify admin, go to Discounts and click Create discount → Discount code.

   ```
   Shopify admin → Discounts → Create discount
   ```

3. Name the code LAUNCH10 (or click Generate code). Select type Percentage and enter Discount value 10%.
4. In Applies to, choose Entire order (or specific collections/products). In Customer eligibility, choose Everyone.
5. In Usage limits, tick Limit number of times this discount can be used in total (e.g. 100) and Limit to one use per customer. Set the Active dates, then click Save discount.
6. Click Create discount → Automatic discount. Name it SPEND150-SAVE15, type Fixed amount $15, applies to Entire order, minimum purchase amount $150. Set the active dates and click Save discount.
7. Test on the storefront: apply LAUNCH10 at checkout and confirm 10% comes off; build a $150 cart and confirm $15 is deducted automatically.
8. Open the Marketing page in your admin and note where campaign performance (sessions, sales and orders from marketing, ad spend) will appear as your promotions run.

   ```
   Shopify admin → Marketing
   ```


**Test it**

Both discounts show as Active on the Discounts page; LAUNCH10 works at checkout and the automatic discount triggers at $150; your one-page marketing plan states message, customers, tactics, goal, channels and how you will measure impact.

> **Note:** A lab summary is in labs/lab-08-*.md. If the Shopify admin looks different from these steps, Shopify has updated its UI — the setting names stay the same; use the admin search bar to find them.

---


### Lab 9 — Set Up SEO, Analytics and Newsletter

Learning outcome: LO6 — Develop and review Shopify store marketing and site performance.

Goal: Make the store measurable and findable: tune SEO metadata with your keywords, connect Google Analytics, understand where the Facebook Pixel and Google Ads tag go, install a newsletter app and read the built-in performance reports.

**What you'll build**

A store with keyword-optimised metadata, Google Analytics connected, a newsletter signup, and a review of the store's traffic and conversion reports.   (Tools: Shopify admin — Online Store → Preferences, Google Analytics, Shopify App Store (newsletter app), Analytics reports.)

**Step-by-step**

1. List 5 keywords your customers would search for your products. Add them naturally to your page titles, meta descriptions, image ALT text and body content (Products → Edit website SEO; Online Store → Preferences for the home page).
2. Shopify handles technical SEO automatically — canonical tags, sitemap.xml, robots.txt and theme title tags. Submit your sitemap (your-store.com/sitemap.xml) to Google Search Console so Google can crawl and index the store.
3. Create a Google Analytics property at https://analytics.google.com — add your store URL and copy the Google tag / Measurement ID.
4. In your Shopify admin, connect Google Analytics: install the official Google & YouTube channel app and paste your Measurement ID (this replaces the old Preferences paste-in box).

   ```
   Shopify admin → Apps → Google & YouTube channel
   ```

5. Note where other trackers live: the Facebook/Meta Pixel is added via the Facebook channel app, and a Google Ads conversion global site tag is pasted between the <head> tags of theme.liquid (Online Store → Themes → Actions → Edit code) when you run paid ads.
6. Go to https://apps.shopify.com/, search for an email marketing app (e.g. Shopify Email, Mailchimp or Klaviyo) and click Install. Enable the newsletter signup section in your theme footer.
7. Open Analytics in your admin: review Online store sessions, the Online store conversion funnel (sessions → add to cart → checkout → converted), Top traffic sources and Top traffic locations.

   ```
   Shopify admin → Analytics
   ```

8. Write down one improvement action from the data (e.g. a top traffic source worth more content, or a funnel step losing customers) — this is the review-and-improve loop the course is about.

**Test it**

Google Analytics Realtime shows your own visit to the storefront; the newsletter signup accepts a test email; you can name your store's top traffic source and the weakest step of the conversion funnel from the Analytics reports.

> **Note:** A lab summary is in labs/lab-09-*.md. If the Shopify admin looks different from these steps, Shopify has updated its UI — the setting names stay the same; use the admin search bar to find them.

---


## Running the Store After Class — Your Weekly Routine

The course ends, the store does not. A successful eCommerce store is a review-and-improve loop:

- Daily: check Orders — fulfill promptly, watch the fraud indicators before shipping.
- Weekly: review Analytics — sessions, conversion funnel, top traffic sources and locations.
- Weekly: publish one piece of content (product, blog post or social post) with your keywords.
- Monthly: review your marketing plan — keep tactics that convert, drop those that don't.
- Monthly: audit content — outdated products, broken links, stale banners, unanswered contact messages.
- Quarterly: revisit pricing plan, shipping rates, taxes and app subscriptions.


## Glossary

- **CMS** — Content Management System — software for creating, managing and publishing web content; your Shopify store is a CMS for commerce.
- **Storefront** — The public website customers see; the admin is the back office where you manage it.
- **Theme** — A template controlling the look and feel of your storefront; customised in the theme editor, published one at a time.
- **Liquid** — Shopify's template language — edit theme code only when the theme editor has no setting for what you need.
- **Variant** — One sellable combination of a product's options (e.g. Black / M) with its own price, SKU and stock.
- **SKU** — Stock Keeping Unit — your internal code for tracking a product or variant.
- **Collection** — A grouping of products (manual or automated by conditions) used for navigation and the catalog page.
- **Fulfillment** — Picking, packing, labelling and shipping the items of an order.
- **Chargeback** — A card payment reversed by the customer's bank — often the cost of a fraudulent order.
- **Meta description** — The page summary shown under the title on search engine results pages.
- **SEO** — Search Engine Optimization — improving your store's ranking so shoppers find you.
- **Conversion rate** — The percentage of sessions that result in an order.
- **Abandoned checkout** — A checkout the customer started but did not complete — recoverable by email.
- **Dropshipping** — A fulfillment model where a supplier ships products directly to your customer.
- **Facebook (Meta) Pixel** — A tracking tag that records store actions for ad targeting and measurement.
