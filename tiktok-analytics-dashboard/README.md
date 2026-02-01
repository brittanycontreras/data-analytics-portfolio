📊 TikTok Engagement & Comment Behavior Analysis

## Overview
This project analyzes engagement patterns across 1,000 trending TikTok videos,
with a specific focus on **comment-driven interaction** rather than passive metrics
such as views or likes.

Instead of asking *what goes viral*, this analysis asks:
**what types of content actually prompt discussion?**

---

## Research Question
How does **video length** influence comment-to-like ratios in trending TikTok videos?

---

## Dataset
- **Source:** TikTok Trending Videos (Kaggle)
- **Size:** 1,000+ trending videos
- **Granularity:** Video-level metrics (views, likes, comments, shares, duration)

---

## Key Metrics
- **Engagement Rate**  
  \[(likes + comments + shares) / views\]
- **Comment-to-Like Ratio**  
  A proxy for *depth of engagement* rather than reach

---

## Key Findings
- **Very short (0–15s)** and **medium-length (30–60s)** videos generate the
  highest comment-to-like ratios
- **Mid-length videos (15–30s)** tend to receive more passive engagement
- **Long videos (60s+)** are underrepresented among trending content

These patterns suggest that discussion is driven either by:
- immediate emotional hooks, or
- sustained narrative tension

---

## Methodology
- Cleaned and flattened raw JSON data into a Pandas DataFrame
- Engineered custom engagement metrics
- Segmented videos into length buckets
- Compared average comment-to-like ratios across segments
- Visualized findings using Matplotlib

---

## Tools
- Python
- Pandas
- Matplotlib
- Jupyter Notebook

---

## Notebook
📘 **Main Analysis**  
`tiktok-analytics-dashboard/notebooks/what_drives_discussion_on_tiktok.ipynb`

---

## Limitations & Future Work
- Trending videos are not representative of all TikTok content
- Comment sentiment was not analyzed
- Causality cannot be inferred from observational data

Potential extensions include:
- NLP-based comment sentiment analysis
- Creator-level engagement clustering
- Time-to-viral dynamics

---

## Status
✅ Complete — exploratory analysis with clear insights
