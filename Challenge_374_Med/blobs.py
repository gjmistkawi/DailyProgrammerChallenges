import sys

class Blob:
    def __init__(self,data):
        self.position = data[0:-2]
        self.size = data[-1]

    def look(self,blobs):


    def move(blob):


    def grow():


class Game:
    def __init__(self,data):
        for i in range(dimensions):
            field.append = [0,0]
        for blob in data:
            self.blobs.append(blob)
            field.append(blob.position)

        game.state = True



            
        

    def turn(self):
        for blob in blobs:
            target = blob.move(blob.look(self.blobs))
            if(target != None):
                blob.grow(target)
        

    def __str__(self):
        



def main():
    game_map = [(0,1,2),
                (10,0,2)]

    game = Game(game_map)
    while (game.state != done):
        game.turn()
        print(game + "\n")




if __name__ == "__main__":
    main()