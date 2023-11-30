from coordinates import Coordinates
import glob

class CoordinatesList(list):
    def __init__(self):
        super().__init__()

    def load(self, sizes):
        coordinates_path = glob.glob('_Image Tagging/coordinates/*.txt')
        print(coordinates_path)
        for f in coordinates_path:
            file = open(f, "r")
            for i, line in enumerate(file.readlines()):
                new_line = line.strip()
                new_line = new_line.split(" ")
                cords = Coordinates(float(new_line[1]), float(new_line[2]), float(new_line[3]), float(new_line[4]), sizes[i])
                self.append(cords)
            file.close()

    def __str__(self):
        tmp = ""
        for i in range(len(self)):
            tmp += f"{self[i]}\n"
        return tmp