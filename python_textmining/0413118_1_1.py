#p1:因為 if ch==" " 是抓到空格時把前一個字append到tokens，那標點符號都會跟著被帶進去前一個字的尾巴，造成無法分析

#p2:換行符要去掉，用replace代替成空字串

from collections import Counter
import string
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
stopword_list = stopwords.words('english')

f=open("corpus.txt",'r')
lines=f.read()

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

##test problematic token
def tokenize(text):
    ##要斷換行
    text = text.replace("\n","")
    tokens=[]
    tok=""
    punc = []
    punc.append(string.punctuation)
    #一次一個ch
    for ch in text:
        #抓到空格時把前一個字送到tokens
        if ch==" ":
            #tok=empty
            if tok:
                tokens.append(tok)
                tok=""
        #遇到符號就丟
        elif ch in punc:
            if tok:
                tokens.append(tok)
                tok=""
        #非空格連起來
        else:
            tok+=ch
    return tokens

print(tokenize(lines))

tokens = tokenize(lines)
tokens = remove_stopwords(remove_punc(tokens))
word_count = Counter(tokens)
print(word_count)