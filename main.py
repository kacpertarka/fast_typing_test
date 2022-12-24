from CMDApp import main_print
from GUIApp import GUIApp
import threading

GAME = threading.Event()


def main() -> None:

    # uzycie GUI
    # GUIApp()
    # przyszlosciowe uzycie cmd
    main_print(GAME)


if __name__ == "__main__":
    main()





