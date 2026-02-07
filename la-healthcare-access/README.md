# 🏥 Socioeconomic Gradients in Healthcare Outcomes and Access

## Overview

This project evaluates whether healthcare access and inpatient outcomes align with socioeconomic vulnerability across California.

Using statewide inpatient discharge data and American Community Survey (ACS) indicators, I conducted a two-level analysis:

1. County-level modeling of inpatient mortality across California.
2. ZIP-level modeling of healthcare facility density within Los Angeles County.

The goal was to distinguish between structural disparities in outcomes versus disparities in infrastructure distribution.

---

## Research Question

Do socioeconomic gradients manifest more clearly in healthcare outcomes (mortality) than in facility distribution?

---

## Data Sources

- California HCAI Inpatient Discharge Data  
- American Community Survey (ACS) 5-Year Estimates (poverty rate, median income)  
- California Licensed Healthcare Facility Dataset  

---

## Methodology

### 1️⃣ County-Level Outcome Model (Statewide)

**Unit of analysis:** 58 California counties  
**Dependent variable:** Percent inpatient mortality (`pct_died`)  
**Independent variables:** Poverty rate, Median household income  

County-level mortality was modeled using Ordinary Least Squares (OLS):

```python
import statsmodels.api as sm

X = county_avg[["poverty_rate", "median_income"]]
X = sm.add_constant(X)

y = county_avg["pct_died"]

model = sm.OLS(y, X).fit()
print(model.summary())
2️⃣ ZIP-Level Access Model (Los Angeles County)

Unit of analysis: 267 ZIP codes
Dependent variable: Facilities per 10,000 residents
Independent variables: Poverty rate, Median household income

##Facility density was normalized per capita:

final["facilities_per_10k"] = (
    final["facility_count"] / final["population"]
) * 10000
##Regression model:

reg_df = final[["facilities_per_10k", "poverty_pct", "median_income"]].dropna()

X = sm.add_constant(reg_df[["poverty_pct", "median_income"]])
y = reg_df["facilities_per_10k"]

model = sm.OLS(y, X).fit()
print(model.summary())
##Because facility density was highly skewed, a log transformation was also tested:

import numpy as np

reg_df["log_facilities"] = np.log1p(reg_df["facilities_per_10k"])

X = sm.add_constant(reg_df[["poverty_pct"]])
y = reg_df["log_facilities"]

model_log = sm.OLS(y, X).fit()
print(model_log.summary())
