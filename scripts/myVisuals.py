import matplotlib.pyplot as plt
import seaborn as sns

def mybars(series, title, palette="viridis", figsize=(10, 6)):
    """
    Custom horizontal bar plot with counts annotated on bars.
    
    Parameters:
    -----------
    series : pd.Series
        A Pandas Series where the index represents categories (e.g., provinces/banks)
        and values represent counts.
    title : str
        Title of the plot.
    palette : str (default: 'viridis')
        Seaborn color palette.
    figsize : tuple (default: (10, 6))
        Figure size (width, height).
    """
    # Create figure
    plt.figure(figsize=figsize)
    
    # Plot horizontal bars
    ax = sns.barplot(
        x=series.values, 
        y=series.index, 
        palette=palette,
        orient='h'
    )
    
    # Customize labels and title
    plt.xlabel("Count", fontsize=12)
    plt.ylabel("Category", fontsize=12)  # Updated from "Province" to generic "Category"
    plt.title(f"{title}", fontsize=14, pad=20)  # Added padding for better spacing
    
    # Annotate values on bars
    for i, v in enumerate(series.values):
        # Dynamic positioning: Place text at (v + 2% of max value, y-position)
        offset = 0.02 * max(series.values)
        ax.text(
            v + offset, 
            i, 
            f"{v:,}",  # Format with commas (e.g., 1,000)
            va='center',
            fontsize=10
        )
    
    # Remove spines for a cleaner look
    sns.despine(left=True)
    
    plt.tight_layout()
    plt.show()
    
def myheatmap(numeric_df, title):
    # Generate correlation heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(numeric_df.corr(), annot=True, fmt='.2f', cmap='coolwarm')
    plt.title(f"Correlation Heatmap - {title}", fontsize=16)
    plt.show()
