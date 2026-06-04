# Last Mile Logistics Auditor

## Project Overview
An audit tool for Veridi Logistics to identify root causes of delivery delays and customer dissatisfaction in their last-mile delivery network.

## Problem Statement
The CEO noticed a spike in negative reviews and suspects the issue is inaccurate estimated delivery dates, not just late packages.

## Key Findings
- **Remote states** have 2x higher late rates (28% vs 14%)
- **Strong negative correlation** (-0.45) between delivery delays and review scores
- **Worst seller** has 64.3% late delivery rate
- **Furniture/Decor** categories have highest delay rates (28%)

## Data Source
Olist Brazilian E-Commerce Dataset (Kaggle)

## Technologies Used
- Python (Pandas, NumPy)
- Streamlit (Dashboard)
- Plotly (Visualizations)
- Google Colab (Analysis)

## Data Cleaning Steps
1. Removed duplicate orders (kept most recent reviews)
2. Filtered to delivered orders only
3. Converted dates to datetime format
4. Handled missing delivery dates
5. Translated product categories (Portuguese → English)

## Dashboard Features
- Geographic heatmap by state
- Sentiment correlation analysis  
- Remote vs non-remote state comparison
- Seller performance audit
- Product category analysis (English)

## How to Run

### 1. Install Requirements
```bash
pip install -r requirements.txt