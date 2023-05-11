
import streamlit as st
import requests


def main():
    st.set_page_config(page_title="Dashboard")
    st.title("Dashboard")
    st.write("Enter your python script")
    script = st.text_area('Script', 'print("Hello, world!")', height=200)

    if st.button('Run'):
        data = requests.post("http://127.0.0.1:5000/", data={'script': script},
                             headers={"Content-Type": "application/json"})
        print("data: ", data)
        print("script: ", script)
        st.write(data)


if __name__ == '__main__':
    main()
