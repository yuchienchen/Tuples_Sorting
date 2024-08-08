def main():
    lst = ['Mehran', 'juliette', 'KaTiE', 'CS106A', 'pYtHoN']

    # 1. Create a list of tuples where each tuple contains all uppercase and the original strings.
    # 2. Sort the list of tuples based on the first element (uppercase)
    tuples_lst = []
    for elem in lst:
        lower_case = elem.lower()
        # print(lower_case)
        tuples = lower_case, elem
        print(tuples)
        tuples_lst.append(tuples)
    print(tuples_lst)
    tuples_lst.sort()

    print(tuples_lst)
    
    # Extract the sorted original strings from the sorted list of tuples
    sorted_lst = [t[1] for t in tuples_lst]

    print(sorted_lst)






if __name__ == '__main__':
    main()
    