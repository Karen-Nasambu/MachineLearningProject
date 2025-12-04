# MachineLearningProject
## Problem Statement
### Predicting County-Level Election Violence Risk in Kenya Ahead of the 2027 General Election
Kenya has experienced repeated cycles of election-related violence, with the most severe outbreak in 2007–2008 claiming over 1,300 lives and displacing more than 600,000 people. While the scale has decreased in 2013, 2017, and 2022, deadly incidents, ethnic clashes, protests, and militia activity still recur in predictable hotspot counties, particularly in the Rift Valley, Nyanza, and parts of Coast and Nairobi. Current early-warning systems rely heavily on qualitative reports and manual monitoring. This project aims to develop an open, data-driven machine learning model that accurately forecasts which of Kenya’s 47 counties are at highest risk of serious election violence in 2027, enabling government agencies, civil society, peace-building organizations, and electoral bodies to target preventive interventions months in advance.

#### Project Overview
Build a transparent, county-level election violence risk prediction system for Kenya’s August 2027 general election using historical conflict data, demographic indicators, and political variables. The final output will be an updated risk index and interactive map refreshed quarterly until the election.

#### Objectives

* Create a reproducible ML model that predicts high-risk counties with at least 80% precision on historical data (1997–2024).
* Identify the strongest predictors of election violence in the Kenyan context (e.g., ethnic diversity, past fatalities, land disputes, youth unemployment).
  
#### Impact

* Enable early deployment of peace committees, dialogue forums, and security resources to the 8–12 highest-risk counties.
* Provide civil society with evidence-based advocacy tools to push for electoral reforms in hotspot areas.
* Contribute the first publicly available, county-granular, forward-looking election violence forecast for Kenya 2027.

#### Target Users

Kenyan Citizen

### Data Sources

ACLED Kenya dataset (1997–present): event-level political violence and protests
Kenya National Bureau of Statistics (KNBS): census and demographic data
IPCC ethnic diversity indices per county
Historical election results and margin-of-victory data
Past NCIC and UWiano Platform reports (for validation)

#### Expected Deliverables

Trained and versioned machine learning model (Random Forest /)

7. Skills Needed

Data cleaning and geospatial analysis (Python/Pandas/Geopandas)
Machine learning (classification, imbalance handling, SHAP/LIME interpretability)
Basic frontend for dashboard (Streamlit or Dash)
Domain knowledge of Kenyan politics and conflict (desirable but not required
