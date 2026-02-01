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

 ## 📌 Conclusion & Implications

This analysis shows that comment-driven engagement behaves differently from traditional view- or like-based metrics.

Very short (0–15s) and medium-length (30–60s) videos consistently produce higher comment-to-like ratios, suggesting that discussion is triggered either by immediate emotional reactions or by narrative payoff. In contrast, mid-length videos (15–30s) tend to receive views without proportional discussion, indicating more passive consumption. Long-form videos are underrepresented among trending content, limiting conclusions about extended formats.

From a creator perspective, optimizing for comments—not just views—may require intentional prompts or emotionally resonant hooks. From a platform or analytics standpoint, comment-to-like ratios provide a useful signal for identifying high-quality engagement and community interaction.

## ⚠️ Limitations

- Dataset includes only trending videos and may not represent average TikTok content
- Engagement metrics are static snapshots and do not capture time dynamics
- Comment sentiment and quality were not analyzed
- Results may be influenced by TikTok’s recommendation system

## 🔮 Future Work

- Sentiment analysis of comments to distinguish constructive vs reactive engagement
- Time-based analysis of engagement decay
- Creator-level engagement consistency metrics
- Hashtag and topic clustering to isolate content themes
