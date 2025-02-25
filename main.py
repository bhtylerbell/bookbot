def main(book_path):
    text = get_book_text(book_path) # Open and read the text for the input book
    num_words = get_num_words(text) # Get number of words found in the book not including whitespace
    characters = get_character_count(text) # Get count of indiviual letters not including special characters
    sorted_characters = sort_character_count(characters) # Sort characters alphabetically
    print(f"--- Begin Report on {book_path} ---")
    print(f"There are {num_words} words found in this document")
    print("")
    for key, value in sorted_characters.items():
        print(f"The letter '{key}' was found {value} times.")
    print("")
    print("--- End Report ---")
    
    
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
            
        
def get_num_words(book):
    word_count = book.split()
    return len(word_count)


def get_character_count(book):
    character = {}
    for i in book:
        if i.isalpha() == True:
            lower = i.lower()
            if lower not in character:
                character[lower] = 1
            else:
                character[lower] += 1
    return character

def sort_character_count(chacter_count):
    sorted_count = {key: chacter_count[key] for key in sorted(chacter_count)}
    return sorted_count
    
main("books/frankenstein.txt")