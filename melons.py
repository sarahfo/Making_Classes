"""This file should have our melon-type classes in it."""

class Melon(object):

    """Method for base price of Melons"""
    def get_base_price(self):
        ##get_base_price = 5      
       ##BASE_PRICE = get_base_price
       return 5
        ##return BASE_PRICE



class WatermelonOrder(Melon):   # is subclass of Melon
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        best_price = super(WatermelonOrder, self).get_base_price()    #look at parent class and use get_base_price method
        if self.species == "Watermelon":
            subtotal = best_price * qty   # calculate subtotal pre-discount
        if qty >= 3:                # discount condition 
            total = subtotal * .75  # add discount for bulk purchase
      
        return float(total)

class CantaloupeOrder(Melon):   # is subclass of Melon
    species = "Cantaloupe"
    color = "tan"
    imported = False 
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self,qty):
        """Calculate price of Cantaloupe given number of melons ordered."""
        best_price = super(CantaloupeOrder, self).get_base_price()    #look at parent class and use get_base_price method
        if self.species == "Cantaloupe":
            subtotal = best_price * qty  #subtotal before discount (if applicable)
        if qty >= 5:                # discount condition
            total = subtotal * .50  #calculates discount for bulk melon purchase

        return float(total)

class CasabaOrder(Melon):   # is subclass of Melon
    species = "Casaba"
    color = "tan" 
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty): 
        """Calculate price, given a number of melons ordered. """
        best_price = super(CasabaOrder, self).get_base_price()    #look at parent class and use get_base_price method
        if self.species == "Casaba":
            subtotal = ((best_price + 1)* qty)
        if self.imported == True:     # import condition for fees
            total = subtotal * 1.5   # add extra cost for import fees
    
        return float(total)

class SharlynOrder(Melon):   # is subclass of Melon
    species = "Sharlyn"
    color = 'tan'
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price given a number of melons ordered."""
        best_price = super(SharlynOrder, self).get_base_price()   #look at parent class and use get_base_price method
        if self.species == "Sharlyn":
            subtotal = best_price * qty
        if self.imported == True:     # import condition for fees
            total = subtotal * 1.5    # add extra cost for import fees
    
        return float(total)

class Santa_ClausOrder(Melon):  # is subclass of Melon

    species = "Santa_Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price given a number of melons ordered."""
        best_price = super(Santa_ClausOrder, self).get_base_price()  #look at parent class and use get_base_price method
        if self.species == "Santa_Claus":
            subtotal = best_price * qty
        if self.imported == True:    # import condition for fees
            total = subtotal * 1.5   # add extra cost for import fees
    
        return float(total)

class ChristmasOrder(Melon):   # Christmas is subclass of Melon
    species = "Christmas" 
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self,qty):
        """Calculate price given a number of melons ordered."""
        best_price = super(ChristmasOrder, self).get_base_price()    #look at parent class and use get_base_price method
        if self.species == "Christmas":
             total = best_price * qty
        
        return float(total)

class Horned_MelonOrder(Melon):   # Horned is subclass of Melon
    species = "Horned_Melon"
    color = "yellow" 
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty): 
        """Calculate price given a number of melons ordered"""
        best_price = super(Horned_MelonOrder, self).get_base_price()   #look at parent class and use get_base_price method
        if self.species == "Horned_Melon":
            subtotal = best_price * qty
        if self.imported == True:      # import condition for fees
            total = subtotal * 1.5     # add extra cost for import fees
    
        return float(total)



class XiguaOrder(Melon):   # Xigua is subclass of Melon
    species = "Xigua"       
    color = "black" 
    imported = True 
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty): 
        """Calculate price given a number of melons ordered"""
        best_price = super(XiguaOrder, self).get_base_price()
        if self.species == "Xigua":
            subtotal = ((best_price * qty) * 2)   # multiply by 2 for square melon cost
        if self.imported == True:     # import condition for fees
            total = subtotal * 1.5    # add extra cost for import fees
    
        return float(total)


class OgenOrder(Melon):     #Ogen is subclass of Melon
    species = "Ogen"
    color = "tan" 
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer'] 

    def get_price(self, qty):
        """Calculate price given a number of melons ordered.""" 
        best_price = super(OgenOrder, self).get_base_price()
        if self.species == "Ogen":
            total = ((best_price + 1)* qty)  # extra 1/per melon cost for exotic melon
    
        return float(total)


