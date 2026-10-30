
import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="SAPM CAPM Laboratory",
    page_icon="📈",
    layout="wide"
)

st.title("CAPM and Security Market Line")
st.write("Interactive SAPM Laboratory for MBA Students")

# Sidebar inputs
st.sidebar.header("CAPM Assumptions")

rf = st.sidebar.number_input(
    "Risk-Free Rate (%)",
    value=6.0
)

rm = st.sidebar.number_input(
    "Expected Market Return (%)",
    value=12.0
)

beta = st.sidebar.slider(
    "Security Beta",
    min_value=0.0,
    max_value=3.0,
    value=1.2,
    step=0.1
)

# CAPM calculation
required_return = rf + beta * (rm - rf)

st.subheader("CAPM Results")

col1, col2, col3 = st.columns(3)

col1.metric("Risk-Free Rate", f"{rf:.2f}%")
col2.metric("Market Risk Premium", f"{rm-rf:.2f}%")
col3.metric("Required Return", f"{required_return:.2f}%")

# Security Market Line
betas = np.linspace(0, 3, 100)
returns = rf + betas * (rm - rf)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=betas,
    y=returns,
    mode="lines",
    name="Security Market Line"
))

fig.add_trace(go.Scatter(
    x=[beta],
    y=[required_return],
    mode="markers",
    name="Selected Security",
    marker=dict(size=12, color="red")
))

fig.update_layout(
    title="Security Market Line",
    xaxis_title="Beta",
    yaxis_title="Expected Return (%)",
    template="plotly_white"
)

st.plotly_chart(fig, width="stretch")

st.subheader("Discussion Questions")

st.markdown("""
1. What happens to required return when beta increases?
2. How does the market risk premium affect the SML?
3. What happens when beta is zero?
4. Can a security have a negative beta?
5. What is the difference between systematic and total risk?
""")

