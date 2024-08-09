def main():
    houses = [('main st.', 4, 4000), ('elm st.', 1, 1200), ('pine st.', 2, 1600)]

    sorted_count = sorted(houses, key=get_count)
    print(sorted_count)
    
    rev_sorted_price = sorted(houses, key=get_price, reverse=True)
    print(rev_sorted_price)

    sorted_price_per_room = sorted(houses, key=get_price_per_room)
    print(sorted_price_per_room)

def get_count(house):
    return house[1]

def get_price(house):
    return house[2]

def get_price_per_room(house):
    return house[2] / house[1]





if __name__ == '__main__':
    main()