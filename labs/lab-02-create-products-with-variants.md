# Lab 2 — Create Products with Variants

**Course:** AI for Shopify eCommerce (C398)  
**Topic 02:** Setting Up Products  
**Learning outcome:** LO2 — Curate product and web content on Shopify store

## Goal

Stock the store two ways: bulk-import the course's mock product catalog (labs/data/mock-products.csv — 6 ready-made products with variants), then add a shirt product manually with a complete product page — title, description, images, pricing, inventory, Colour and Size variants, search engine listing, tags and sales channels.

## What you'll build

A stocked store: 6 imported mock products plus a fully-curated shirt with Colour/Size variants, SEO listing, tags and sales channels.

**Tools:** Shopify admin — Products, CSV product import, product images, SEO listing editor

## Steps

1. Get the mock product catalog mock-products.csv from the labs/data folder of the course repository (also in the Activities folder on the course Drive). It contains 6 ready-made products — shirts, yoga gear and a virtual class package — in Shopify's product CSV format.

   `labs/data/mock-products.csv`

2. From your Shopify admin, go to Products and click Import. Click Add file, select mock-products.csv, then click Upload and preview.

   `Shopify admin → Products → Import`

3. Review the preview (it shows the first product) and click Import products. Shopify emails you when the import completes — refresh the Products page to see all 6 mock products with their variants and prices.
4. Spot-check an imported product (e.g. Pro Yoga Mat): open it and confirm the Colour/Length variants, prices and stock came in. If a product image failed to download from the image URL, add one manually from burst.shopify.com or unsplash.com.
5. Now add a product manually: go to Products → All products and click Add product.

   `Shopify admin → Products → Add product`

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

## Test it

The Products page must list the 6 imported mock products plus your shirt. On the storefront, the shirt's Colour and Size selectors must switch price and image per variant, and the Google preview in Edit website SEO must show your custom title and description.
