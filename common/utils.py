import os
from config.config import DICTIONARY_PATH


def check_file_exists(method):
    print ("wrapping the method")
    def wrapper(*args):
        print ("am entering the decorator")
        if os.path.exists(DICTIONARY_PATH):
            method(*args)

        print ("am exiting the decorator")
    return wrapper

@check_file_exists
def example(a=1):
    print ("am in example",a)

if __name__ == "__main__":
    print("am in main")
    example()
