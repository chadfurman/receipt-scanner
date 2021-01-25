from PIL import Image
img1 = Image.open('./receipt-1.jpg')
img1.rotate(90)
img2 = Image.open('./receipt-2.jpg')
img2.rotate(90)

def combine(image1,image2):
    xsize1,ysize1=image1.size
    xsize2,ysize2=image2.size
    max_xsize = xsize1 if xsize1 > xsize2 else xsize2

    new_dimensions = (max_xsize,ysize1+ysize2)
    new_img = Image.new(image1.mode, new_dimensions)

    new_img.paste(image1, (0,0))
    new_img.paste(image2, (0,ysize1))
    return new_img

result = combine(img1,img2)
result.save('result.jpg')
    
