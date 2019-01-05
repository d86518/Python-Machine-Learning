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

f=open("metamorphosis_franz_kafka.txt",'r')
lines=f.read()
tokens = word_tokenize(lines)
tokens = remove_stopwords(remove_punc(tokens))
#各單字數量
word_count = Counter(tokens)

#Counting Collocations with dist

##################################################            
print("************frequency-based with stopword removing************")
print("W1\tW2\tCount")
window_size = 9
word_pair_counts = Counter()
word_pair_dist_counts = Counter()
for i in range(len(tokens)-1):
    for dist in range(1,window_size):
        if i+dist<len(tokens):
            w1 = tokens[i]
            w2 = tokens[i+dist]
            word_pair_dist_counts[(w1,w2,dist)]+=1
            word_pair_counts[(w1,w2)]+=1

for (w1,w2),c in word_pair_counts.most_common(40):
    print("%s\t%s\t%d" % (w1,w2,c))
print("*****************************************")         
##################################################            
#chi-square part
# o11 = w1w2 o12 = w2
# o21 = w1 o22 = X
# a = 0.05 x^2=3.841 Ho independent if大於 = 拒絕 => 有關連
def chisqu(o11,o12,o21,o22):
    n = o11+o12+o21+o22
    x2 = (n*((o11*o22-o12*o21)**2))/((o11+o12)*(o11+o21)*(o12+o22)*(o21+o22))
    return x2   

##.most_common抓最常
print("************ Chi-square test ************")
print("W1\tW2\tChi-square")
for (w1,w2),c in word_pair_counts.most_common(40):
    o11 = c
    o21 = Counter(tokens)[w1] - o11 
    o12 = Counter(tokens)[w2] - o11  
    o22 = len(tokens) - o21 - o12 + o11     
    chi = chisqu(o11,o21,o12,o22)
    print("%s\t%s\t%d" % (w1,w2,chi))
print("*****************************************")
####################################################

#mutual_information
import math
def mutual_information(w1_w2_prob, w1_prob, w2_prob):
    return math.log2(w1_w2_prob / (w1_prob * w2_prob))

print("************ Mutual Information ************")
print("W1\tW2\tMI")
for (w1,w2),c in word_pair_counts.most_common(40):
    w1_prob = Counter(tokens)[w1]/len(tokens)
    w2_prob = Counter(tokens)[w2]/len(tokens)
    w1_w2_prob = c
    mutual = mutual_information(w1_w2_prob, w1_prob, w2_prob)
    print("%s\t%s\t%s" % (w1,w2,mutual))
print("*****************************************")
####################################################