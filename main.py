import decorators


phone_book = {}


def hello_handler():
    return 'How can I help you?'


@decorators.add_error_decorator
def add_handler(*args):
    phone_book.update({args[0]: args[1]})
    return 'Telephone number has beem added'


@decorators.change_error_decorator
def change_handler(*args):
    phone_book[args[0]] = args[1]
    return 'Telephone number has beem changed'


@decorators.phone_error_decorator
def phone_handler(*args):
    return phone_book[args[0]]


def show_all_handler():
    title = 'Telephone Book\n'
    contacts = '\n'.join(f'{name} - {phone_number}' for name, phone_number in phone_book.items())
    f_contacts = 'Number does not  exist' if contacts == '' else contacts
    return title + f_contacts


def exit1_handler():
    return 'Good bye!'


def exit2_handler():
    return 'Good bye!'


def exit3_handler():
    return 'Good bye!'


commands = {
            hello_handler: 'hello',
            add_handler: 'add',
            change_handler: 'change',
            phone_handler: 'phone',
            show_all_handler: 'show all',
            exit1_handler: 'exit',
            exit2_handler: 'close',
            exit3_handler: 'good bye',
        }


def user_input_parser(user_input):
    arguments = []
    command = ""
    for k, v in commands.items():
        if user_input.startswith(v):
            command = k
            arguments = user_input.replace(v, "").split()
    return command, arguments


def main():
    while True:
        user_input = input('Command: ').lower()
        command, arguments = user_input_parser(user_input)
        print(command(*arguments))
        if command == exit1_handler or command == exit2_handler or command == exit3_handler:
            break


if __name__ == '__main__':
    main()