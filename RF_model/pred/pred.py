import numpy as np
import pandas as pd
import joblib
import csv
import codecs

save_path = r'E:\Python task\result.csv'

#引入预测文件
ds = pd.read_csv('bsln_pred_all.csv')
X = ds.iloc[:, [3,4,5,6,7,8,9,10]]

#调用训练结果，进行预测
classifier = joblib.load("save_model/0.7272727272727273.m")

#进行预测
predict_result = classifier.predict(X)

#遍历结果保存CSV中
for i, j in  enumerate(predict_result):
    #因为i是从0开始计数，所以+1
    temp_list = [i+1, j]
    #讲结果保存进新的CSV
    with codecs.open(save_path,'a', 'utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=temp_list)
        writer.writeheader()
print('[-]已经预测完成')

