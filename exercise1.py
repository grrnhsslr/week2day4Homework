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

book = {}

def book_entry():
    name = input('Enter a name ')
    address = input('Enter an Address ')
    # book = {name: address}
    book[name] = address


is_running = True

while is_running:
    prompt = input('type add to add an entry. type quit to quit ')
    if prompt == 'add':
        book_entry()
    elif prompt == 'quit':
        is_running = False
    else:
        print('invalid input')

print(book)
