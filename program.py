def main():
    print_header()
    run_event_loop()


def print_header():
    print('----------------------')
    print('     JOURNAL APP')
    print('----------------------')
    print()


def run_event_loop():

    print('What do you want to do with your journal?')
    cmd = None  # init variable
    journal = []

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()  # make lower case and rm spaces

        if cmd == 'l':
            print("L")
        elif cmd == 'a':
            print("A")
        elif cmd != 'x':
            print("Sorry, we don't understand '{}'.".format(cmd))

    print("Done, goodbye!")


def list_entries():
    print("Listing...")


def add_entry():
    print("adding...")


main()