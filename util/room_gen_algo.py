
## START AT A ROOM

# const [rooms, setRooms] = useState({
#     rooms: {
#         planet1: [
#             {room1 sdfasdfdsaf},
#             {room2 wesdfasffasdf},
#             {room3 asdfasdfasdfa},
#         ],
#         planet2: [
#             {room1 sdfasdfdsaf},
#             {room2 wesdfasffasdf},
#             {room3 asdfasdfasdfa},
#         ],
#         planet3: [
#             {room1 sdfasdfdsaf},
#             {room2 wesdfasffasdf},
#             {room3 asdfasdfasdfa},
#         ]
#     }
# })


# const [planet, setPlanet] = useState('default')

# rooms.planet1


# const [room, setRoom] = 

# rooms = {}


## n = 5

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

#              [Origin]
# [1, 2 ,3, 4, 5], array i
# [1, 2, 3, 4, 5], array j
# [1, 2, 3, 4, 5], array k
# [1, 2 ,3, 4, 5],
# [1, 2 ,3, 4, 5],

# 7x7
# [0, 0, 0, 0, 0, 0, 0],
# [0, 1, 2, 3, 4, 5, 0],
# [0, 1, 2, 3, 4, 5, 0],
# [0, 1, 2, 3, 4, 5, 0],
# [0, 1, 2, 3, 4, 5, 0],
# [0, 1, 2, 3, 4, 5, 0],
# [0, 0, 0, 0, 0, 0, 0],

from adventure.models import Room
choices_weighted= [0,0,1,1,1,2,3]
from random import choice
def make_planet(planet, num_rows):
    rooms = [[Room(planet=planet) for row in range(num_rows)] for row in range(num_rows)] 
    for i in range(num_rows):
        for j in range(num_rows):
            if i == num_rows-1 or i == 0:
                rooms[i][j].tile_num = 0
            elif j == num_rows-1 or j==0:
                rooms[i][j].tile_num = 0
            else:
                rooms[i][j].tile_num = choice(choices_weighted)
            rooms[i][j].save()
    for i in range(num_rows):
        for j in range(num_rows):
            if rooms[i][j].tile_num != 0:
                if rooms[i+1][j].tile_num == 0 and rooms[i-1][j].tile_num == 0 and rooms[i][j+1].tile_num == 0 and rooms[i][j-1].tile_num == 0:
                    rooms[i][j].tile_num = 0
                else:
                    if rooms[i-1][j].tile_num != 0:
                        rooms[i][j].connectRooms(rooms[i-1][j], 'n')
                    if rooms[i+1][j].tile_num != 0:
                        rooms[i][j].connectRooms(rooms[i+1][j], 's')
                    if rooms[i][j+1].tile_num != 0:
                        rooms[i][j].connectRooms(rooms[i][j+1], 'e')
                    if rooms[i][j-1].tile_num != 0:
                        rooms[i][j].connectRooms(rooms[i][j-1], 'w')
    for row in rooms:
        print(row)
        
make_planet('cool', 12)    


## Generate 25 rooms, and they MUST be connected to one other room, at least
## choices = ['w_to', 'n_to', 's_to', 'e_to']
## connected = choices.random(choices, k= //random num 1-4): any other room

## Generate 25 rooms, give them all id's
## then, take a random choice and connect it to another room,
## block off that other room's connecter, so if your room is east of another room, another room cannot also be east of it.
## at the end, pick one to be the landing point.




