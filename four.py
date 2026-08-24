def input_error(func): #Функція, яка приймє значення потрібної функції та передає його inner
    def inner(*args, **kwargs): #Функція, яка приймає будь-яке надане значення та перевіряє на помилки при виконанні заданої фукції з заданими значеннями
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "Enter the argument for the command"
        except IndexError:
            return "Enter the argument for the command"
    return inner



def parse_input(user_input):# Функція, яка обробляє те, що ввів користувач. Перше слово це команда, а далі список рядків
    try:     # Якщо користувач просто натисне ентер і нічого не введе запобігаємо ValueError
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except ValueError:
        return "Nothing was entered"

@input_error
def add_contact(args, contacts):  #Функція яка додає контакт. 
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def main():       #Основна функція, яка розпізнає команди та запускає функції
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
    
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
           
        elif command =="change":
           
            print(change_username_phone(contacts, args))
            
        elif command =="phone":
           
            print(phone_username(contacts, args))
           
        elif command=="all":
            print(all(contacts))


@input_error
def change_username_phone(contacts, args):  # Функція, яка змінює номер телефону
    name, new_phone = args
    if name in contacts:  #Якщо в списку args елемент 0(ім'я) є у контактах - змінюємо його номер на вказаний.
        contacts[name]=new_phone
        return "Contact changed"
    else:               #Якщо ім'я не було зайдено в словнику contacts - повертаємо, що ім'я не було знайдено
        return "Name is not defined"

@input_error
def phone_username(contacts, args):  #Функція, яка виводить номер телефону вказаного контакту
    name = args[0]
    return contacts[name]
    
@input_error
def all(contacts):  #Функція, яка просто виводить весь словнк contacts. Якщо контактів немає - словник буде пустий
    return contacts

if __name__ == "__main__":
    main()
