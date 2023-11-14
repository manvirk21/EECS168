'''
Author: Manvir Kaur
KUID: 3064194
Date: 11/01/2021
Lab: lab08
Last modified: 11/08/2021
Purpose: Processing Romeo and Juliet
'''


def clean_word(word):
    word = word.lower()
    word = word.strip()
    word = word.replace(".","")
    word = word.replace(";","")
    word = word.replace("!","")
    word = word.replace("?","")
    word = word.replace(":","")
    word = word.replace(".","")
    word = word.replace("--","")
    word = word.replace(",","")
    return word

def build_count(text):
    count_dict = {}
    text = text.split()
    for word in text:
        word = clean_word(word)
        if word in count_dict.keys():
            count_dict[word] = count_dict[word] + 1
        else:
            count_dict[word] = 1
        return count_dict
    
#Below is what I thought I could use in order to make the format
#look neat and good however I got confused and it didn't work properly
#hence I am leaving it in but not letting it run.
#Can I get some points for effort and determination?

'''
def str_dict():
    input_file = open("source1.txt", "r")
    new_dict = build_count(input_file.read())
    for word, line in enumerate(newdict):
        for i in range(len(line)):
            line[i] = str(line[i])
        line_str = " "
        newdict[word] = line_str.join(line)
    dict_str = "\n"
    dict_str = dict_str.join(newdict)
    print(dict_str)
'''    

def unique_words(word_counts):
    unique = []
    for word, count in word_counts.items():
        if count == 1:
            unique.append(word)
    return unique

def main():
    word_data_file = open("word_data.txt", "w")
    unique_words_file = open("unique_words.txt", "w")
    message = "Welcome to the word counter!"
    print(message.center(20, '='))
    file = input("Enter a file name: ")
    input_file = open(file, "r")
    print(f"The file {file} has been processed.")
    
    new_dict = build_count(input_file.read())
    word_data_file.write(str(new_dict))

    new_list = unique_words(new_dict)
    unique_words_file.write(str(new_list))
    word_data_file.close()
    unique_words_file.close()
    print("Output stored in word_data.txt and unique_words.txt")
    print("Exiting...")
    
main()
    
