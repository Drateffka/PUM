import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(path):
    df = pd.read_csv(path)
    return df


def data_info(path):
    st.write(
        "Info about dataset: https://www.kaggle.com/datasets/abhinavshaw09/data-science-job-salaries-2024?resource=download"
    )

    data = load_data(path)

    st.write("You can download this file here:")
    st.download_button("Download file", data.to_csv().encode("utf-8"))

    st.write(
        "If you want to upload your own file you can do it here (only csv files with headers will work properly!):"
    )

    file = st.file_uploader("Upload file", "csv", accept_multiple_files=False)

    if file is not None:
        data = load_data(file)

    return data


def histograms(df):
    st.subheader("Histogram")

    series = (df.dtypes == "int64") | (df.dtypes == "float")
    series = series[series].index.to_list()

    option = st.selectbox("Select column for histogram", series)
    x = st.slider(
        "Histogram max value",
        min_value=df[option].min(),
        max_value=df[option].max(),
        value=int(df[option].mean()),
    )

    plt.figure(figsize=(8, 6))
    ax = sns.histplot(data=df, x=option, color="salmon")
    ax.set(xlim=[df[option].min(), x])
    st.pyplot(plt)


def boxplots(df):
    st.subheader("Box plots:")
    sns.boxplot(df, palette="flare")
    st.pyplot(plt)


def countplots(df):
    st.subheader("Count plot:")
    series = (df.dtypes == "int64") | (df.dtypes == "float")
    series = series[~series].index.to_list()
    option = st.selectbox("Select column for countplot", series)

    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x=option, palette="flare")
    st.pyplot(plt)


def cardinality(df):
    st.subheader("Cardinality & counts:")
    option = st.selectbox(
        "Select column that you want to check cardinality", df.columns
    )

    st.write(option)
    st.write(df[option].value_counts())


def explore_data(df):
    st.subheader("Data:")
    st.write(df)

    st.subheader("Basic statistical informations:")
    st.write(df.describe())

    st.subheader("Missing values:")
    st.write(df.isnull().sum())

    # Histogram
    histograms(df)

    # Boxplots
    boxplots(df)

    # Count plot
    countplots(df)

    # Cardinality
    cardinality(df)


def main():

    st.title("EDA app for Data Science Job Salaries 2024 dataset")

    path = "salaries.csv"
    data = data_info(path)

    explore_data(data)


if __name__ == "__main__":
    main()
