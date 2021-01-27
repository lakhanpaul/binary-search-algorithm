# Binary Search

def binary_search(data, elem):
    low = 0
    high = len(data) - 1

    while low <= high:

        middle = (low + high) // 2

        if data[middle] == elem:
            print("Your desired element ", elem, "is at position ", middle)
            return middle
        elif data[middle] > elem:
            print("This position's values is too high, still searching...")
            high = middle - 1
        elif data[middle] < elem:
            print("This position's values is too low, still searching...")
            low = middle + 1
        else:
            print("Your desired element does not exist in this list of data")

    return -1


data_values = [1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    desired_element = int(input("Enter your desired element here: "))
    binary_search(data_values, desired_element)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
