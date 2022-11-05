from bs4 import BeautifulSoup
import urllib.request
import re
import nltk
import heapq
import requests

class Summarizer():
    def __init__(self, url):
        self.url = url
    def main(self):
        if self.status() == 200:
            self.summarizer()
    def status(self):
        statuses = {
        200: "Website Available",
        301: "Permanent Redirect",
        302: "Temporary Redirect",
        404: "Not Found",
        500: "Internal Server Error",
        503: "Service Unavailable"
        }

        try:
            web_response = requests.get(self.url)
            print(self.url, statuses[web_response.status_code])
            return web_response.status_code
        except:
            print("Website can't be reached")
            return 0

    def summarizer(self):
        scraped_data = urllib.request.urlopen(self.url)
        article = scraped_data.read()

        parsed_article = BeautifulSoup(article,'lxml')

        paragraphs = parsed_article.find_all('p')

        article_text = ""

        for p in paragraphs:
            article_text += p.text

        # Remove square brackets and extra spaces
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
        article_text = re.sub(r'\s+', ' ', article_text)
        # Remove special characters and digits
        formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
        formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
        
        # Tokenize the sentences
        sentence_list = nltk.sent_tokenize(article_text)

        # Find weighted frequency of word occurrence
        stopwords = nltk.corpus.stopwords.words('english')

        word_frequencies = {}
        for word in nltk.word_tokenize(formatted_article_text):
            if word not in stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1

        maximum_frequncy = max(word_frequencies.values())

        for word in word_frequencies.keys():
            word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

        # Calculate sentence score
        sentence_scores = {}
        for sent in sentence_list:
            for word in nltk.word_tokenize(sent.lower()):
                if word in word_frequencies.keys():
                    if len(sent.split(' ')) < 30:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word]
                        else:
                            sentence_scores[sent] += word_frequencies[word]

        summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

        summary = ' '.join(summary_sentences)
        print(summary)