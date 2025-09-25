def count_words(text):
    return len(text.split())

def count_characters(text):
    character_counts = {}
    for char in text:
        if char.isalpha():  # Count only alphabetic characters
            char = char.lower()
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1
    return character_counts

def sort_dict(this_dict):
    sorted_by_frequency = dict(sorted(this_dict.items(),reverse=True,key=lambda item:item[1]))
    return(sorted_by_frequency)