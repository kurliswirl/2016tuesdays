import random
dollars = 10
lemons = 0
sugar = 0         # in tablespoons
cups = 0
signs = 0 
cups_lemonade = 0

def print_stock():
  print ""
  print "You are running a lemonade stand! You have:"
  print "$%i" % dollars
  print "%i lemons" % lemons
  print "%i tablespoons of sugar" % sugar
  print "%i empty cups" % cups
  print "and as much water as you need."

# 2 lemons, 2 tablespoons sugar, 1 cup 
def make_cups_lemonade():
  global cups
  global lemons
  global sugar
  global cups_lemonade
  valid = False
  num_cups = 0
  while not valid:
    num_cups = int(raw_input("How many cups of lemonade do you want to make? "))
    valid = (num_cups >= 0)
    cups_needed = num_cups
    lemons_needed = num_cups * 2
    sugar_needed = num_cups * 2
    if cups_needed > cups:
      valid = False
      print "You don't have enough empty cups (you have %i and need %i)." % (cups, cups_needed)
    if sugar_needed > sugar:
      valid = False
      print "You don't have enough sugar (you have %i tablespoons and need %i)." % (sugar, sugar_needed)
    if lemons_needed > lemons:
      valid = False
      print "You don't have enough lemons (you have %i and need %i)." % (lemons, lemons_needed)
  sugar -= num_cups * 2
  lemons -= num_cups * 2
  cups -= num_cups
  cups_lemonade += num_cups
  print "You have %i cups of lemonade ready to sell." % cups_lemonade

def buy_things():
  global dollars
  global lemons
  global sugar
  global cups
  global signs
  global x
  while dollars > 0:
    print ""
    print "The store sells:"
    print "Lemons at $1 each"
    print "Sugar at $1 for 16 tablespoons"
    print "Cups at $1 for 10"
    print "You have $%i" % dollars
    amount_to_spend = int(raw_input("How much money do you want to spend right now? (0 to leave the store)"))
    if amount_to_spend <= 0:
      print "Have a nice day!"
      return
    while amount_to_spend > dollars:
      amount_to_spend = int(raw_input("You don't have that much, try again "))
    choice = raw_input("What do you want to buy with it? (lemons/sugar/cups/signs) ")
    if choice == "lemons":
      dollars -= amount_to_spend 
      lemons += amount_to_spend
      print_stock()
    elif choice == "sugar":
      dollars -= amount_to_spend 
      sugar += 16 * amount_to_spend
      print_stock()
    elif choice == "cups":
      dollars -= amount_to_spend
      cups += 10 * amount_to_spend
      print_stock()
    elif choice == "signs":
      dollars -= amount_to_spend
      signs += amount_to_spend/2
      signContent = raw_input("What do you want to put on your signs? ")
      for x in range (0, signs):
        spacing = len(signContent) + 2
        print("")
        print("|" + spacing * "-" + "|")
        print("|" + spacing * " " + "|")
        print("| " + signContent + " |")
        print("|" + spacing * " " + "|")
        print("|" + spacing * "-" + "|")
        spacing = (spacing + 2) / 2
        print(spacing * " " + "|")
        print(spacing * " " + "|")
        print(spacing * " " + "|")
      print_stock()
    else:
      print "Unrecognized choice, try again"
  print "Sorry, you're out of money"

def sell_cups_lemonade():
  global cups_lemonade
  global dollars
  price = int(raw_input("What's the price of lemonade today, in dollars? "))
  quantity_sold = random.randint(0, cups_lemonade)
  earnings = price * quantity_sold
  dollars += earnings
  print "You sold %i cups of lemonade and earned %i dollars." % (quantity_sold, earnings)
  if cups_lemonade > quantity_sold:
    print "Your siblings drink your %i leftover cups of lemonade." % (cups_lemonade - quantity_sold)
  cups_lemonade = 0

while True:
  print_stock()
  buy_things()
  make_cups_lemonade()
  sell_cups_lemonade()
  
