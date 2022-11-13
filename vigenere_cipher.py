def vigenere(coded_text, keyword):

    decoded_text = ''
    counter = 0

    for letter in coded_text.lower():

        if ord(letter) > 122 or ord(letter) < 97:              # so only code that is a lower case letter is deciphered
            decoded_text += letter

        else:
            num = ord(letter) - ord(keyword[counter % len(keyword)])      # use modulus here so python continuously loops over keyword until it has looped through coded text

            if num < 0:
                num += 26

            unicode = num + 97                      # converts alphabet position back to unicode integer
            counter += 1

            decoded_text += chr(unicode)

    return decoded_text
