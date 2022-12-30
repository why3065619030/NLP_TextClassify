#https://blog.csdn.net/selinda001/article/details/80446766
doc1 = "Since the general aim for every human on earth is to grow and infrastructure and trade are the primary means for any kind of growth, I find it a net good deal considering all possible pros and cons it could bring to everyone."
doc2 = "Thanks for delineating in bits and pieces the belt and road initiative programs."
doc3 = "Given china is mainly a export oriented economy, China feels strongly that it needs a secure and diversified trading routes which  it lacks now and it current trading route can be easily cut off by the US especially in areas like the south china sea and Singapore straits in event there is any trade or oil embargo impose on China. So this really explain why China desperately wants to create new alternative trading routes through the one belt one road to improve connectivity between countries so that it will be able to safely transport its good across."
doc4 = "China needs to leverage a long term approach. Trade routes need to be economic to make economic sense."
doc5 = "China gets to use their excess labor, state-owned enterprise capacity, and keep strategic allies indebted to them. The leaders of the target country get to tout achievements and are paid under the table. The general population gets desperately needed infrastructure. It's a win-win-win strategy. I'm not implying China cares about the target country, but why would/should they?"
doc6 = "The freedom of navigation is the primary reason why trade can rely on this for goods to be reliably exchanged globally. Can land route achieved the same kind of freedom of movement? During times of peace, I think it may still be possible but it is still challenging. Without international law governing the freedom of movement of goods via land route, any country can simply impose unilateral border control measures."
doc7 = "With the kind of leaders pakistan has, and it's never ending dependency to rely on others, it will always remain a stooge of other super powers."
# 整合文档数据

import json
with open('../bertData/Chinese Medicine.json',encoding='utf-8-sig', errors='ignore') as json_file:
    data = json.load(json_file)

doc_complete = []
for i in range(len(data)):
    for j in range(len(data[i]["comment"])):
        doc_complete.append(data[i]["comment"][j]["text"])

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
#移除标点符号，停用词和标准化语料库（Lemmatizer，对于英文，将词归元）。
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

#计算困惑度
def perplexity(num_topics):
    ldamodel = LdaModel(corpus, num_topics=num_topics, id2word = dictionary, passes=30)
    print(ldamodel.print_topics(num_topics=num_topics, num_words=15))
    print(ldamodel.log_perplexity(corpus))
    return ldamodel.log_perplexity(corpus)
#计算coherence
def coherence(num_topics):
    ldamodel = LdaModel(corpus, num_topics=num_topics, id2word = dictionary, passes=30,random_state = 1)
    print(ldamodel.print_topics(num_topics=num_topics, num_words=10))
    ldacm = CoherenceModel(model=ldamodel, texts=data_set, dictionary=dictionary, coherence='c_v')
    print(ldacm.get_coherence())
    return ldacm.get_coherence()

doc_clean = [clean(doc).split() for doc in doc_complete]

import gensim
from gensim import corpora

# 创建语料的词语词典，每个单独的词语都会被赋予一个索引
dictionary = corpora.Dictionary(doc_clean)

# 使用上面的词典，将转换文档列表（语料）变成 DT 矩阵
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# 使用 gensim 来创建 LDA 模型对象
Lda = gensim.models.ldamodel.LdaModel

# 在 DT 矩阵上运行和训练 LDA 模型
ldamodel = Lda(doc_term_matrix, num_topics=6, id2word = dictionary, passes=50)

#输出结果
print("数据总长度：",len(doc_complete))
list = ldamodel.print_topics(num_topics=6, num_words=6)
print(list)
nums = []   #存放关键词
for i in range(6):
    st = list[i][1]
    ans = st.split("\"")
    nums.append(ans[1])
    nums.append(ans[3])
    nums.append(ans[5])
    nums.append(ans[7])
    nums.append(ans[9])
    nums.append(ans[11])
print(set(nums))
#写入文件方便解析
f = open("../词云图/Chinese Medicine.txt", "w")

for line in nums:
    f.write(line+'\n')
f.close()
