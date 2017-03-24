def rotate_character(char,rot):
    shift = 97 if char.islower() else 65
    return chr((ord(char) + rot -shift) % 26 + shift)


def encrypt(text,rot):
    encrypted = ""
    for char in text:
        if char.isalpha() == False:
            encrypted = encrypted + char
        else:
            encrypted = encrypted + rotate_character(char,rot)
    return encrypted
