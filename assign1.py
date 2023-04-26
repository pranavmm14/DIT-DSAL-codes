"""
ASSIGNMENT NO.1

Title:
Consider telephone book database of N clients. Make use of a hash table implementation to
quickly look up client's telephone number.

"""

# A class to represent a record of a contact


class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"


# A class to represent a hash table data structure

class HashTable:
    def __init__(self, size):
        self.size = size
        # Creating a list of size 'size' with None values
        self.table = [None] * size

    # A hash function that converts a key (name) to a hash value within the size of the hash table
    def hash_function(self, key):
        total = 0
        for i in range(len(key)):
            total += ord(key[i])
        return total % self.size

    # Method to insert a new contact in the hash table
    def insert(self, name, phone):
        # Find the index to insert the contact in the hash table
        key = self.hash_function(name)
        if self.table[key] is None:
            self.table[key] = [Record(name, phone)]
        else:
            self.table[key].append(Record(name, phone))

    # Method to search for a contact in the hash table
    def search(self, name):
        results = []
        for i in range(self.size):
            if self.table[i] is not None:
                for record in self.table[i]:
                    if record.name.startswith(name):
                        results.append(record.phone)
        return results if len(results) > 0 else None

    # Method to delete a contact from the hash table
    def delete(self, name):
        # Find the index where the contact to be deleted is present
        key = self.hash_function(name)
        if self.table[key] is not None:
            for i, record in enumerate(self.table[key]):
                if record.name == name:
                    # Remove the contact from the hash table
                    self.table[key].pop(i)
                    return

    # Method to display all the contacts in the hash table
    def display(self):
        for i in range(self.size):
            if self.table[i] is not None:
                for record in self.table[i]:
                    print(record)


# Main function to run the phone book program
def main(phone_book):

    # Continuously prompt the user to choose an operation until they choose to quit
    while True:
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. Display all contacts")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        # Add a new contact to the phone book
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            phone_book.insert(name, phone)
            print("Contact added successfully")

        # Search for a contact in the phone book
        elif choice == "2":
            name = input("Enter name to search: ")
            results = phone_book.search(name)
            if results is not None:
                print("Phone numbers found:")
                for result in results:
                    print(result)
            else:
                print("No matching records found")

        # Delete a contact from the phone book
        elif choice == "3":
            name = input("Enter name to delete: ")
            phone_book.delete(name)
            print("Contact deleted successfully")

        # Display all the contacts in the phone book
        elif choice == "4":
            phone_book.display()

        # Quit the program
        elif choice == "5":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    phone_book = HashTable(10)

    # Created Random Contacts
    phone_book.insert("Rashmi Desai", "5432109876")
    phone_book.insert("Sunita Gupta", "4321098765")
    phone_book.insert("Sachin Singh", "3210987654")
    phone_book.insert("Ankit Jain", "2109876543")
    phone_book.insert("Ankit Mishra", "1098765432")
    
    main(phone_book)        #Calling the main function
    
    print("Code by Pranav Mehendale")
