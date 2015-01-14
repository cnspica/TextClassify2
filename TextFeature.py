__author__ = 'LiNing'
#coding: utf-8


def TextBool(words_feature, text):
    bool_features = []
    words = set(text)
    for word_feature in words_feature: # 根据words_feature生成每个text的feature
        if word_feature in words:
            bool_features.append(1)
        else:
            bool_features.append(0)
    return bool_features


def ComputeTf(words_feature, text): # 每个text的tf
    tf_results = {}
    tf_features = []
    for word_feature in words_feature:
        word_count = text.count(word_feature)
        length = float(len(text))
        tf = word_count/length # 把一个数转为float型
        # tf_result[word_feature] = tf_result.get(word_feature, tf)
        tf_results[word_feature] = tf
        tf_features.append(tf)
    return tf_results, tf_features


def ExtractTags(words_feature, text, topK=10): # 每个text对应tags
    tf_results, tf_features = ComputeTf(words_feature, text)
    # key函数利用词频进行降序排序
    tf_list = sorted(tf_results.items(), key=lambda tf_result:tf_result[1], reverse=True) # 内建函数sorted参数需为list
    top_tuples = tf_list[:topK]
    tags = [top_tuple[0] for top_tuple in top_tuples]
    return tags