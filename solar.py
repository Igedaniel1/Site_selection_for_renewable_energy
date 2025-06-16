import streamlit as st
import pandas as pd

# Load dataset
prime_data = pd.read_csv("C:/Users/HP/Documents/SolarDeployment/SolarDeploymentDataset_Scored.csv")

# Define thresholds
grid_threshold = 50
solar_threshold = prime_data['Solar_Irradiance_kWh_m2_day'].median()
cost_threshold = prime_data['Electricity_Cost_USD_per_kWh'].median()

# Create High_Priority flag
prime_data['High_Priority'] = (
    (prime_data['Grid_Access_Percent'] < grid_threshold) &
    (prime_data['Solar_Irradiance_kWh_m2_day'] > solar_threshold) &
    (prime_data['Electricity_Cost_USD_per_kWh'] > cost_threshold)
).astype(int)

st.title("Solar Site Suitability Dashboard")

# Region selection (no if check here)
regions = prime_data['Region'].unique()
selected_region = st.selectbox("Select a Region", options=regions)

filtered_data = prime_data[prime_data['Region'] == selected_region]

# Show summary metrics for the selected region
st.subheader(f"Summary Metrics for {selected_region}")
st.write(f"**Total Sites in Region:** {len(filtered_data)}")

col1, col2, col3 = st.columns(3)
col1.metric("Median Solar Irradiance", f"{filtered_data['Solar_Irradiance_kWh_m2_day'].median():.2f} kWh/m²/day")
col2.metric("Median Grid Access", f"{filtered_data['Grid_Access_Percent'].median():.2f}%")
col3.metric("Median Electricity Cost", f"${filtered_data['Electricity_Cost_USD_per_kWh'].median():.2f} per kWh")

# Rank sites by solar irradiance (descending)
ranked_sites = filtered_data.sort_values(by='Solar_Irradiance_kWh_m2_day', ascending=False)

# Display top 10 sites with key columns
st.subheader("Top 10 Solar Sites Ranked by Solar Irradiance")
st.dataframe(ranked_sites[['Region', 'Solar_Irradiance_kWh_m2_day', 'Grid_Access_Percent', 'Electricity_Cost_USD_per_kWh', 'High_Priority']].head(10))

# Summary recommendations
st.markdown("""
### Summary Recommendations:
- **Prioritize sites with high solar irradiance and low grid access** to maximize solar deployment impact.
- Focus on regions where electricity cost is high, indicating greater economic benefit.
- Use the `High_Priority` flag as a quick filter to identify the best candidate sites.
""")
