
def main():
    print_header()
    run_event_loop()


def print_header():
    print('---------------------------')
    print('        Journal App')
    print('---------------------------')


def run_event_loop():
    print('What do you want to do with your Journal?')
    cmd = None
    journal_data = [] #list()

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
           list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("Sorry we don't understand '{}'.".format(cmd))

    print('Done, Goodbye.')


def list_entries(data):
    print('Your journal entries: ')
    for entry in data:
        print(entry)

def add_entry(data):
    text = input('Type your entry, <Enter> to exit')
    data.append(text)

main()