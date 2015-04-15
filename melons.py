"""This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        
        total = base_price * qty   # TODO, calculate the real amount!

        return total

class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False 
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self,qty):
        """Calculate price of Cantaloupe given number of melons ordered."""

        total = 0  # this is where we make the equation for calculating price

        return total

class Casaba(object):
    species = "Casaba"
    color = "tan" 
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty): 
        """Calculate price, given a number of melons ordered. """
        
        total = 0

        return total

class Sharlyn(object):
    species = "Sharlyn"
    color = 'tan'
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price given a number of melons ordered."""

        total = 0

        return total

class Santa_Claus(object):

    species = "Santa_Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price given a number of melons ordered."""

        total = 0

        return total

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

        total = 0

        return total



class Xigua(object):
    species = "Xigua"       
    color = "black" 
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty): 
        """Calculate price given a number of melons ordered"""

        total = 0

        return total


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


