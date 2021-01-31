from PIL import Image
from ImageProcessor import combine

def run():
    img1 = Image.open('assets/receipt-1.jpg').rotate(-90)
    img2 = Image.open('assets/receipt-2.jpg').rotate(-90)

    result = combine.combine_y(img1,img2)

    result.save('assets/result.jpg')

    
if __name__ == '__main__':
    run()
