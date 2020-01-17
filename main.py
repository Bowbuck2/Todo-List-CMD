import datetime
import json


class ToDo:
    def __init__(self, message: str, complete: bool, lwidth: int, position: int):
        self.message = message
        self.bool = complete
        self.lwidth = lwidth
        self.position = position

    def __repr__(self):
        header = ('-' * self.lwidth + '-' * 27)
        date = datetime.datetime.now()
        return header + '\n' + f'{self.position} | {self.message.ljust(self.lwidth)} | {date.month}-{date.day}-{date.year} | {str(self.bool).ljust(5)} |'

    def __len__(self):
        return len(self.message)


ls = []

try:
    read = open("todo.json", "r")
    f = json.load(read)
    for item in f:
        ls.append(ToDo(item['message'], item['bool'], item['lwidth'], item['position']))
except IOError:
    print("No Database Found")


def viewToDo():
    lg_msg = len(max(ls, key=len))
    for obj in ls:
        obj.position = ls.index(obj)
        obj.lwidth = lg_msg
        print(f'''{obj}''')


def addToDo():
    ls.insert(0, ToDo(input('What is your new ToDo? '), False, 10, 0))
    menu()


def completeToDo():
    index = catchType('What Task got Completed? ', 'Please enter a digit in the list ')
    ls[index].bool = True
    ls.append(ls.pop(index))
    menu()


def removeToDo():
    ls.pop(catchType('What Task Do you want to Remove? ', 'Please enter a digit in the list '))
    menu()


def catchType(message, err_msg):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print(err_msg)
            pass


def saveToDo():
    print("Saving To File...")
    with open("todo.json", "w", encoding="utf-8") as f:
        temp = []
        for obj in ls:
            temp.append(obj.__dict__)

        json.dump(temp, f, ensure_ascii=False, indent=4)


def menu():
    print(
        '''
      TO DO LIST PROJECT
        1: Add ToDo
        2: Complete ToDo
        3: Remove ToDo
        4: Quit Program
        '''
    )
    if len(ls) != 0:
        viewToDo()
    selection = catchType('Selection: ', 'Please enter a digit in the menu ')
    if selection == 1:
        addToDo()
    elif selection == 2:
        completeToDo()
    elif selection == 3:
        removeToDo()
    else:
        saveToDo()


if __name__ == '__main__':
    menu()
