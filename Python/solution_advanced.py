
word = input("Please enter a word or string of characters: ")
keep_sentence_structure = input("Do you want to keep sentence structure? [Y/n]: ").lower()
sorted_word = ""

if keep_sentence_structure == "y" or keep_sentence_structure == "yes":
    words = word.split(" ")
    letters = [[letter for letter in word] for word in words]
    letters = [sorted(word) for word in letters]
    sorted_word = ' '.join(''.join(word) for word in letters)
else:
    letters = [letter for letter in word]
    sorted_word = ''.join(sorted(letters))

print(f"Sorted \"{word}\" alphabetically to \"{sorted_word}\"")