import pandas as pd
import yfinance as yf
import streamlit as st
import boto3

def main():

    newfile = st.file_uploader("Upload file", type="csv")
    show_file = st.empty()

    if not newfile:
        show_file.info("Please upload a file of type: " + ", ".join(["csv"]))
        return

    upload_files(newfile)

    data = pd.read_csv(newfile)
    st.dataframe(data.head(10))

def upload_files(newfile):
    s3 = boto3.resource('s3')
    bucket = 'parkerroy-source'
    #bucket = s3.Bucket('parkerroy-source')
    file_details = newfile.name
    content = newfile.getvalue()

    s3.Bucket(bucket).put_object(Key=file_details, Body=content)

    print(file_details, "Uploaded Successfully to S3 Bucket:", bucket)
    return True

main()
