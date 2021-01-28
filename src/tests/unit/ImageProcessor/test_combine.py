from PIL import Image
from ImageProcessor import combine

def test_combine_big_x():
    x1 = 100
    x2 = 50
    y1 = 50
    y2 = 50
    test_image_big_x = Image.new('RGBA',(x1,y1))
    test_image_small_x = Image.new('RGBA',(x2,y2))
    new_img = combine.combine_y(test_image_small_x, test_image_big_x)
    assert img.size[0] == x1 ## should be the bigger of the X
    assert img.size[1] == y1+y2
