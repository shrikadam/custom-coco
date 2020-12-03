import os
import numpy as np
import sys
import json
import random

f = open("datasets/output/coco_instances.json", 'r')
coco = json.load(f)

img = coco['images']
annot = coco['annotations']
width = coco['images'][0]['width']
height = coco['images'][0]['height']
seglist = open('datasets/output/Test.txt','w')
image_id = 0
for i in range(len(coco['annotations'])):
    a = annot[i]['image_id']
    b = annot[i]['category_id']
    c = annot[i]['bbox'][0] / width
    d = annot[i]['bbox'][1] / height
    e = annot[i]['bbox'][2] / width
    f = annot[i]['bbox'][3] / height
    print('{} {} {:.6f} {:.6f} {:.6f} {:.6f}'.format(a, b - 1, c, d, e, f), file = seglist)
seglist.close()

seglist = open('datasets/output/Test.txt', 'r')
lines = seglist.read().split('\n')
lines.pop()
j = 0
catbbox = open('datasets/output/labels/{:08d}.txt'.format(j),'w')
for line in lines:
    line = line.split(' ')
    if int(line[0]) == j:
        catbbox.write("{} {:.6f} {:.6f} {:.6f} {:.6f}".format(int(line[1]), float(line[2]), float(line[3]), float(line[4]), float(line[5])) + "\n")
    else:
        j = j+1
        catbbox = open('datasets/output/labels/{:08d}.txt'.format(j),'w')
        catbbox.write("{} {:.6f} {:.6f} {:.6f} {:.6f}".format(int(line[1]), float(line[2]), float(line[3]), float(line[4]), float(line[5])) + "\n")
catbbox.close()
seglist.close()
os.remove('datasets/output/Test.txt')

dirlist = open('datasets/output/Test1.txt', 'w')
for i in os.listdir('datasets/output/images'):
    print("data/trashcan_v0.2/images/{}".format(i), file=dirlist)
dirlist.close()

dirlist = open('datasets/output/Test1.txt', 'r')
lines = dirlist.read().split('\n')
lines.pop()
random.shuffle(lines)
trainfile = open('datasets/output/train.txt', 'w')
valfile = open('datasets/output/val.txt', 'w')
n_train = 80*len(lines)/100
n_val = len(lines) - n_train
for i in range(int(n_train)):
    lines[i]
    trainfile.write(lines[i] + '\n')
for j in range(int(n_val)):
    valfile.write(lines[int(n_train)+j] + '\n')
trainfile.close()
valfile.close()
dirlist.close()
os.remove('datasets/output/Test1.txt')

