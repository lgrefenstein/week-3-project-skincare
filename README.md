# Clean vs. Conventional Skincare: Are “Clean” Products Less Irritating?

## Project Overview
This project explores whether skincare products marketed as **“clean”** actually contain fewer potentially irritating ingredients than **conventional** products.

The analysis was conducted as part of the Ironhack Data Analytics Bootcamp (Data Wrangling Project).

---

## Research Question
Do clean skincare products contain fewer potentially irritating ingredients than conventional skincare products?

---

## Hypothesis
Clean skincare products contain fewer potentially irritating ingredients on average than conventional products.

---

## Data Sources

### Clean Skincare Products
- Source: Lookfantastic (clean category)
- Method: Web scraping
- File: `data/clean_skincare_final.csv`

### Conventional Skincare Products
- Source: Kaggle cosmetics dataset https://www.kaggle.com/datasets/kingabzpro/cosmetics-datasets
- Method: Filtering + manual brand selection (top conventional brands)
- File: `data/conventional_skincare_final.csv`

### Irritant Ingredient List
- Source: Curated list of commonly known cosmetic irritants
- File: `data/irritants.csv`

---

## Key Challenge
Our initial plan was to use the **Open Beauty Facts API**, but it lacked a clear classification between *clean* and *conventional* products.

Additional scraping attempts were unreliable, so we adapted our approach and constructed both datasets manually based on:
- retailer-defined clean categories
- curated selection of conventional brands

---

## Data Cleaning & Preparation
Main steps included:

- Removing duplicates  
- Standardizing column names  
- Aligning dataset structures  
- Checking for missing values  
- Cleaning ingredient strings  
- Selecting relevant columns for comparison  
- Merging datasets into a unified analysis dataset  

---

## Methodology

### Irritation Score
We created a simple **irritation score** by counting how many potentially irritating ingredients appear in each product’s ingredient list.

This serves as a proxy to compare products across both categories.

---

## Results

- **Clean products (avg. score):** 2.75  
- **Conventional products (avg. score):** 3.37  

### Key Insight
Clean products tend to have **lower average irritation scores**, while conventional products show **more high-score outliers**.

This supports the hypothesis — but only partially.

---

## Interpretation

- “Clean” products are **less irritating on average**  
- However, **both categories still contain irritants**  
- “Clean” ≠ irritation-free  

---

## Limitations

- Irritation score is a **simplified proxy**, not a clinical measure  
- No information on **ingredient concentration**  
- “Clean” is based on **retailer classification**, not a universal definition  
- Ingredient list is **not exhaustive**  
- Individual skin sensitivity is not considered  

---

## Project Structure

```bash
week-3-project-skincare/
│
├── data/
│   ├── clean_skincare_final.csv
│   ├── conventional_skincare_final.csv
│   ├── irritants.csv
│   └── products_with_scores.csv
│
├── notebooks/
│   ├── Clean Scraping.ipynb
│   ├── Clean Skincare Dataset.ipynb
│   ├── conventional-skincare.ipynb
│   ├── final_analysis.ipynb
│   └── app.py
│
├── .gitignore
└── README.md

Key Files
* notebooks/final_analysis.ipynbMain notebook containing data merging, feature engineering, and analysis
* notebooks/conventional-skincare.ipynbPreparation of conventional skincare dataset
* notebooks/Clean Skincare Dataset.ipynbPreparation of clean skincare dataset
* notebooks/app.pyStreamlit app for interactive exploration

⸻

Interactive Dashboard (Bonus)
We developed a small Streamlit dashboard that allows users to:
* explore irritant ingredients
* compare their frequency across product types
* better understand ingredient-level differences

⸻

Tools & Technologies
* Python
* Pandas
* Seaborn & Matplotlib
* Jupyter Notebook
* Streamlit
* Git & GitHub
* Trello
* Slack

⸻

Repository
https://github.com/lgrefenstein/week-3-project-skincare

⸻

Project Management
Trello board: https://trello.com/invite/b/69dca2fa41557d7325f89d08/ATTI0d826488234939ed8f7c9bdd639f83e4F8F972DC/week-3-project

⸻

Presentation
Slides: https://docs.google.com/presentation/d/1Gbl55odjiI3AKXKOJku__5ASdd1HwEk4itnMoCYvOq0/edit?usp=sharing

⸻

Data Sources (Links)
* Lookfantastic: https://www.lookfantastic.com/c/health-beauty/organic-natural/view-all-natural-organic/
* Kaggle Cosmetics Dataset: https://www.kaggle.com/datasets/kingabzpro/cosmetics-datasets

⸻

Team
* Adriana Alves
* Ludmilla Grefenstein

⸻

Key Learning
Working with real-world data requires flexibility —data availability and structure often shape the final approach more than the initial plan.

⸻

Future Improvements
* Expand irritant classification
* Include ingredient concentration data
* Apply statistical testing
* Perform brand-level analysis
* Integrate dermatological data
