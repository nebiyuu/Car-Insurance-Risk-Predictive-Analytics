import pandas as pd
from scipy.stats import chi2_contingency, f_oneway

def chi2_test(df, group_col, target_col, alpha=0.05, print_table_head=True):
    contingency = pd.crosstab(df[group_col], df[target_col])
    if print_table_head:
        print(f"Contingency Table ({group_col} vs. {target_col}):\n", contingency.head())
    else:
        print(f"Contingency Table ({group_col} vs. {target_col}):\n", contingency)
    chi2, p, dof, expected = chi2_contingency(contingency)
    print(f"\nChi-squared Statistic: {chi2:.4f}")
    print(f"P-value: {p:.4f}")
    print(f"Degrees of Freedom: {dof}")
    if p < alpha:
        print(f"\nResult: Reject the Null Hypothesis (p < {alpha}).")
        print(f"Conclusion: There is a statistically significant difference in {target_col} across {group_col}.")
    else:
        print(f"\nResult: Fail to Reject the Null Hypothesis (p >= {alpha}).")
        print(f"Conclusion: There is no statistically significant difference in {target_col} across {group_col}.")
    # Return for further use if needed
    return contingency, chi2, p, dof, expected

def anova_test(df, group_col, value_col, filter_positive=False, alpha=0.05):
    if filter_positive:
        df = df[df[value_col] > 0].copy()
    groups = df[group_col].unique()
    values_by_group = [df[value_col][df[group_col] == g].values for g in groups]
    print(f"Mean {value_col} by {group_col}:")
    print(df.groupby(group_col)[value_col].mean().sort_values(ascending=False))
    f_stat, p = f_oneway(*values_by_group)
    print(f"\nANOVA F-statistic: {f_stat:.4f}")
    print(f"P-value: {p:.4f}")
    if p < alpha:
        print(f"\nResult: Reject the Null Hypothesis (p < {alpha}).")
        print(f"Conclusion: There is a statistically significant difference in {value_col} across {group_col}.")
    else:
        print(f"\nResult: Fail to Reject the Null Hypothesis (p >= {alpha}).")
        print(f"Conclusion: There is no statistically significant difference in {value_col} across {group_col}.")
    return f_stat, p