import random
import shutil
import os
number_list = []
image_list = os.listdir("data/image")
for i in range(0,5289):
    random_number = random.randint(0,17631)
    number_list.append(random_number)
for k in range(0,5289):
    shutil.copy("data/image/"+image_list[number_list[k]], "data/valid/"+image_list[number_list[k]])
    os.remove("data/image/"+image_list[number_list[k]])
print(number_list)
