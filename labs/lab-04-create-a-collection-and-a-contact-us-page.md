# Lab 4 — Create a Collection and a Contact Us Page

**Course:** AI for Shopify eCommerce (C398)  
**Topic 03:** Customizing Theme  
**Learning outcome:** LO3 — Improve customer experience by customising Shopify theme

## Goal

Control the catalog page with an automated 'All' collection, then add a Contact Us page using the built-in page.contact template so customers can reach you.

## What you'll build

An automated All collection ordering your catalog page, plus a working Contact Us page with a built-in contact form.

**Tools:** Shopify admin — Collections, Pages, page.contact template

## Steps

1. From your Shopify admin, go to Products → Collections and click Create collection.

   `Shopify admin → Products → Collections`

2. Give the collection the title All. In the Collection type section, select Automated.
3. Set the condition Product price is greater than 0. Optional: to hide sold-out products, add Inventory stock is greater than 0. Click Save.
4. Visit your-store.myshopify.com/collections/all and note the catalog page order now follows your All collection.
5. Go to Online Store → Pages and click Add page.

   `Shopify admin → Online Store → Pages → Add page`

6. In the Title box type Contact Us. In the Content box add a short welcome line such as 'We would love to hear from you.'
7. In the Template section (Theme template), choose contact (page.contact) from the drop-down. Click Save.
8. Go to Online Store → Navigation, open the Main menu, click Add menu item, name it Contact Us and link it to your new page. Click Save menu.

## Test it

Open the storefront: the Contact Us link must appear in the main menu and the page must show a working contact form (Name, Email, Message). Submit a test message to yourself.
