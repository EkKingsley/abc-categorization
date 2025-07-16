import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="ABC Categorization Tool", layout="centered")
st.title("📊 ABC Categorization App")

uploaded_file = st.file_uploader("Upload your .xlsx or .csv file", type=["xlsx", "csv"])

if uploaded_file:
    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("### Preview of Uploaded Data", df.head())

    # ID column
    id_col = st.selectbox("Select the ID column (e.g., Product, SKU, or Customer)", df.columns)

    # Value/Volume columns
    value_cols = st.multiselect(
        "Select one or two numeric columns for ABC categorization",
        [col for col in df.columns if col != id_col],
    )

    if len(value_cols) not in [1, 2]:
        st.warning("Please select either one or two columns.")
    else:
        if st.button("Run ABC Categorization"):
            # Always start with ID + selected columns
            result_df = df[[id_col] + value_cols].copy()

            def abc_classify(input_df, col):
                temp = input_df[[id_col, col]].copy()
                temp = temp.sort_values(by=col, ascending=False)
                temp["Cumulative"] = temp[col].cumsum()
                total = temp[col].sum()
                temp["Perc"] = temp["Cumulative"] / total
                temp[f"{col}_ABC"] = pd.cut(
                    temp["Perc"],
                    bins=[0, 0.8, 0.95, 1.0],
                    labels=["A", "B", "C"],
                    include_lowest=True
                )
                return temp[[id_col, f"{col}_ABC"]]

            # Collect all ABC columns
            abc_frames = []
            for col in value_cols:
                abc_labels = abc_classify(df, col)
                abc_frames.append(abc_labels)

            # Merge all ABC labels back to result_df
            for abc_frame in abc_frames:
                result_df = result_df.merge(abc_frame, on=id_col, how="left")

            st.write("### ✅ Final Categorized Table", result_df.head())

            towrite = io.BytesIO()
            result_df.to_excel(towrite, index=False, sheet_name="ABC_Result")
            towrite.seek(0)

            st.download_button(
                label="📥 Download Categorized Data",
                data=towrite,
                file_name="abc_categorization.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
