#!/usr/bin/env python3

import os

test_file = open('./m0-train.txt', 'w')

for file in os.listdir("./0/po-test"):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        test_file.write("/home/phl48/Downloads/augment_image_yolo/env/augmented/m0-train/%s\n" % file)
