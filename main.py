from prettytable import PrettyTable
def menu():
    print("Bill")
    choice = None
    while choice != 'q':
        print("1.Bill")
        choice = int(input(":"))
        if choice != 'q':
            data_table = PrettyTable(['Index','Name','Price'])

        else:
            break