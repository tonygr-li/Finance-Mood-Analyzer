from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User

import cohere
import nltk
from cohere import ClassifyExample
from nltk.tokenize import sent_tokenize

# from .models import Classifier
from django.utils import timezone

# Create your views here.

co = cohere.Client('') # This is your trial API key

# Function to get sentiment from Cohere
def get_sentiment_from_cohere(sentence):
    response = co.classify(
        model='', #fine tuned model id
        inputs=[sentence]
    )
    print('The confidence levels of the labels are: {}'.format(response.classifications))
    return response.classifications[0]

# Aggregation by percentage
def aggregate_sentiments_percentage(sentiments):
    total_sentences = len(sentiments)
    pos_num = 0
    neg_num = 0
    neu_num = 0
    pos_con = 0
    neg_con = 0
    neu_con = 0
    other = 0
    for sentence in sentiments:
        if sentence.prediction == "positive":
            pos_num += 1
            pos_con += sentence.confidence
        elif sentence.prediction == "neutral":
            neu_num += 1
            neu_con += sentence.confidence
        elif sentence.prediction == "negative":
            neg_num += 1
            neg_con += sentence.confidence
        else:
            other += 1

    positive_percentage = (pos_num / total_sentences) * 100
    neutral_percentage = (neu_num / total_sentences) * 100
    negative_percentage = (neg_num / total_sentences) * 100
    
    confidence_num = pos_con - neg_con

    answer_sentence = (f"The analysis results are as follows: {positive_percentage}% positive, "
            f"{neutral_percentage}% neutral, {negative_percentage}% negative, "
            f"with a total confidence of {confidence_num}%.")

    return answer_sentence

def get_percentage(sentiment):
    answer_sentence = "Sentiment analysis results: " + str(sentiment.prediction) + " with a confidence of " + str(sentiment.confidence) + "."
    return answer_sentence

def call_main(message):
    return get_percentage(get_sentiment_from_cohere(message))

def classifier(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        try:
            response = call_main(message)
        except Exception as e:
            response = "Make sure to input valid cohere api key and your fine tuned model id!"
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'classifier.html')