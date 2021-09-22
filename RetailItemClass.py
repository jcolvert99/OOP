class RetailItem:
    
    def __init__(self,des,inv,pri):
        self.__item_description = des
        self.__units_inventory = inv
        self.__price = pri

    
    def set_description(self,des):
        self.__item_description = des

    def set_units_of_inventory(self, inv):
        self.__units_inventory = inv

    def set_price(self,pri):
        self.__price = pri

    
    def get_description(self):
        return self.__item_description

    def get_units_inventory(self):
        return self.__units_inventory

    def get_price(self):
        return self.__price

    

