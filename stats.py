def words_in_book(book_text):
    return len(book_text.split())


def amount_per_character(book_text):
    char_dict = {}
    for char in book_text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_on(dict):
    return dict[1]


def sort_dict(char_dict):
    list_of_tuples = list(char_dict.items())
    list_of_tuples.sort(reverse=True, key=sort_on)
    return list_of_tuples
