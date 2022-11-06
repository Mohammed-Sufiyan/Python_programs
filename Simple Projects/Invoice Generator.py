# This project is invoice generator, if you purchase anything in the shop this invoice will be the proof for it
# This project contains basic of python some variables, .format(), \t tab Sequence etc.

product1_name, product1_price = "Mechanical Keyboard", 750
product2_name, product2_price = "Dell wireless mouse", 354
product3_name, product3_price = "Pendrive 64GB", 106

company_name = "D4Rk-007.pvt.ltd."
company_address = "Backside, pakfoods, matfolds"
company_city = "Nottinggham, UK"

message = "Thanks for shopping with us today, Have a good Day..."
# Create a border for top of the sheet
print("=" * 50)

print("\t\t\t\t\t\t{}".format(company_name.title()))
print("\t\t\t\t\t\t{}".format(company_address.title()))
print("\t\t\t\t\t\t{}".format(company_city.title()))

print("=" * 50)

print("\tProduct Name\tProduct Price in Pounds")
print("1.\t{}\t{}".format(product1_name.title(), product1_price))
print("2.\t{}\t{}".format(product2_name.title(), product2_price))
print("3.\t{}\t\t{}".format(product3_name.title(), product3_price))
print("=" * 50)

Total = product1_price + product2_price + product3_price
print("\tTotal\t\t\t{}".format(Total))
Discount = Total*10/100
print("\tDiscount 9%\t\t{}".format(Discount))
print("\tTotal-Discount ", Total - Discount,"Only")
print("=" * 50)

print("\t\t{}".format(message))
print("=" * 50)
