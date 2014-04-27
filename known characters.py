# Known Characters.py

class DbElem:
    def __init__(self, trad = None, simple = None, index = -1):
        self.traditional = trad
        self.simple = simple
        self.index = index

# find the given character c in the database db. If found, returns the index of
# the first match found. Else returns None
def findChar(c, db):
    if c in db:
        return db[c].index

def initDb(file):
    '''
        Input:
            A file object to initialize the database with
            The file should be follow this format:

                Trad Char[,Simpl Char]

        Initializes the database using the given file object
    '''
    pos = 1
    str = ''
    file.seek(0)
    for line in file:
        str = line[:len(line)-1]

        if not str or str.isspace():
            continue

        c_list = str.split(',')
        key = c_list[0]
        simple = None
        if len(c_list) > 1:
            simple = c_list[1]
    
        if key in charDb:
            print("Warning: duplicate character %s found at %d and %d\n" %
                  (str, charDb[key].index, pos))
        else:
            value = DbElem(trad = key, index = pos, simple = simple)
            charDb[key] = value
        pos += 1

# -----------------------------------------------------------

file = open('db.txt', 'a+', -1, 'utf-8')

# a database with traditional character as keys and DbElem objects as values
charDb = {}

# TODO: newCharDb should really be a hashtable with characters as keys
newCharDb = []

initDb(file)

quit = False
while not quit:
    userInput = input("> ")

    if not userInput:
        continue # ignore empty inputs

    args = userInput.split(' ')
    cmd = args[0]

    if len(args) > 1:
        character = args[1]
        
    if cmd == 'help':
        print(\
            '''Known Characters Help
        add <character>       add the given character to the database
        search <character>    search for the given character in the database
        help                  Display this help page
        quit                  Quit the program
               ''')
    elif "add" == cmd:
        while 1:
            character = input("add> ")
            if not character:
                break
            if character in charDb:
                print("Invalid: %s already in database\n" % (character))
            else:
                newCharDb.append(character)
                charDb.append(character)
    elif cmd == "quit":
        quit = True
    else: # by default just do a search on characters
        for c in userInput:
            ndx = findChar(c, charDb)
            if not ndx:
                print(c + ": Not Found")
            else:
                print(c + ": Found at index", ndx)

for i in range(0, len(newCharDb)):
    file.write("%c\n" % (newCharDb[i]))
    
file.close()

