def main():
    nums = [3, 2, -1, 7, -7, 5, 14]

    # 1. Create a list of tuples where each tuple contains the absolute value and the original value.
    # 2. Sort the list of tuples based on the first element (the absolute value)
    tuples_nums = []
    for elem in nums:
        value = abs(elem)
        tuple = value, elem
        print(tuple)
        tuples_nums.append(tuple)
    print(tuples_nums)
    tuples_nums.sort()
    
    print(tuples_nums)

    # Extract the sorted original values from the sorted list of tuples
    sorted_nums = [t[1] for t in tuples_nums]
    
    print(sorted_nums)
    
    

if __name__ == '__main__':
    main()