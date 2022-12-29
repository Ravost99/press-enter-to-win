# Main colors
WHITE=white="\u001b[38;2;255;255;255m"
TAN=tan="\u001b[38;2;189;189;78m"
BROWN=brown="\u001b[38;2;139;69;19m"
CYAN=cyan="\u001b[38;2;0;255;255m"
GREEN=green="\u001b[38;2;0;128;0m"
ORANGE=orange="\u001b[38;2;255;128;0m"
BLUE=blue="\u001b[38;2;3;69;252m"
PINK=pink="\u001b[38;2;255;0;255m"
PURPLE=purple="\u001b[38;2;127;0;255m"
DARKCYAN=darkcyan="\u001b[38;2;0;204;204m"
YELLOW=yellow="\u001b[38;2;255;255;0m"
RED=red="\u001b[38;2;255;0;0m"
DARK_RED=dark_red="\u001b[38;2;153;0;0m"
BLACK=black="\u001b[38;2;0;0;0m"
MAGENTA=magenta="\u001b[38;2;255;0;255m"
LIME=lime="\u001b[38;2;0;255;0m"
GRAY=gray="\u001b[38;2;209;209;209m"
LIGHT_BLUE=light_blue="\u001b[38;2;132;155;173m"

# Background colors
bg_none='\x1b[0m'
bg_white="\u001b[48;2;255;255;255m"
bg_tan="\u001b[48;2;189;189;78m"
bg_brown="\u001b[48;2;139;69;19m"
bg_cyan="\u001b[48;2;0;255;255m"
bg_green="\u001b[48;2;0;128;0m"
bg_orange="\u001b[48;2;255;128;0m"
bg_blue="\u001b[48;2;0;0;255m"
bg_pink="\u001b[48;2;255;0;255m"
bg_purple="\u001b[48;2;127;0;255m"
bg_darkcyan="\u001b[48;2;0;204;204m"
bg_yellow="\u001b[48;2;255;255;0m"
bg_red="\u001b[48;2;255;0;0m"
bg_dark_red="\u001b[48;2;153;0;0m"
bg_black="\u001b[48;2;0;0;0m"
bg_magenta="\u001b[48;2;255;0;255m"
bg_lime="\u001b[48;2;0;255;0m"
bg_gray="\u001b[48;2;128;128;128m"

# Styles
BOLD=bold="\033[1m"
underline="\033[4m"
RESET=reset="\033[0m"
END=NONE=none=reset

# Misc color functions for generating colors
import random
def rand():
  all_colors = ["\u001b[38;2;255;0;0m", "\u001b[38;2;255;140;3m", "\u001b[38;2;255;255;0m", "\u001b[38;2;0;255;0m", "\u001b[38;2;0;0;255m", "\u001b[38;2;255;0;255m", "\u001b[38;2;255;255;255m"]
  return random.choice(all_colors)

def color(red: int, green: int, blue: int, text: str=""):
  return f"\u001b[38;2;{str(red)};{str(green)};{str(blue)}m{text}"