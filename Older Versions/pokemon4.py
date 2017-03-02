import pygame, random, math, time







class Map(object):
    def __init__(self):
         self.x = 50
         self.y = 50
         self.speedX = 0
         self.speedY = 0
         self.length = 400
         self.width = 400
         self.Collision = False


#create the layer using rect and fill method
    def displayMap(self,screen):
        pygame.draw.rect(
        screen,
        (24,123,47),
        (self.x,self.y,self.length,self.width),
        0)
        font = pygame.font.Font(None,25)

        # Debugging
        # font = pygame.font.Font(None,25)
        # text1 = "(%d, %d)" % (self.x, self.y)
        # thing1 = font.render(text1,True,(0,0,255))
        # screen.blit(thing1,(self.x,self.y))
        #
        # text2 = "(%d, %d)" % (self.x, self.y + self.length)
        # thing2 = font.render(text2,True,(0,0,255))
        # screen.blit(thing2,(self.x, self.y + self.length))
        #
        # text3 = "(%d, %d)" % (self.x + self.width, self.y + self.length)
        # thing3 = font.render(text3,True,(0,0,255))
        # screen.blit(thing3,(self.x + self.width, self.y + self.length))
        #
        # text4 = "(%d, %d)" % (self.x + self.width, self.y)
        # thing4 = font.render(text4,True,(0,0,255))
        # screen.blit(thing4,(self.x + self.width,self.y))

    def hasCollided():
        return self.Collision

    def checkInnerCollision(self, char):
        # solve for the edge sides of the character
        charTop = char.y - (char.radius)
        charLeft = char.x - (char.radius)
        charBottom = char.y + (char.radius)
        charRight = char.x + (char.radius)

        #solve to find the edge sides of the map
        edgeTop = self.y + 5
        edgeLeft = self.x + 5
        edgeBottom = self.x + self.width - 5
        edgeRight = self.y + self.length - 5

        #if as long as any map edge doesnt exceeds that of the char, return true
        if(charTop > edgeTop and charLeft > edgeLeft and charBottom < edgeBottom and charRight < edgeRight):
            self.Collision = False
        else:
            self.Collision = True

        return self.Collision

    def move(self,char):
        #move if there is no collision with map edges and character
        if (self.checkInnerCollision(char)):
            #bring the map and constructs back into to
            #approved area after collision with character
            if ((self.x + self.width) < char.x + 20):
                self.x += 1

            elif(self.x > char.x - 20):
                self.x -= 1

            elif((self.y + self.length) < char.y + 20):
                self.y += 1

            elif(self.y > char.x - 20):
                self.y -= 1

        else:

            #move the map
            self.x += self.speedX
            self.y += self.speedY

class AbstractNonMaps(object):
    def __init__(self):
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0
        self.length = 50
        self.width = 50
        self.Collision = False
        self.lastX = 0
        self.lastY = 0
        self.colDist = 30



    def hasCollided():
        return self.Collision

#Theres a problem implementing the the same technique used for maps onto non map objects.
#When implemented on a smaller object, it considers everything out side of that box a
#collision, which is a serious problem that can lead to Walls, Pits and others moving on their
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
        i = 0
        for n in self.num:

            if (n < self.colDist):

                print "***TRUE*** %d" % i

                self.Collision = True
            else:
                self.Collision = False

                print "***FALSE***%d" % i

            i+=1
        #time.sleep(.2)
        print "*****************************************"
        return self.Collision


    def move(self,char):

        #num contains 16 values of distances compared between corners of the
        #abstract and the character.
        #0 - 3 compares all abstract corners to char corner CTL
        #4 - 7 compares all abstract corners to char corner CBL
        #8 - 11 compares all abstract corners to char corner CBR
        #12 - 15 compares all abstract corners to char corner CTR

        # 0,5,10 and 15 are not compared to 30 below because it is not
        # possible for them to come in contact with their respective
        # Char corner (eg. topleft of char to topleft of abstract)

        #certian elements are paired together because they provide the same
        #result in behavior the abstract must do to move away from the char.
        #(eg bottomLeft corner and )


        #check the abstract objects corners distance the hero's corners
        #add the appropriate values to move away from that specific corner
        if (self.checkOuterCollision(char)):
            self.x = 100#self.lastX
            self.y = 100#self.lastY

            # if(self.num[1] < 30 or self.num[14] < 30):
            #     print "A MOVE UP"
            #     self.y =
            # elif(self.num[3] < 30 or self.num[6] < 30):
            #     print "A MOVE LEFT"
            #     self.x -= 1
            # elif(self.num[4] < 30 or self.num[11] < 30):
            #     print "A MOVE DOWN"
            #     self.y += 1
            # elif(self.num[9] < 30 or self.num[12] < 30):
            #     print "A MOVE RIGHT"
            #     self.x += 1
            # elif(self.num[2] < 30):
            #     print "MOVE UP LEFT"
            #     self.y -= 1
            #     self.x -= 1
            # elif(self.num[7] < 30):
            #     print "MOVE DOWN LEFT"
            #     self.y += 1
            #     self.x -= 1
            # elif(self.num[8] < 30):
            #     print "MOVE DOWN RIGHT"
            #     self.y += 1
            #     self.x += 1
            # elif(self.num[13] < 30):
            #     print "MOVE UP RIGHT"
            #     self.y -= 1
            #     self.x += 1



            #bring the Abstract Object and constructs back into to
            #approved area after collision with character

        else:
            #move the map
            self.lastX = self.x
            self.lastY = self.y
            self.x += self.speedX
            self.y += self.speedY


        #remove the contents of the list and create a new one for the next iteration of corner distances
        del self.num[:]
        self.num = []


