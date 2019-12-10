lowest_char = 'a'
rang = range(ord('z') - ord(lowest_char) + 2)


def get_ord(char):
    if (char == '\n'):
        return ord('z') - ord(lowest_char) + 1
    return ord(char) - ord(lowest_char)


def get_char(ord1):
    if (ord1 == 26):
        return ''
    return chr(ord1 + ord(lowest_char))
