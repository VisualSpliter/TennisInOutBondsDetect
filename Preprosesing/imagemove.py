#this programm is basically moving the image to the data/image folder
import os
import shutil
import csv
picture_height = 720
picture_width = 1280
w = 12/picture_width
h = 12/picture_height
game_folder = os.listdir("Dataset") #get folder name
print(game_folder)
for i in range(0,len(game_folder)):
    clip_folder = os.listdir("Dataset/"+game_folder[i]) #get clip folder name
    print(clip_folder)
    for j in range(0,len(clip_folder)):
        pictures = os.listdir("Dataset/"+game_folder[i]+"/"+clip_folder[j])
        csv_file = "Dataset/"+game_folder[i]+"/"+clip_folder[j]+"/Label.csv"
        with open(csv_file) as csvfile: #open csv file
            content = csv.reader(csvfile, delimiter=',')
            x_column = [row[2] for row in content] #get x column
        with open(csv_file) as csvfile:
            content = csv.reader(csvfile, delimiter=',')
            y_column = [row[3] for row in content] #get y column
        with open(csv_file) as csvfile:
            content = csv.reader(csvfile, delimiter=',')
            visiblility_column = [row[1] for row in content] #get visiblity column
        del(x_column[0]) #because the first line is the header
        del(y_column[0])
        del(visiblility_column[0])
        del(pictures[-1])
        # print(x_column)
        # print(y_column)
        # print(visiblility_column)
        for k in range(0,len(x_column)):
            if visiblility_column[k] == "1":
                shutil.copy("Dataset/"+game_folder[i]+"/"+clip_folder[j]+"/"+pictures[k], "data/image/"+game_folder[i]+"_"+clip_folder[j]+"_"+pictures[k])