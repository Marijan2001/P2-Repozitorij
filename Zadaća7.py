from zadaća6.py import reverse(string)

def reverse(string):
    if not string:
        return string

    first, *rest = string.split(maxsplit=1)

    if not rest:
        return first

    return reverse(*rest) + ' ' + first

print(reverse("Programski jezik Python"))
