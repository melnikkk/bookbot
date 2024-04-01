DEFAULT_PATH = "books/frankenstein.txt"

def count_words(content):
    words = content.split()

    return len(words)

def get_book_content(path):
    with open(path) as f:
        return f.read()
    
def count_letters(content):
    result = {}

    for letter in content:
        current_char = letter.lower()
        
        if current_char in result:
            result[current_char] += 1
        else:
            result[current_char] = 1
    
    return result

def log_report(counted_letters):
    sorted_letters_pairs = sorted(counted_letters.items(), key=lambda x:x[1])
    sorted_letters_dict = dict(sorted_letters_pairs)

    print(f"--- Begin report of  {DEFAULT_PATH} ---")

    for letter in sorted_letters_dict: 
        if letter.isalpha() or letter.isdigit():
            print(f"The '{letter}' character was found {sorted_letters_dict[letter]} times")

    print(f"--- End of report ---")

def main(path):
    content = get_book_content(path)
    letters_dict = count_letters(content)

    log_report(letters_dict)

main(DEFAULT_PATH)
