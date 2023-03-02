from colorama import Fore, Back, Style


# print(inspect.isclass(colorama.ansi.AnsiFore))
print("AnsiFore() class is used to change color of text:")
print(Fore.RED + "Exam" + Fore.BLUE + "ple")
print(Style.RESET_ALL)

# print(inspect.isclass(colorama.ansi.AnsiBack))
print("AnsiBack() class is used to change background color:")
print(Back.WHITE + "Example")
print(Style.RESET_ALL)

# print(inspect.isclass(colorama.ansi.AnsiStyle))
print("AnsiStyle() class can reset Fore and Back values to default")



