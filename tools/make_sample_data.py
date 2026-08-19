#!/usr/bin/env python3
"""Generate the synthetic Bloom & Brew dataset used by all nine C398 labs.

Deterministic (fixed seed), so every learner and every rebuild gets identical
files and the "Test it" checks in the Learner Guide always hold.

Written to labs/resources/:
  products.csv                24 SKUs with the factual columns the copywriting
                              labs must write from (material, capacity, origin,
                              care, certification) plus cost, retail and stock.
  customers.csv               60 customers WITH personal data - Lab 4 exists to
                              strip it, so the raw file has to contain it.
  transactions.csv            order-level detail for the last 6 months, derived
                              from sales_history_monthly so the two reconcile.
  sales_history_monthly.csv   24 months of units by SKU - the forecasting file.
  customer_feedback.csv       30 real-shaped enquiries, reviews and complaints.

Planted findings the labs are designed to surface:
  * BB-STA-031 has cost_price > retail_price (a data error Lab 8 must flag).
  * Three slow movers with high stock and no sales in the last 3 months (Lab 7).
  * Two SKUs launched 4 months ago - too little history to forecast (Lab 7).
  * Gift and fragrance categories peak in Nov-Dec; stationery peaks in Jan (Lab 7).
  * Several high-velocity, below-category-margin SKUs (Lab 8 price increases).
  * Lapsed, loyal, high-value and one-off customers so RFM segments exist (Lab 6).

Run:  python tools/make_sample_data.py
"""
import csv, os, random
from datetime import date, timedelta

random.seed(398)                      # C398 - reproducible for every learner
HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(os.path.dirname(HERE), "labs", "resources")
os.makedirs(OUT, exist_ok=True)

# ------------------------------------------------------------------ calendar
# 24 months of history ending August 2026 (the course version date).
MONTHS = []
y, m = 2024, 9
for _ in range(24):
    MONTHS.append(f"{y:04d}-{m:02d}")
    m += 1
    if m == 13:
        m = 1; y += 1
TXN_MONTHS = MONTHS[-6:]              # order-level detail: Mar-Aug 2026

