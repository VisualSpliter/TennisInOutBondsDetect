#this is a program converting prelabeled data to a format that can be used by the yolov5
#you should preinstall csv module
import csv
import os
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
                file_name = game_folder[i]+"_"+clip_folder[j]+"_"+pictures[k][0:4]+".txt"
                print(game_folder[i]+"_"+clip_folder[j]+"_"+pictures[k][0:4]+".txt")
                txt_file = open("data/label/"+file_name,"w")
                x = float(x_column[k])/picture_width
                y = float(y_column[k])/picture_height
                txt_file.write("0 "+str(x)+" "+str(y)+" "+str(w)+" "+str(h))
                txt_file.close()