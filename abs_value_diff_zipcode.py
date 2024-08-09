STANFORD_ZIPCODE = "94305"

def main():
    addresses = [("115 Fifth Avenue", "New York", "NY", "10003"), ("9805 63rd Rd", "Rego Park", "NY", "11374"), ("1626 Shadybrook Dr", "Houston", "TX", "77094")]

    diff_zipcode = []
    for address in addresses:
        diff = int(get_zipcode(address)) - int(STANFORD_ZIPCODE)
        print(diff)
        diff_zipcode.append(diff)
    print(diff_zipcode)

    tuples_diff_zipcode = []
    for diff in diff_zipcode:
        value = abs(diff)
        tuple = value, (diff + int(STANFORD_ZIPCODE))
        tuples_diff_zipcode.append(tuple)
    print(tuples_diff_zipcode)
    tuples_diff_zipcode.sort()

    print(tuples_diff_zipcode)

    sorted_diff_zipcode = [t[1] for t in tuples_diff_zipcode]
    print(sorted_diff_zipcode)

    # sorted_addresses = sorted(addresses, key=get_zipcode)
    # print(sorted_addresses)

def get_zipcode(address):
    return address[3]










if __name__ == '__main__':
    main()