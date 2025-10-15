def get_book_text():
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

path_to_file = "/Users/shawn/Documents/bootdev/bookbot/books/frankenstein.txt"


def main():
    book_text = get_book_text()
    print(book_text)

main()

