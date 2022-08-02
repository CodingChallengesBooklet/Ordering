
numbers = input("Please enter the numbers you wish to be sorted separated by a space: ").split()
numbers = [int(number) for number in numbers]

option = input("Would you like to sort your numbers into ascending or descending order?: ")
if option == "descending":
    descending_numbers = sorted(numbers, reverse=True)
    print(f"Sorted {numbers} into descending order: {descending_numbers}!")
elif option == "ascending":
    ascending_numbers = sorted(numbers)
    print(f"Sorted {numbers} into ascending order: {ascending_numbers}!")
else:
    print(f"\"option\" is not a valid option!")
