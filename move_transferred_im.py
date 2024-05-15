from os import listdir
from os.path import isfile, join
import shutil

data_dir = "./data/coco-ir-pix2pix/"
train_dir = "train2017/"
val_dir = "val2017/"
test_dir = "test2017/"

wrong_path = "images/_latest/images/"
correct_path = "images/"

fake_im_train = listdir(data_dir+train_dir+wrong_path)
fake_im_val = listdir(data_dir+val_dir+wrong_path)
fake_im_test = listdir(data_dir+test_dir+wrong_path)

fake_im_train = [file for file in fake_im_train if "fake" in file]
fake_im_val = [file for file in fake_im_val if "fake" in file]
fake_im_test = [file for file in fake_im_test if "fake" in file]

print('train')
i=0
for file in fake_im_train:
    shutil.copy(data_dir+train_dir+wrong_path+file, data_dir+train_dir+correct_path+file[:12]+".png")
    if i%1000==0 :
        print('.', end='')
    i+=1
print()

print('val')
i=0
for file in fake_im_val:
    shutil.copy(data_dir+val_dir+wrong_path+file, data_dir+val_dir+correct_path+file[:12]+".png")
    if i%1000==0 :
        print('.', end='')
    i+=1
print()

print('test')
i=0
for file in fake_im_test:
    shutil.copy(data_dir+test_dir+wrong_path+file, data_dir+test_dir+correct_path+file[:12]+".png")
    if i%1000==0 :
        print('.', end='')
    i+=1
print()    