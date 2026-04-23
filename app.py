import streamlit as st
import pandas as pd
import altair as alt

# Tax calculation functions
def calculate_tax(income):
    if income <= 400000:
        tax = 0
    elif income <= 800000:
        tax = (income - 400000) * 0.05
    elif income <= 1200000:
        tax = (400000 * 0.05) + (income - 800000) * 0.10
    elif income <= 1600000:
        tax = (400000 * 0.05) + (400000 * 0.10) + (income - 1200000) * 0.15
    elif income <= 2000000:
        tax = (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (income - 1600000) * 0.20
    elif income <= 2400000:
        tax = (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (400000 * 0.20) + (income - 2000000) * 0.25
    else:
        tax = (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (400000 * 0.20) + (400000 * 0.25) + (income - 2400000) * 0.30
    return tax

def calculate_surcharge(tax, income):
    if income <= 5000000:
        return 0
    elif income <= 10000000:
        return tax * 0.10
    elif income <= 20000000:
        return tax * 0.15
    elif income <= 50000000:
        return tax * 0.25
    else:
        return tax * 0.37

# Page layout
st.set_page_config(
    page_title="Income Tax Calculator 💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("💰 Income Tax Calculator")
st.markdown("Calculate your income tax under the **new regime** with rebate, surcharge, and cess included.")

# Sidebar lead form
with st.sidebar.form(key='lead_form', clear_on_submit=True):
    st.header("📋 Get Your Tax Report")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    income_input = st.number_input("Annual Income (₹)", min_value=0.0, step=10000.0)
    submit_button = st.form_submit_button(label='Submit & Calculate Tax')

# Only process when the form is submitted
if submit_button:
    if not name or not email or not phone:
        st.warning("⚠ Please fill all the fields to proceed.")
    else:
        st.success(f"✅ Thanks {name}! Your lead is submitted successfully.")
        
        # Tax calculation
        income = income_input
        tax = calculate_tax(income)
        rebate = min(tax, 25000) if income <= 700000 else 0
        tax_after_rebate = tax - rebate
        surcharge = calculate_surcharge(tax_after_rebate, income)
        cess = (tax_after_rebate + surcharge) * 0.04
        total_tax = tax_after_rebate + surcharge + cess

        # Layout: two columns
        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader("🧾 Tax Breakdown")
            st.metric("Income", f"₹{income:,.2f}")
            st.metric("Tax before rebate", f"₹{tax:,.2f}")
            st.metric("Rebate (87A)", f"₹{rebate:,.2f}")
            st.metric("Tax after rebate", f"₹{tax_after_rebate:,.2f}")
            st.metric("Surcharge", f"₹{surcharge:,.2f}")
            st.metric("Cess @4%", f"₹{cess:,.2f}")
            st.success(f"💵 Total Tax Payable: ₹{total_tax:,.2f}")

        with col2:
            st.subheader("📊 Tax Visualization")
            tax_data = pd.DataFrame({
                'Component': ['Tax', 'Rebate', 'Surcharge', 'Cess', 'Total Tax'],
                'Amount': [tax, -rebate, surcharge, cess, total_tax]
            })
            chart = alt.Chart(tax_data).mark_bar().encode(
                x=alt.X('Amount:Q', title='Amount (₹)'),
                y=alt.Y('Component:N', sort='-x', title=''),
                color=alt.Color('Component:N', scale=alt.Scale(scheme='category10'), legend=None)
            ).properties(height=300)
            st.altair_chart(chart, use_container_width=True)

        st.divider()
        st.info("🔹 Note: This calculator is based on the **new tax regime slabs** and includes Section 87A rebate, surcharge, and 4% cess. For precise filing, consult a tax professional.")