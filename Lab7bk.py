# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: __________________
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: _________________________________________
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.
class Games:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_price(self, price):
        if price < 0:
            print("no")
        else:
            self.price = price

item1 = Games("Nfs most wanted", 50)
item1.set_price(-5)
if item1.price < 0:
    print("no")
else:
    print("save it")


class AddOns:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_price(self, price):
        if price < 0:
            print("no")
        else:
            self.price = price

item2 = AddOns("extra graphics", 60)
item2.set_price(-60)
if item2.price < 0:
    print("no")
else:
    print("save it")




    


# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT what happens: _it will print no_____________
#   Paste the message you see here: _no, save it_____________


# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.



# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: ______________


class games:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_price(self, price):
        if price < 0:
            print("no")
        else:
            self.price = price

    def action(self):
        print("Playing the game!")

class AddOns(games):  #inherit from the games class
    def action(self):
        print(f"Using the add-on: {self.name}")
    

item1 = games("Nfs most wanted", 50)
item2 = AddOns("extra graphics", 60)

item1.action()  # Output: Playing the game!
item2.action()  # Output: Using the add-on: extra graphics



class cars:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_price(self, price):
        if price < 500:
            print("no")
        else:
            self.price = price

item3 = cars("Scion TC", 1000)
item3.set_price(400)
if item3.price < 500:
    print("second hand")
else:
    print("first hand")



class colours:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_price(self, price):
        if price < 100:
            print("Affordable")
        else:
            self.price = price

item4 = colours("Blue", 200)
item4.set_price(80)
if item4.price < 100:
    print("Affordable")
else:
    print("Expensive")




# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
#   PREDICT what print(item1.name) shows: ______________



# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.



# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.


# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.



# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: ______________



# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.


# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================
