# 📊 ABC Categorization Tool

A simple Streamlit app for your procurement, sales, and finance teams to quickly perform **ABC analysis** on products or customers.

---

## 🚀 What it does

- 📁 Upload a `.csv` or `.xlsx` file with your data (e.g., products, sales, customers).
- ✅ Choose the **ID column** (Product, SKU, or Customer).
- 📈 Select **one or two numeric columns** for ABC analysis (e.g., Sales Value, Sales Volume).
- 🔤 The app calculates **ABC categories**:
  - **A:** Top ~80% of value/volume
  - **B:** Next ~15%
  - **C:** Remaining ~5%
- 📥 Download the categorized data for reporting or further analysis.

---

## 📂 Example input

| Product | Sales Value | Sales Volume |
|---------|--------------|---------------|
| Prod A  | 10,000       | 200           |
| Prod B  | 8,000        | 180           |
| Prod C  | 3,000        | 100           |
| ...     | ...          | ...           |

---

## ✅ Example output

| Product | Sales Value | Sales Volume | Sales Value_ABC | Sales Volume_ABC |
|---------|--------------|---------------|------------------|-------------------|
| Prod A  | 10,000       | 200           | A                | A                 |
| Prod B  | 8,000        | 180           | A                | A                 |
| Prod C  | 3,000        | 100           | B                | B                 |
| ...     | ...          | ...           | ...              | ...               |

---

## 📌 How to use it

1. Click the **"Deploy"** button or open the deployed app link.
2. Upload your data file (`.xlsx` or `.csv`).
3. Select the **ID column** and **numeric columns** for ABC.
4. Click **Run**.
5. View the categorized data.
6. Download the result.

---

## 🌐 Deployed App

👉 [Click here to open the app](YOUR_DEPLOYED_APP_LINK)

Replace `YOUR_DEPLOYED_APP_LINK` with your **Streamlit Cloud** deployment URL.

---

## 🛠️ Local development (optional)

If you want to run it locally:
```bash
# Clone this repo
git clone https://github.com/YOUR_ORG/abc-categorization-tool.git
cd abc-categorization-tool

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
