#coding: utf-8
__author__ = 'LiNing'

import re
import nltk
import jieba
from os.path import exists


def TextSeg(datas, lag):
    dict_path = "./Config/dict"
    if lag == "chs" and exists(dict_path): # 中文情况
        jieba.set_dictionary(dict_path) # jieba分词词典，可以修改
    datasseg = []
    for data in datas:
        if lag == "eng": # 英文情况
            word_list = nltk.word_tokenize(data)
        elif lag == "chs": # 中文情况
            word_cut = jieba.cut(data, cut_all=False) # 精确模式，返回的结构是一个可迭代的genertor
            word_list = list(word_cut) # genertor转化为list，每个词unicode格式
        # print " ".join(word_list)
        datasseg.append(word_list)
    return datasseg


def MakeAllWordsList(train_datasseg):
    # 统计词频
    all_words = {}
    for train_dataseg in train_datasseg:
        for word in train_dataseg:
            if all_words.has_key(word):
                all_words[word] += 1
            else:
                all_words[word] = 1
    # 所有出现过的词数目
    # print "all_words length in all the train datas: ", len(all_words.keys())
    # key函数利用词频进行降序排序
    all_words_reverse = sorted(all_words.items(), key=lambda word_item:word_item[1], reverse=True) # 内建函数sorted参数需为list
    # for all_word_reverse in all_words_reverse:
    #     print all_word_reverse[0], "\t", all_word_reverse[1]
    all_words_list = [all_word_reverse[0] for all_word_reverse in all_words_reverse if len(all_word_reverse[0])>1]
    return all_words_list


def MakeStopWordsList(stopwords_file):
    fp = open(stopwords_file, 'r') # stopwords_file最后有一个空行，可以添加或删除单词
    stopwords = []
    for line in fp.readlines():
        stopword = line.strip().decode("utf-8") # 由utf-8编码转换为unicode编码
        if len(stopword)>0:
            stopwords.append(stopword)
    fp.close()
    # 去重
    stopwords_list = sorted(list(set(stopwords)))
    return stopwords_list


def MakeFeatureWordsDict(all_words_list, stopwords_list, dict_size, lag): # 特征词words_feature是选用的word-词典
    dict = open("./Config/fea_dict_"+lag, 'w')
    n = 1
    words_feature = []
    if lag == "eng": # 英文情况
        wordlen_min = 2
        wordlen_max = 15
        for all_words in all_words_list:
            if n > dict_size:
                break
            # if not all_words.isdigit(): # 不是数字
            # if re.match(ur'^[a-z A-Z -]+$', all_words) and not all_words == "\r\n": # 英文
            if re.match(ur'^[a-z A-Z -]+$', all_words) and not all_words == "\r\n" and not all_words in stopwords_list: # 英文
            # if re.match(ur'^[\u4e00-\u9fa5]+$', all_words) and not all_words == "\r\n": # 中文
            # if re.match(ur'^[\u4e00-\u9fa5]+$', all_words) and not all_words == "\r\n" and not all_words in stopwords_list: # 中文
                if (len(all_words)>wordlen_min) and (len(all_words)<wordlen_max): # unicode长度
                    dict.writelines(all_words.encode("utf-8")) # 将unicode转换为utf-8
                    dict.writelines("\n")
                    words_feature.append(all_words)
                    n += 1
    elif lag == "chs": # 中文情况
        wordlen_min = 1
        wordlen_max = 5
        for all_words in all_words_list:
            if n > dict_size:
                break
            # if not all_words.isdigit(): # 不是数字
            # if re.match(ur'^[a-z A-Z -]+$', all_words) and not all_words == "\r\n": # 英文
            # if re.match(ur'^[a-z A-Z -]+$', all_words) and not all_words == "\r\n" and not all_words in stopwords_list: # 英文
            # if re.match(ur'^[\u4e00-\u9fa5]+$', all_words) and not all_words == "\r\n": # 中文
            if re.match(ur'^[\u4e00-\u9fa5]+$', all_words) and not all_words == "\r\n" and not all_words in stopwords_list: # 中文
                if (len(all_words)>wordlen_min) and (len(all_words)<wordlen_max): # unicode长度
                    dict.writelines(all_words.encode("utf-8")) # 将unicode转换为utf-8
                    dict.writelines("\n")
                    words_feature.append(all_words)
                    n += 1
    dict.close()
    print "all_words length in words_feature: ", len(words_feature)
    return words_feature
