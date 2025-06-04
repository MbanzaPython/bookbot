def get_num_words(text):
    words = text.split()
    return len(words)

letters = {}

def get_num_characters(text):
    for char in text.lower():
        if char not in letters:
            letters[char] = 0
        letters[char] += 1
    return letters

def sort_on(dict):
    return dict[1]

def sorted_list_of_characters(characters, words, path):
    sorted_characters = []
    for character in characters:
        if not character.isalpha():
            None
        else:
            sorted_characters.append((character, characters[character]))
    sorted_characters.sort(reverse=True, key=sort_on)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}\n----------- Word Count ----------\nFound {words} total words\n--------- Character Count -------")
    for character in sorted_characters:
        print(f"{character[0]}: {character[1]}")
    print("============= END ===============")
    return None