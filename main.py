import sys
from stats import words_in_book, amount_per_character, sort_dict


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

        return file_contents


def main(path):
    # print(get_book_text("books/frankenstein.txt"))
    num_words = words_in_book(get_book_text(path))
    char_dict = amount_per_character(get_book_text(path))
    sorted_list = sort_dict(char_dict)

    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {path}...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {num_words} total words\n")
    print("--------- Character Count -------")
    for item, value in sorted_list:
        print(f"{item}: {value}")
    print("============= END ===============")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(sys.argv[1])
