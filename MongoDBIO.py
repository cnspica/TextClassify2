__author__ = 'LiNing'
#coding: utf-8

import os
import pymongo


class MongoDBIO:
    # 申明相关的属性
    def __init__(self, host, port, name, password, database, collection):
        self.host = host
        self.port = port
        self.name = name
        self.password = password
        self.database = database
        self.collection = collection

    # 连接数据库，db和posts为数据库和集合的游标
    def Connection(self):
        # connection = pymongo.Connection() # 连接本地数据库
        connection = pymongo.Connection(host=self.host, port=self.port)
        # db = connection.datas
        db = connection[self.database]
        if self.name or self.password:
            db.authenticate(name=self.name, password=self.password) # 验证用户名密码
        print "Database:", db.name
        # posts = db.cn_live_news
        posts = db[self.collection]
        print "Collection:", posts.name
        return posts


# 查询操作
def TrainDataSelect(host, port, name, password, database, collection):
    posts = MongoDBIO(host, port, name, password, database, collection).Connection()
    print "Number of All Documents in the Collection:", posts.count() # 查询数量

    train_datas_targets = {"datas":[], "targets":[]}
    #-------------------------------------------------------------------------------
    # 以下几行根据实际情况修改
    for post in posts.find({}, {"_id":1, "content":1, "district":1, "type":1}):
        # print post
        if post.has_key("content") and len(post["content"])>1 and post.has_key("district") and post.has_key("type"):
            train_datas_targets["datas"].append(post["content"])
            Classify_Dimension = {"District":post["district"], "Type":post["type"]} ## 支持多维分类
            train_datas_targets["targets"].append(Classify_Dimension)
        else:
            print '{"_id":ObjectId("%s")}' % post["_id"] # MongoVUE中find命令
    #-------------------------------------------------------------------------------
    print "Number of Selected Documents in the Collection:", len(train_datas_targets["datas"]) # 选择数量
    return train_datas_targets


def TestDataSelect(host, port, name, password, database, collection, Limit_Number):
    posts = MongoDBIO(host, port, name, password, database, collection).Connection()
    print "Number of all Documents in the Collection:", posts.count() # 查询数量

    test_ids_datas = {"ids":[], "datas":[]}
    #-------------------------------------------------------------------------------
    # 以下几行根据实际情况修改
    for post in posts.find({"test_status":{"$ne":1}}, {"_id":1, "content":1}).limit(Limit_Number):
        # print post
        if post.has_key("content") and len(post["content"])>1:
            test_ids_datas["ids"].append(post["_id"])
            test_ids_datas["datas"].append(post["content"])
        else:
            print '{"_id":ObjectId("%s")}' % post["_id"] # MongoVUE中find命令
    #-------------------------------------------------------------------------------
    print "Number of Selected Documents in the Collection:", len(test_ids_datas["datas"]) # 选择数量
    return test_ids_datas


# 更新操作
def ResultUpdate(test_host, test_port, test_name, test_password, test_database, test_collection, test_ids_targets):
    posts = MongoDBIO(test_host, test_port, test_name, test_password, test_database, test_collection).Connection()
    test_ids = test_ids_targets["ids"]
    test_targets = test_ids_targets["targets"]

    for i in range(len(test_ids)):
        id = test_ids[i]
        test_target = test_targets[i]
        #-------------------------------------------------------------------------------
        # 以下几行根据实际情况修改
        posts.update({"_id":id}, {"$set":{"district_test":test_target["District"], "type_test":test_target["Type"], "test_status":1}}) ## 支持多维分类
        #-------------------------------------------------------------------------------
        print '{"_id":ObjectId("%s")}' % id # MongoVUE中find命令


# 保存操作
def ResultSave(save_host, save_port, save_name, save_password, save_database, save_collection, save_ids_targets):
    posts = MongoDBIO(save_host, save_port, save_name, save_password, save_database, save_collection).Connection()

    for save_id_target in save_ids_targets:
        posts.save(save_id_target)
