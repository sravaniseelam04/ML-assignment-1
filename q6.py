string = "I am a teacher and I love to inspire and teach people"
words_string = string.split()
print(words_string)
unique_words = []
for word in words_string:
    if word not in unique_words:
        unique_words.append(word)
print(unique_words)