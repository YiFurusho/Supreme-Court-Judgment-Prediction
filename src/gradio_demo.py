import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
from PIL import Image

__doc__ = """
 ╔═══════════════════════════════════════════╗
 ║                                           ║
 ║  ◆◆ Author Information ◆◆                 ║
 ║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━              ║
 ║  Author: I Furusho                        ║
 ║  Role: Upcoming Data Analyst              ║
 ║  Date: March 9, 2025                      ║
 ║                                           ║
 ║  ◆◆ Script Description ◆◆                 ║
 ║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━              ║
 ║  This script performs an exploratory      ║
 ║  data analysis (EDA) on 'justice.csv'.    ║
 ║  • Viewing dataset structure              ║
 ║  • Handling missing values                ║
 ║  • Examining columns for insights         ║
 ║  • Visualizing distributions              ║
 ║  • Investigating relationships            ║
 ║                                           ║
 ║  ◆◆ Libraries Used ◆◆                     ║
 ║  ━━━━━━━━━━━━━━━━━━━━━                    ║
 ║  • pandas                                 ║
 ║  • matplotlib                             ║
 ║  • seaborn                                ║
 ║  • gradio                                 ║
 ║                                           ║
 ╚═══════════════════════════════════════════╝
"""

# Set cyberpunk color scheme
plt.style.use('dark_background')
# colors = ['#00ff00', '#ff00ff', '#00ffff', '#ffff00']
colors = ['#008080', '#fa8072', '#003366', '#468499']

def load_data():
    path = 'data/justice.csv'
    df = pd.read_csv(path)

    # Handle missing values
    df['docket'] = df['docket'].fillna('Unknown')
    df['first_party'] = df['first_party'].fillna('Unknown')
    df['second_party'] = df['second_party'].fillna('Unknown')
    df['first_party_winner'] = df['first_party_winner'].fillna('Unknown')
    df['decision_type'] = df['decision_type'].fillna('Unknown')
    df['disposition'] = df['disposition'].fillna('Not Specified')
    df['issue_area'] = df['issue_area'].fillna('Not Specified')

    return df


def perform_eda(df):
    fig, axs = plt.subplots(2, 2, figsize=(15, 15))

    # Increase font size for all subplots
    plt.rcParams.update({'font.size': 27})

    # Facts Length Distribution
    sns.histplot(df['facts_len'], bins=20, kde=True, ax=axs[0, 0], color=colors[0])
    axs[0, 0].set_title('Distribution of Facts Length', color=colors[0])

    # Majority Vote Distribution
    sns.histplot(df['majority_vote'], bins=20, kde=True, ax=axs[0, 1], color=colors[1])
    axs[0, 1].set_title('Distribution of Majority Vote', color=colors[1])

    # Minority Vote Distribution
    sns.histplot(df['minority_vote'], bins=20, kde=True, ax=axs[1, 0], color=colors[2])
    axs[1, 0].set_title('Distribution of Minority Vote', color=colors[2])

    # Scatter Plot
    sns.scatterplot(x='facts_len', y='majority_vote', data=df, ax=axs[1, 1], color=colors[3])
    axs[1, 1].set_title('Facts Length vs Majority Vote', color=colors[3])

    plt.tight_layout()

    # Save and convert to PIL Image
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    pil_img = Image.open(buf)
    plt.close()

    return pil_img


def analyze():
    df = load_data()

    # Generate summary
    summary = f"""
    === Dataset Overview ===
    Shape: {df.shape}
    Columns: {', '.join(df.columns)}

    === Missing Values ===
    {df.isnull().sum().to_string()}

    === Duplicate Rows ===
    {df.duplicated().sum()}

    === Key Statistics ===
    {df.describe().to_string()}

    === Category Distributions ===
    Term:
    {df['term'].value_counts().to_string()}

    Decision Type:
    {df['decision_type'].value_counts().to_string()}

    First Party Winner:
    {df['first_party_winner'].value_counts().to_string()}
    """

    return perform_eda(df), summary


# Custom cyberpunk theme
cyberpunk_theme = gr.themes.Default(
    primary_hue="cyan",
    secondary_hue="green",
    neutral_hue="slate"
).set(
    body_background_fill='#0a0a23',
    button_primary_background_fill='*primary_200',
    button_primary_background_fill_hover='*primary_100',
)

iface = gr.Interface(
    fn=analyze,
    inputs=[],
    outputs=[
        gr.Image(label="Cyberpunk EDA Visualizations", type="pil"),
        gr.Textbox(label="Dataset Analysis", lines=25)
    ],
    title="⚡ Justice Data Analyzer ⚡",
    description="Exploratory analysis of Supreme Court justice data with cool styling",
    # theme=cyberpunk_theme,
    # css="""
    # .gradio-container {
    #     background: linear-gradient(45deg, #1a1a2e, #16213e);
    #     color: #00ff9d !important;
    #     font-family: 'Courier New', monospace;
    # }
    # h1 {
    #     color: #ff00ff !important;
    #     text-shadow: 0 0 10px #ff00ff;
    # }
    # .output-image {
    #     border: 2px solid #00ffff;
    #     box-shadow: 0 0 15px #00ffff;
    # }
    # """
)

if __name__ == "__main__":
    iface.launch(share=True)
