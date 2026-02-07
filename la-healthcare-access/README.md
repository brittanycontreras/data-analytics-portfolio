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
```
## Results

### County-Level Outcomes (Statewide)

The county-level regression model evaluated the relationship between socioeconomic indicators and inpatient mortality across 58 California counties.

Key findings:

- Higher poverty rates were associated with modestly higher inpatient mortality.
- Median household income was negatively associated with mortality.
- Socioeconomic variables explained a meaningful portion of variation in mortality outcomes.
- The overall model was statistically significant.

Interpretation:

Counties with greater socioeconomic disadvantage tend to experience slightly worse inpatient survival outcomes. While the explanatory power of the model is moderate, the direction and statistical significance of the coefficients suggest the presence of measurable socioeconomic gradients in severe health outcomes.

---

### ZIP-Level Access (Los Angeles County)

The ZIP-level regression model evaluated whether healthcare facility density per capita aligns with poverty burden within Los Angeles County.

Key findings:

- Poverty rate alone did not significantly predict facility density per capita.
- Median household income showed a small negative association with facility density.
- Model explanatory power was modest (R² ≈ 6%).
- Facility density was highly skewed across ZIP codes.

Interpretation:

Healthcare infrastructure density at the ZIP level does not strongly track poverty burden. While economically advantaged ZIP codes may have slightly fewer facilities per capita, the overall relationship between poverty and facility density appears weak.

---

## Analytical Insight

The contrast between the two models is the central finding of this project:

- Socioeconomic gradients are detectable in inpatient mortality.
- The same gradients are not strongly observable in facility counts per capita.

This suggests that structural inequality may manifest more clearly in outcomes than in raw infrastructure distribution. Simply counting facilities does not necessarily capture equity in realized health outcomes.

In other words, access quantity alone is insufficient to evaluate healthcare equity.

---

## Limitations

- Facility counts do not measure bed capacity, service quality, or specialty care availability.
- County-level aggregation may mask within-county disparities.
- Cross-sectional regression does not imply causation.
- Skewed distribution of facility density may limit linear modeling assumptions.

---

## Technical Approach

This project demonstrates:

- Multi-source data integration (ACS + health discharge + facility records)
- Census API data extraction
- Per-capita normalization
- Handling multicollinearity
- Log transformation for skew correction
- Ordinary Least Squares (OLS) regression modeling
- Comparative geographic modeling (county vs ZIP level)

---

## Conclusion

This analysis highlights the complexity of evaluating healthcare equity.

While facility density per capita does not strongly align with poverty at the ZIP level in Los Angeles County, socioeconomic gradients are more clearly visible in inpatient mortality rates at the county level across California.

These findings suggest that disparities may emerge more clearly in health outcomes than in infrastructure distribution alone. Evaluating healthcare equity therefore requires examining not only access metrics but also realized outcomes.

