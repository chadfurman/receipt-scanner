from PIL import Image
img = Image.open('./receipt-1.jpg')
print(img.format, img.size, img.mode)
