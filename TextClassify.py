__author__ = 'LiNing'  
#coding: utf-8
import datetime


def Gne_Train_Dimensions(train_targets):
    dimensions = train_targets[0].keys()
    train_targets_names_dimensions = [] # 每个分类维度下的分类名称
    train_targets_dimensions = [] # 每个分类维度下的分类情况
    for dimension in dimensions:
        temp = [train_target[dimension] for train_target in train_targets]
        temp_list = sorted(list(set(temp)))
        train_targets_names_dimensions.append(temp_list)
        # 统计每个分类名称下的数目
        print "The Classify Dimension \"", dimension, "\":"
        for train_targets_names in temp_list:
            print train_targets_names, "\t", temp.count(train_targets_names)
        temp_num = [temp_list.index(temp_i) for temp_i in temp]
        train_targets_dimensions.append(temp_num)
    return train_targets_names_dimensions, train_targets_dimensions


def TextClassifier(fea_train, fea_test, train_targets_dimensions):
    results = []

    # ######################################################
    # date1 = datetime.datetime.now()
    # # Multinomial Naive Bayes Classifier (Gaussian Likelihood)
    # from sklearn.naive_bayes import MultinomialNB
    # nbcclf = MultinomialNB() # default with alpha = 1.0 # 分类器模型
    # nbcclf.fit(fea_train, train_targets_dimensions) # 分类器训练
    # pred = nbcclf.predict(fea_test) # 分类器识别
    # # print "*************************\nMultinomial Naive Bayes Classifier (Gaussian likelihood)\n*************************"
    # results.append(list(pred))
    ######################################################
    date2 = datetime.datetime.now()
    # Linear SVM Classifier (Linear kernel)
    from sklearn.svm import LinearSVC
    lsvclf = LinearSVC()
    lsvclf.fit(fea_train, train_targets_dimensions)
    pred = lsvclf.predict(fea_test)
    # print "*************************\nLinear SVM Classifier (Linear kernel)\n*************************"
    results.append(list(pred))
    # ######################################################
    # date3 = datetime.datetime.now()
    # # Decision Tree (Classification not Regression)
    # from sklearn.tree import DecisionTreeClassifier
    # dtclf = DecisionTreeClassifier() # default with criterion = "gini"
    # dtclf.fit(fea_train, train_targets_dimensions)
    # pred = dtclf.predict(fea_test)
    # # print "*************************\nDecision Tree (Classification not Regression)\n*************************"
    # results.append(list(pred))
    # ######################################################
    # date4 = datetime.datetime.now()
    # # Ensemble (Random Forests, Classification not Regression)
    # from sklearn.ensemble import RandomForestClassifier
    # rfclf = RandomForestClassifier() # default with n_estimators = 10
    # rfclf.fit(fea_train, train_targets_dimensions)
    # pred = rfclf.predict(fea_test)
    # # print "*************************\nEnsemble (Random Forests, Classification not Regression)\n*************************"
    # results.append(list(pred))
    # ######################################################
    # date5 = datetime.datetime.now()
    # print date2-date1, "\t", date3-date2, "\t", date4-date3, "\t", date5-date4

    return results


def Vote(votelist): 
    elements_list = sorted(list(set(votelist))) # 去重
    elements_dict = {}
    for element in elements_list:
        elements_dict[element] = votelist.count(element)
    # key函数利用词频进行降序排序
    elements_sortlist = sorted(elements_dict.items(), key=lambda elements_dict:elements_dict[1], reverse=True) # 内建函数sorted参数需为list
    return elements_sortlist[0][0]
