import urllib.request, os, time, queue
from threading import Thread

reset = "\033[0m"
dark_red = "\u001b[38;2;153;0;0m"
underline = "\033[4m"
green = "\u001b[38;2;0;128;0m"
timeout = 10

def get_input(message, channel):
    response = input(message)
    channel.put(response)

def timeout_input(message, _timeout=timeout):
    channel = queue.Queue()
    thread = Thread(target=get_input, args=(message, channel))
    thread.daemon = True
    thread.start()

    try:
        response = channel.get(True, _timeout)
        return response
    except queue.Empty:
        pass
    return None

# Pretty much like auto `git pull`
def update(send_return=True):
  # All the files to be updated
  stuff_to_update = ["main.py", "update.py", "colors.py", "shop_ppe.json", "README.md", "shop_pps.json"]
  for item in stuff_to_update:
    new_data = ""
    update_data = ""
    # Getting github repo
    data = urllib.request.urlopen("https://raw.githubusercontent.com/Ravost99/press-enter-to-win/master/" + item)
    for line in data.readlines():
      # formatting the new file contents
      new_data += line.decode("utf-8")
    with open(item) as f:
      for line in f.readlines():
        update_data += line
      if new_data == update_data:
        if send_return == True:
          print(f"{green}No update in {item}!{reset}")
      else:
        update = timeout_input(f"There is a new update in {item}, would you like to update?\nYou have {timeout} seconds. (Will override {underline}everything{reset} in {item}) (Y/N) ")
        if update is not None and update.lower() == "y":
          with open(item, "w") as file:
            file.write(new_data)
          print(f"{green}Updated Successfully!{reset}")
        else:
          print(f"{dark_red}Cancled Update in {item}{reset}")
  print("Restarting...")
  time.sleep(0.3)
  os.system("clear")