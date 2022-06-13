#!/usr/bin/env python3
# Created by: Paterry Baptichon
# Created on: 2022-06-09
# This program asks the user to enter a sentence. The program will then call a
# function that accepts the user's sentence as a string and returns a list
# of the words in the sentence. The words will then get displayed, one per
# line without any spaces.


def string_parcer(sentence):
    # split the sentence into multiple words
    list_of_words = sentence.split(" ")

    # return the list
    return list_of_words


def main():

    # declare the list
    list_of_words = []

    # greet the user
    print(
        "This program will ask the user for a sentence and then display each word, without spaces, one per line."
    )

    # get the user input
    sentence = input("Enter a sentence: ")

    # call the function
    list_of_words = string_parcer(sentence)

    # display the output to the user
    print("The words in your sentence, without spaces, are: ")
    print()

    for a_num in list_of_words:
        print(a_num)


if __name__ == "__main__":
    main()