def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_string_length(text)
    print(char_count)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_string_length(text):
    lower_text = text.lower()  # Convert the entire text to lowercase
    letter_string = 'abcdefghijklmnopqrstuvwxyz'
    char_count = {}  # Dictionary to store the count of each character

    for char in lower_text:
        if char in letter_string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    sorted_char_count = dict(sorted(char_count.items()))
    sorted_list = []
    for key, value in sorted_char_count.items():
        sorted_list.append(f"{key}: {value}")
        
    return sorted_list
    
main()
