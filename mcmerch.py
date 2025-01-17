import argparse
def main():
    # configure first cli arg to be the price of the time
    parser = argparse.ArgumentParser()
    parser.add_argument("price", type=float, help="The price of the item")
    parser.add_argument("--province", type=str, default="Ontario", choices=["Ontario", "Quebec"], help="The province where the tax is applied (default: Ontario)")
    args = parser.parse_args()

    # add tax to the price
    if args.province == "Ontario":
        tax_rate = 1.13
    elif args.province == "Quebec":
        tax_rate = 1.14975
    
    total = args.price * tax_rate
    
    print(f"The total price is {total:.2f}")

if __name__ == '__main__':
    main()