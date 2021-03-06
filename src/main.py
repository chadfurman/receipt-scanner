import os

from PIL import Image
from ImageProcessor import combine, edge_finder
from Google.Vision.detect import detect_text
from Parser import parser
import pickle

def run():
    img1 = Image.open('assets/receipt-1.jpg').rotate(-90)
    img2 = Image.open('assets/receipt-2.jpg').rotate(-90)

    result = combine.combine_y(img1,img2)
#    edge_finder.find_left_right_edge_on_horizontal_line(result)

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

    products = parser.get_all_products(raw_text[0])
    for product in products:
        print(str(product))


if __name__ == '__main__':
    run()
