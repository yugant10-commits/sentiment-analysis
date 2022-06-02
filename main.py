import streamlit as st

from src.plotgraphs import make_radar_graph
from src.sentanalysis import hf_analysis
from src.sentanalysis import spacy_sentiment

if __name__ == "__main__":
    st.write("Welcome")
    user_input = st.text_input("Enter a sentence", key="name")
    result = st.button("Submit")
    if result:
        new_sentiment = hf_analysis(user_input)
        output = new_sentiment.pop()
        doc = spacy_sentiment(user_input)
        st.plotly_chart(make_radar_graph(doc))
        st.write(doc)
        st.write(
            "Prediction by using SiEBERT - English-Language Sentiment Classification"
        )
        st.write(output)
