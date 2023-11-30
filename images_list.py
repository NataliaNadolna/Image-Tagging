import glob
import cv2
import os

class ImagesList(list):
    def __init__(self):
        super().__init__()

    def load(self):
        images_path = glob.glob('_Image Tagging/images/*.jpg')
        for file in images_path:
            img = cv2.imread(file)
            self.append(img)

    def size(self):
        sizes = []
        for img in self:
            size = int(img.shape[0])
            sizes.append(size)
        return sizes

    def copy_names(self):
        images_path = glob.glob('_Image Tagging/images/*.jpg')
        names = []
        for file in images_path:
            names.append(os.path.basename(file))
        return names

    def tag(self, coordinates_list: list):
        tagged_images = []
        for i, img in enumerate(self):
            img = cv2.rectangle(img, (coordinates_list[i].x1, coordinates_list[i].y1), 
                                     (coordinates_list[i].x2, coordinates_list[i].y2), (128, 128, 128), 5)
            cv2.imshow('frame', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            tagged_images.append(img)
        return tagged_images

    def save(self, images):
        names = self.copy_names()
        for i, img in enumerate(images):
            file_name = f"_Image Tagging/tagged/{names[i]}"
            cv2.imwrite(file_name, img)