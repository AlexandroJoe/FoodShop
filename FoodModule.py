class FoodModule:
    # constructor takes parameters
    def __init__(self, name,amount):
        self.name = name
        self.amount=amount
        self.standardPrice=0
        #Update prices
        self.__PriceList()
        #Assign calculated price
        self.calculatedPrice=self.getCalculatedCost()
        
        
        
    # setter method
    def __PriceList(self):
        if self.name.lower()=='Dry Cured Iberian Ham'.lower():
            self.standardPrice=177.8
        elif self.name.lower()=='Wagyu Steaks'.lower():
            self.standardPrice=450.0
        elif self.name.lower()=='Matsutake Mushrooms'.lower():
            self.standardPrice=272
        elif self.name.lower()=='Kopi Luwak Coffee'.lower():
            self.standardPrice=317.5
        elif self.name.lower()=='Moose Cheese'.lower():
            self.standardPrice=487.2
        elif self.name.lower()=='White Truffles'.lower():
            self.standardPrice=3600.0
        elif self.name.lower()=='Blue Fin Tuna'.lower():
            self.standardPrice=3603.0
        elif self.name.lower()=='Le Bonnotte Potatoes'.lower():
            self.standardPrice=270.81
        else:
            self.standardPrice=0.0
            
    # setter method
    def getCalculatedCost(self):
        #self.calculatedPrice=(self.amount*self.standardPrice)
        return (self.amount*self.standardPrice)
        
    # getter method
    def get_Name(self):
        return self.name
    
    # getter method
    def get_Amount(self):
        return self.amount
    
    # Returns string
    def __str__(self):

        return "Item: % s\nAmount Ordered: %.1f pounds\nPrice per pound:$%.2f\nPrice of order: $%.2f" % (self.name, self.amount,self.standardPrice,self.calculatedPrice)