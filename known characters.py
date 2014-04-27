# Known Characters.py

file = open('db.txt', 'a+', -1, 'utf-8')

# TODO: charDb should really be a hashtable with characters as keys
charDb = []
newCharDb = []

# find the given character c in the database db. If found, returns the index of
# the first match found. Else returns None
def findChar(c, db):
    for i, v in enumerate(db):
        if c == v:
            return i

def initDb(file):
    '''
        Input:
            A file object to initialize the database with

        Initializes the database using the given file object
    '''
    pos = 0
    str = ''
    file.seek(0)
    for line in file:
        str = line[:len(line)-1]

        if not str or str.isspace():
            continue
    
        index = findChar(str, charDb)
        if index:
            print("Warning: duplicate character %s found at %d and %d\n" %
                  (str, index+1, pos+1))
        else:
            charDb.insert(pos, str)
        pos += 1

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
                print(c + ": Found at index", ndx+1)

for i in range(0, len(newCharDb)):
    file.write("%c\n" % (newCharDb[i]))
    
file.close()

