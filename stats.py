def get_num_words(text):
    return len(text.split())


def get_char_dict(text):
    chars = {}
    for ch in text:
        lowered = ch.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(char_info):
    return char_info["num"]


def chars_dict_to_sorted_list(chars_dict):
    sorted_chars = []
    for char, count in chars_dict.items():
        sorted_chars.append({"char": char, "num": count})
    sorted_chars.sort(key=sort_on, reverse=True)
    return sorted_chars
