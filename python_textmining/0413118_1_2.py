from nltk.tokenize import word_tokenize
import nltk

from collections import Counter
import string

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')

from nltk.corpus import stopwords
nltk.download('stopwords')
stopword_list = stopwords.words('english')

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

def remove_punc(tokens):
    clean_tokens=[]
    for tok in tokens:
        if tok not in string.punctuation:
            clean_tokens.append(tok)
    return clean_tokens

def remove_stopwords(tokens):
    tokens_clean=[]
    for tok in tokens:
        if tok not in stopword_list:
            tokens_clean.append(tok)
    return tokens_clean

#unnecessary
def lowercase(tokens):
    tokens_lower = []
    for tok in tokens:
        tokens_lower.append(tok.lower())
    return tokens_lower

def lemmatize(token):
    for p in ['v','n','a','r','s']:
        l = wordnet_lemmatizer.lemmatize(token,pos=p)
        if l!=token:
            return l 
    return token

f=open("corpus.txt",'r')
lines=f.read()
tokens = word_tokenize(lines)
tokens = remove_stopwords(remove_punc(tokens))

#做stem (unnecessary)
#stemmed_tokens=[]
#for tok in tokens:
#    stemmed_tokens.append(stemmer.stem(tok))   
#print(lemmatize(stemmed_tokens))
#tokens = stemmed_tokens

#visualize preparing
vis=""
for i in tokens:
    vis+=i
    vis+=' '
    
word_count = Counter(tokens)
print(word_count)