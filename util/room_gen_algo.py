
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

names = ["The Foxtail Ravine", 'The Mirrored Fjords', 'The Gloomy Fjords', 'The Frozen Bluffs', 'The Granite Fjord', 'The Sandstone Canyon', 'Hanston Gulch', 'Barkmagne Gulch', 'Plavern Gorge', 'Churchbridge Crag', 'The Whimpering Wall', 'The Black Cliffs', 'The Tempest Abyss', 'The Eagle Cliff', 'The Sighing Bluff', 'The Fractured Bluffs', 'Warsend Cliffs', 'Walchill Fjords', "Digchester Fjords", 'Beaverdeen Bluffs', 'Tulsa, Oklahoma', 'Murfreesboro, Tennessee', 'Oakland, California', 'Twin Cities, Minnesota', 'The Steaming Wastes', 'The Wild Expanse', 'The Ember Territory', 'The Torment Badlands', 'The Fiery Desert', 'The Grotyll Territory', 'The Bragohs Emberlands', 'The Uqelst Flamelands', 'The Cursed Emptiness', 'The Enchanted Savanna', 'The Open Wilderness', 'The Southern Flatlands', 'The Lonely Desert', 'Fearsome Fields', 'Voiceless Emptiness', 'Black Prairie', 'Hot Wilds', 'Deserted Expanse', 'Copper Mount Woodland', 'Misty Raspberry Wilds', 'Lively Grove', 'Curious Forest', 'Spotted Hare Forest', 'Black Panda Wilds', 'Brosvons Timberland', 'Monkmouth Forest', 'Croyswell Wood', 'Niacoln Covert', 'Bikini Bottom', 'Azeroth', 'Twitter', 'Zuckerville', "Jeff Bezos's House", "The Kitchen", ""]
forest_landscapes = ["You stand in a flat terrain covered with diverse trees and gigantic grass.  You can see a stream miles away and a fort nearby.  The temperature is hot and the sky is overcast.", "You stand in a flat region scattered with evergreen shrubs.  You can see the ocean to the east.  The temperature is a little cool and the sky is mostly clear.", "You stand in a flat area dotted with small trees, shrubs, and strange-looking grass.  You can see a marsh not too far away.  The temperature is somewhat warm and the sky is partially cloudy.", ]
desert_landscapes = ["You stand in a flat region dotted with various dark rocks.  You can see a bog in the distance.  The temperature is cool and the sky is clear.", "You stand in a flat region spotted with unusual pale rocks. It's also sprinkled with various trees, dead shrubs, and grass.  You can see a monastery miles away.  The temperature is quite cool and the sky is clear.", "You stand in a broken region abounding with gigantic brown stones.  You can see a castle to the south.  The temperature is somewhat warm and the sky is mostly clear.", "You stand in a hilly terrain dotted with dead plants.  You can see a large lake close by and a fort to the south.  The temperature is cold and the sky is mostly clear." ]
mountainous_landscapes = ['You stand in a mountainous region scattered with small trees and unusual grass.  You can see a waterfall to the south.  The temperature is somewhat warm and the sky is mostly clear.', "You stand in a mountainous area covered with various colorful rocks. It's also smattered with small wildflowers.  You can see a marsh close by.  The temperature is a little cool and the sky is mostly clear.", "You stand in a mountainous region replete with gigantic reddish rocks.  You can see a marsh to the west and a tower to the north.  The temperature is quite cool and the sky is mostly clear.", "You stand in a mountainous terrain spotted with gigantic trees and huge grass.  You can see a river not too far away.  The temperature is quite cool and the sky is overcast.", "You stand in a mountainous region scattered with various bluish stones.  You can see a stream to the west.  The temperature is quite cool and the sky is partially cloudy.", "You stand in a mountainous region replete with unusual greenish rocks.  You can see a bog to the south and a town to the north.  The temperature is very warm and the sky is mostly clear.", "You stand in a mountainous terrain covered with gigantic pale brown stones.  You can see a stream miles away.  The temperature is quite cool and the sky is overcast.", "You stand in a flat terrain scattered with dead wildflowers.  You can see the ocean to the west.  The temperature is hot and the sky is clear.", "You stand in a hilly terrain spotted with huge purplish stones.  You can see a bog to the west and a castle to the south.  The temperature is very warm and the sky is clear.", "You stand in a broken area covered with unusual grass and foul-smelling wildflowers.  You can see a large river nearby.  The temperature is very warm and the sky is mostly clear.", ]
other_landscapes = ['You stand in a flat region spotted with huge trees and wildflowers.  You can see a waterfall nearby.  The temperature is hot and the sky is mostly clear.', "You stand in a hilly terrain smattered with gigantic dark stones. It's also spotted with plants.  You can see a small body of water not too far away.  The temperature is somewhat warm and the sky is overcast.", "You stand in a flat region dotted with various shrubs.  You can see a stream miles away.  The temperature is somewhat warm and the sky is overcast.", "You stand in a flat terrain smattered with worn-down gray stones.  You can see the ocean to the west.  The temperature is quite cool and the sky is overcast.", "You stand in a flat terrain scattered with small multicolored stones.  You can see a small body of water to the south and a tower to the south.  The temperature is somewhat warm and the sky is partially cloudy.",  ]
all_landscapes = forest_landscapes + desert_landscapes + mountainous_landscapes + other_landscapes
from adventure.models import Room
choices_weighted= [0,0,1,1,1,2,3]
from random import choice
def make_planet(planet, num_rows):
    rooms = [[Room(planet=planet, title=choice(names), description=choice(all_landscapes)) for row in range(num_rows)] for row in range(num_rows)] 
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
        
make_planet('Kevin', 42)    


## Generate 25 rooms, and they MUST be connected to one other room, at least
## choices = ['w_to', 'n_to', 's_to', 'e_to']
## connected = choices.random(choices, k= //random num 1-4): any other room

## Generate 25 rooms, give them all id's
## then, take a random choice and connect it to another room,
## block off that other room's connecter, so if your room is east of another room, another room cannot also be east of it.
## at the end, pick one to be the landing point.




