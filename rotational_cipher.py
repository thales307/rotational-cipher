chars = "abcdefghijklmnopqrstuvwxyz"

def rotate(text, key):
    letters = chars[key:] + chars[:key]
    trans = str.maketrans(chars + chars.upper(), letters + letters.upper())
    return text.translate(trans)