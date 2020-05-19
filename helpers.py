def display(message, is_warning=False):
    if is_warning:
        print('Wwarning!!')
    print(message)
    
    def error(something, is_critical=False):
        if is_warning:
            print('Critical!!')
        print(something)