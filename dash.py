
import streamlit as st
import requests
import pandas as pd


def main():
    st.set_page_config(page_title="Dashboard")
    st.title("Dashboard")
    st.write("Enter your python script")
    script = st.text_area('Script', 'print("Hello, world!")', height=200)

    if st.button('Run'):
        data = requests.post("http://127.0.0.1:5000/", data=script,
                             headers={"Content-Type": "application/json"})
        print("DASH >>> \n data: ", data.json())
        print("DASH >>> \n script: ", script)
        st.write(data.json())
        df = pd.DataFrame(data.json()['data'])
        st.bar_chart(df)


if __name__ == '__main__':
    main()
