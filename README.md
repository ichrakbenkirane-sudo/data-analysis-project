# Taobao Shopper Behavior Analysis

## Project Question
Where do Taobao shoppers drop off between viewing a product and buying it, and what do buyers do differently?

## Data
Taobao User Behavior dataset (Kaggle / Alibaba Tianchi). I analyzed a sample of the first 2,000,000 rows. Columns: user_id, item_id, category_id, behavior (pv, cart, fav, buy), timestamp.

## Tools
Python, pandas, matplotlib

## Findings

### 1. Shoppers drop off most between viewing and adding to cart
In the sample, there were 1,791,216 product views, 111,015 cart adds (about 6.2% of views) and 40,243 purchases (about 2 purchases per 100 views).

![Funnel](funnel.png)

### 2. Purchases peak in the evening
Purchases are highest between 20:00 and 22:00 (China time), stay steady from 10:00 to 16:00, and are lowest between 02:00 and 06:00. Evening promotions are likely to reach the most buyers.

![Purchases by hour](hours.png)

### 3. Most users buy, but they browse a lot first
Counting unique users instead of actions: 19,463 users viewed products, 14,672 (about 75%) added something to the cart, and 13,330 (about 68.5%) made a purchase. Compared with the action-level funnel (about 2 purchases per 100 views), this shows that shoppers view many products and buy only a few. Because the dataset covers about 9 days of activity from active users, these rates are higher than a typical store's conversion rate.

## Limitations
This is a sample of the first 2 million rows, and the counts are actions, not unique users. The sample is the first 2 million rows of the file, which is ordered by user ID, so it is not a random sample.

## How to run
1. Download UserBehavior.csv from Kaggle ("User Behavior Data from Taobao for Recommendation") and put it in the same folder as analysis.py.
2. Install the libraries: `pip install pandas matplotlib`
3. Run: `python analysis.py`

The script saves sample.csv, funnel.png and hours.png and prints the action and user counts.
