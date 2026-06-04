# Last Mile Logistics Auditor

## Executive Summary
I analyzed 96,478 delivered orders and found that remote states have much higher late delivery rates than other regions. There is a clear link between delivery delays and customer reviews, where late packages receive much lower ratings. One seller stands out with a 64.3% late rate, and I recommend auditing this seller immediately while adjusting delivery estimates for remote states.

## Project Links
- **Link to Notebook:** https://colab.research.google.com/drive/1OK6LAKf4ZWv_TWxi-ghO8AqBvHPbxC1O?usp=sharing
- **Link to Dashboard:**https://last-mile-logistics-auditor-rniel3bsf8zhpvyq6j3a96.streamlit.app/
- **Link to Presentation:**https://canva.link/zbzy84xn0k2yw6z


## Technical specifications
**Data Cleaning Steps**
1. Removed 551 duplicate orders (kept most recent reviews)
2. Filtered to delivered orders only
3. Converted dates to datetime format
4. Handled missing delivery dates
5. Translated product categories (Portuguese → English)

**Candidate's Choice: Seller performance analysis**
- I identified which specific sellers are causing the most delivery delays by analyzing their individual performance.

**Note:** My analysis code (Colab notebook) handles data processing and exports CSV files. 
All visualizations are in the **Streamlit dashboard** (`app.py`), which reads these CSVs 
to generate interactive charts.

**Dashboard built for Veridi Logistics | Data: Olist Brazilian E-Commerce Dataset**
