import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True) # Reset Colour after every line

colorama.init() #Initialize

def col_info(msg):
    print(Fore.MAGENTA + msg)

def col_upload(method,path):
    print(Fore.GREEN + method+" ",end=" ")
    print(Fore.YELLOW + path)

def col_connect(msg):
    print(Fore.CYAN + msg)

def col_warning(msg):
    print(Fore.YELLOW + msg)

def col_error(msg):
    print(Fore.RED + msg)