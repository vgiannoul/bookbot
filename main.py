# Config
file_path = "./books/frankenstein.txt"

def count_words(s):
    words = s.split()
    i = 0
    for word in words:
        i += 1
    return i

def count_char(s):
    string = s.lower()
    chars = {}
    for letter in string:
        if not letter in chars:
            chars[letter] = 1
        else:
            chars[letter] += 1
    return chars

def main():
    with open(file_path) as f:
        file_contents = f.read()
        # Count words 
        # print(count_words(file_contents))
        
        # Count characters
        chars_array = count_char(file_contents)
        # print(chars_array)
        
        # Print characters report
        print(f"--- Begin report of {file_path} ---")
        print(f"{count_words(file_contents)} words found in the document")
        # converting input dictionary items(key-value pair)
        # to a list of tuples
        result_list = list(chars_array.items())
        # Sort list by second item
        result_list.sort(key=lambda x: x[1],reverse=True)
        for item in result_list:
            if item[0].isalpha():
                print(f"The '{item[0]}' character was found {item[1]} times")
        print(f"--- End report ---")
main()
