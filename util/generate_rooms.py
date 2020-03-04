from adventure.models import Player, Room
import random

room_titles = {
    "1": "Room 1",
    "2": "Room 2",
    "3": "Room 3",
    "4": "Room 4",
    "5": "Room 5",
    "6": "Room 6",
    "7": "Room 7",
    "8": "Room 8",
    "9": "Room 9",
    "10": "Room 10",
    "11": "Room 11",
    "12": "Room 12",
    "13": "Room 13",
    "14": "Room 14",
    "15": "Room 15",
    "16": "Room 16",
    "17": "Room 17",
    "18": "Room 18",
    "19": "Room 19",
    "20": "Room 20",
    "21": "Room 21",
    "22": "Room 22",
    "23": "Room 23",
    "24": "Room 24",
    "25": "Room 25",
}

for i in range(25):
    num = str(random.randrange(1, 26))
    print(room_titles[num])
    # new_room = Room(title=room_titles[num])
    del room_titles[num]
    # print(new_room)



from adventure.models import Player, Room
def make_planet(title, num_rows):
    rooms = [[] for row in range(num_rows)] 
    for i in range(num_rows):
        for j in range(num_rows):
            rooms[i].append(Room())

    for i in range(num_rows):
        for j in range(num_rows):
            if i == num_rows-1 or i == 0:
                rooms[i][j] = 0
            elif j == num_rows-1 or j==0:
                rooms[i][j] = 0
            else:
                pass

    for row in rooms:
        print(row)

    return