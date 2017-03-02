import pygame, random, math, time


class BoundedItem(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.lastX = 0
        self.lastY = 0


class Map(BoundedItem):
    def __init__(self):
        self.x = 50
        self.y = 50
        self.speedX = 0
        self.speedY = 0
        self.length = 256
        self.width = 512
        self.Collision = False
        self.stopMoving = False


#create the layer using rect and fill method
    def displayMap(self,screen):

        pygame.draw.rect(
        screen,
        (24,123,47),
        (self.x,self.y,self.length,self.width),
        0)
        font = pygame.font.Font(None,25)

    def checkInnerCollision(self, char):
        # solve for the edge sides of the character
        charTop = char.y - (char.radius)
        charLeft = char.x - (char.radius)
        charBottom = char.y + (char.radius)
        charRight = char.x + (char.radius)

        #solve to find the edge sides of the map
        edgeTop = self.y -10
        edgeLeft = self.x -10
        edgeBottom = self.x + self.width - 10
        edgeRight = self.y + self.length - 10

        #if as long as any map edge doesnt exceeds that of the char, return true
        if(charTop > edgeTop and charLeft > edgeLeft and charBottom < edgeBottom and charRight < edgeRight):
            self.Collision = False
        else:
            self.Collision = True
        return self.Collision

    def move(self,char):
        #move the the last previous viable position
        if (self.checkInnerCollision(char)):
            self.x = self.lastX
            self.y = self.lastY
            return 1
        else:
            #move the map and keep note of the last viable position
            self.lastX = self.x
            self.lastY = self.y
            self.x += self.speedX
            self.y += self.speedY
            return 0

class AbstractNonMaps(BoundedItem):
    def __init__(self):
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0
        self.length = 70
        self.width = 70
        self.lastX = 0
        self.lastY = 0
        self.colDist = 50


#Theres a problem implementing the the same technique used for maps onto non map objects.
#When implemented on a smaller object, it considers everything out side of that box a
#collision, which is a serious problem that 3 lead to Walls, Pits and others moving on their
#own stating that the player is violating their collision conditions while they are no where
#near. So instead, the corners of all objects and the distance they have with the players
#corners were considered

    def checkOuterCollision(self, char):
        #solve to find the corners of the character (C) numbers are added for tighter collision
        CTL = (char.x, char.y)
        CBL = (char.x , char.y + char.length)
        CBR = (char.x + char.width, char.y + char.length)
        CTR = (char.x + char.width, char.y)
        cornersC = [CTL,CBL,CBR,CTR]

        #solve to find the 4 corners of the abstract (A) (wall, pit etc)
        ATL = (self.x - 5, self.y + 5)
        ABL = (self.x - 5, self.y + self.length)
        ABR = (self.x + self.width - 5, self.y + self.length)
        ATR = (self.x + self.width - 5, self.y + 5)
        cornersA = [ATL,ABL,ABR,ATR]
        #solve for the distance between each corner
        for elemC in cornersC:
            for elemA in cornersA:

                xA , yA = elemA
                xC , yC = elemC

                ma = xA - xC
                mb = yA - yC

                distance = math.sqrt(math.pow(ma, 2) + math.pow(mb, 2))
                self.num.append(distance)

        #check to see if any of the corners are too close (< 32)
        for n in self.num:
            if (n < self.colDist):
                self.Collision = True
            else:
                self.Collision = False
        return self.Collision


    def move(self,char):
        #move the the last previous viable position
        if (self.checkOuterCollision(char)):
            self.x = self.lastX
            self.y = self.lastY
            self.stopMoving = True
            return 1
        else:
            #move the map and keep note of the last viable position
            self.lastX = self.x
            self.lastY = self.y
            self.x += self.speedX
            self.y += self.speedY
        #remove the contents of the list and create a new one for the next iteration of corner distances
        del self.num[:]
        self.num = []
        return 0


class Wall(AbstractNonMaps):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0
        self.length = 30
        self.width = 30
        self.num = []
        self.lastX = 0
        self.lastY = 0
        self.colDist = 20

    def displayWall(self,screen):
        pygame.draw.rect(
        screen,
        (44,248,176),
        (self.x,self.y,self.length,self.width),
         0)

    def move(self,wall):
        #move the the last previous viable position
        if (self.checkOuterCollision(wall)):
            self.x = self.lastX
            self.y = self.lastY
            return 1
        else:
            #move the map and keep note of the last viable position
            self.lastX = self.x
            self.lastY = self.y
            self.x += self.speedX
            self.y += self.speedY
        #remove the contents of the list and create a new one for the next iteration of corner distances
        del self.num[:]
        self.num = []
        return 0


class Pit(AbstractNonMaps):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0
        self.length = 30
        self.width = 30
        self.num = []
        self.lastX = 0
        self.lastY = 0
        self.colDist = 30
        self.fires_contained = 0

    def displayPit(self,screen):
        pygame.draw.rect(
        screen,
        (38,6,51),
        (self.x,self.y,self.length,self.width),
         0)



class Character(object):
    def __init__(self):
        self.x = 500/2
        self.y = 500/2
        self.radius = 20
        self.length = self.radius*2
        self.width = self.radius*2

#a circle and square is contained in the character
#circle makes it easier to deal with distance differences
#square makes is easier to implement corners
    def displayChar(self,screen):
        pygame.draw.circle(
        screen,
        (176,68,44),
        (self.x+self.radius,self.y+self.radius),
         self.radius,
         0)

        pygame.draw.rect(
        screen,
        (176,68,44),
        (self.x,self.y,self.length,self.width),
         0)


def main():
    i = 0
    if i == 0:
        R = False
    i+=1
    width = 500
    height = 500
    green_color = (9, 29, 35)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Help Chandelure!')
    clock = pygame.time.Clock()

    pygame.mixer.init()
    #soundWin = pygame.mixer.Sound('../sounds/win.wav')
    #soundLose = pygame.mixer.Sound('../sounds/lose.wav')
    pygame.mixer.music.load('FF10.wav')
    pygame.mixer.music.play(-1)


    f1 = False
    f2 = False
    f3 = False
    endcondition1 = False

    KEY_W = 119
    KEY_A = 97
    KEY_S = 115
    KEY_D = 100

    KEY_ENTER = 13
    KEY_ESCAPE = 27

    #create the map object so that the event listener can edit fields of object
    map1 = Map()

    wall1 = Wall(140, 100)
    wall2 = Wall(200, 200)
    pit1 = Pit (370,128)
    char1 = Character()

    font = pygame.font.Font(None, 25)

    # Game initialization
    stop_game = False
    while not stop_game:

    # Event handling

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_W: #UP
                    map1.speedY = 3
                    wall1.speedY = 3
                    wall2.speedY = 3
                    pit1.speedY = 3
                if event.key == KEY_A: #LEFT
                    R = False
                    map1.speedX = 3
                    wall1.speedX = 3
                    wall2.speedX = 3
                    pit1.speedX = 3
                if event.key == KEY_S: #DOWN
                    map1.speedY = -3
                    wall1.speedY =-3
                    wall2.speedY =-3
                    pit1.speedY = -3
                if event.key == KEY_D: #RIGHT
                    R = True
                    map1.speedX = -3
                    wall1.speedX =-3
                    wall2.speedX =-3
                    pit1.speedX = -3

            if event.type == pygame.KEYUP:
                # deactivate the corresponding speeds
                # when an arrow key is released
                if event.key == KEY_W:
                    map1.speedY = 0
                    wall1.speedY = 0
                    wall2.speedY = 0
                    pit1.speedY = 0
                elif event.key == KEY_A:
                    R = False
                    map1.speedX = 0
                    wall1.speedX = 0
                    wall2.speedX = 0
                    pit1.speedX = 0
                elif event.key == KEY_S:
                    map1.speedY = 0
                    wall1.speedY = 0
                    wall2.speedY = 0
                    pit1.speedY = 0
                elif event.key == KEY_D:
                    R = True
                    map1.speedX = 0
                    wall1.speedX = 0
                    wall2.speedX = 0
                    pit1.speedX = 0
            if event.type == pygame.QUIT:
                stop_game = True

    # Game logic

    #Responsible for ensuring that everything moves together
    #Both (Maps and AbstractNonMaps)

        m1 = map1.move(char1)
        w1 = wall1.move(char1)
        w2 = wall2.move(char1)
        p1 = pit1.move(char1)
        if (m1 == 1):
            wall1.speedX = 0
            wall1.speedY = 0
            wall2.speedX = 0
            wall2.speedY = 0
            pit1.speedX = 0
            pit1.speedY = 0
        elif(w1 == 1):
            map1.speedX = 0
            map1.speedY = 0
            wall2.speedX = 0
            wall2.speedY = 0
            pit1.speedX = 0
            pit1.speedY = 0
        elif(w2 == 1):
            map1.speedX = 0
            map1.speedY = 0
            wall1.speedX = 0
            wall1.speedY = 0
            pit1.speedX = 0
            pit1.speedY = 0
        elif(p1 == 1):
            map1.speedX = 0
            map1.speedY = 0
            wall1.speedX = 0
            wall1.speedY = 0
            wall2.speedX = 0
            wall2.speedY = 0

        def distanceFormula(x1,x2,y1,y2):
            X = x1 - x2
            Y = y1 - y2
            distance = math.sqrt(math.pow(X, 2) + math.pow(Y, 2))
            return distance

        if (distanceFormula(wall1.x,pit1.x,wall1.y,pit1.y) < 50):
            f1 = True
        elif(distanceFormula(wall2.x,pit1.x,wall2.y,pit1.y) < 50):
            f2 = True

        if (f1 and f2):
            endcondition1 = True




    # Game display
        #(0th layer)
        #create the background for the background screen
        screen.fill(green_color)
        if ((f1 == True and f2 == True)):
            text1 = font.render("Both Flames are Burning the Tree!", True, (255,255,255))
            screen.blit(text1, (30,30))
            text2 = font.render("Chandelure is Ecstatic!", True, (255,255,255))
            screen.blit(text2, (30,50))


        #(1st layer)
        #display the map screen
        #map1.displayMap(screen)
        bg_image = pygame.image.load('floor22.png').convert_alpha()
        screen.blit(bg_image, (map1.x,map1.y))

        #(2nd layer)w
        #create constructs to place on the map
        tree = pygame.image.load('Tree.png').convert_alpha()
        screen.blit(tree, (pit1.x-55,pit1.y-70))
        #pit1.displayPit(screen)

        #2wall1.displayWall(screen)
        fire = pygame.image.load('fire.png').convert_alpha()
        screen.blit(fire, (wall1.x-25,wall1.y-30))
        #screen.blit(wal, (wall2.x,wall2.y))

        #wall2.displayWall(screen)
        screen.blit(fire, (wall2.x-25,wall2.y-30))



        #call the method responsible for creating the shape

        #create the main character that it looks like you are "controlling"

        #char1.displayChar(screen)
        if (R == False):
            chan = pygame.image.load('chan.png').convert_alpha()
            screen.blit(chan, (char1.x-40,char1.y-55))
        elif (R == True):
            Rchan = pygame.image.load('Rchan.png').convert_alpha()
            screen.blit(Rchan, (char1.x-40,char1.y-55))


        pygame.display.update()
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    main()
