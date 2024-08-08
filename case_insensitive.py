def main():
    lst = ['Mehran', 'juliette', 'KaTiE', 'CS106A', 'pYtHoN']

    tuples_lst = []
    for elem in lst:
        upper_case = elem.upper()
        print(upper_case)
        tuples = upper_case, elem
        print(tuples)
        tuples_lst.append(tuples)
    print(tuples_lst)







if __name__ == '__main__':
    main()
    