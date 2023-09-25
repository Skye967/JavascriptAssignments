class Store(object):
    def __init__(self, owner, location):
        self.owner = owner
        self.location = location
        self.products = []
        
    def addProduct(self, product):
        self.products.append(product)
        print("{} added {} to product list.".format(self.owner,product))
        return self.products
    
    def removeProduct(self, remove):
        indy = self.products.remove(remove)
        print("{} removed {} from product list.".format(self.owner,remove))
        
        
    
newStore = Store("Skye", "Maui")
newStore.addProduct("milk")
newStore.addProduct("eggs")
newStore.addProduct("bread")
newStore.addProduct("butter")
newStore.removeProduct("bread")