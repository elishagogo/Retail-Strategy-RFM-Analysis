# Business Requirements Document (BRD)

## Project Overview
**Project Name:** Customer Lifecycle & Revenue Optimization (Online Retail II)\
**Date:** February 2026\
**Business Analyst:** Elisha Lee\
**Version:** 1.0

## Executive Summary
THis project analyzes the Online Retail II dataset to transform raw transactional logs
into a strategic custome segmentation model. By applying RFM (Recency, Frequency, Monetary) analysis,
we will identify high-value "Champions" and "At-Risk" segments to drive a 15% revenue increase through
targeted retention.

## Business Objectives
1. Segment the Customer Base: Categorize 4,000+ customers into 
   actionable groups (e.g., VIP, At-Risk, New).
2. Identify Revenue Leakage: Quantify the value of customers who haven't purchased in >90 days.
3. Optimize Product Mix: Identify the top 10% of Stock Codes 
   contributing to 80% of the revenue (Pareto Analysis).

## Stakeholders
- **Marketing Manager:** Needs customer lists for segmented email campaigns.
- **Inventory Lead:** Needs to know which products drive repeat purchases.
- **Head of Data:** Requires a reproducible Python/SQL pipeline and a Tableau dashboard.

## Scope
### In Scope
- **Data Cleaning:** Handling 500k+ rows, including removing "C" prefix cancellations.
- **RFM Modeling:** Feature engineering using Python/Pandas.
- **Interactive Visualization:** A Tableau Public dashboard with drill-down capabilities
    by Country and Segment.
- **Actionable Insights:** Specific "Next-Step" recommendations for each customer segment.

### Out of Scope
- Predictive Machine Learning models (e.g., K-Means)
- Real-time data streaming.

## Functional Requirements
1. **Data Collection**
   - Calculate Total_Sum as Quantity * Price.
   - Filter out non-customer transactions (Null Customer ID).
   - Separate "Manual" and "Postage" fees from actual product sales.
   - Handle missing or incorrect data

2. **Data Analysis**
   - Calculate key performance indicators (KPIs): Compute monthly Total Revenue,
     Average Order Value (AOV), and Unique Customer Count.
   - Identify sales trends and seasonal patterns.
   - Segment customers based on behavior, such as Recency (last purchase),
     Frequency ()
   - Compare regional performance by comparing the UK market performance against International markets.

3. **Reporting**
   - Tableau Executive Dashboard: Create a high-level view 
     for the Finance team showing revenue trends and top-selling products.
   - Marketing Drill-Down: Create a specific view that lists "At-Risk" Customer IDs 
     so the Marketing team can export them for a "Win-Back" campaign.
   - Actionable Recommendations: Provide a summary of the top 3 segments to target for the next quarter.

## Success Criteria
- Report generation completed within 2 hours
- Data accuracy rate of 99% or higher
- Actionable insights delivered to stakeholders
- Positive feedback from stakeholders (>80% satisfaction)

## Key Performance Indicators (KPIs)
1. Gross Revenue: Total sales before returns.
2. Net Revenue: Revenue after subtracting the "C" prefix cancellations (returns).
3. Repeat Purchase Rate: Percentage of customers who bought more than once.
4. Customer Value (CV): The average revenue per customer.
5. Churn Risk %: Percentage of customers who haven't purchased in over 90 days.
6. Return Rate: The ratio of cancelled invoices to total invoices (crucial for retail).


## Risks and Mitigation
| Risk | Impact | Probability | Mitigation Strategy |
|------|--------|-------------|---------------------|
| Data Noise | High | High | Explicitly filter out Invoice codes starting with "C". |
| Outliers | Medium | High | Identify and isolate bulk oders that skew averages |
| Missing Identity | High | Low | Drop rows without Cusomer ID since they cannot be used for segmentation |
| Currency Inconsistency | Low | Low | The dataset is in GBP for all transactions |

