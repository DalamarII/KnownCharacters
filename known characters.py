# Known Characters.py

# find the given character c in the database db. If found, returns the index of
# the first match found. Else returns None
def findChar(c, tDb = None, sDb = None):
    if tDb:
        if c in tDb:
            return tDb[c]
    elif sDb:
        if c in sDb:
            return sDb[c]

def initDb(file, tDb, sDb):
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
        trad = c_list[0]
        simple = None
        if len(c_list) > 1:
            simple = c_list[1]

        ndx = findChar(trad, tDb, None)
        if not ndx:
            ndx = findChar(simple, None, sDb)
            
        if ndx:
            print("Warning: duplicate character %s found at %d and %d\n" %
                  (str, ndx, pos))
        else:
            tDb[trad] = pos
            if simple:
                sDb[simple] = pos
                
        pos += 1

# -----------------------------------------------------------

file = open('db.txt', 'a+', -1, 'utf-8')

# databases with characters as keys and physical index as values
traditionalDb = {}
simpleDb = {}


# TODO: newCharDb should really be a hashtable with characters as keys
newCharDb = []

initDb(file, traditionalDb, simpleDb)

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
            ndx = findChar(c, traditionalDb, simpleDb)
            if not ndx:
                print(c + ": Not Found")
            else:
                print(c + ": Found at index", ndx)

for i in range(0, len(newCharDb)):
    file.write("%c\n" % (newCharDb[i]))
    
file.close()

