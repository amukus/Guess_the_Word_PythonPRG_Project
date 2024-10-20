#Importing random library for random generation and requests to request for API

import random
import requests

#Function for shuffling letters within a word

def shuffle_word(word):
    listed_word = list(word)
    random.shuffle(listed_word)
    return ''.join(listed_word)

#To fetch a random word using API we use the function below

def get_word_random():

    try:
        response = requests.get("https://random-word-api.herokuapp.com/word")
        response.raise_for_status() #This part will check for http errors
        word = response.json()[0] #This uses json for getting the first available word from API response
        return word
    except (requests.RequestException, IndexError) as e:
        print("Error while fetching word from API: {e}")
        return "fallback" # Provides a fallback word in case of API failure

#Function to check if the guessed word is correct

def guess_correct(guess, original_word):
    return guess.lower() == original_word.lower()

