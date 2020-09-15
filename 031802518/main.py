import jieba
import math
import sys
#import cut
def tokenization(orig,orig_sim):
    stopwords_position=open('stop_words','r',encoding="UTF-8")
    stopwords = stopwords_position.read()
    stopwords_position.close()
    #分别对原论文和需要查重的论文进行分词，采用结巴分词，并且在结巴分词后要去掉停用词以提高准确性
    orig_cut = []
    data1 = jieba.cut(orig)
    for i in data1:
        if (i not in stopwords) and i != '':
            orig_cut.append(i)
    orig_sim_cut = []
    data2 = jieba.cut(orig_sim)
    for j in data2:
        if (j not in stopwords) and j != '':  # 不是停词表中的可以加
            orig_sim_cut.append(j)
    # print('s1_cut:',s1_cut)
    # print('s2_cut:',s2_cut)
    word_set = set(orig_cut).union(set(orig_sim_cut))

    # print('word_set',word_set)#s1_cut是s1的分词表，s1_cut是s2的分词表，word_set是这两个表的集合，可以把这两个表中重合的删掉
    return word_set,orig_cut,orig_sim_cut
#import dict
def dictionary(word_set,orig_cut,orig_sim_cut):
    # 用字典保存两篇文章中出现的所有词并编上号
    word_dict = dict()  # 生成字典，这个字典现在是空的，下面要对他进行配置，word_dict[word]是指word所对应的值

    i = 0
    for word in word_set:
        word_dict[word] = i
        i += 1
        # print(word_dict)

    # 根据词袋模型统计词在每篇文档中出现的次数，形成向量
    orig_cut_code = [0] * len(word_dict)

    for word in orig_cut:
        orig_cut_code[word_dict[word]] += 1

    # print("s1_cut_code:",s1_cut_code)
    orig_sim_cut_code = [0] * len(word_dict)
    for word in orig_sim_cut:
        orig_sim_cut_code[word_dict[word]] += 1
    return orig_cut_code,orig_sim_cut_code
#import sim_ans
def sim_ans(orig_cut_code,orig_sim_cut_code):
    #sum=0.0

    sum = 0
    side1= 0
    side2 = 0
    for i in range(len(orig_cut_code)):
        sum += orig_cut_code[i] * orig_sim_cut_code[i]
        side1 += pow(orig_cut_code[i], 2)
        side2+= pow(orig_sim_cut_code[i], 2)
    try:
        result = float(sum) / (math.sqrt(side1) * math.sqrt(side2))
    except ZeroDivisionError:
        result = 0.0
        print("这是一个空文本或者两个文本毫无相关，查重率为：",result)
    print("余弦相似度为：%.2f"%result)
    return result
def write_ans(result):
    ans_txt = open("./ans.txt", 'w', encoding="UTF-8")
    sim = str('%.2f' % result)
    ans_txt.write(sim)
    ans_txt.close()
if __name__=='__main__':
    doc1=open(sys.argv[1],'r',encoding="UTF-8")
    doc1_txt=doc1.read()
    doc1.close()
    doc2=open(sys.argv[2],'r',encoding="UTF-8")
    doc2_txt=doc2.read()
    doc2.close()
    word_set,doc1_cut,doc2_cut=tokenization(doc1_txt,doc2_txt)
    doc1_cut_code,doc2_cut_code=dictionary(word_set,doc1_cut,doc2_cut)
    sim=sim_ans(doc1_cut_code,doc2_cut_code)
    write_ans(sim)

