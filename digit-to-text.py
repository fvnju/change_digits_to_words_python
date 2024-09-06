from math import ceil

number = str(int(input("Give us a number that's an integer: ")))

def text_to_list(txt):
    lst = []
    for i in range(ceil(len(txt)/3)):
        to_cut = i * 3
        lst = [txt[::-1][to_cut:to_cut+3][::-1]] + lst
    return lst

number = text_to_list(number)

map_num_to_text = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

dict_of_tens = {
    "1": ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}

def is_text_null(txt):
    if txt is None or txt == "":
        return " "
    else:
        return " and " + txt

how_big = ["", "thousand", "million", "billion", "trillion"]

def handle_single_set(nm):
    text = ""
    for d in range(len(nm)):
        if nm == "0" and len(number) == 1:
            print("zero")
            break
        if d == 0:
            text = map_num_to_text.get(nm[-(d + 1)], "")
        if d == 1:
            if nm[-(d + 1)] != "1" and nm[-(d + 1)] != "0":
                text = dict_of_tens.get(nm[-(d + 1)]) + " " + text
            elif nm[-(d + 1)] == "1":
                text = dict_of_tens.get("1")[int(nm[-1])]
        if d == 2 and nm[0] != "0":
            text = map_num_to_text.get(nm[-(d + 1)], "") + " " + "hundred" + is_text_null(text)

    return text

def digits_to_words():
    def find_empty_string(tt, n):
        if tt != "":
            if n == 0 and len(number) > 1:
                return "and " + tt
            else:
                return tt + f" {how_big[n]} "
        else:
            return ""

    text = ""
    for i in range(len(number)):
        text = find_empty_string(handle_single_set(number[-(i+1)]), i) + text

    print(text)

digits_to_words()
