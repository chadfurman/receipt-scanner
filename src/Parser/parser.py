import re

THRESHOLD = 200


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
    header_bottom = get_header_bottom(raw)
    return is_word_below_line(word, header_bottom, raw)


def is_word_below_line(word, line, raw):
    word_spots = get_word_top_right_bottom_left_from_raw_parts(word, raw)
    if word_spots['top'] > line:
        return True
    else:
        return False


def word_is_close_to_word(word1, word2):
    threshold = THRESHOLD
    parts1 = get_word_top_right_bottom_left_from_verteces(word1['vertices'])
    parts2 = get_word_top_right_bottom_left_from_verteces(word2['vertices'])
    top1 = parts1['top']
    bottom1 = parts1['bottom']
    top2 = parts2['top']
    bottom2 = parts2['bottom']

    if abs(top1 - top2) < threshold or abs(bottom1 - bottom2) < threshold:
        return True


def get_product_below_line(raw, line=None):
    product = None
    result_word = ''
    for text in raw:
        description = text['description']
        if not product:
            if not line:
                if is_word_below_header(text['description'], raw):
                    product = text
            else:
                if is_word_below_line(text['description'], line, raw):
                    product = text

        if product and word_is_close_to_word(text, product):
            result_word += ' ' + description
    if product :
        coords = get_word_top_right_bottom_left_from_verteces(product['vertices'])
        if coords:
            return (result_word, coords['bottom'] + THRESHOLD)
    return (None, None)

def get_raw_products_from_raw_text(raw):
    raw = raw['description'].replace('\n', ' ')
    products_extractor = re.compile('.*Clerk.*?([\d]{5,}.*)')
    matches = products_extractor.match(str(raw))
    return matches.group(1)

def get_product_line_from_products(products):
    product_matcher = re.compile('.*?([\d]{5,}.*?)([\d]{5,}.*)')
    match = product_matcher.match(products)
    if not match:
        return (None, None)
    return (match.group(1), match.group(2))

def get_all_products(raw):
    raw_products = get_raw_products_from_raw_text(raw)
    products = []

    (product, rest) = get_product_line_from_products(raw_products)
    products.append(product)
    while rest is not None:
        (product, rest) = get_product_line_from_products(rest)
        products.append(product)
    return products
