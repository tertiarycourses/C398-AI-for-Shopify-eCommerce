# Lab 5 — Process, Fulfill and Refund an Order

**Course:** AI for Shopify eCommerce (C398)  
**Topic 04:** Managing Orders  
**Learning outcome:** LO4 — Manage orders on Shopify store

## Goal

Place a trial order on your own store using a manual payment method, then work the full order lifecycle in the admin — view the order and its Timeline, fulfill it, and process a partial refund.

## What you'll build

A completed order lifecycle: a test order that has been viewed, paid, fulfilled and refunded, with the Timeline recording every event.

**Tools:** Shopify admin — Orders, order Timeline, fulfillment, refunds

## Steps

1. On your storefront, add your shirt product to the cart and check out as a customer. Choose the manual payment method (e.g. Bank Deposit — set up in Lab 6, or Cash on Delivery) and complete the order.
2. From your Shopify admin, go to Orders — the new order appears with a yellow Payment pending / Unfulfilled badge. Click the order number to open it.

   `Shopify admin → Orders`

3. Scroll to the Timeline section and expand the events — order placed, confirmation email sent. The Timeline is your audit trail for troubleshooting payments and refunds.
4. Click Collect payment → Mark as paid to record receipt of the manual payment.
5. Click Fulfill item(s). Optionally add a tracking number, tick Send shipment details to your customer now, then click Fulfill items — the order is now marked Fulfilled.
6. Add a Tag (e.g. test-order) and a Note (e.g. staff training order) in the right panel so the order is searchable.
7. Click Refund. Enter the quantity to refund — Shopify recalculates the Refund total. Untick Restock items if stock did not come back; keep Send a notification to the customer ticked. Click Refund.
8. Back on the Orders page, select the order and choose Archive to remove it from your open orders list.

## Test it

The order page must show Paid → Fulfilled → Refunded events on the Timeline, and the customer email inbox must have the confirmation, shipment and refund notifications.
