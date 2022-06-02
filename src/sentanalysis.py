import typing
from ast import Str
from typing import List

import spacy
from transformers import pipeline

def spacy_sentiment(sentence: Str)->typing.Dict[Str, float]:
    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe('spacytextblob')
    doc = nlp(sentence)
    output_dict = {}
    output_dict['polarity'] = (doc._.blob.polarity)
    output_dict['subjectivity'] = (doc._.blob.subjectivity)
    return output_dict

def hf_analysis(sentence: Str)->List:
    sentiment_analysis = pipeline("sentiment-analysis", model="siebert/sentiment-roberta-large-english")
    return sentiment_analysis(sentence)
