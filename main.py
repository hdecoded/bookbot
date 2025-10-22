from stats import get_num_words, get_char_dict, chars_dict_to_sorted_list
def get_book_text(file_name):
    with open(file_name) as f:
        return f.read()

def main():

    print("============ BOOKBOT ============")
    book_path = "books/frankenstein.txt"
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    chars_dict = get_char_dict(text)
    sorted_chars = chars_dict_to_sorted_list(chars_dict)
    for char_info in sorted_chars:
        char = char_info["char"]
        if not char.isalpha():
            continue
        print(f"{char}: {char_info['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
