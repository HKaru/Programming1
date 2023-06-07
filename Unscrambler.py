def unscramble_word(scrambled_word, wordlist):
    for word in wordlist:
        word = word.strip().lower()
        if sorted(word) == sorted(scrambled_word):
            return word
    return None

with open("wordlist.txt", "r") as wordlist_file:
    wordlist = wordlist_file.read().splitlines()

print("CTRL+V kõikide sõnadega")
scrambled_words = []
num_words = 10 
for i in range(num_words):
    scrambled_word = input(f"Sõna #{i+1}: ")
    scrambled_words.append(scrambled_word)

original_words = []
for scrambled_word in scrambled_words:
    unscrambled_word = unscramble_word(scrambled_word, wordlist)
    original_words.append(unscrambled_word if unscrambled_word else "Ei leia")

output = ', '.join(original_words)

print("Algsed sõnad:")
print(output)
