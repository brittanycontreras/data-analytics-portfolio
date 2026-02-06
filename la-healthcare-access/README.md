# Healthcare Access Disparities in Los Angeles County
### Understanding How Neighborhood Poverty Affects Emergency Care and Recovery Outcomes

## Background & Motivation

Growing up in Lincoln Heights, Los Angeles, I watched my mother navigate the healthcare system while managing neurological conditions from a car accident. Over the years, her balance and mobility deteriorated, leading to multiple falls, hospitalizations, and surgeries. Our neighborhood had limited access to specialists and rehabilitation services, forcing reliance on emergency care.

This project examines whether her experience reflects broader patterns: **Do low-income LA neighborhoods face systematic barriers to healthcare access, and how does this impact outcomes for residents with chronic conditions?**

## Research Questions

1. How does healthcare facility access (hospitals, specialists, rehab centers) vary across LA County by income level?
2. Are emergency department utilization rates higher in low-income neighborhoods?
3. What is the relationship between poverty rates and injury-related hospitalizations?
4. How far do residents in different neighborhoods travel for specialized care?

## Data Sources

- **LA County Open Data**: Emergency department visits, hospitalization data
- **US Census Bureau**: Income, poverty rates, insurance coverage (ACS 2018-2022)
- **CA Health & Human Services**: Healthcare facility locations and types
- **CDC WONDER**: Injury and fall-related hospitalization rates
- **LA County GIS**: Geographic boundaries for mapping

## Methodology

1. **Data Collection & Cleaning**: Merging datasets by zip code/census tract
2. **Geographic Analysis**: Mapping healthcare facilities against poverty rates
3. **Statistical Analysis**: Calculating correlations between socioeconomic factors and health outcomes
4. **Comparative Analysis**: Contrasting Lincoln Heights with higher-income LA neighborhoods

## Project Status

🚧 **In Progress** - Currently collecting and cleaning data

## Key Findings

*Analysis in progress - findings will be updated as the project develops*

## Technical Skills Demonstrated

- Python (pandas, geopandas, matplotlib, seaborn)
- Geospatial analysis and mapping
- Statistical correlation analysis
- Data cleaning and merging from multiple sources
- Data visualization and storytelling

## Repository Structure
```
├── data/
│   ├── raw/              # Original data files
│   └── processed/        # Cleaned datasets
├── notebooks/            # Jupyter notebooks for analysis
├── visualizations/       # Charts and maps
└── README.md
```

## Next Steps

- [ ] Download LA County health and Census data
- [ ] Create data cleaning pipeline
- [ ] Perform exploratory data analysis
- [ ] Build geospatial visualizations
- [ ] Write final analysis and recommendations

---

**Note**: This analysis is dedicated to my mother and the countless families in underserved communities who deserve equitable access to healthcare.
