from images_list import ImagesList
from coordinates_list import CoordinatesList

images = ImagesList()
coordinates = CoordinatesList()

images.load()
coordinates.load(sizes=images.size())
print(coordinates)
tagged = images.tag(coordinates_list=coordinates)
images.save(tagged)
