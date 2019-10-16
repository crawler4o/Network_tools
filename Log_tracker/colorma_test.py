from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text' + Style.RESET_ALL)
# print(Style.RESET_ALL)
print('back to normal now')