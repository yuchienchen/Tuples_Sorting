def main():
    info = [('Juliette Woodrow', 75000000, 'jwoodrow@stanford.edu', 2022, 243), ('Yuqian Chen', 82000000, 'yuqianchen@tamu.edu', 2012, 52), 
            ('Yongfei Gu', 10000000, 'ygu@cornell.edu', 2013, 105)]

    sorted_info = sorted(info, key=get_year)
    print(sorted_info)
    
    rev_sorted_info = sorted(info, key=get_year, reverse=True)
    print(rev_sorted_info)

def get_year(info):
    return info[3]





if __name__ == '__main__':
    main()