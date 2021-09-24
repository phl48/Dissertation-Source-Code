import random
import cv2
import os
import albumentations as A
from yolo_format import images_annotations_yolo_info, write_yolo
from augment_methods import getTransform

if __name__ == "__main__":
    category_id_to_name = {0: "frisbee", 1: "kite", 2: "baseball glove"}
    # image_path = "test/test.jpg"
    # label_path = "test/test.txt"
    path = "/home/phl48/Downloads/augment_image_yolo/env/augmented/po-train/"
    all_file = os.listdir(path)
    all_image_path = []
    count = 0

    for file_name in all_file:
        if file_name[-3:] == 'jpg':
            all_image_path.append(path + file_name)
    for file_path in all_image_path:
        image_name = file_path[file_path.rfind('/') + 1:file_path.rfind('.jpg')]
        image_path = file_path
        label_path = file_path.replace('jpg', 'txt')
        image_original = cv2.imread(image_path)
        category_ids, bboxes = images_annotations_yolo_info(label_path=label_path)
        print(bboxes)
        method_index = 0

        transform_save = getTransform(method_index, img_height=image_original.shape[0],
                                      img_width=image_original.shape[1])
        try:
            transformed_save = transform_save(image=image_original, bboxes=bboxes, category_ids=category_ids)
            print(transformed_save['bboxes'])
            if not os.path.exists("./augmented/" + str(method_index) + "/"):
                os.makedirs("./augmented/" + str(method_index) + "/")
            write_yolo(name="./augmented/" + str(method_index) + "/" + image_name,
                       method_index=str(method_index),
                       coords=transformed_save['bboxes'],
                       category=transformed_save['category_ids'],
                       image=transformed_save['image'])
            print(image_path)
        except:
            count += 1
            print("fail image path is: " + image_path)
    print(count)

