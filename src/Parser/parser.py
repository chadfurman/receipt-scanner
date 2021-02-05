def get_word_top_right_bottom_left_from_verteces(verteces):
    top = max(verteces[0][1], verteces[1][1])
    right = max(verteces[1][0], verteces[2][0])
    bottom = max(verteces[2][1], verteces[3][1])
    left = max(verteces[0][0], verteces[3][0])
    return {'top': top, 'right': right, 'bottom': bottom, 'left': left}


def get_word_top_right_bottom_left_from_raw_parts(word,raw):
    for text in raw:
            if word.lower() in text['description'].lower():
                    top = max(text['vertices'][0][1], text['vertices'][1][1])
                    right = max(text['vertices'][1][0], text['vertices'][2][0])
                    bottom = max(text['vertices'][2][1], text['vertices'][3][1])
                    left = max(text['vertices'][0][0], text['vertices'][3][0])
                    return {'top': top, 'right': right, 'bottom': bottom, 'left': left}
    return None


def get_header_bottom(raw):
    return get_word_top_right_bottom_left_from_raw_parts('terminal', raw)['bottom']

def get_receipt_left(raw):
    return get_word_top_right_bottom_left_from_raw_parts('clerk', raw)['left']


def get_receipt_right(raw):
    return get_word_top_right_bottom_left_from_raw_parts('terminal', raw)['right']


def is_word_below_header(word,raw):
    word_spots = get_word_top_right_bottom_left_from_raw_parts(word, raw)
    header_bottom = get_header_bottom(raw)
    if word_spots['top'] > header_bottom:
        return True
    else:
        return False


def word_is_close_to_word(word1, word2):
    threshold = 100
    parts1 = get_word_top_right_bottom_left_from_verteces(word1['vertices'])
    parts2 = get_word_top_right_bottom_left_from_verteces(word2['vertices'])
    top1 = parts1['top']
    bottom1 = parts1['bottom']
    top2 = parts2['top']
    bottom2 = parts2['bottom']

    if abs(top1 - top2) < threshold or abs(bottom1 - bottom2) < threshold:
        return True


def get_first_product(raw):
    product = None
    for text in raw:
        description = text['description']
        if not product and is_word_below_header(text['description'], raw) :
            product = text
        if product and word_is_close_to_word(text, product):
            print(description)
    return None
