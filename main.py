import commands

print("Welcome to RS Toolkit\ntype 'exit' to quit, 'help' for a list of commands")

args = ""
prev_result = None
while args != "exit":
    cont = True
    args = input()
    if args != "exit":
        args = args.split()
        command = args.pop(0)
        for i, arg in enumerate(args):
            if arg == 'prev':
                if prev_result is not None:
                    args[i] = prev_result
                else:
                    print('No previous result to use')
                    cont = False
        try:
            cur_result = getattr(commands, command)(args)
            if cur_result is not None:
                prev_result = cur_result
        except AttributeError as e:
            print('No command {} found: {}'.format(command, e))
