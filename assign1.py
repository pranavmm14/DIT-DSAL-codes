class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def __str__(self):
        return f"{self.name}: {self.phone}"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        total = 0
        for i in range(len(key)):
            total += ord(key[i])
        return total % self.size
    
    def insert(self, name, phone):
        key = self.hash_function(name)
        if self.table[key] is None:
            self.table[key] = [Record(name, phone)]
        else:
            self.table[key].append(Record(name, phone))
    
    def search(self, name):
        results = []
        for i in range(self.size):
            if self.table[i] is not None:
                for record in self.table[i]:
                    if record.name.startswith(name):
                        results.append(record.phone)
        return results if len(results) > 0 else None
    
    def delete(self, name):
        key = self.hash_function(name)
        if self.table[key] is not None:
            for i, record in enumerate(self.table[key]):
                if record.name == name:
                    self.table[key].pop(i)
                    return
    
    def display(self):
        for i in range(self.size):
            if self.table[i] is not None:
                for record in self.table[i]:
                    print(record)

def main(phone_book):
    # phone_book = HashTable(10)  # create a hash table of size 10
    
    while True:
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. Display all contacts")
        print("5. Quit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            phone_book.insert(name, phone)
            print("Contact added successfully")
        elif choice == "2":
            name = input("Enter name to search: ")
            results = phone_book.search(name)
            if results is not None:
                print("Phone numbers found:")
                for result in results:
                    print(result)
            else:
                print("No matching records found")
        elif choice == "3":
            name = input("Enter name to delete: ")
            phone_book.delete(name)
            print("Contact deleted successfully")
        elif choice == "4":
            phone_book.display()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    phone_book=HashTable(10)
    phone_book.insert("Rashmi Desai", "5432109876")
    phone_book.insert("Sunita Gupta", "4321098765")
    phone_book.insert("Sachin Singh", "3210987654")
    phone_book.insert("Ankit Jain", "2109876543")
    phone_book.insert("Ankit Mishra", "1098765432")
    main(phone_book)