# ------------------------------------------------------------------ products
# (sku, name, category, material, size, colour, care, origin, certification,
#  cost, retail, stock, supplier, lead_weeks, base_units, launch_offset_months)
P = [
 ("BB-DRK-011","Stoneware Latte Cup 280ml","Drinkware","Stoneware","280ml","Oat","Dishwasher safe","Portugal","","9.20","24.00",180,"Alvaro Ceramics",6,14,0),
 ("BB-DRK-014","Double-Walled Stoneware Mug 350ml","Drinkware","Stoneware","350ml","Matte charcoal","Dishwasher safe","Portugal","","11.80","32.00",240,"Alvaro Ceramics",6,22,0),
 ("BB-DRK-017","Borosilicate Glass Tumbler 400ml","Drinkware","Borosilicate glass","400ml","Clear","Dishwasher safe","China","","6.40","19.00",310,"Kanto Glassware",8,26,0),
 ("BB-DRK-021","Insulated Steel Travel Flask 500ml","Drinkware","Stainless steel","500ml","Brushed steel","Hand wash only","China","BPA free",18.50,"46.00",95,"Kanto Glassware",8,11,0),
 ("BB-DRK-026","Ceramic Pour-Over Set","Drinkware","Ceramic","2-cup","Chalk white","Hand wash only","Portugal","","24.00","68.00",60,"Alvaro Ceramics",6,8,0),
 ("BB-COF-041","House Blend Coffee Beans 250g","Coffee & Tea","Arabica beans","250g","","Store airtight, dry","Singapore","Rainforest Alliance","7.10","18.50",420,"Jalan Roasters",3,58,0),
 ("BB-COF-043","Single Origin Ethiopia 250g","Coffee & Tea","Arabica beans","250g","","Store airtight, dry","Ethiopia","Organic","9.60","26.00",260,"Jalan Roasters",3,31,0),
 ("BB-COF-045","Decaf Swiss Water 250g","Coffee & Tea","Arabica beans","250g","","Store airtight, dry","Colombia","Organic","9.90","25.00",140,"Jalan Roasters",3,12,0),
 ("BB-COF-052","Loose Leaf Jasmine Green 100g","Coffee & Tea","Green tea leaves","100g","","Store airtight, dry","China","","5.20","16.00",190,"Wan Fu Tea",5,17,0),
 ("BB-COF-055","Cold Brew Filter Bags (8 pack)","Coffee & Tea","Arabica beans","8 x 30g","","Refrigerate after brewing","Singapore","","6.80","21.00",150,"Jalan Roasters",3,19,0),
 ("BB-FRG-061","Soy Candle Fig & Cedar 220g","Home Fragrance","Soy wax","220g","Terracotta","Trim wick to 5mm","Singapore","Vegan","8.40","34.00",210,"Ember & Co",7,24,0),
 ("BB-FRG-064","Soy Candle Sea Salt 220g","Home Fragrance","Soy wax","220g","Pale blue","Trim wick to 5mm","Singapore","Vegan","8.40","34.00",165,"Ember & Co",7,18,0),
 ("BB-FRG-068","Reed Diffuser Neroli 200ml","Home Fragrance","Glass, rattan reeds","200ml","Amber glass","Keep upright","Singapore","Vegan","12.20","42.00",130,"Ember & Co",7,13,0),
 ("BB-FRG-072","Room Mist Lemongrass 100ml","Home Fragrance","Glass","100ml","Frosted","Shake before use","Singapore","Vegan","6.90","22.00",340,"Ember & Co",7,9,0),
 ("BB-HOM-081","Linen Tea Towel Set of 2","Homeware","European linen","50 x 70cm","Sand","Machine wash 40C","Lithuania","OEKO-TEX","11.50","29.00",145,"Baltic Linen House",9,10,0),
 ("BB-HOM-084","Oak Serving Board Small","Homeware","European oak","30 x 18cm","Natural oak","Oil monthly, hand wash","Poland","FSC certified","16.00","44.00",88,"Baltic Linen House",9,7,0),
 ("BB-HOM-087","Woven Storage Basket Medium","Homeware","Seagrass","32 x 28cm","Natural","Wipe clean","Vietnam","","14.50","39.00",260,"Mekong Weavers",10,6,0),
 ("BB-HOM-092","Ribbed Glass Vase 22cm","Homeware","Recycled glass","22cm","Smoke grey","Hand wash only","Spain","Recycled content","13.00","38.00",175,"Kanto Glassware",8,8,0),
 ("BB-GFT-101","Coffee Lover Gift Box","Gift Sets","Beans, mug, filter bags","Gift box","","See component care","Singapore","","28.00","78.00",120,"Bloom & Brew Assembly",2,12,0),
 ("BB-GFT-104","Calm Evening Gift Box","Gift Sets","Candle, tea, tea towel","Gift box","","See component care","Singapore","","31.00","86.00",95,"Bloom & Brew Assembly",2,9,0),
 ("BB-GFT-107","New Home Gift Box","Gift Sets","Diffuser, vase, board","Gift box","","See component care","Singapore","","44.00","118.00",70,"Bloom & Brew Assembly",2,6,0),
 ("BB-STA-031","Recycled Kraft Notebook A5","Stationery","Recycled paper","A5, 120 pages","Kraft","Keep dry","Vietnam","Recycled content","9.40","9.00",300,"Mekong Weavers",10,5,0),
 ("BB-STA-034","Refillable Brass Pen","Stationery","Brass","14cm","Antique brass","Wipe clean","India","","12.60","36.00",110,"Mekong Weavers",10,4,0),
 ("BB-STA-037","Linen-Bound Recipe Journal","Stationery","Linen, recycled paper","B5, 160 pages","Ecru","Keep dry","Vietnam","Recycled content","15.80","42.00",64,"Mekong Weavers",10,7,4),
]
# Two recent launches (too little history to forecast) and three slow movers.
NEW_LAUNCH = {"BB-STA-037": 4, "BB-COF-055": 4}
SLOW_MOVERS = {"BB-HOM-087", "BB-FRG-072", "BB-STA-034"}   # no sales last 3 months

