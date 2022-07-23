'''
   Jazib's Implementation of the Insertion Sort Algorithm

   Author: Jazib Ahmed
   Email: jazib7537@gmail.com

   All my algorithms are done by looking at diagrams, no code is looked up.
'''
# Unsorted list example
unsorted = [769, 873, 932, 422, 908, 296, 786, 431, 442, 336, 806, 205, 265, 202, 525, 302, 670, 177, 254, 760, 824, 930, 423, 254, 867, 565, 763, 415, 657, 869, 399, 752, 665, 648, 952, 887, 783, 421, 928, 685, 937, 835, 191, 138, 151, 819, 329, 501, 562, 264, 50, 311, 795, 964, 516, 770, 939, 26, 804, 349, 493, 460, 329, 168, 555, 50, 749, 107, 751, 604, 784, 312, 412, 558, 346, 441, 774, 887, 367, 798, 386, 64, 485, 494, 606, 524, 477, 133, 913, 793, 926, 23, 179, 172, 397, 800, 343, 34, 597, 862]

def insertion_sort(list1):
    """
    This function takes a list and uses the insertion sort algorithm to sort it.
    """

    # If statement to avoid errors with a list with 0 or 1 elements.
    if len(list1) < 2:
        return list1

    sorting = list1.copy()

    # For loop to go through each index of the list
    for i in range(1,len(sorting)):

        # Assigning a variable to the current element being compared in the list.
        comparison = sorting[i]
        index1,j = 0,0

        # If statement to compare the current element with the one before it.
        if comparison < sorting[i-1]:

            # While loop that looks through the previous elements and finds the
            # index for the current variable to be sorted into
            while j <= i:
                if comparison < sorting[j]:
                    index1 = j
                    j = i+1
                j+=1

            # Removing the variable from its current place and inserting it into
            # the index determined from the loop above
            del sorting[i]
            sorting.insert(index1,comparison)

    return sorting


# Calling the insertion_sort function to sort the unsorted list and print it
sorted = insertion_sort(unsorted)
print(sorted)