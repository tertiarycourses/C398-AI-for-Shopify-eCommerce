# Lab 9 — Set Up SEO, Analytics and Newsletter

**Course:** AI for Shopify eCommerce (C398)  
**Topic 06:** Marketing and Performance  
**Learning outcome:** LO6 — Develop and review Shopify store marketing and site performance

## Goal

Make the store measurable and findable: tune SEO metadata with your keywords, connect Google Analytics, understand where the Facebook Pixel and Google Ads tag go, install a newsletter app and read the built-in performance reports.

## What you'll build

A store with keyword-optimised metadata, Google Analytics connected, a newsletter signup, and a review of the store's traffic and conversion reports.

**Tools:** Shopify admin — Online Store → Preferences, Google Analytics, Shopify App Store (newsletter app), Analytics reports

## Steps

1. List 5 keywords your customers would search for your products. Add them naturally to your page titles, meta descriptions, image ALT text and body content (Products → Edit website SEO; Online Store → Preferences for the home page).
2. Shopify handles technical SEO automatically — canonical tags, sitemap.xml, robots.txt and theme title tags. Submit your sitemap (your-store.com/sitemap.xml) to Google Search Console so Google can crawl and index the store.
3. Create a Google Analytics property at https://analytics.google.com — add your store URL and copy the Google tag / Measurement ID.
4. In your Shopify admin, connect Google Analytics: install the official Google & YouTube channel app and paste your Measurement ID (this replaces the old Preferences paste-in box).

   `Shopify admin → Apps → Google & YouTube channel`

5. Note where other trackers live: the Facebook/Meta Pixel is added via the Facebook channel app, and a Google Ads conversion global site tag is pasted between the <head> tags of theme.liquid (Online Store → Themes → Actions → Edit code) when you run paid ads.
6. Go to https://apps.shopify.com/, search for an email marketing app (e.g. Shopify Email, Mailchimp or Klaviyo) and click Install. Enable the newsletter signup section in your theme footer.
7. Open Analytics in your admin: review Online store sessions, the Online store conversion funnel (sessions → add to cart → checkout → converted), Top traffic sources and Top traffic locations.

   `Shopify admin → Analytics`

8. Write down one improvement action from the data (e.g. a top traffic source worth more content, or a funnel step losing customers) — this is the review-and-improve loop the course is about.

## Test it

Google Analytics Realtime shows your own visit to the storefront; the newsletter signup accepts a test email; you can name your store's top traffic source and the weakest step of the conversion funnel from the Analytics reports.
