# Write your code here :-)
# utils.py
def url_decode(string):
    import binascii
    string = string.replace('+', ' ')  # Replace + with space
    parts = string.split('%')
    if len(parts) == 1:
        return string
    string = parts[0]
    for item in parts[1:]:
        try:
            string += chr(int(item[:2], 16)) + item[2:]
        except ValueError:
            string += '%' + item
    return string
