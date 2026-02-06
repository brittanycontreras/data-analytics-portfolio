# Healthcare Access Disparities in Los Angeles County
### Analyzing How Neighborhood Income Levels Affect Emergency Care Access and Health Outcomes

## Background & Motivation

This project examines healthcare access disparities across Los Angeles County neighborhoods. Motivated by observing healthcare challenges in underserved communities, this analysis investigates whether low-income neighborhoods face systematic barriers to healthcare access and how this impacts health outcomes for residents with chronic conditions.

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
4. **Comparative Analysis**: Comparing healthcare access across different income levels

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

- [X] Download LA County health and Census data
- [ ] Create data cleaning pipeline
- [ ] Perform exploratory data analysis
- [ ] Build geospatial visualizations
- [ ] Write final analysis and recommendations
