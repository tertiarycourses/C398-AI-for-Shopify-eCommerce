# Lab 7 — Configure Shipping Rates and Taxes

**Course:** AI for Shopify eCommerce (C398)  
**Topic 05:** Payment and Shipping  
**Learning outcome:** LO5 — Manage payment and shipping issues on Shopify store

## Goal

Plan your shipping strategy and implement it: add product weights, create a Singapore shipping zone with a flat rate, add free shipping for orders above $200, and review tax settings for the regions you sell to.

## What you'll build

A working shipping setup — Singapore zone with a flat rate plus free shipping over $200 — and taxes configured for your selling regions.

**Tools:** Shopify admin — Settings → Shipping and delivery, Settings → Taxes and duties

## Steps

1. Decide your strategy first: free shipping (build cost into price), exact carrier rates, or flat rates. Flat rate + free-above-threshold is the common starter combination — it also lifts average order value.
2. Confirm every physical product has a weight (Products → your product → Shipping section) so rates based on weight work correctly.
3. From your Shopify admin, go to Settings → Shipping and delivery. In General shipping rates, click the General profile to edit it.

   `Shopify admin → Settings → Shipping and delivery`

4. Click Create shipping zone, name it Singapore and select Singapore. Click Done.
5. In the Singapore zone, click Add rate → Use flat rate. Name it Standard Delivery, price $5. Click Done.
6. Click Add rate again. Name it Free Shipping, price $0, then click Add conditions → Based on order price → Minimum price $200. Click Done, then Save.
7. Go to Settings → Taxes and duties, open Singapore and review the GST treatment for your store (charge GST only if your business is GST-registered).
8. Run a test checkout: a cart under $200 must offer Standard Delivery $5; add items past $200 and Free Shipping must appear.

## Test it

Checkout shows Standard Delivery ($5) below $200 and Free Shipping at/above $200 for a Singapore address; product weights and tax regions are in place.
