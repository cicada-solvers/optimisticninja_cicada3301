#!/usr/bin/env python3

# File must be run from root of repo
#
# $ ./scripts/2012.03-reddit-book-code.py
#
# This decodes the subreddit's post titles using a vignere cipher

file = open("2012/03.subreddit/reddit/txt/post_titles.txt", "r")
post_titles = file.read().upper()
vignere_key = [10, 2, 14, 7, 19, 6, 18, 12, 7, 8, 17, 0, 19, 7, 14, 18, 14, 19, 13, 0, 1, 2, 0] # the key
plaintext = ''
i = 0

for char in post_titles:
     # Reset key on New Line or wrap
    if i >= len(vignere_key) or ord(char) == 10:
        i = 0
    # if character is out of bounds, Num, punctuation etc... add it to the finalString and skip translation
    if char > 'Z' or char < 'A':
        plaintext += char
        continue
    # get the character in ASCII
    ascii_code = ord(char)
    #Shift it by the key
    new_char = ascii_code - vignere_key[i]
    #if it's too big subtract the number of letters in the alphabet (Wrap)
    if new_char > ord('Z'):
        new_char= new_char - 26
    #if it's too small add the number of letters in the alphabet (Wrap)
    if new_char < ord('A'):
        new_char= new_char + 26
    #Add the character to the finalString
    plaintext += chr(new_char)
    #next value in key
    i += 1

print(plaintext)
