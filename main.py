from CMDApp import main_print
from GUIApp import GUIApp
import threading
import argparse

GAME = threading.Event()


def main() -> None:

    parser = argparse.ArgumentParser()
    parser.add_argument('--type', default="")
    parser.add_argument('-t', default="")
    args = parser.parse_args()
    print(f"type = {type(args.type)}\nt = {type(args.t)}")
    if args.type == "" and args.t == "":
        # use cli
        main_print(GAME)
    elif args.t.lower() == 'gui' or args.type.lower() == 'gui':
        #  use gui
        GUIApp()
    else:
        print("Sorry I don't understand :/")


if __name__ == "__main__":
    main()





