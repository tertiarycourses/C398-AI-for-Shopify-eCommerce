# Lab 6 — Set Up Payment Methods

**Course:** AI for Shopify eCommerce (C398)  
**Topic 05:** Payment and Shipping  
**Learning outcome:** LO5 — Manage payment and shipping issues on Shopify store

## Goal

Configure how your store gets paid: activate PayPal, add a manual Bank Deposit method with customer instructions, set automatic payment capture and review Shopify's fraud analysis indicators.

## What you'll build

A store that accepts PayPal and Bank Deposit, captures card payments automatically, and a fraud-check routine for suspicious orders.

**Tools:** Shopify admin — Settings → Payments, PayPal, manual payment methods

## Steps

1. From your Shopify admin, go to Settings → Payments.

   `Shopify admin → Settings → Payments`

2. In the PayPal section, select your PayPal account type and click Activate. Enter the email address and password for your PayPal account, click I Give Permission, then Go back to Shopify. (No PayPal account yet? Shopify created a PayPal Express Checkout entry for your store email — sign up with the same email.)
3. In the Manual payment methods section, click Add manual payment method → Bank Deposit.
4. In Additional details, enter what the customer sees at checkout (e.g. 'Pay by PayNow/bank transfer within 24 hours'). In Payment instructions, enter your bank account / PayNow details shown on the order confirmation page. Click Activate.
5. In the Payment capture section, choose Automatically capture payment for orders. Click Save.
6. Review fraud prevention practice for every suspicious order: verify the IP address, call the phone number, search the email address, check that billing and shipping addresses match, and review high-value orders before fulfilling.
7. Place a test checkout on your storefront and confirm both PayPal and Bank Deposit appear as payment options.

## Test it

Your checkout must offer PayPal and Bank Deposit; the Bank Deposit order confirmation page must show your payment instructions; Settings → Payments must show automatic capture enabled.
