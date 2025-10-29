# 💳 Credit Card Market Analysis & Launch Strategy  

## 👨‍💻 Author
**R. Shrinivass**  
Aspiring Data Scientist  

---

## 🧭 Project Overview
This project aims to identify and analyze the **target market** for launching a **new Credit Card product**, focusing primarily on **young consumers (ages 18–25)**.  

Through a combination of **Exploratory Data Analysis (EDA)** and **A/B Testing**, the project uncovers behavioral and demographic patterns to determine whether launching a **Youth Credit Card** would be a viable and profitable decision.  

---

## 🎯 Objectives

### 🏁 Phase 1 Objective
> To **understand the market** for the credit card launch through analysis of customer profiles, credit behavior, and transaction trends.

### 🧪 Phase 2 Objective
> To **evaluate the effectiveness of the youth-targeted marketing campaign** using **A/B Testing**.

---

## 🧩 Dataset Description

Two primary datasets were used and merged for analysis:

| Dataset | Description |
|----------|--------------|
| `df_cust` | Customer demographic and credit information (age, income, marital status, credit score, credit limit etc.) |
| `df_trans` | Transactional data including transaction ID, platform, payment type, product category, and transaction amount |

After merging, the unified dataset (`df_merged`) provided a 360° view of each customer’s spending and credit behavior.

---

## 🛠️ Tools & Libraries

| Category | Tools Used |
|-----------|-------------|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Statistics | SciPy (for A/B Testing) |
| IDE | Jupyter Notebook / VS Code |

---

## 🔍 Phase 1 – Exploratory Data Analysis (EDA)

The first phase focused on understanding customer demographics, spending patterns, and credit behavior to identify the potential target market.

### 🧱 Steps Performed

1. **Data Cleaning**
   - Treated missing values in demographic and transactional fields.  
   - Handled outliers in the `age` column (removed records < 15 or > 80).  
   - Standardized categorical values.  

2. **Data Merging**
   - Combined `df_cust` and `df_trans` on common customer ID.  

3. **Feature Engineering**
   - Created `age_group` bins:  
     - 18–25, 26–48, 49–65  
   - Derived transaction-based metrics such as total and average transaction value.  

---

### 📊 Visualizations & Insights

#### 1️⃣ Distribution of Payment Types
> *(Insert your countplot here)*  

This helped identify the most common transaction methods used by customers.

---

#### 2️⃣ Customer Age vs Payment Type / Platform / Product Category
> *(Insert your grouped countplots here — two on top, one below)*  

Clear trends emerged showing that the **18–25 age group** predominantly shops online through **Amazon and Flipkart**, mainly purchasing **Fashion & Apparel** and **Electronics**.

---

#### 3️⃣ Average Transaction Value by Demographics
> *(Insert your average transaction value visualization)*  

Younger customers (18–25) had **consistent average transaction values**, making them an attractive, stable target segment.

---

#### 4️⃣ Average Annual Income / Credit Limit / Credit Score by Age Group
> *(Insert the income, limit, and credit score bar charts here)*  

Even though income is relatively lower for younger users, their **credit scores remain healthy**, indicating **low default risk** and **high growth potential**.

---

### 📈 Phase 1 Key Findings

- The **18–25 age group** is the **most promising segment** for a new credit card.  
- Major spending categories: **Fashion & Apparel** and **Electronics**.  
- Preferred platforms: **Amazon**, **Flipkart**.  
- Credit scores are **stable**, showing responsible usage.  

**✅ Conclusion (Phase 1):**  
> The youth segment (18–25 years) has strong potential for a new **Youth Credit Card** with category-specific rewards and digital-first campaigns.

---

## 🧪 Phase 2 – A/B Testing Analysis

### 🎯 Objective
To measure the **effectiveness of the marketing campaign** designed to promote the Youth Credit Card.

### 🧮 Methodology
Two groups were used:  
- **Group A (Control):** No campaign exposure  
- **Group B (Test):** Exposed to the marketing campaign  

Statistical tests:
- **Z-Test** for comparing proportions  
- **p-Value Analysis** for significance  

---

### 📊 Results

- **Z-Score** > **Critical Z-Value** → Reject H₀  
- **p-Value** < **α (0.05)** → Reject H₀  

This shows a **statistically significant difference** between groups — confirming that the marketing campaign **positively impacted customer response**.

---

### 📉 Interpretation

The campaign successfully influenced the youth audience:  
- Improved **engagement and conversion rates**  
- Validated the **receptiveness of the 18–25 age group**  
- Proved the **campaign’s effectiveness** beyond random chance  

---

## 💳 Final Conclusion & Recommendations

Combining findings from **Phase 1** and **Phase 2**:

| Phase | Outcome | Key Insight |
|:------|:--------|:------------|
| Phase 1 | Market Understanding | Identified 18–25 as the most promising segment |
| Phase 2 | Campaign Evaluation | Campaign was statistically effective |

### ✅ Final Conclusion
> The Youth Credit Card can be **successfully launched**, targeting the **18–25 age group**.

### 🚀 Recommendations
- Focus marketing on **digital channels** (social media, e-commerce).  
- Provide **discounts on Fashion & Electronics** purchases.  
- Introduce **cashback and reward points** programs.  
- Keep **credit limits moderate** with **easy onboarding and digital KYC**.  

---


