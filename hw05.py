"""
Name: Paw Poe
Peers: N/A
References: Homework 5 Instructions
"""

def get_letter():
    """ Asks user for a single uppercase letter with the valid options being A,B, and C.
    Can only be one of these three letters and can only be a single letter otherwise
    an error message will appear."""
    
        
    while True:
        letter = input("Give an single uppercase letter: ")
        
        if len(letter) != 1:
            print("Error: it needs to be a single character.")
            continue
        if letter not in("A", "B", "C"):
            print("Error: You provided the wrong character." )
            continue
        return letter

def get_digit():
    """ Asks user for a single digit number with the valid options being 1, 2, and 3.
    Can only be one of these three numbers if not an error will appear."""
    
    while True:
        digit = input("Give an single number character: ")
        
        if not digit.isdigit():
            print("Error: your input should be only digits.")
            continue
        if digit not in("1", "2", "3"):
            print("Error: a single digit needs to be in [1,3].")
            continue
        return digit


def check_pattern(letter, digit, lst):
    """Checks if any of the words inside the list contain the letter and number (in that order)
    and prints any that do contain them. """
    
    for word in lst:
        found = False
        
        for i in range(len(word)):
            if word[i] == letter:
                for j in range(i + 1, len(word)):
                    if word[j]== digit:
                        found = True

        
        if found:
            print(word, end=" ")
    
    print()


def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    while True:
        
        letter = get_letter()
        
        digit = get_digit()
        
        check_pattern(letter, digit, st_list)
        
        again = input("Try Again? (y/n): ")
        
        if again != "y":
            break
        
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------

    # Your code Here

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()