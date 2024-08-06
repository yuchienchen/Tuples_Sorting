def main():
    nums = [3, 2, -1, 7, -7, 5, 14]

    abs_nums = []
    for elem in nums:
        if elem < 0:
            abs(elem) == - elem
        else:
            abs(elem) == elem
        print(abs(elem))
        abs_nums.append(abs(elem))
    print(abs_nums)
    abs_nums.sort()
    print(abs_nums)
    




if __name__ == '__main__':
    main()