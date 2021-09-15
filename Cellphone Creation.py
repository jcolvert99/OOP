import CellphoneClass as cc


def main():
    manufact = input('Enter phone manufacturer here: ')
    model = input('Enter phone model here: ')
    retail_price = input('Enter phone retail price here: ')

    phone = cc.Cellphone(manufact, model, retail_price)

    print('Here is the data you entered')
    print('Phone manufacturer:', phone.get_manufact())
    print('Phone model: ', phone.get_model())
    print('Retail price: ', phone.get_retail_price())


main()
