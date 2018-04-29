print("first statement")

print(__name__)


# its not necessary to have the name of main method as main
# __name__ is the special variable that python sets when running the program to __main__.
def main():
    print("inside main function in python")


if __name__ == "__main__":
    main()

print("next statement")
