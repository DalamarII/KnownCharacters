# Known Characters.py
file = open('db.txt', 'a+', -1, 'utf-8')

charDb = []
newCharDb = []

pos = 0
str = ''
file.seek(0)
for line in file:
    str = line[:len(line)-1]
    if str in charDb:
        print("Warning: duplicate found at %d, %s already in db\n" % (pos+1, str))
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
        if character in charDb:
            print("Found\n")
        else:
            print("Not found\n")
    elif cmd == "quit":
        quit = True

for i in range(0, len(newCharDb)):
    file.write("%c\n" % (newCharDb[i]))
    
file.close()

