"""
Module 2 — Lesson 3: Loops & Lists
Student: [your name]
Date: [date]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]


============================================
KEY VOCABULARY
============================================
- list: variables holder
- for loop: repeat code for each items in collection
- while loop: run the condition while the statement is true 
- index: the position of the item starting from 0 
- iteration: indefinite(while loop) and finite(for loop)
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
while True:
    pick = input("Choose 1 to continue and 0 to stop: ")
    if pick == "1": 
        names = ["Renz", "Christian", "Ethan"]
        for i in names:
            print(i)
    elif pick == "0":
        break
    else:
        print("Invalid input!")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]
a mistake to avoid is the identation of the functions like "if" inside while loop and "for" inside the if process


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
