list1 = []
set1 = set()

print("to convert \n list to set(press 1) \n set to list(press 2)")
choice = input("enter your choice:")

match choice:
    case '1':

        while True:
            user_input = input("enter the elements in the list(enter 'done' when complete):")

            if user_input == 'done':
                break

            list1.append(user_input)

        print(f"the list is {list1}")
        print("The items in the list are:")

        for i, j in enumerate(list1):
            print(f"{i + 1}. {j}")

        set1.update(list1)

        print("\n\n")

        print(f"the converted set is {set1}")

    case '2':

        while True:
            user_input = input("enter items in set(enter 'done' when complete):")

            if user_input == 'done':
                break

            set1.add(user_input)

        print(f"the set is {set1}")

        for j in set1:
            list1.append(j)

        print("the converted list is ", list1)