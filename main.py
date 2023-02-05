import colors, os, json, time, random
from threading import Thread

# Colors from colors.py
bold = colors.bold
reset = colors.none
blue = colors.blue
l_blue = colors.light_blue
gray = colors.gray
gold = "\u001b[38;2;199;180;36m"

# Scoring variables
seen_chance_shop = False
chance_msg = True
arrow = ""
enters = 0
ppe = 1
pps = 0
chance_enters = 1

# Loaded within this file, so I can change things for every run without overwritting the file
with open("shop_ppe.json") as f:
  ppe_data = json.load(f)
  # cost: round(math.pow(ppe, 3.6) + 15)

with open("shop_pps.json") as f:
  pps_data = json.load(f)
  # cost: round(math.pow(pps, 3.8) + 15)

# General functions
def help():
  print(f"Press {bold}b{reset} to view your balance.")
  print(f"Press {bold}s{reset} to view the shop.")
  print(f"Press {bold}c{reset} to clear the console.")
  print(f"Press {bold}h{reset} to get help on some commands.")

def balance():
  print(f"Your Balance: {bold}{l_blue}{str(enters)}{reset}")
  print(f"Your PPE: {bold}{l_blue}{str(ppe)}{reset}")
  print(f"Your PPS: {bold}{l_blue}{str(pps)}{reset}")
  print(f"Your Chance Enters: {bold}{l_blue}{str(chance_enters)}{reset}")

# Starting pps system
def start_pps():
  print() # Loading check
  def add_pps():
    global enters
    enters += pps
  while True:
    Thread(target=add_pps).start()
    time.sleep(1)

def pick_shop():
  if seen_chance_shop == False:
    shop = input(f"Which shop? ({bold}PPE/PPS/{gold}Chance{reset}) ")
  else:
    shop = input(f"Which shop? ({bold}PPE/PPS/Chance{reset}) ")
  if shop.lower() == "ppe":
    ppe_shop()
  elif shop.lower() == "pps":
    pps_shop()
  elif shop.lower() == "chance":
    chance_shop()
  else:
    pick_shop()

def error(type: str, arg=None):
  # Error messages
  # balance -> insufficient balance
  # cmd_not_found -> Command not found
  # not_num -> not an integer error
  errors = {"balance": f"You don't have enough enters!\nUse {blue}b{reset} for your balance.", "cmd_not_found": f"Command \"{arg}\" not found!\nUse {bold}h{reset} for commands.", "not_num": f"It doesn't look like \"{arg}\" is a valid response!"}
  try:
    return errors[type]
  except Exception as e:
    return f"An error occurred: {e}"

def ppe_shop():
  global enters, ppe, ppe_data

  # Printing all ppe items
  for item in reversed(list(ppe_data)):
    enter_item = ppe_data[item]
    if enter_item["name"] == "default":
      continue

    print(f"[: {bold}{enter_item['name']}{reset} :]")
    print(f"{gray}{enter_item['description']}{reset}")
    if enters > ppe_data[item]["cost"]:
      print(f"Buy {bold}{blue}now{reset} for {blue}{enter_item['cost']:,}{reset} enters and get {bold}{blue}{enter_item['ppe']}{reset}{bold} PPE{reset}\n")
    else:
      print(f"Buy for {blue}{enter_item['cost']:,}{reset} enters and get {bold}{blue}{enter_item['ppe']}{reset}{bold} PPE{reset}\n")
      
  pick = input(f"{reset}Current Balance: {bold}{l_blue}{enters}{reset}\nCurrent PPE: {bold}{l_blue}{ppe}{reset}\nWhat do you want to buy? ")
  if pick == "" or pick == " " or pick == None:
    print("Please enter a valid item!")

  for item in reversed(list(ppe_data)):
    if any(x in pick for x in ppe_data[item]["keywords"]): # Checking if the input is is any of the item's "keywords"
      if enters > ppe_data[item]["cost"]:
        enters -= ppe_data[item]["cost"]
        ppe += ppe_data[item]["ppe"]
        print(f"\nYou bought [: {bold}{ppe_data[item]['name']}{reset} :]")
        print(f"Your PPE: {bold}{l_blue}{ppe}{reset}\nCurrent Balance: {bold}{l_blue}{enters}{reset}")
      else:
        print(error("balance"))
      # New price for item bought (~0.2)
      ppe_data[item]["cost"] += round(ppe_data[item]["cost"]/5)
    

