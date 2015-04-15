"""This file should have our melon-type classes in it."""
BASE_PRICE = 5

class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if self.species == "Watermelon":
            subtotal = BASE_PRICE * qty   # TODO, calculate the real amount!
        if qty >= 3: 
            total = subtotal * .75
        ##return subtotal
        return total

class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False 
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self,qty):
        """Calculate price of Cantaloupe given number of melons ordered."""
        if self.species == "Cantaloupe":
            subtotal = BASE_PRICE * qty
        if qty >= 5:
            total = subtotal * .50 # this is where we make the equation for calculating price

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
            subtotal = BASE_PRICE * qty
        if self.imported == True:
            total = subtotal * 1.5
    
        return float(total)

class Sharlyn(object):
    species = "Sharlyn"
    color = 'tan'
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price given a number of melons ordered."""
        if self.species == "Casaba":
            subtotal = BASE_PRICE * qty
        if self.imported == True:
            total = subtotal * 1.5
    
        return float(total)

class Santa_Claus(object):

    species = "Santa_Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price given a number of melons ordered."""
        if self.species == "Casaba":
            subtotal = BASE_PRICE * qty
        if self.imported == True:
            total = subtotal * 1.5
    
        return float(total)

class Christmas(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self,qty):

        """Calculate price given a number of melons ordered."""
        total = 0

        return total

class Horned_Melon(object):
    species = "Horned_Melon"
    color = "yellow" 
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty): 
        """Calculate price given a number of melons ordered"""
        
        if self.species == "Casaba":
            subtotal = BASE_PRICE * qty
        if self.imported == True:
            total = subtotal * 1.5
    
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
            subtotal = ((BASE_PRICE * qty) * 2)
        if self.imported == True:
            total = subtotal * 1.5
    
        return float(total)


class Ogen(object):
    species = "Ogen"
    color = "tan" 
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer'] 

    def get_price(self, qty):
        """Calculate price given a number of melons ordered.""" 

        total = 0 

        return total 


