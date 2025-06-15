import matplotlib.pyplot as plt
import seaborn as sns

def bars(series):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=series.values, y=series.index, palette='viridis')
    
    plt.xlabel("Count")
    plt.ylabel("Bank")
    plt.title("Bank Distribution", fontsize=14)
    
    for i, v in enumerate(series.values):
        plt.text(v + (v * 0.01), i, f"{v:,}", va='center')
    
    plt.tight_layout()
    plt.show()
