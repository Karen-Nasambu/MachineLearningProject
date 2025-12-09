
import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="Kenya 2027 Risk Predictor", page_icon="Kenya", layout="wide")

@st.cache_resource
def load_model():
    return joblib.load("best_election_risk_pipeline.pkl")

@st.cache_data
def load_data():
    df = pd.read_csv("kenya_locations_with_risk.csv")
    # Re-add the 6 features the model needs
    df['total_events_30km'] = df_features['total_events_30km']
    df['riots_count'] = df_features['riots_count']
    df['violence_against_civilians'] = df_features['violence_against_civilians']
    df['battles_count'] = df_features['battles_count']
    df['max_fatalities_single_event'] = df_features['max_fatalities_single_event']
    df['avg_fatalities_per_event'] = df_features['avg_fatalities_per_event']
    return df

model = load_model()
df_locations = load_data()

st.title("Kenya 2027 Election Violence Risk Predictor")
st.markdown("Enter any location to see its risk for the 2027 election")

loc = st.text_input("Location (e.g. Kisumu, Eldoret, Kibera, Nakuru, Nyeri):", "Kisumu")

if st.button("Predict Risk"):
    result = df_locations[
        df_locations['location_name'].str.contains(loc, case=False, na=False) |
        df_locations['admin2'].str.contains(loc, case=False, na=False) |
        df_locations['admin1'].str.contains(loc, case=False, na=False)
    ]
    
    if result.empty:
        st.error("Location not found. Try a bigger town or county.")
    else:
        place = result.iloc[0]
        feats = np.array([[place['total_events_30km'],
                          place['riots_count'],
                          place['violence_against_civilians'],
                          place['battles_count'],
                          place['max_fatalities_single_event'],
                          place['avg_fatalities_per_event']]])
        
        risk = model.predict(feats)[0]
        fatalities = int(place['expected_fatalities'])
        
        if risk >= 80:   level = "VERY HIGH"
        elif risk >= 60: level = "HIGH"
        elif risk >= 40: level = "MODERATE"
        elif risk >= 20: level = "LOW"
        else:            level = "VERY LOW"
        
        st.success(f"**{place['location_name']}, {place['admin1']}**")
        st.metric("Risk Score", f"{risk:.1f}/100")
        st.markdown(f"**Risk Level: {level}**")
        st.metric("Expected Fatalities (2027)", f"~{fatalities}")
        st.info(f"Based on {int(place['total_events_30km'])} past violent events within 30 km.")
