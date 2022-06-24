room1 = (
    1, #the room num
    'you have spawned in the starting point ', #the greeting
    ['',], #objects
    [
    ['S',9,False], #direction,destination,is it locked
    ['E',2,False]] #direction,destination,is it locked
    )

room2 = (
    2, #the room num
    'you have arrived in the armoury ', #the greeting
    ['sword'], #objects
    [
    ['W',1,False], #direction,destination,is it locked
    ['E',3,False],] #direction,destination,is it locked
    )

room3 = (
    3, #the room num
    'you have arrived in the room of unimportance ', #the greeting
    ['',], #objects
    [
    ['W',2,False],
    ['S',11,False],]#direction,destination,is it locked
    )

    
room9 = (
    9, #the room num
    'you have arrived in the brewery ', #the greeting
    ['poison',], #objects
    [
    ['N',1,False], #direction,destination,is it locked
    ['S',17,False],]
    )


room11 = (
    11, #the room num
    'you have arrived in the room of nothingness ', #the greeting
    ['',], #objects
    [
    ['N',3,False], #direction,destination,is it locked
    ['E',12,False] #direction,destination,is it locked
    ]
    )

      
room12 = (
    12, #the room num
    'you have arrived in the room of unimportance ', #the greeting
    ['',], #objects
    [
    ['W',11,False], #direction,destination,is it locked
    ['S',20,False], #direction,destination,is it locked
    ]
    )

room17 = (
    17, #the room num
    'you have arrived in the gunrange #notsponseredbyamerica   ', #the greeting
    ['gun'], #objects
    [
    ['N',9,False], #direction,destination,is it locked
    ['E',18,False]
    ]
    )

room18 = (
    18, #the room num
    'you have arrived in the room of unimportance', #the greeting
    [], #objects
    [
    ['W',17,False], #direction,destination,is it locked
    ['S',26,False],]
    )

room20 = (
    3, #the room num
    'you have arrived in the room of unimportance ', #the greeting
    [], #objects
    [
    ['N',12,False], #direction,destination,is it locked
    ['S',28,False],]
    )

room25 = (
    25, #the room num
    'you have arrived in the room of no horizons ', #the greeting
    ['',], #objects
    [
    ['E',26,False], #direction,destination,is it locked
    ['S',33,True],]
    )

room26 = (
    26, #the room num
    'you have arrived in the room of bleakness ', #the greeting
    ['',], #objects
    [
    ['N',18,False], #direction,destination,is it locked
    ['W',25,False],]
    )

room27 = (
    27, #the room num
    'you have arrived in the room of locksmithing ', #the greeting
    ['key',], #objects
    [
    ['E',28,False] #direction,destination,is it locked
    ]
    )

room28 = (
    28, #the room num
    'you have arrived in the room of despair ', #the greeting
    ['',], #objects
    [
    ['N',20,False], #direction,destination,is it locked
    ['W',27,False],
    ])

room33 = (
    33, #the room num
    'you have arrived in the room of the final boss ', #the greeting
    ['troll',], #objects
    [
    ['S',40,False], #direction,destination,is it locked
    ['N',25,False],
    ])
room40 = (
    40, #the room num
    'you have conquered the troll and completed the quest you can leave and see your family', #the greeting
    ['sweet victory','mountains of gold'], #objects
    [
    ])





# dictionary for all rooms
rooms = {
    1 : room1,
    2 : room2,
    3 : room3,
    9 : room9,
    11 : room11,
    12 : room12,
    17 : room17,
    18 : room18,
    20 : room20,
    25 : room25,
    26 : room26,
    27 : room27,
    28 : room28,
    33 : room33,
    40 : room40
    
    }

def show_room(room):
    '''
    shows a particular room.
    '''
    global inventory
    
    (number, greeting, objects, doors) = room
    #print greeting
    print(greeting)
    print('--------------------------------------')
    #list the inventory
    print('you have the following items:')
    for item in inventory:
        print('*' + item + '*')
    print()
    #list any objects
    print('you see')
    for item in objects:
        print ('*' + item)
    print()    
    #list exits
    print('you see the following exits:')
    print('----------------------------')
    for door in doors:
        (direction, destination, locked) = door
        if locked:
            print('* ' + direction + ' (locked)')
        else:
            print(' * ' + direction)
    print()



