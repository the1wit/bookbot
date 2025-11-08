def get_num_words(text):
    num_words = 0
    book_in_words = text.split()
    num_words = len(book_in_words)
    return num_words


def get_num_characters(text):
    text_to_work = text.lower()
    counted_chars = dict()
    for char in text_to_work:
        if not char.isalpha():
            continue
        elif char not in counted_chars:
            counted_chars[char] = 1
        else:
            counted_chars[char] += 1
    return counted_chars


def sort_on(items):
    return items["num"]


def sort_data(counted_chars):
    counted_chars_list = []
    for char in counted_chars:
        counted_chars_list.append({"char": char, "num": counted_chars[char]})
    counted_chars_list.sort(key=sort_on, reverse=True)
    return counted_chars_list
