import jieba
import math
#import cut
def tokenization(s1,s2):
    stopwords_position=open('stop_words','r',encoding="UTF-8")
    stopwords = stopwords_position.read()
    stopwords_position.close()
    s1_cut = []
    data1 = jieba.cut(s1)
    for i in data1:
        if (i not in stopwords) and i != '':
            s1_cut.append(i)
    s2_cut = []
    data2 = jieba.cut(s2)
    for j in data2:
        if (j not in stopwords) and j != '':  # 不是停词表中的可以加
            s2_cut.append(j)
    # print('s1_cut:',s1_cut)
    # print('s2_cut:',s2_cut)

    word_set = set(s1_cut).union(set(s2_cut))
    # print('word_set',word_set)#s1_cut是s1的分词表，s1_cut是s2的分词表，word_set是这两个表的集合，可以把这两个表中重合的删掉
    return word_set,s1_cut,s2_cut
#import dict
def dictionary(word_set,s1_cut,s2_cut):
    # 用字典保存两篇文章中出现的所有词并编上号
    #from cut import word_set, s1_cut, s2_cut

    word_dict = dict()  # 生成字典，这个字典现在是空的，下面要对他进行配置，word_dict[word]是指word所对应的值

    i = 0
    for word in word_set:
        word_dict[word] = i
        i += 1
        #
        # print(word_dict)

    ##dict['Age']返回Age所对应的值

    # 根据词袋模型统计词在每篇文档中出现的次数，形成向量
    s1_cut_code = [0] * len(word_dict)

    for word in s1_cut:
        s1_cut_code[word_dict[word]] += 1
    # print("s1_cut_code:",s1_cut_code)
    s2_cut_code = [0] * len(word_dict)
    for word in s2_cut:
        s2_cut_code[word_dict[word]] += 1
    return s1_cut_code,s2_cut_code
#import sim_ans
def sim_ans(s1_cut_code,s2_cut_code):
    #sum=0.0

    sum = 0
    sq1 = 0
    sq2 = 0
    for i in range(len(s1_cut_code)):
        sum += s1_cut_code[i] * s2_cut_code[i]
        sq1 += pow(s1_cut_code[i], 2)
        sq2 += pow(s2_cut_code[i], 2)
    try:
        result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 3)
    except ZeroDivisionError:
        result = 0.0
        print("这是一个空文本或者两个文本毫无相关，查重率为：",result)
    print("余弦相似度为：%.2f" % result)
    return result
def write_ans(result):
    ans_txt = open("./ans.txt", 'w', encoding="UTF-8")
    sim = str('%.2f' % result)
    ans_txt.write(sim)
    ans_txt.close()

def main_test(orig_position,orig_sim_position,ans_position):
    s1_position=open(orig_position,'r',encoding="UTF-8")
    s1= s1_position.read()
    s1_position.close()
    s2_position=open(orig_sim_position,'r',encoding="UTF-8")
    s2 = s2_position.read()
    s2_position.close()
    word_set, s1_cut, s2_cut = tokenization(s1, s2)
    s1_cut_code, s2_cut_code = dictionary(word_set, s1_cut, s2_cut)
    result = sim_ans(s1_cut_code, s2_cut_code)
    write_ans(result)
    '''
if __name__=='__main__':
    s1 = open("./data/1.txt", mode='r', encoding="UTF-8").read()
    s2 = open("./data/33.txt", mode='r', encoding="UTF-8").read()
    word_set,s1_cut,s2_cut=tokenization(s1,s2)
    s1_cut_code,s2_cut_code=dictionary(word_set,s1_cut,s2_cut)
    result=sim_ans(s1_cut_code,s2_cut_code)
    write_ans(result)
    '''


