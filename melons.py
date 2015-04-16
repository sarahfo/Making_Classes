"""This file should have our melon-type classes in it."""

class Melon(object):
    species = ["Watermelon", "Casaba", "Cantaloupe", "Christmas", 
    "Santa_Claus", "Sharlyn", "Xigua", "Ogen", "Horned_Melon"]
    color = ["green", "tan", "black", "yellow"]
    imported = [True, False]
    shape = ['natural', 'square']
    seasons = ['Winter', 'Spring', 'Summer', 'Fall']

    """docstring for Melon"""
    def get_base_price(self):
        get_base_price = 5      
        BASE_PRICE = get_base_price

        return BASE_PRICE



class WatermelonOrder(Melon):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if self.species == "Watermelon":
            subtotal = BASE_PRICE * qty   # calculate subtotal pre-discount
        if qty >= 3:                # discount condition 
            total = subtotal * .75  # add discount for bulk purchase
      
        return float(total)

class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False 
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self,qty):
        """Calculate price of Cantaloupe given number of melons ordered."""
        if self.species == "Cantaloupe":
            subtotal = BASE_PRICE * qty  #subtotal before discount (if applicable)
        if qty >= 5:                # discount condition
            total = subtotal * .50  #calculates discount for bulk melon purchase

        return float(total)

class Casaba(object):
    species = "Casaba"
    color = "tan" 
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty): 
        """Calculate price, given a number of melons ordered. """
        if self.species == "Casaba":
            subtotal = ((BASE_PRICE + 1)* qty)
        if self.imported == True:     # import condition for fees
            total = subtotal * 1.5   # add extra cost for import fees
    
        return float(total)

class Sharlyn(object):
    species = "Sharlyn"
    color = 'tan'
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price given a number of melons ordered."""
        if self.species == "Sharlyn":
            subtotal = BASE_PRICE * qty
        if self.imported == True:     # import condition for fees
            total = subtotal * 1.5    # add extra cost for import fees
    
        return float(total)

class Santa_Claus(object):

    species = "Santa_Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price given a number of melons ordered."""
        if self.species == "Santa_Claus":
            subtotal = BASE_PRICE * qty
        if self.imported == True:    # import condition for fees
            total = subtotal * 1.5   # add extra cost for import fees
    
        return float(total)

class Christmas(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self,qty):
        """Calculate price given a number of melons ordered."""
        if self.species == "Christmas":
             total = BASE_PRICE * qty
        
        return float(total)

class Horned_Melon(object):
    species = "Horned_Melon"
    color = "yellow" 
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty): 
        """Calculate price given a number of melons ordered"""
        if self.species == "Horned_Melon":
            subtotal = BASE_PRICE * qty
        if self.imported == True:      # import condition for fees
            total = subtotal * 1.5     # add extra cost for import fees
    
        return float(total)



class Xigua(object):
    species = "Xigua"       
    color = "black" 
    imported = True 
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty): 
        """Calculate price given a number of melons ordered"""
        if self.species == "Xigua":
            subtotal = ((BASE_PRICE * qty) * 2)   # multiply by 2 for square melon cost
        if self.imported == True:     # import condition for fees
            total = subtotal * 1.5    # add extra cost for import fees
    
        return float(total)


class Ogen(object):
    species = "Ogen"
    color = "tan" 
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer'] 

    def get_price(self, qty):
        """Calculate price given a number of melons ordered.""" 
        if self.species == "Ogen":
            total = ((BASE_PRICE + 1)* qty)  # extra 1/per melon cost for exotic melon
    
        return float(total)


