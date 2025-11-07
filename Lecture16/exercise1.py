#!/usr/bin/python

#With the aid of a function and a dictionary, write an interactive Python programme/script that will ask the user the following questions
##What's your name?
##How old are you?
##What is your favourite colour?
##Do you like Python?
##The world is flat: True or False?
#and then, based on their answers, make some comments back to them (this doesn't have to be at all serious, it's the methods used that we are trying out here....!)


def func():
    dictionary = {}

    name = input("What is ur name?")
    age = input("How old r u")
    colour = input("What's ur favourite colour?")
    like = input("Do u like python?")
    while True:
        flat = input("Is the world flat, true or false").lower()
        if flat in ["true", "false"]:
            break
        else:
            print("please give a valid response (true/false)")
    values_list = [age, colour, like, flat]
    value = ", ".join(values_list)
    dictionary[name] = value
    return dictionary

if __name__ == "__main__":
    result = func()
    print(result)

