"""
Super Bowl LX Analysis: Seahawks vs Patriots
Data Analysis and Visualization Script

Author: [Your Name]
Date: February 2026
"""

import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set style
sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

# Load data
with open('../data/superbowl_stats.json', 'r') as f:
    data = json.load(f)

# Create output directory
import os
os.makedirs('../images', exist_ok=True)

# ============================================================
# 1. SCORE PROGRESSION CHART
# ============================================================
def create_score_progression():
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    ne_cumulative = [0, 0, 0, 13]
    sea_cumulative = [3, 9, 12, 29]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    x_pos = np.arange(len(quarters))
    width = 0.35
    
    ax.bar(x_pos - width/2, ne_cumulative, width, label='Patriots', color='#002244', alpha=0.8)
    ax.bar(x_pos + width/2, sea_cumulative, width, label='Seahawks', color='#002244', alpha=0.8)
    
    ax.set_xlabel('Quarter', fontweight='bold', fontsize=12)
    ax.set_ylabel('Cumulative Score', fontweight='bold', fontsize=12)
    ax.set_title('Super Bowl LX: Score Progression by Quarter', fontweight='bold', fontsize=14)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(quarters)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for i, (ne, sea) in enumerate(zip(ne_cumulative, sea_cumulative)):
        ax.text(i - width/2, ne + 0.5, str(ne), ha='center', va='bottom', fontweight='bold')
        ax.text(i + width/2, sea + 0.5, str(sea), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('../images/score_progression.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Score progression chart created")

# ============================================================
# 2. QB COMPARISON
# ============================================================
def create_qb_comparison():
    qb_data = data['quarterbacks']
    
    metrics = ['Completion %', 'Yards', 'TDs', 'INTs', 'Sacks', 'Rating']
    maye_values = [
        qb_data['Drake_Maye']['completion_pct'],
        qb_data['Drake_Maye']['yards'] / 10,  # Scale for visualization
        qb_data['Drake_Maye']['touchdowns'] * 10,
        qb_data['Drake_Maye']['interceptions'] * 10,
        qb_data['Drake_Maye']['sacks'] * 5,
        qb_data['Drake_Maye']['passer_rating']
    ]
    darnold_values = [
        qb_data['Sam_Darnold']['completion_pct'],
        qb_data['Sam_Darnold']['yards'] / 10,
        qb_data['Sam_Darnold']['touchdowns'] * 10,
        qb_data['Sam_Darnold']['interceptions'] * 10,
        qb_data['Sam_Darnold']['sacks'] * 5,
        qb_data['Sam_Darnold']['passer_rating']
    ]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(metrics))
    width = 0.35
    
    ax.bar(x - width/2, maye_values, width, label='Drake Maye (NE)', color='#C60C30', alpha=0.8)
    ax.bar(x + width/2, darnold_values, width, label='Sam Darnold (SEA)', color='#69BE28', alpha=0.8)
    
    ax.set_ylabel('Value (scaled)', fontweight='bold')
    ax.set_title('Quarterback Performance Comparison', fontweight='bold', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, rotation=15, ha='right')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('../images/qb_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ QB comparison chart created")

# ============================================================
# 3. DEFENSIVE DOMINATION
# ============================================================
def create_defensive_stats():
    defense = data['defense']
    
    categories = ['Sacks', 'INTs', 'Forced\nFumbles', 'QB Hits', '3-and-Outs\nForced']
    ne_def = [
        defense['NE']['sacks'],
        defense['NE']['interceptions'],
        defense['NE']['forced_fumbles'],
        defense['NE']['qb_hits'],
        defense['NE']['three_and_outs_forced']
    ]
    sea_def = [
        defense['SEA']['sacks'],
        defense['SEA']['interceptions'],
        defense['SEA']['forced_fumbles'],
        defense['SEA']['qb_hits'],
        defense['SEA']['three_and_outs_forced']
    ]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(categories))
    width = 0.35
    
    ax.bar(x - width/2, ne_def, width, label='Patriots Defense', color='#C60C30', alpha=0.8)
    ax.bar(x + width/2, sea_def, width, label='Seahawks Defense', color='#002244', alpha=0.8)
    
    ax.set_ylabel('Count', fontweight='bold', fontsize=12)
    ax.set_title('Defensive Performance: Seattle\'s Domination', fontweight='bold', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for i, (ne, sea) in enumerate(zip(ne_def, sea_def)):
        ax.text(i - width/2, ne + 0.2, str(ne), ha='center', va='bottom', fontweight='bold')
        ax.text(i + width/2, sea + 0.2, str(sea), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('../images/defensive_stats.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Defensive stats chart created")

# ============================================================
# 4. TURNOVER IMPACT
# ============================================================
def create_turnover_analysis():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Turnovers
    teams = ['Patriots', 'Seahawks']
    turnovers = [
        data['team_stats']['NE']['turnovers'],
        data['team_stats']['SEA']['turnovers']
    ]
    colors = ['#C60C30', '#002244']
    
    ax1.bar(teams, turnovers, color=colors, alpha=0.8, edgecolor='black', linewidth=2)
    ax1.set_ylabel('Turnovers', fontweight='bold', fontsize=12)
    ax1.set_title('Total Turnovers', fontweight='bold', fontsize=14)
    ax1.set_ylim(0, 4)
    ax1.grid(axis='y', alpha=0.3)
    
    for i, v in enumerate(turnovers):
        ax1.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold', fontsize=14)
    
    # Points off turnovers (estimated)
    points_off_turnovers = [0, 7]  # Pick-six
    
    ax2.bar(teams, points_off_turnovers, color=colors, alpha=0.8, edgecolor='black', linewidth=2)
    ax2.set_ylabel('Points', fontweight='bold', fontsize=12)
    ax2.set_title('Points Off Turnovers', fontweight='bold', fontsize=14)
    ax2.set_ylim(0, 10)
    ax2.grid(axis='y', alpha=0.3)
    
    for i, v in enumerate(points_off_turnovers):
        ax2.text(i, v + 0.2, str(v), ha='center', va='bottom', fontweight='bold', fontsize=14)
    
    plt.suptitle('The Turnover Battle: Game Decider', fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('../images/turnover_impact.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Turnover impact chart created")

# ============================================================
# 5. OFFENSIVE EFFICIENCY COMPARISON
# ============================================================
def create_offensive_comparison():
    categories = ['Total\nYards', 'Rush\nYards', 'Pass\nYards', 'First\nDowns']
    ne_stats = [
        data['team_stats']['NE']['total_yards'],
        data['team_stats']['NE']['rushing_yards'],
        data['team_stats']['NE']['passing_yards'],
        data['team_stats']['NE']['first_downs']
    ]
    sea_stats = [
        data['team_stats']['SEA']['total_yards'],
        data['team_stats']['SEA']['rushing_yards'],
        data['team_stats']['SEA']['passing_yards'],
        data['team_stats']['SEA']['first_downs']
    ]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(categories))
    width = 0.35
    
    ax.bar(x - width/2, ne_stats, width, label='Patriots', color='#C60C30', alpha=0.8)
    ax.bar(x + width/2, sea_stats, width, label='Seahawks', color='#002244', alpha=0.8)
    
    ax.set_ylabel('Value', fontweight='bold', fontsize=12)
    ax.set_title('Offensive Efficiency Comparison', fontweight='bold', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for i, (ne, sea) in enumerate(zip(ne_stats, sea_stats)):
        ax.text(i - width/2, ne + 5, str(ne), ha='center', va='bottom', fontweight='bold', fontsize=9)
        ax.text(i + width/2, sea + 5, str(sea), ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('../images/offensive_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Offensive comparison chart created")

# ============================================================
# 6. SUMMARY DASHBOARD
# ============================================================
def create_summary_dashboard():
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.4, wspace=0.3)
    
    # Title
    fig.suptitle('Super Bowl LX: Complete Analysis Dashboard\nSeattle Seahawks 29, New England Patriots 13', 
                 fontsize=18, fontweight='bold', y=0.98)
    
    # 1. Final Score (large)
    ax1 = fig.add_subplot(gs[0, :])
    teams = ['Patriots', 'Seahawks']
    scores = [13, 29]
    colors = ['#C60C30', '#002244']
    bars = ax1.barh(teams, scores, color=colors, alpha=0.8, edgecolor='black', linewidth=3)
    ax1.set_xlabel('Points', fontweight='bold', fontsize=14)
    ax1.set_title('FINAL SCORE', fontweight='bold', fontsize=16)
    ax1.set_xlim(0, 35)
    for i, (bar, score) in enumerate(zip(bars, scores)):
        ax1.text(score + 0.5, i, f'{score}', va='center', fontweight='bold', fontsize=20)
    ax1.grid(axis='x', alpha=0.3)
    
    # 2. Turnovers
    ax2 = fig.add_subplot(gs[1, 0])
    turnovers = [3, 0]
    ax2.bar(teams, turnovers, color=colors, alpha=0.8)
    ax2.set_ylabel('Count', fontweight='bold')
    ax2.set_title('Turnovers', fontweight='bold', fontsize=12)
    ax2.set_ylim(0, 4)
    for i, v in enumerate(turnovers):
        ax2.text(i, v + 0.1, str(v), ha='center', fontweight='bold', fontsize=14)
    
    # 3. Sacks
    ax3 = fig.add_subplot(gs[1, 1])
    sacks_allowed = [6, 1]
    ax3.bar(teams, sacks_allowed, color=colors, alpha=0.8)
    ax3.set_ylabel('Count', fontweight='bold')
    ax3.set_title('Sacks Allowed', fontweight='bold', fontsize=12)
    ax3.set_ylim(0, 7)
    for i, v in enumerate(sacks_allowed):
        ax3.text(i, v + 0.1, str(v), ha='center', fontweight='bold', fontsize=14)
    
    # 4. Time of Possession
    ax4 = fig.add_subplot(gs[1, 2])
    top_minutes = [26.82, 33.18]  # Converted to minutes
    ax4.bar(teams, top_minutes, color=colors, alpha=0.8)
    ax4.set_ylabel('Minutes', fontweight='bold')
    ax4.set_title('Time of Possession', fontweight='bold', fontsize=12)
    ax4.set_ylim(0, 40)
    for i, v in enumerate(top_minutes):
        ax4.text(i, v + 0.5, f'{v:.1f}', ha='center', fontweight='bold', fontsize=12)
    
    # 5. Total Yards
    ax5 = fig.add_subplot(gs[2, 0])
    total_yards = [331, 335]
    ax5.bar(teams, total_yards, color=colors, alpha=0.8)
    ax5.set_ylabel('Yards', fontweight='bold')
    ax5.set_title('Total Yards', fontweight='bold', fontsize=12)
    for i, v in enumerate(total_yards):
        ax5.text(i, v + 5, str(v), ha='center', fontweight='bold', fontsize=12)
    
    # 6. First Downs
    ax6 = fig.add_subplot(gs[2, 1])
    first_downs = [18, 20]
    ax6.bar(teams, first_downs, color=colors, alpha=0.8)
    ax6.set_ylabel('Count', fontweight='bold')
    ax6.set_title('First Downs', fontweight='bold', fontsize=12)
    for i, v in enumerate(first_downs):
        ax6.text(i, v + 0.3, str(v), ha='center', fontweight='bold', fontsize=14)
    
    # 7. Key Stat Text
    ax7 = fig.add_subplot(gs[2, 2])
    ax7.axis('off')
    key_stats_text = """
    KEY INSIGHTS:
    
    • Patriots shutout through Q3
    • Pick-six sealed the game
    • Myers: 5/5 FGs (15 pts)
    • Seattle: 0 turnovers
    • Maye: 6 sacks, 2 INTs
    """
    ax7.text(0.1, 0.5, key_stats_text, fontsize=11, verticalalignment='center',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    plt.savefig('../images/summary_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Summary dashboard created")

# ============================================================
# RUN ALL VISUALIZATIONS
# ============================================================
if __name__ == "__main__":
    print("\n🏈 Generating Super Bowl LX Analysis Visualizations...\n")
    
    create_score_progression()
    create_qb_comparison()
    create_defensive_stats()
    create_turnover_analysis()
    create_offensive_comparison()
    create_summary_dashboard()
    
    print("\n✅ All visualizations created successfully!")
    print("📁 Check the 'images/' folder for output files\n")
