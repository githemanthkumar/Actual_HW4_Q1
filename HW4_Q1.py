import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab') # Download the punkt_tab data

def preprocess_sentence(sentence):
    # Initialize stemmer
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))

    # Step 1: Tokenization
    tokens = word_tokenize(sentence)
    print("Original Tokens:", tokens)

    # Step 2: Remove Stopwords
    tokens_no_stopwords = [word for word in tokens if word.lower() not in stop_words and word.isalpha()]
    print("Tokens Without Stopwords:", tokens_no_stopwords)

    # Step 3: Apply Stemming
    stemmed_tokens = [stemmer.stem(word) for word in tokens_no_stopwords]
    print("Stemmed Words:", stemmed_tokens)

# Example sentence
sentence = "NLP techniques are used in virtual assistants like Alexa and Siri."
preprocess_sentence(sentence)
