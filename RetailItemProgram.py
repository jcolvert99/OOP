import RetailItemClass as RI

def main():

    #create objects
    jacket = RI.RetailItem('Jacket',12,59.95)
    designer_jeans = RI.RetailItem('Designer Jeans',40,34.95)
    shirt = RI.RetailItem('Shirt',20,24.95)


    #display output
    print('Product description:',jacket.get_description())
    print('Units in inventory:',jacket.get_units_inventory())
    print('Price: $',jacket.get_price(),sep='')
    
    print()
    print('Product description:',designer_jeans.get_description())
    print('Units in inventory:',designer_jeans.get_units_inventory())
    print('Price: $',designer_jeans.get_price(),sep='')
    
    print()
    print('Product description:',shirt.get_description())
    print('Units in inventory:',shirt.get_units_inventory())
    print('Price: $',shirt.get_price(),sep='')

    print()

main()