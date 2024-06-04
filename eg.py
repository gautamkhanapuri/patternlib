# -*- coding: utf-8 -*-

import argparse
import importlib
import inspect

pattern_lib_obj = importlib.import_module("patternlib")
pattern_list = [i for i in dir(pattern_lib_obj) if not i.startswith("__") and
                hasattr(getattr(pattern_lib_obj, i), '__call__')]
p = argparse.ArgumentParser(description="Helps to understand the working of patternlib")
p.add_argument("-l", "--list", help="Prints the entire list of patterns available in patternlib",
               action="store_true")
p.add_argument("-s", "--show", help="Displays the details of the pattern you have passed as argument")
p.add_argument("-r", "--run", help="Runs the argument you have passed with default parameters.")
p.add_argument("-p", "--param", help="Sets the size of the pattern")
args = p.parse_args()
if args.list:
    for pattern_name in pattern_list:
        print(pattern_name)
elif args.show:
    if args.show in pattern_list:
        pattern_function = getattr(pattern_lib_obj, args.show)
        print(pattern_function.__doc__)
        print('*' * 50)
        print("The parameters that can be passed to the function are:")
        print(inspect.signature(pattern_function))
    else:
        print(f"Error: Unknown pattern - '{args.show}'")
elif args.run:
    if args.run in pattern_list:
        pattern_function = getattr(pattern_lib_obj, args.run)
        if hasattr(pattern_function, '__call__'):
            if pattern_lib_obj.is_input_str(args.run):
                if args.param:
                    pattern_function(args.param)
                else:
                    pattern_function()
            else:
                try:
                    if args.param:
                        value = int(args.param)
                        pattern_function(value)
                    else:
                        pattern_function()
                except:
                    print("Incorrect input type for the pattern.")
                    pattern_function()

            print('*' * 50)
    else:
        print(f"Error: Cannot run unknown pattern - '{args.run}'")

else:
    for pattern_name in pattern_list:
        print(pattern_name)
