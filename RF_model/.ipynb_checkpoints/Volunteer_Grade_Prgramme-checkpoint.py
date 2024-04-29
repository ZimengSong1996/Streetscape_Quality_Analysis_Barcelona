import os
import cv2        #anaconda的base环境中没有 需要单独安装
import csv
import codecs
import os

path = './image/'
fileName = 'Score.csv'

imagelist = os.listdir(path)

print("打分请输入0-6分之间的数字!")
for imgname in imagelist:   #遍历image文件夹下的图片
    if (imgname.endswith(".jpg")):
        image = cv2.imread(path + imgname)
        cv2.imshow(imgname, image)
        # k = cv2.waitKey(0)
        cv2.waitKey(15000)
        cv2.destroyWindow(imgname)
        score = input("输入分数:")  #手动输入分数

        if int(score) < 10:
            # 结果写入csv
            with codecs.open(fileName, 'a', 'utf-8') as csvfile:
                filednames = [imgname, score]
                writer = csv.DictWriter(csvfile, fieldnames=filednames)
                writer.writeheader()

            # 将打分结果分类存入文件夹
            #if not os.path.exists(pic_path + '/' + score):
                #os.makedirs(pic_path + '/' + score)
            #cv2.imwrite(pic_path + '/' + score + '/' + imgname, image)

        else:
            print("请重新打分输入0-6分之间的数字!")
            score = input("输入分数:")

            # 结果写入csv
            with codecs.open(fileName, 'a', 'utf-8') as csvfile:
                filednames = [imgname, score]
                writer = csv.DictWriter(csvfile, fieldnames=filednames)
                writer.writeheader()

            # 将打分结果分类存入文件夹
            if not os.path.exists(pic_path + '/' + score):
                os.makedirs(pic_path + '/' + score)
            cv2.imwrite(pic_path + '/' + score + '/' + imgname, image)

