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
            if tok!="''" and tok!='``' and tok!= "'s":
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
##token original
token = word_tokenize(lines)
tokens = remove_stopwords(remove_punc(tokens))
#各單字數量
word_count = Counter(tokens)

#Counting Collocations with dist
window_size = 9
word_pair_counts = Counter()
word_pair_dist_counts = Counter()

tokens = nltk.pos_tag(tokens)


#mutual_information
import math
def mutual_information(w1_w2_prob, w1_prob, w2_prob):
    return math.log2(w1_w2_prob / (w1_prob * w2_prob))

## N/N MI
for i in range(len(tokens)-1):
    for dist in range(1,window_size):
        if i+dist<len(tokens):
            if tokens[i][1]=='NN':
                w1 = tokens[i][0]
                if tokens[i+dist][1]=='NN':
                    w2 = tokens[i+dist][0]
                    word_pair_dist_counts[(w1,w2,dist)]+=1
                    word_pair_counts[(w1,w2)]+=1

print("--------N / N --------")
for (w1,w2),c in word_pair_counts.most_common(40):
    w1_prob = Counter(token)[w1]/len(token)
    w2_prob = Counter(token)[w2]/len(token)
    w1_w2_prob = c
    mutual = mutual_information(w1_w2_prob, w1_prob, w2_prob)
    print("%s\t%s\t%s" % (w1,w2,mutual))





word_pair_counts = Counter()
word_pair_dist_counts = Counter()
## N/N MI
for i in range(len(tokens)-1):
    for dist in range(1,window_size):
        if i+dist<len(tokens):
            if tokens[i][1]=='NNP':
                w1 = tokens[i][0]
                if tokens[i+dist][1]=='NN':
                    w2 = tokens[i+dist][0]
                    word_pair_dist_counts[(w1,w2,dist)]+=1
                    word_pair_counts[(w1,w2)]+=1

print("--------NNP / N --------")
for (w1,w2),c in word_pair_counts.most_common(40):
    w1_prob = Counter(token)[w1]/len(token)
    w2_prob = Counter(token)[w2]/len(token)
    w1_w2_prob = c
    mutual = mutual_information(w1_w2_prob, w1_prob, w2_prob)
    print("%s\t%s\t%s" % (w1,w2,mutual))
    
    
    
    
    
word_pair_counts = Counter()
word_pair_dist_counts = Counter()
## N/N MI
for i in range(len(tokens)-1):
    for dist in range(1,window_size):
        if i+dist<len(tokens):
            if tokens[i][1]=='JJ':
                w1 = tokens[i][0]
                if tokens[i+dist][1]=='NN':
                    w2 = tokens[i+dist][0]
                    word_pair_dist_counts[(w1,w2,dist)]+=1
                    word_pair_counts[(w1,w2)]+=1

print("-------- J / N --------")
for (w1,w2),c in word_pair_counts.most_common(40):
    w1_prob = Counter(token)[w1]/len(token)
    w2_prob = Counter(token)[w2]/len(token)
    w1_w2_prob = c
    mutual = mutual_information(w1_w2_prob, w1_prob, w2_prob)
    print("%s\t%s\t%s" % (w1,w2,mutual))