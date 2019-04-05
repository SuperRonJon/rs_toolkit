import commands
import osrs_net

print("Welcome to RS Toolkit\ntype 'exit' to quit, 'help' for a list of commands")

args = ""
prev_result = None
while args != "exit":
    args = input()
    if args != "exit":
        args = args.split()
        command = args.pop(0)
        if command == "div":
            if prev_result is not None:
                prev_result = commands.div(prev_result, args)
            else:
                print("Cannot divide after that command.")
        else:
            try:
                cur_result = getattr(commands, command)(args)
                if cur_result is not None:
                    prev_result = cur_result
            except AttributeError as e:
                print('No command {} found'.format(command))
