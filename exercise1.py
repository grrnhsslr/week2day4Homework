# Develop a user-friendly program that acts as an address book. The program should have the following functionalities:
# Upon starting the program, create an empty dictionary to store names and addresses.
# Allow the user to add people to the address book. For each entry, prompt the user to
# input a name and its corresponding address. Store these as key-value pairs in the dictionary.
# Provide a clear and straightforward menu for the user, including options to add a new entry or quit the program.
# Implement a loop that allows users to continue adding entries until they explicitly choose to quit.
# When the user decides to quit, break out of the loop and display the collected information.
# Print out the names and addresses of everyone in the address book in a well-formatted manner.
# Consider adding error handling to handle unexpected inputs gracefully.
# For instance, if the user provides invalid input
# when prompted for a name or address, handle the error and ask for the information again.
# Provide a user-friendly and informative message when the program terminates,
# summarizing the data entered and thanking the user for using the address book.

book = {}  # creates an empty dictionary to the addresses and names to be added to

def book_entry():
    name = input('Enter a name ')  # prompts the user to enter a name
    address = input('Enter an Address ')  # prompts the user to enter an address
    if name in book:  # if the name already exists in the dictionary
        print(f'{name} already exists')  # prints a line that says that the name is already inside the dictionary
    else:  # if the name does not exist
        # book = {name: address}
        book[name] = address  # if the name does not already exist in the dictionary it adds it


is_running = True  # boolean statement that keeps the code below running until they type quit

while is_running:  # loop that continues to run until they type quit
    print(book)  # prints the empty dictionary from above
    prompt = input('type add to add an entry. type quit to quit ')  # prompts the user
    if prompt == 'add':  # if they say add
        book_entry()  # calls the function from above
    elif prompt == 'quit':  # if they say quit in the prompt
        is_running = False  # shuts down the loop
    else:
        print('invalid input')

print(book)  # shows all available times that works for the whole team
