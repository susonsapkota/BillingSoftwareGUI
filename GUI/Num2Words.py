# list of suffix used while converting
ones_place = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ",
              "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]

twenties_place = ["", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]

thousands_place = ["", "Thousand ", "Million ", "Billion "]


# this handles number to word to 999
def num_upto_999(n):
    c = n % 10  # singles digit
    b = ((n % 100) - c) / 10  # tens digit
    a = ((n % 1000) - (b * 10) - c) / 100  # hundreds digit
    t = ""
    h = ""
    if a != 0 and b == 0 and c == 0:
        t = ones_place[int(a)] + "hundred "
    elif a != 0:
        t = ones_place[int(a)] + "hundred and "
    if b <= 1:
        h = ones_place[n % 100]
    elif b > 1:
        h = twenties_place[int(b)] + ones_place[c]
    st = t + h
    return st


# handles number greater than 3 digits incorporating them
def num_to_word(num):
    if num == 0: return 'Zero'

    i = 3
    n = str(num)
    word = ""
    k = 0
    while i == 3:
        nw = n[-i:]
        n = n[:-i]
        if int(nw) == 0:
            word = num_upto_999(int(nw)) + thousands_place[int(nw)] + word
        else:
            word = num_upto_999(int(nw)) + thousands_place[k] + word
        if n == '':
            i = i + 1
        k += 1
    return word[:-1]
