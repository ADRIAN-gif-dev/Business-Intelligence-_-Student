# EPIC Story: Amazon Electronics Data Sales Analysis

## 1. Engage 
> The Business Problem Realized
Our analysis focuses on understanding how different electronics products perform on Amazon, with the goal of improving inventory and pricing decisions. The electronics market is crowded, especially with accessories such as cables and adapters, and we want to determine which products truly drive customer interest and how pricing affects customer satisfaction.

> Build-up question:
> How can we use high-volume but low-cost items to boost overall revenue, and does increasing the price of premium products affect customer ratings negatively?

---

## 2. Present
> The Data Visuals
Using the Amazon Sales dataset, our team generated several visualizations to highlight the most essential patterns in product categories, customer engagement, pricing, and ratings.

### A. Product Dominance
**Chart used:** `visuals/bar_categories.png`
- USB Cables appear most frequently in the dataset, dominating the market.
- Their presence is nearly three times that of the next leading category.

### B. Customer Interaction
**Chart used:** `visuals/bar_top_reviews.png`
- Products with the highest number of reviews are mostly low-cost accessories.
- Items such as MicroUSB and HDMI cables consistently attract high customer engagement.

### C. Pricing and Customer Satisfaction
**Charts used:** `visuals/scatter_price_rating.png`, `visuals/hist_ratings.png`
- There is no strong relationship between higher prices and higher ratings.
- Many expensive items (above 50k) average around 4.0 stars, while cheaper accessories often reach above 4.5 stars.
- Overall effect is positive, with most products rated between 4.0 and 4.5.

### D. Correlation Insights
**Chart used:** `visuals/heatmap_correlation.png`
- A small negative correlation (**-0.24**) exists between `discounted_price` and `rating`.
- This suggests that as prices increase, customer ratings tend to decrease slightly.

---

## 3. Interpret
> What the Patterns Mean

### 1. Accessories Drive Customer Activity
Low-cost products, especially cables, play a major role in attracting customers. They may not generate high revenue per item, but they consistently bring traffic to the store due to their volume.

### 2. Higher Prices Lead to Higher Expectations
Premium products receive more scrutinization. When an expensive item underperforms, lower ratings reflect higher customer expectations, which aligns with the negative price-rating correlation.

### 3. Strong Overall Customer Satisfaction
Most products perform well in terms of ratings. Any product below 3.5 stars stands out and should be investigated by inventory or quality teams.

---

## 4. Conclude 
> Recommendations
Based on the findings, the following actions are recommended:

### Increase the quantity of high-demand accessories
Maintain strong stock levels for USB and HDMI cables. These items have high turnover and contribute significantly to customer engagement.

### Increase quality checks for premium products
For products priced above ₹20,000, introduce more thorough quality control. These customers expect reliability, and negative reviews tend to be more severe on revenue.

### Apply strategic pricing
- Since higher prices are linked to slightly lower ratings, avoid aggressive price increases for mid-range electronics. 
- Competitive pricing or moderate discounts can help preserve customer satisfaction.