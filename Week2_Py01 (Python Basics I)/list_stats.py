# List statistics

def count_list(list):
    count = 0
    for element in list:
        count += 1
    print(list)
    print(f"Total count of elements: {count}")


numbers = [1, 5, 9, 7]
count_list(numbers)
