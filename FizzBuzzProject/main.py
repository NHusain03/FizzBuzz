# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def fizzBuzzLogic(rules, max):

    for x in range (1, max+1):
        out_list = []

        if x % 3 == 0 and "3" in rules:
            out_list.append("Fizz")

        if x % 5 == 0 and "5" in rules:
            out_list.append("Buzz")

        if x % 7 == 0 and "7" in rules:
            out_list.append("Bang")

        if x % 11 == 0 and "11" in rules:
            out_list.clear()
            out_list.append("Bong")

        if x % 13 == 0 and "13" in rules:
            found = False

            for i in range(len(out_list)):
                if out_list[i][0] == "B":
                    out_list.insert(i, "Fezz")
                    found = True
                    break

            if not found:
                out_list.append("Fezz")


        if x % 17 == 0 and "17" in rules:
            out_list.reverse()

        if not out_list:
            out_list.append(str(x))

        out_string = ""
        for element in out_list:
            out_string += element

        print(out_string)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    max = int(input("Enter the maximum number for FizzBuzz: "))
    rule_nums = input("Enter the rules that you want to implement, each separated by a space: ")
    rules = rule_nums.split()

    fizzBuzzLogic(rules, max)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
