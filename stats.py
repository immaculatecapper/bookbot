def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main(filepath):
    text = get_book_text(filepath)
    word_list = text.split()
    book_word_count = len(word_list)

    print(f"Found {book_word_count} total words")

def character_count(filepath):
    text = get_book_text(filepath)
    character_list = list(text)
    char_count_dict = {}

    for char in character_list:
        char = char.lower()
        if char.isalpha():
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1
    
    return char_count_dict

def dictionary_sort(x):
    dict_list = []

    for key, value in x.items():
        dict_list.append({key: value})
    
    sorted_list = sorted(dict_list, key=lambda d: list(d.values())[0], reverse=True)

    for kvp in sorted_list:
        first_key = list(kvp.keys())[0]
        first_value = kvp[first_key]
        
        print(f"{first_key}: {first_value}")

