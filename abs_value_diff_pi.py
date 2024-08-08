pi = 3.14

def main():
    diff_pi = []
    nums = [3, 2, -1, 7, -7, 5, 14]
    for elem in nums:
        diff = elem - pi
        diff_pi.append(diff)
    print(diff_pi)  

    tuples_diff_pi = []
    for diff in diff_pi:
        value = abs(diff)
        tuple = value, (diff + pi)
        tuples_diff_pi.append(tuple)
    print(tuples_diff_pi)
    tuples_diff_pi.sort()

    print(tuples_diff_pi)

    sorted_diff_pi = [t[1] for t in tuples_diff_pi]
    print(sorted_diff_pi)

    

    # # 1. Create a list of tuples where each tuple contains the absolute value and the original value.
    # # 2. Sort the list of tuples based on the first element (the absolute value)
    # tuples_nums = []
    # for elem in nums:
    #     value = abs(elem)
    #     tuple = value, elem
    #     print(tuple)
    #     tuples_nums.append(tuple)
    # print(tuples_nums)
    # tuples_nums.sort()
    
    # print(tuples_nums)

    # # Extract the sorted original values from the sorted list of tuples
    # sorted_nums = [t[1] for t in tuples_nums]
    
    # print(sorted_nums)
    
    



if __name__ == '__main__':
    main()