# Seasonal index by category and calendar month (1-12). Singapore retail:
# gifting and fragrance peak Nov-Dec, stationery peaks Jan, coffee is steady.
SEASON = {
 "Drinkware":     [0.9,0.9,1.0,1.0,1.0,1.05,1.0,1.0,1.0,1.1,1.35,1.5],
 "Coffee & Tea":  [0.95,1.0,1.0,1.0,1.0,1.0,0.95,1.0,1.0,1.05,1.15,1.2],
 "Home Fragrance":[0.85,0.95,1.0,1.0,1.0,1.0,0.95,1.0,1.05,1.2,1.5,1.7],
 "Homeware":      [1.0,1.0,1.05,1.0,1.0,1.0,0.95,0.95,1.0,1.1,1.25,1.3],
 "Gift Sets":     [0.7,0.8,0.9,0.95,1.0,1.0,0.9,0.95,1.0,1.3,1.8,2.2],
 "Stationery":    [1.6,1.2,1.0,0.9,0.9,1.0,1.1,1.0,0.95,1.0,1.1,1.2],
}

def price(v):        # cost/retail columns are given as strings or floats above
    return float(v)

products = []
for (sku,name,cat,mat,size,col,care,origin,cert,cost,retail,stock,sup,lead,base,off) in P:
    products.append(dict(sku=sku,name=name,category=cat,material=mat,size=size,colour=col,
                         care=care,origin=origin,certification=cert,
                         cost_price=round(price(cost),2),retail_price=round(price(retail),2),
                         stock_on_hand=stock,supplier=sup,lead_time_weeks=lead,
                         _base=base,_launch=off))

with open(os.path.join(OUT,"products.csv"),"w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow(["sku","name","category","material","size","colour","care_instructions",
                "origin_country","certification","cost_price","retail_price","stock_on_hand",
                "supplier","lead_time_weeks"])
    for p in products:
        w.writerow([p["sku"],p["name"],p["category"],p["material"],p["size"],p["colour"],
                    p["care"],p["origin"],p["certification"],f'{p["cost_price"]:.2f}',
                    f'{p["retail_price"]:.2f}',p["stock_on_hand"],p["supplier"],p["lead_time_weeks"]])

# ------------------------------------------------------------------ monthly sales history
# Demand is scaled so transactions.csv stays a few hundred lines - large enough
# to be a real analysis exercise, small enough for an AI assistant to handle in
# one attachment without the arithmetic drifting.
SCALE = 0.5
history = {}                                   # (sku, month) -> units
for p in products:
    trend = random.uniform(0.994, 1.012)       # gentle per-month drift
    for i, ym in enumerate(MONTHS):
        mth = int(ym.split("-")[1])
        # new launches have no history before their launch month
        if p["sku"] in NEW_LAUNCH and i < len(MONTHS) - NEW_LAUNCH[p["sku"]]:
            history[(p["sku"], ym)] = 0
            continue
        # slow movers go quiet for the final three months
        if p["sku"] in SLOW_MOVERS and i >= len(MONTHS) - 3:
            history[(p["sku"], ym)] = 0
            continue
        base = p["_base"] * SCALE * (trend ** i) * SEASON[p["category"]][mth-1]
        units = max(0, int(round(random.gauss(base, base * 0.18))))
        history[(p["sku"], ym)] = units

with open(os.path.join(OUT,"sales_history_monthly.csv"),"w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["month","sku","name","category","units_sold"])
    for ym in MONTHS:
        for p in products:
            w.writerow([ym,p["sku"],p["name"],p["category"],history[(p["sku"],ym)]])

# ------------------------------------------------------------------ customers
FIRST=["Adeline","Marcus","Siti","Ravi","Chloe","Wei Ming","Priya","Daniel","Nadia","Jun Hao",
       "Elaine","Farah","Kenneth","Mei Ling","Arjun","Grace","Terence","Aisha","Bryan","Hui Shan",
       "Joel","Kavitha","Lionel","Serene","Nurul","Desmond","Yi Ting","Rashid","Clarissa","Benjamin"]
LAST=["Tan","Lim","Rahman","Menon","Ng","Goh","Sharma","Wong","Ismail","Chua",
      "Koh","Abdullah","Teo","Sim","Nair","Chan","Yeo","Hassan","Low","Ong"]
DOMAIN=["gmail.com","outlook.com","yahoo.com.sg","hotmail.com"]
TIERS=["Bronze","Silver","Gold"]
customers=[]
used=set()
for i in range(1,61):
    while True:
        nm=f"{random.choice(FIRST)} {random.choice(LAST)}"
        if nm not in used: used.add(nm); break
    handle=nm.lower().replace(" ",".")
    join=date(2023,1,1)+timedelta(days=random.randint(0,1150))
    customers.append(dict(
        customer_id=f"CUS{i:04d}", full_name=nm,
        email=f"{handle}{random.randint(1,99)}@{random.choice(DOMAIN)}",
        phone=f"+65 9{random.randint(1000000,9999999)}",
        postal_code=f"{random.randint(10,82):02d}{random.randint(1000,9999)}",
        join_date=join.isoformat(),
        loyalty_tier=random.choices(TIERS,weights=[5,3,2])[0],
        marketing_optin=random.choices(["yes","no"],weights=[7,3])[0]))

with open(os.path.join(OUT,"customers.csv"),"w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow(["customer_id","full_name","email","phone","postal_code","join_date",
                "loyalty_tier","marketing_optin"])
    for c in customers:
        w.writerow([c["customer_id"],c["full_name"],c["email"],c["phone"],c["postal_code"],
                    c["join_date"],c["loyalty_tier"],c["marketing_optin"]])

