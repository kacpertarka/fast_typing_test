import os
import random
import readchar
import threading
import time

FILE_PATH = "random.txt"
TIME: float = 0.0


def clear() -> None:
    """Function clear cmd screen"""
    if os.name == "nt":  # windows
        os.system("cls")
    else:  # linux ?
        os.system("clear")


def load_random_sentence(file: str) -> str:
    """Open file with sentences in each row and return one of them"""
    with open(file, "r") as f:
        sentences: list[str] = f.read().split("\n")[:-1]
        return random.choice(sentences)


def print_screen(to_guess: str, my_sent: str) -> None:
    """Function print sentence to write and what I have written"""
    print(to_guess)
    print(my_sent)
    if TIME != 0:
        characters_per_seconds = len(my_sent) / TIME
        characters_per_minute = characters_per_seconds * 60
        print(f"{characters_per_seconds:.2f}CPS \n{characters_per_minute:.2f}CPM")


def timer(game: threading.Event) -> None:
    """Count time in thread"""
    counter: float = 0.0
    global TIME
    while game.is_set():
        time.sleep(0.1)
        counter += 0.1
        TIME = counter


def time_start(game: threading.Event) -> None:
    """Start other thread?"""
    if not game.is_set():
        game.set()
        threading.Thread(target=timer, args=(game,)).start()


def main_print(game: threading.Event) -> None:
    """Print random text in loop and get one char from user. Next compare given char with sentence"""
    sentence: str = load_random_sentence(FILE_PATH)
    my_sentence: str = ""
    while True:
        clear()
        print_screen(sentence, my_sentence)
        my_sent_len = len(my_sentence)
        char = readchar.readchar()
        # after first or any next click any key game is start -> game = True
        time_start(game)
        if char == chr(27) or char == chr(8):  # keycode ESC = 27, BACKSPACE = 8
            game.clear()  # "wyzerowanie" zmiennej GAME: threading.Event()
            print("Thanks for game. See you later. :)")
            break
        if char == sentence[my_sent_len]:  # if given char is equal to sentence in the same position
            my_sentence = "".join([my_sentence, char])

        if my_sentence == sentence:
            clear()
            print_screen(sentence, my_sentence)
            game.clear()
            print("Congratulation!! You write gud!!")
            print(f"\nYour time was {TIME:.2f}sec")
            break
