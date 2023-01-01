import json
import gensim
from gensim import corpora
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
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

def get_LDA(name):
    with open('./Data/'+name+'.json', encoding='utf-8-sig', errors='ignore') as json_file:
        data = json.load(json_file)

    doc_complete = []
    for i in range(len(data)):
        for j in range(len(data[i]["comment"])):
            doc_complete.append(data[i]["comment"][j]["text"])

    # 移除标点符号，停用词和标准化语料库（Lemmatizer，对于英文，将词归元）。
    stop = set(stopwords.words('english'))
    exclude = set(string.punctuation)
    lemma = WordNetLemmatizer()

    doc_clean = [clean(doc).split() for doc in doc_complete]

    # 创建语料的词语词典，每个单独的词语都会被赋予一个索引
    dictionary = corpora.Dictionary(doc_clean)

    # 使用上面的词典，将转换文档列表（语料）变成 DT 矩阵
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

    # 使用 gensim 来创建 LDA 模型对象
    Lda = gensim.models.ldamodel.LdaModel

    # 在 DT 矩阵上运行和训练 LDA 模型
    ldamodel = Lda(doc_term_matrix, num_topics=6, id2word=dictionary, passes=50)

    # 输出结果
    print("数据总长度：", len(doc_complete))
    list = ldamodel.print_topics(num_topics=6, num_words=6)
    print(list)
    nums = []  # 存放关键词
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


    #进行数据库的操作

    # 写入文件方便解析
    f = open("../词云图/Chinese Medicine.txt", "w")

    for line in nums:
        f.write(line + '\n')
    f.close()
