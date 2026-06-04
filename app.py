
# COMPLETE DASHBOARD - Using Real Data

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Last Mile Auditor", layout="wide")
st.title("Last Mile Logistics Auditor")

# Load existing CSV files
@st.cache_data
def load_data():
    master = pd.read_csv('master_delivery_data.csv')
    state = pd.read_csv('state_analysis.csv')
    sentiment = pd.read_csv('sentiment_analysis.csv')
    return master, state, sentiment

master, state, sentiment = load_data()

# STORY 3: Geographic Heatmap
st.subheader("Late Delivery % by State")
fig3 = px.bar(
    state.sort_values('late_percentage', ascending=False).head(15),
    x='customer_state', y='late_percentage',
    color='late_percentage', color_continuous_scale='Reds',
    text='late_percentage'
)
fig3.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
st.plotly_chart(fig3, use_container_width=True)

remote = ['AM', 'RR', 'AC', 'AP', 'PA', 'RO', 'TO']
remote_avg = state[state['customer_state'].isin(remote)]['late_percentage'].mean()
other_avg = state[~state['customer_state'].isin(remote)]['late_percentage'].mean()
st.info(f"Remote states: {remote_avg:.1f}% late vs {other_avg:.1f}% for others")

# STORY 4: Sentiment Correlation
st.subheader("Delivery Delay vs Review Score")
fig4 = px.bar(
    sentiment, x='delivery_status', y='avg_review',
    color='avg_review', color_continuous_scale='RdYlGn',
    text='avg_review'
)
fig4.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig4.update_layout(yaxis_range=[0, 5])
st.plotly_chart(fig4, use_container_width=True)

corr = master['Days_Difference'].corr(master['review_score'])
st.metric("Correlation (Delay vs Review)", f"{corr:.3f}")

# STORY 6: Seller Performance (Using real data from analysis)
st.markdown("---")
st.subheader("Seller Performance Insight (From Actual Data)")

# Result from Colab analysis
st.markdown(f"""
###Worst Seller Identified

| Metric | Value |
|--------|-------|
| **Seller ID** | `b1b3948701c5c72445495bd161b83a4c` |
| **Late Delivery Rate** | **64.3%** |

**Business Impact:** This seller's late rate is critically high and likely causing significant customer dissatisfaction.

**Action Items:**
1. Audit this seller's shipping process
2. Review customer feedback for this seller
3. Implement performance improvement plan
""")

# Summary
st.markdown("---")
st.subheader("Key Metrics Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Overall Late Rate", f"{state['late_percentage'].mean():.1f}%")
col2.metric("Worst State", f"{state.iloc[0]['customer_state']} ({state.iloc[0]['late_percentage']:.1f}%)")
col3.metric("Correlation", f"{corr:.3f}")