def pps_shop():
  global enters, pps, pps_data

  # Printing all pps items
  for item in reversed(list(pps_data)):
    enter_item = pps_data[item]
    if enter_item["name"] == "default":
      continue

    print(f"[: {bold}{enter_item['name']}{reset} :]")
    print(f"{gray}{enter_item['description']}{reset}")
    if enters > pps_data[item]["cost"]:
      print(f"Buy {bold}{blue}now{reset} for {blue}{enter_item['cost']:,}{reset} enters and get {bold}{blue}{enter_item['pps']}{reset}{bold} PPS{reset}\n")
    else:
      print(f"Buy for {blue}{enter_item['cost']:,}{reset} enters and get {bold}{blue}{enter_item['pps']}{reset}{bold} PPS{reset}\n")

  pick = input(f"{reset}Current Balance: {bold}{l_blue}{enters}{reset}\nCurrent PPS: {bold}{l_blue}{pps}{reset}\nWhat do you want to buy? ")
  if pick == "" or pick == " " or pick == None:
    print("Please enter a valid item!")

  for item in reversed(list(pps_data)):
    if any(x in pick for x in pps_data[item]["keywords"]): # Checking if the input is is any of the item's "keywords"
      if enters > pps_data[item]["cost"]:
        enters -= pps_data[item]["cost"]
        pps += pps_data[item]["pps"]
        print(f"\nYou bought [: {bold}{pps_data[item]['name']}{reset} :]")
        print(f"Your PPS: {bold}{l_blue}{pps}{reset}\nCurrent Balance: {bold}{l_blue}{enters}{reset}")
      else:
        print(error("balance"))
      # New price for item bought (~0.2)
      pps_data[item]["cost"] += round(pps_data[item]["cost"]/5)

def chance_shop():
  global seen_chance_shop, chance_enters, enters, chance_msg
  # disables the "Confused?" message
  seen_chance_shop = True
  
  chance_list = [1, 2, 5, 10, 25, 50, 100, 150, 300, 500, 1000, 2000, 5000, 10000] # Example chance prices, sorry no deals :(
  print("Buy chance enters to increase your lucky enters!\n")
  print(f"{bold}[HINT]{reset} Your chance enters are how many enters you get everytime you get a '{bold}{gold}LUCKY!!{reset}' message.{l_blue}**\n")
  for item in chance_list:
    print(f"{reset}Buy {blue}{item:,}{reset} chance enters for {blue}{item*100:,}{reset} enters")
  print(f"{reset}{bold}Buy {blue}x{reset}{bold} chance enters for {blue}x * 100{reset}{bold} enters{reset}")
  
  print(f"\n{l_blue}**{reset} Does not increase chance at getting lucky")
  pick = input(f"\nCurrent Balance: {l_blue}{enters}{reset}\nCurrent Chance Enters: {l_blue}{chance_enters}{reset}\n\nDisable of Enable lucky messages by entering \"{bold}disable{reset}\" or \"{bold}enable{reset}\" below.\nHow many chance enters do you want to buy (1-10,000)? ")
  # Disabling / Enabling "Lucky!!" messages
  if pick.lower() == "disable":
    chance_msg = False
    print(f"Lucky messages successfully {bold}disabled!{reset} (You still get lucky tho)")
  elif pick.lower() == "enable":
    chance_msg = True
    print(f"Lucky messages successfully {bold}enabled!{reset} Yay!")
  # Other checks (number check, >10000, balance...)
  elif pick.isnumeric() and int(pick) < 10000:
    pick = int(pick)
    if enters >= pick*100:
      chance_enters += pick
      enters -= pick*100
      print(f"You bought {bold}{blue}{pick}{reset} chance enters!")
      print(f"Your chance enters: {bold}{l_blue}{chance_enters}{reset}\nCurrent balance: {bold}{l_blue}{enters}{reset}")
    else:
      print(error("balance"))
  else:
    print(error("not_num", pick))
    print("You can only buy up to 10,000 chance enters at a time.")
    
# Starting messages
print(f"{reset}Welcome to press enter to win (in python)!\n")

print(f"{bold}{l_blue}Enters{reset} can be used to buy various things in the shop!")
print(f"Your {bold}PPE{reset} is how many {bold}{l_blue}enters{reset} you get each time you press enter.")
print(f"Your {bold}PPS{reset} is how many {bold}{l_blue}enters{reset} you get per second.")
help()

# Starting pps system
Thread(target=start_pps).start()

# Main game loop
while True:
  # PPS testing NOT WORKING!!! make it work :(
  before_pressed_time = time.time()
  
  enter = input(f"{bold}{arrow}{reset} ")
  
  enter_pressed_time = time.time()
  elapsed = round(enter_pressed_time-before_pressed_time, 1)
  #print(elapsed)
  if elapsed > 1:
    enters += 0#round(elapsed*pps)

  # Adding score and checking for commands
  if enter == "" or enter == " ":
    enters += ppe
    # lucky chance enters
    chance = random.randint(0, 20)
    if chance == 5:
      enters += chance_enters
      if chance_msg == True:
        print(f"{bold}{gold}LUCKY!!{reset} You got an extra {bold}{chance_enters}{reset} enters!")
      
        if seen_chance_shop == False:
          print(f"Confused? Open the chance shop using '{l_blue}s{reset}'")
  elif enter == "b":
    balance()
  elif enter == "s":
    pick_shop()
  elif enter == "c":
    os.system("clear")
  elif enter == "h":
    help()
  else:
    print(error("cmd_not_found", enter))

quit(blue+"\nThank you for playing!")