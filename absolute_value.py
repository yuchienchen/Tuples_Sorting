def main():
    nums = [3, 2, -1, 7, -7, 5, 14]

    abs_nums = []
    for elem in nums:
        value = abs(elem)
        value, elem = elem, value
        print(value, elem)
        abs_nums.append(elem)
        abs_nums.sort()
    
    print(abs_nums)
    
    




if __name__ == '__main__':
    main()