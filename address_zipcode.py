def main():
    addresses = [("115 Fifth Avenue", "New York", "NY", "10003"), ("9805 63rd Rd", "Rego Park", "NY", "11374"), ("1626 Shadybrook Dr", "Houston", "TX", "77094")]
    print(sorted(addresses))

    print(sorted(addresses, reverse=True))

    sorted_addresses = sorted(addresses, key=get_zipcode)
    print(sorted_addresses)
    
    rev_sorted_addresses = sorted(addresses, key=get_zipcode, reverse=True)
    print(rev_sorted_addresses)

def get_zipcode(address):
    return address[3]










if __name__ == '__main__':
    main()