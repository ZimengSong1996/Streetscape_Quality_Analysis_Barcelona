import os
import cv2        #anaconda的base环境中没有 需要单独安装
import csv
import codecs
import os


path = 'RF_model/train/train_image/'
fileName = 'RF_model/train/Score.csv'

imagelist = os.listdir(path)

print("Please grade the street view between 0-6 (low-high quality)")
for imgname in imagelist:   #遍历image文件夹下的图片
    if (imgname.endswith(".jpg")):
        image = cv2.imread(path + imgname)
        cv2.imshow(imgname, image)
        # k = cv2.waitKey(0)
        cv2.waitKey(1000)
        score = input("{} Grade the View:".format(imgname.split('.')[0]))  # 手动输入分数
        cv2.destroyWindow(imgname)

        if int(score) <= 6:
            # 结果写入csv
            with codecs.open(fileName, 'a', 'utf-8') as csvfile:
                filednames = [imgname.split('.')[0], score]
                writer = csv.DictWriter(csvfile, fieldnames=filednames)
                writer.writeheader()

        else:
            print("Please grade the view between 0-6 and try again")
            score = input("{} Grade the View:".format(imgname.split('.')[0]))

            # 结果写入csv
            with codecs.open(fileName, 'a', 'utf-8') as csvfile:
                filednames = [imgname, score]
                writer = csv.DictWriter(csvfile, fieldnames=filednames)
                writer.writeheader()

            # 将打分结果分类存入文件夹
            if not os.path.exists(pic_path + '/' + score):
                os.makedirs(pic_path + '/' + score)
            cv2.imwrite(pic_path + '/' + score + '/' + imgname, image)

