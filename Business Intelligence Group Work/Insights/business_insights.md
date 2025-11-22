## Amazon Product Data Insights

This document summarizes key business decisions and insights derived from the analysis of Amazon product data, covering trends in product categories, pricing strategies and customer satisfaction.

# 1. Product Strategy and Inventory Management
The product count distribution and top-reviewed items indicate priority areas for inventory and development focus.

**Focus on High-Volume categories: USB Cables, Smartwatches and Smartphones are the most numerous categories in the dataset, with USB Cables alone accounting for over 230 products.
    **Decision: Continue to invest heavily in inventory and development within these segments, as they represent high-demand areas.

**Prioritize Top-Reviewed Products: THe top 10 most reviewed products all hover near 900 to 1000 reviews.
    **Decision: These are flagship or high-performing items that should be prioritized for:
       -Inventory Security: Maintain consistent stock levels to meet predictable high demand.
       -Marketing Focus: Leverage their proven popularity in major promotional campaigns.
       -Quality Control: Ensure quality remains exceptionally high to preserve their strong social proof which is evident in the high review counts.

# 2. Pricing and Discounting Strategy
Analysis of price and discount columns reveals important trends in perceived value and consumer appeal.

**Weak Price-to-Rating Relationship: The scatter plot of Actual Price vs Rating shows a large cluster of products across a broad price range maintaining high ratings(4.0 to 4.5 stars).
    **Decision: Avoid assuming a high price automatically justifies a higher rating or signals superior quality to customers. Focus on competitive pricing while maintaining quality, as budget-friendly items can achieve equally high ratings.

**Optimal Discount Band: The most frequently occuring discount percentages are 50% and 60%.
    **Decision: These psychological price points appear to be highly effective at driving customer conversions. Promotional planning should utilise discounts within this range to maximize consumer interest.

**Strong Price Correlation: The discounted price and actual price show a very high correlation, indicating that the sale price is tightly linked to the original price.

# 3. Quality Control and Customer Satisfaction
The product rating distribution highlights customer expectations and critical benchmarks for product quality.

**High Rating Concentration: The distribution of product ratings is highly concentrated, with the majority of products rated between 4.0 stars and 4.5 stars. The most frequent single top rating is 4.1 stars with 244 occurences.
    **Decision: The market standard is high. Any product performing below 4.0 stars should be flagged for immediate review and quality improvement, as it is falling below average customer expectation.
**Positive Feedback Analysis: Focus on analysing the rich, descriptive positive reviews found for high-rated products, such as those with a 4.1 star-rating, in order to identify and amplify specific positive product attributes in future product descriptions and advertising copy.