# Owen Kroeger
# Lab Question 13


# receive inputs
plaintext = input("Enter text to decode: ")
code = int(input("Enter a code for caesar cypher: "))


# function to encode string based on caesar cypher
def encode(text, key):

    text = text.lower()

    encoded = []

    # for i in range length of input string
    for i in range(len(text)):

        # if special character, only add if a space
        if(ord(text[i]) < 97 or ord(text[i]) > 122):
            if(ord(text[i]) == 32):
                encoded.append(text[i])
            else:
                encoded.append('')

        # else, encrypt using key
        else:
            tempchar = (((ord(text[i]) - 97) + key) % 26) + 97
            tempchar = chr(tempchar)
            encoded.append(tempchar)

    # join char array into single string and print
    encoded = ''.join(str(x) for x in encoded)

    print("Encoded string...")
    print(encoded)



encode(plaintext, code)