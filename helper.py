# helper.py 

from colorama import init, Fore

def display(message, is_warning=False):
    if is_warning:
        print(Fore.RED + message)
    else:
        
        print(Fore.BLUE + message)
    
    
# def display(critical, is_critical=False):
#     if is_critical:
#         print('Critical error!!')
#     print(critical)