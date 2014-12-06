# -*- coding: cp1252 -*-
import nltk
import re
import glob
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

class process:

    def clean(self,text):
        t=self.remove_stopwords(nltk.word_tokenize(text))
        t1=self.lemmatize(t)
        t2=self.stemming(t1)
        return t2

    def remove_stopwords(self,text_tokens):
        nostop=[word for word in text_tokens if not word in stopwords.words('english') and len(word)>3]
        return nostop

    def lemmatize(self,text_tokens):
        wnl = nltk.WordNetLemmatizer()
        return [wnl.lemmatize(t) for t in text_tokens ]


    def stemming(self,text_tokens):
        porter = nltk.PorterStemmer()
        return [porter.stem(t) for t in text_tokens if len(porter.stem(t)) > 3]

    def generateTopics(corpus, dictionary):
        # Build LDA model using the above corpus
        lda = models.LdaModel(corpus, id2word=dictionary, num_topics=15)
        corpus_lda = lda[corpus]

        # Group topics with similar words together.
        tops = set(lda.show_topics(15,15))
        top_clusters = []
        for l in tops:
            top = []
            for t in l.split(" + "):
                top.append((t.split("*")[0], t.split("*")[1]))
            top_clusters.append(top)

     # Generate word only topics
        top_wordonly = []
        for i in top_clusters:
            top_wordonly.append(":".join([j[1] for j in i]))

        return lda, corpus_lda, top_clusters, top_wordonly


    def run(self):
        texts=[]
        file = "destinaton.csv"
        with open(file,'r') as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
        	text=line[1]
                clean_text=self.clean(text)
                texts.append(clean)
        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]
        tfidf = models.TfidfModel(corpus)
        corpus_tfidf = tfidf[corpus]
        lda, corpus_lda, topic_clusters, topic_wordonly = generateTopics(corpus_tfidf, dictionary)
        lda.save("lda{0}_model.lda".format(15))

        for i in range(0, 15):
            temp = lda.show_topic(i, 10)
            terms = []
            for term in temp:
                terms.append(term[1])
                print "Topic #" + str(i) + ": "+ ", ".join(terms)



handle=process()    
handle.run()
