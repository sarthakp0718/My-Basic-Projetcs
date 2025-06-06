def Translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "S"
            else:
                translation += "s"
        else:
            translation += letter  # Fixed spelling error

    return translation

# Calling the function correctly
print(Translator(input("Enter a phrase: ")))