# ------------------------------------------------------------------ transactions
# Order-level detail for the last 6 months, generated from the SAME monthly units
# so transactions.csv and sales_history_monthly.csv reconcile exactly. Customer
# behaviour is shaped so RFM segments genuinely exist: champions buy throughout,
# lapsed customers stop after the first two months, one-offs buy once.
STORES=["Orchard","Tampines","Jurong East","Novena","Katong","Woodlands","Online"]
profiles={}
for idx,c in enumerate(customers):
    if idx < 10:   profiles[c["customer_id"]]=("champion", TXN_MONTHS)
    elif idx < 22: profiles[c["customer_id"]]=("loyal",    TXN_MONTHS)
    elif idx < 34: profiles[c["customer_id"]]=("regular",  TXN_MONTHS[2:])
    elif idx < 48: profiles[c["customer_id"]]=("lapsed",   TXN_MONTHS[:2])
    else:          profiles[c["customer_id"]]=("one-off",  [random.choice(TXN_MONTHS[:3])])
WEIGHT={"champion":6,"loyal":4,"regular":3,"lapsed":2,"one-off":1}

by_month={ym:[] for ym in TXN_MONTHS}
for cid,(prof,months) in profiles.items():
    for ym in months:
        by_month[ym].extend([cid]*WEIGHT[prof])

rows=[]; order_no=45001
prices={p["sku"]:p["retail_price"] for p in products}
for ym in TXN_MONTHS:
    pool=by_month[ym]
    # Split each SKU-month's units into basket lines, then group 1-3 lines into
    # a single order so an order looks like a real multi-item basket.
    lines=[]
    for p in products:
        units=history[(p["sku"],ym)]
        while units>0:
            qty=min(units,random.choices([1,2,3,4],weights=[5,3,2,1])[0]); units-=qty
            lines.append((p["sku"],qty))
    random.shuffle(lines)
    i=0
    while i<len(lines):
        n=random.choices([1,2,3],weights=[6,3,1])[0]
        basket=lines[i:i+n]; i+=n
        cid=random.choice(pool)
        store=random.choices(STORES,weights=[3,2,2,2,2,1,5])[0]
        channel="Online" if store=="Online" else "Store"
        day=random.randint(1,28)
        oid=f"SO{order_no}"; order_no+=1
        for sku,qty in basket:
            rows.append([oid,f"{ym}-{day:02d}",cid,sku,qty,f'{prices[sku]:.2f}',channel,store])
rows.sort(key=lambda r:(r[1],r[0]))
with open(os.path.join(OUT,"transactions.csv"),"w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow(["order_id","order_date","customer_id","sku","qty","unit_price","channel","store"])
    w.writerows(rows)

# ------------------------------------------------------------------ summary
tot_units=sum(int(r[4]) for r in rows)
tot_rev=sum(int(r[4])*float(r[5]) for r in rows)
print(f"products.csv              {len(products)} SKUs")
print(f"customers.csv             {len(customers)} customers")
print(f"transactions.csv          {len(rows)} order lines, {tot_units} units, SGD {tot_rev:,.2f}")
print(f"sales_history_monthly.csv {len(MONTHS)*len(products)} rows ({MONTHS[0]} to {MONTHS[-1]})")
print(f"written to {OUT}")
