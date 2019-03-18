import commands

print("Welcome to RS Toolkit\ntype 'exit' to quit, 'help' for a list of commands")

args = ""
while args != "exit":
    args = input()
    if args != "exit":
        args = args.split()
        command = args.pop(0)
        try:
            getattr(commands, command)(args)
        except AttributeError as e:
            print(e)
