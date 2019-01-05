from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import CountVectorizer


filesid = []
content = []
contents = []
for label in movie_reviews.categories():
    for fileid in movie_reviews.fileids(label):
        filesid.append(fileid)
        content.append(movie_reviews.words(fileid))

#join成一個list
for i in range(len(content)):
    content[i] = [' '.join(content[i])]      
#    降維(去中括號)
    content[i] = str(content[i])
    content[i] = content[i].replace('[','')
    content[i] = content[i].replace(']','')
    contents.append(content[i])
    
#word_dict={
#        "ID":filesid,
#        "content":content
#        }        

#BOW 某個單詞在文檔中出現次數
vectorizer = CountVectorizer()
X =  vectorizer.fit_transform(contents)
print(vectorizer.get_feature_names())
print(X.toarray())

#查看X內的出現次數
for i in range(1,10000):
    if X[0,i]>0:
        print(X[0,i])