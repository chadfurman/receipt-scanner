import os

from PIL import Image
from ImageProcessor import combine
from Google.Vision.detect import detect_text
from Parser import parser
import pickle

def run():
    img1 = Image.open('assets/receipt-1.jpg').rotate(-90)
    img2 = Image.open('assets/receipt-2.jpg').rotate(-90)

    result = combine.combine_y(img1,img2)

    result.save('assets/result.jpg')

    filepath = 'assets/raw_file_text'
    if (os.path.exists(filepath)):
        file = open(filepath, 'rb')
        raw_text = pickle.load(file)
        file.close()
    else:
        texts = list(detect_text('assets/result.jpg', return_text=True))
        raw_text = []
        for text in texts:
            vertices = []
            for vertex in text.bounding_poly.vertices:
                vertices.append([vertex.x, vertex.y])
            raw_text.append({
                'description': str(text.description),
                'vertices': vertices
            })
        file = open(filepath, 'wb')
        pickle.dump(raw_text, file)
        file.close()

    bottom_of_first_product = parser.get_product_below_line(raw_text[1:])
    print('----')
    bottom_of_second_product = parser.get_product_below_line(raw_text[1:], bottom_of_first_product)


if __name__ == '__main__':
    run()
