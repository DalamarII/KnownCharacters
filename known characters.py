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

quit = False
while not quit:
    userInput = input("> ")

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
    elif "search" == cmd:
        ndx = findChar(character, charDb)
        if not ndx:
            print("Not Found\n")
        else:
            print("Found at index", ndx+1)
    elif cmd == "quit":
        quit = True

for i in range(0, len(newCharDb)):
    file.write("%c\n" % (newCharDb[i]))
    
file.close()

