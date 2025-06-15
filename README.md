# AlphaCare Insurance Solutions (ACIS) - Car Insurance Risk & Predictive Analytics

Welcome to the ACIS Car Insurance Analytics project!  
This repository contains all code, data, and documentation for analyzing historical car insurance claims in South Africa, with the goal of optimizing marketing strategies and identifying low-risk customer segments for premium reduction.

---



## Business Objectives

- **Understand risk and profitability drivers** across geography, demographics, and vehicle features.
- **Validate hypotheses** about risk differences (e.g., by province, gender, zip code).
- **Build predictive models** for claim severity and premium optimization.
- **Deliver actionable recommendations** for marketing and product teams.

---

## Data

- **Source:** Historical car insurance data (Feb 2014 – Aug 2015)
- **File:** `data/MachineLearningRating_v3.txt`
- **Format:** Pipe-separated (`|`) text file

### Key Data Columns

- **Policy Info:** UnderwrittenCoverID, PolicyID, TransactionMonth
- **Client Info:** IsVATRegistered, Citizenship, LegalType, Title, Language, Bank, AccountType, MaritalStatus, Gender
- **Location:** Country, Province, PostalCode, MainCrestaZone, SubCrestaZone
- **Vehicle:** ItemType, mmcode, VehicleType, RegistrationYear, Make, Model, Cylinders, cubiccapacity, kilowatts, bodytype, NumberOfDoors, VehicleIntroDate, CustomValueEstimate, AlarmImmobiliser, TrackingDevice, CapitalOutstanding, NewVehicle, WrittenOff, Rebuilt, Converted, CrossBorder, NumberOfVehiclesInFleet
- **Plan:** SumInsured, TermFrequency, CalculatedPremiumPerTerm, ExcessSelected, CoverCategory, CoverType, CoverGroup, Section, Product, StatutoryClass, StatutoryRiskType
- **Claims:** TotalPremium, TotalClaims

---

## Project Tasks

### Task 1: Git, EDA & Stats

- Set up GitHub repo & branches
- Perform Exploratory Data Analysis (EDA)
  - Data summarization & quality checks
  - Univariate & bivariate analysis
  - Outlier detection
  - Visualization (at least 3 creative plots)
- Commit work regularly with descriptive messages

### Task 2: Data Version Control (DVC)

- Install and initialize DVC
- Track and version datasets
- Set up local remote storage
- Commit `.dvc` files and push data

### Task 3: A/B Hypothesis Testing

- Define and segment data for hypothesis tests
- Test for risk and margin differences by province, zip code, and gender
- Use appropriate statistical tests (chi-squared, t-test, etc.)
- Interpret results and provide business recommendations

### Task 4: Predictive Modeling

- Prepare data (imputation, encoding, feature engineering)
- Build and evaluate models:
  - Linear Regression
  - Random Forest
  - XGBoost
- Use SHAP or LIME for model interpretability
- Report on feature importance and business implications

---

## Project Workflow

This project follows a typical data analytics and machine learning pipeline, designed for transparency, reproducibility, and business impact:

1. **Repository & Environment Setup**
   - Initialize a GitHub repository for version control and collaboration.
   - Set up your Python environment and install all dependencies from `requirements.txt`.
   - (Optional but recommended) Initialize [DVC](https://dvc.org/doc/) for data versioning and reproducibility.

2. **Data Acquisition & Understanding**
   - Obtain the historical car insurance dataset (`data/MachineLearningRating_v3.txt`).
   - Load the data using pandas, ensuring correct parsing of pipe-separated values.
   - Review the data schema and familiarize yourself with key columns related to policy, client, vehicle, plan, and claims.

3. **Exploratory Data Analysis (EDA)**
   - Summarize the dataset: check data types, missing values, and descriptive statistics.
   - Visualize distributions of key variables (e.g., TotalPremium, TotalClaims, CustomValueEstimate).
   - Detect and handle outliers and missing data.
   - Explore relationships between variables using correlation matrices, scatter plots, and group comparisons (e.g., by province, gender, vehicle type).
   - Document initial insights and potential data quality issues.

4. **Statistical Analysis & Hypothesis Testing**
   - Formulate business-relevant hypotheses (e.g., risk differences across provinces, zip codes, or gender).
   - Segment the data as needed for control and test groups.
   - Apply appropriate statistical tests (e.g., t-tests, chi-squared tests) to validate or reject hypotheses.
   - Interpret results in the context of insurance risk and profitability.

5. **Feature Engineering & Data Preparation**
   - Clean and preprocess the data: impute missing values, encode categorical variables, and engineer new features as needed.
   - Convert relevant columns to appropriate data types (e.g., dates, categories, numerics).
   - Split the data into training and testing sets for modeling.

6. **Predictive Modeling**
   - Build regression and classification models to predict claim severity and optimize premiums.
   - Experiment with different algorithms (e.g., Linear Regression, Random Forest, XGBoost).
   - Evaluate model performance using metrics such as RMSE, R-squared, accuracy, and F1-score.
   - Use model interpretation tools (e.g., SHAP, LIME) to identify the most influential features and explain predictions.

7. **Insight Generation & Reporting**
   - Summarize key findings from EDA, hypothesis testing, and modeling.
   - Visualize important results with clear, business-focused plots.
   - Provide actionable recommendations for marketing strategy and risk-based pricing, supported by data and statistical evidence.

8. **Reproducibility & Collaboration**
   - Use Git for code versioning and collaboration.
   - Track data and model versions with DVC to ensure full reproducibility.
   - Document your workflow, decisions, and results clearly in notebooks and reports.

---

## Learning Outcomes

- Data engineering and pipeline management
- EDA, visualization, and statistical analysis
- A/B testing design and interpretation
- Predictive modeling and model explainability
- Version control and reproducibility

---

## Getting Started

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up DVC (optional, for data versioning)**
   ```bash
   dvc init
   dvc remote add -d localstorage /path/to/your/local/storage
   dvc add data/MachineLearningRating_v3.txt
   dvc push
   ```
4. **Run the analysis**
   - Open `notebook/understand.ipynb` in VS Code or Jupyter
   - Follow the code and add your own analysis as needed

---

## References

- [50 Common Insurance Terms and What They Mean — Cornerstone Insurance Brokers](https://www.cornerstoneins.ca/blog/50-common-insurance-terms-and-what-they-mean/)
- [A/B Testing Guide](https://www.optimizely.com/optimization-glossary/ab-testing/)
- [DVC Documentation](https://dvc.org/doc/)
- [SHAP Documentation](https://shap.readthedocs.io/en/latest/)

---





## License

This project is for educational and internal use at AlphaCare Insurance Solutions (ACIS).
