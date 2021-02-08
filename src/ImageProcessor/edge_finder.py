from PIL import ImageFilter, ImageEnhance

def find_left_right_edge_on_horizontal_line(image):
    grayscale_image = image.convert("L")
    grayscale_image.save(r"assets/grayscale_result.png")
    #image = grayscale_image.filter(ImageFilter.FIND_EDGES)
    enhanced = increase_contrast(grayscale_image)
    enhanced.save(r'assets/grayscale_image_enhanced.png')
    edges = enhanced.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8, -1, -1, -1, -1), 1, 0))
    edges.save(r"assets/edge_sample.png")

def increase_contrast(image):
    # image brightness enhancer
    enhancer = ImageEnhance.Contrast(image)

    # factor = 1  # gives original image
    # im_output = enhancer.enhance(factor)
    # im_output.save('original-image.png')
    #
    # factor = 0.5  # decrease constrast
    # im_output = enhancer.enhance(factor)
    # im_output.save('less-contrast-image.png')

    factor = 10  # increase contrast
    return enhancer.enhance(factor)