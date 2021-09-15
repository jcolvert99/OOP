class Cellphone:

    def __init__(self, manu, model, retail):
        self.__manufact = manu
        self.__model = model
        self.__retail_price = retail

    def set_manufact(self, manu):
        self.__manufact = manu

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, retail):
        self.__retail_price = retail

# only need self as an argument because .__manufact is an attribute of self
    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
