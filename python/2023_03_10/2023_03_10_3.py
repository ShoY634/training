class Product:
    def __init__(self, name:str, price:int, stock:int):
        self._name = name
        self._price = price
        self._stock = stock
        
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    @property
    def stock(self):
        return self._stock
    
    @classmethod    
    def create_product(cls, name:str, price:int, stock:int):
        return cls(name, price, stock)
    
    def update_product_name(self, new_name):
        print(f'{self._name}を{new_name}に更新しました')
        self._name = new_name
    
    def update_product_price(self, new_price):
        print(f'{self._price}を{new_price}に更新しました')
        self._price = new_price
        
    def update_product_stock(self, new_stock):
        print(f'{self._stock}を{new_stock}に更新しました')
        self._stock = new_stock
    
mouse = Product.create_product('Mouse', '10000', '30')
mouse.update_product_name("Mouse_G703")
print(mouse.name)
