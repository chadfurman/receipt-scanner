from PIL import Image
from ImageProcessor import combine_y

img1 = Image.open('./receipt-1.jpg').rotate(-90)
img2 = Image.open('./receipt-2.jpg').rotate(-90)

result = combine_y(img1,img2)

result.save('result.jpg')
    
