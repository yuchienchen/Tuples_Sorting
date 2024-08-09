def main():
    # create an empty list
    info = []
    with open('student_info.txt') as file:
        for line in file: 
            line = line.strip() 
            print(line)
            info.append(line)
        print(info)

        # create tuple from list 
        tuple_info = tuple(info)
        print(tuple_info)



if __name__ == '__main__':
    main()