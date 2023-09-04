def count_words(book_str):
    words = book_str.split()
    count = len(words)
    return count

def count_letters(book_str):
    dict_result = {}
    for letter in book_str:
        letter = letter.lower()
        if letter not in dict_result:
            dict_result[letter] = 0
        dict_result[letter] += 1
    return dict_result

def convert_to_list(dict_result):
    list_of_tuples = list(dict_result.items()) 
    sorted_list_of_tuples = sorted(list_of_tuples)
    return sorted_list_of_tuples

def keep_alpha_chars(sorted_list_of_tuples):
    alpha_tuple_list = []
    for i in sorted_list_of_tuples:
        if i[0].isalpha():
            alpha_tuple_list.append(i)
    return alpha_tuple_list

def print_report(alpha_tuple_list, words):
    print("")
    print("--- Begin report of books/frankenstein.txt --")
    print(f"{words} words found in the document")
    print("")
    for i in alpha_tuple_list:
        print(f"The '{i[0]}' character was found {i[1]} times")
    print("--- End report ---")
    print("")

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()


words = count_words(file_contents)
dict_result = count_letters(file_contents)
sorted_list = convert_to_list(dict_result)
alpha_tuple_list = keep_alpha_chars(sorted_list)
print_report(alpha_tuple_list, words)

