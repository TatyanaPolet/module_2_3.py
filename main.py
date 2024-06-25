my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5] # This is a sample Python script.
a = 0
while a < len(my_list):
    if my_list[a] < 0:
        break
    if my_list[a] > 0:
        print(my_list[a])
    a += 1


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
