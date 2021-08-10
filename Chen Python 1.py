


def translation (word):
    translation_word = ""
    for letter in word:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation_word = translation_word + "G"
            else:
                translation_word = translation_word + "g"
        else:
            translation_word = translation_word + letter
    return translation_word

print (translation (input("Enter a word")))













































































