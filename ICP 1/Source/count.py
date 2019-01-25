def main():
    sentence = input("Enter a sentence:")

    wordCount = len(sentence.split())

    dig = letter = 0
    for c in sentence:
        if c.isdigit():
            dig = dig + 1
        elif c.isalpha():
            letter = letter + 1
        else:
            pass
    print("Letters", letter)
    print("Digits", dig)
    print("words: %s"% wordCount)

main()