def go(direction):
    '''
    moves from the current room.
    parameters:
    -----------
    direction(string): the direction to move (N,E,W,S)
    
    Updates the current_room if the move is valid.
    '''
    global current_room
    global rooms
    doors = current_room[3]
    
    #doors is a list that looks like this:
    #[('N',25,false), ('E', 24,false)]
    
    for door in doors:
        (door_direction, destination, locked) = door
        if door_direction.lower() == direction.lower():
            if locked:
                print('that door is locked')
                print()
                return
            else:
                current_room = rooms[destination]
                if current_room[0] == 40: # you are in the final room!
                    print("yoy win pogger camping")
                    exit()
                return
        
    print('there is a wall there idiot look around you') 








def take(thing):
    '''
    takes an object - remove it from the room, add it to inventory
    parameters:
    -----------
    thing (str): the object to take
    '''
    global inventory
    global current_room
    
    #check if the item is in the room
    objects = current_room[2]
    if (thing in objects):
        if thing == "troll":
            # todo troll kills  you
            print("knocks you into a wall knocking you unconsious it then crushes your head")
            exit()
        else:
            #remove item from inventory
            objects.remove(thing)
            #add item to inventory
            inventory.append(thing)
    else:
        # warn user item is not in a room
        print('where is it are you having a mirage dummy?')






def slash():
    '''
    slashes sword
    parameters
    -------------
    if troll is in the room kill it,
    if not wave about randomly
    '''
    global current_room
    global rooms
    objects = current_room[2]
    if "troll" in objects:
        objects.remove('troll')
        print("You stab the troll heroicaly through the heart getting covered in green slimy blood.")
    else:
        print('you look cool but foolish')
    

def poison():
    # make the poison kill self
    print('you start to feel your knee\'s crumple you fall your heart stops you die')
    exit()
    

def unlock():
    '''
    unlock's all of the doors in a current room.
    '''
    global current_room
    doors = current_room [3]
    #door's is a list of tuples,like[('N, 25, True')]
    for door in doors:
        # TODO unlock the door
        door[2] = False


def bang():
    '''
    pretends to be a useful weapon
    '''
    global current_rooms
    global rooms
    objects = current_room[2]
    if "troll" in objects:
        print("you pull the trigger the recoil makes the gun hit you in the face you feel loads of pain.")
        print("you hear the troll yell 'oof what was that' he turns around 'oh a tiny human trying to kill me with bullet how cute'")
        print("he then proceeds to use you as a toothbrush")
        exit()
    else:
        print('you look down the barrel (of gun) and with your -2 iq you pull the trigger blasting your brain on the carpet come on man you can\'t be doing t-
        hat as a guest')
        exit()

    


def use(thing):
    '''
    uses the specified thing in the current room.
    parameters:
    -----------
    thing(str): the thing to use
    '''
    global inventory
    global current_room
    
    print("using [{}]".format(thing))
    print(inventory)
    #TODO: check that thing is in inventory
    thing = thing.lower()
    if (thing in inventory):
        #TODO: an if statement for each supported thing
        #continue form 'ere bruv
        #valid things to use
        if thing == 'sword':
            slash()
        elif thing == 'poison':
            poison()
        elif thing == 'gun':
            bang()
        elif thing == 'key':
            unlock()
        else:
            #warn the user that they don't have item
            print('I don\'t know what a '+thing+' is.')
            print()
    else:
        print('what is that')
        
    
    
    
    
current_room = rooms[1]#setup starting room

#set up inventory
inventory = []

while True:#gameloop
    show_room(current_room)
    #num = input('what room would you like to show')
    cmd = input('enter command: > ')
    bits = cmd.split(' ')
    action = bits[0]
    qualifier = bits[1]
    print('action:' + action)
    print('qualifier:' + qualifier)
    
    action = action.lower()
    if action == 'go':
        go(qualifier)
    elif action == 'take':
        take(qualifier)
    elif action == 'use':
        use(qualifier)
    else:
        print('invalid command NO HACKER GO DIE')
        print('--------------------------------')