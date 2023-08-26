def count_word_frequency(text):
    words = text.lower().split()
    word_frequency = {}

    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    return word_frequency

text = input("Enter the text: ")
frequency = count_word_frequency(text)
for word, count in frequency.items():
    print(f"{word}: {count} times")