class Wall(AbstractNonMaps):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0
        self.length = 30
        self.width = 30
        self.collision = False
        self.num = []
        self.lastX = 0
        self.lastY = 0
        self.colDist = 30

    def displayWall(self,screen):
        pygame.draw.rect(
        screen,
        (44,148,176),
        (self.x,self.y,self.length,self.width),
         0)
        # #Debugging
        # font = pygame.font.Font(None,25)
        # text1 = "(%d, %d)" % (self.x, self.y)
        # thing1 = font.render(text1,True,(0,0,255))
        # screen.blit(thing1,(self.x-50,self.y))
        #
        # text2 = "(%d, %d)" % (self.x, self.y + self.length)
        # thing2 = font.render(text2,True,(0,0,255))
        # screen.blit(thing2,(self.x-50, self.y + self.length))
        #
        # text3 = "(%d, %d)" % (self.x + self.width, self.y + self.length)
        # thing3 = font.render(text3,True,(0,0,255))
        # screen.blit(thing3,(self.x + self.width, self.y + self.length))
        #
        # text4 = "(%d, %d)" % (self.x + self.width, self.y)
        # thing4 = font.render(text4,True,(0,0,255))
        # screen.blit(thing4,(self.x + self.width,self.y))


# class Pit(Map):
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def displayPit(self,screen):
#         pygame.draw.rect(
#         screen,
#         (38,6,51),
#         (self.x,self.y,150,150),
#          0)
#
# class Teleporters(Map):
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#
#


class Character(object):
    def __init__(self):
     self.x = 500/2
     self.y = 500/2
     self.radius = 10
     self.length = self.radius*2
     self.width = self.radius*2


    def displayChar(self,screen):
        pygame.draw.circle(
        screen,
        (176,68,44),
        (self.x,self.y),
         self.radius,
         0)

        pygame.draw.rect(
        screen,
        (68,176,88),
        (self.x,self.y,self.length,self.width),
         0)

        #Debugging
        # font = pygame.font.Font(None,25)
        # text1 = "(%d, %d)" % (self.x, self.y)
        # thing1 = font.render(text1,True,(0,0,255))
        # screen.blit(thing1,(self.x-50,self.y))
        #
        # text2 = "(%d, %d)" % (self.x, self.y + self.length)
        # thing2 = font.render(text2,True,(0,0,255))
        # screen.blit(thing2,(self.x-50, self.y + self.length))
        #
        # text3 = "(%d, %d)" % (self.x + self.width, self.y + self.length)
        # thing3 = font.render(text3,True,(0,0,255))
        # screen.blit(thing3,(self.x + self.width, self.y + self.length))
        #
        # text4 = "(%d, %d)" % (self.x + self.width, self.y)
        # thing4 = font.render(text4,True,(0,0,255))
        # screen.blit(thing4,(self.x + self.width,self.y))




def main():
    width = 500
    height = 500
    green_color = (9, 29, 35)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    KEY_W = 119
    KEY_A = 97
    KEY_S = 115
    KEY_D = 100

    KEY_ENTER = 13
    KEY_ESCAPE = 27

    #create the map object so that the event listener can edit fields of object
    map1 = Map()
    wall1 = Wall(120, 170)
    char1 = Character()


    # Game initialization
    stop_game = False
    while not stop_game:

    # Event handling
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_W: #UP
                    map1.speedY = 3
                    wall1.speedY = 3
                if event.key == KEY_A: #LEFT
                    map1.speedX = 3
                    wall1.speedX = 3
                if event.key == KEY_S: #DOWN
                    map1.speedY = -3
                    wall1.speedY =-3
                if event.key == KEY_D: #RIGHT
                    map1.speedX = -3
                    wall1.speedX =-3

            if event.type == pygame.KEYUP:
                # deactivate the corresponding speeds
                # when an arrow key is released
                if event.key == KEY_W:
                    map1.speedY = 0
                    wall1.speedY = 0
                elif event.key == KEY_A:
                    map1.speedX = 0
                    wall1.speedX = 0
                elif event.key == KEY_S:
                    map1.speedY = 0
                    wall1.speedY = 0
                elif event.key == KEY_D:
                    map1.speedX = 0
                    wall1.speedX = 0
            if event.type == pygame.QUIT:
                stop_game = True

    # Game logic
        #map1.move(char1)
        wall1.move(char1)






    # Game displa
        #(0th layer)
        #create the background for the background screen
        screen.fill(green_color)

        #(1st layer)
        #display the map screen
        #map1.displayMap(screen)

        #(2nd layer)
        #create constructs to place on the map


        wall1.displayWall(screen)
        #pit1.displayPit(screen)

            #call the method responsible for creating the shape

            #create the main character that it looks like you are "controlling"
        char1 = Character()
        char1.displayChar(screen)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
