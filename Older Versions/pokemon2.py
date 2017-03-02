import pygame, random, math, time


class Map(object):
    def __init__(self):
         self.x = 50
         self.y = 50
         self.speedX = 0
         self.speedY = 0
         self.length = 400
         self.width = 400
         self.collision = False


#create the layer using rect and fill method
    def displayMap(self,screen):
        pygame.draw.rect(
        screen,
        (24,123,47),
        (self.x,self.y,self.length,self.width),
        0)


        # Debugging
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
        return self.collision

    def checkCollision(self, char):
        # solve for the edges of the character
        charTop = char.y - (char.radius)
        charLeft = char.x - (char.radius)
        charBottom = char.y + (char.radius)
        charRight = char.x + (char.radius)

        #solve to find the edges of the map
        edgeTop = self.y + 5
        edgeLeft = self.x + 5
        edgeBottom = self.x + self.width - 5
        edgeRight = self.y + self.length - 5

        #if as long as any map edge doesnt exceeds that of the char, return true
        if(charTop > edgeTop and charLeft > edgeLeft and charBottom < edgeBottom and charRight < edgeRight):
            self.collision = False
            return self.hasCollided()
        else:
            self.collision = True
            return self.hasCollided()


    def move(self, char):
        #move if there is no collision with map edges and character
        if (self.hasCollided):

            #move the map
            self.x += self.speedX
            self.y += self.speedY

        else:

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




class Construct(Map):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def displayConst(self,screen):
        pygame.draw.rect(
        screen,
        (44,148,176),
        (self.x,self.y,50,50),
         0)


class Pit(Map):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0
        self.length = 50
        self.width = 50
        self.collision = False

    def displayPit(self,screen):
        pygame.draw.rect(
        screen,
        (38,6,51),
        (self.x,self.y,self.length,self.width),
         0)

        # # Debugging
        # font = pygame.font.Font(None,25)
        # text1 = "(%d, %d)" % (self.x, self.y)
        # thing1 = font.render(text1,True,(0,0,255))
        # screen.blit(thing1,(self.x-70,self.y))
        #
        # text2 = "(%d, %d)" % (self.x, self.y + self.length)
        # thing2 = font.render(text2,True,(0,0,255))
        # screen.blit(thing2,(self.x-70, self.y + self.length))
        #
        # text3 = "(%d, %d)" % (self.x + self.width, self.y + self.length)
        # thing3 = font.render(text3,True,(0,0,255))
        # screen.blit(thing3,(self.x + self.width, self.y + self.length))
        #
        # text4 = "(%d, %d)" % (self.x + self.width, self.y)
        # thing4 = font.render(text4,True,(0,0,255))
        # screen.blit(thing4,(self.x + self.width,self.y))

    #anything thats not a map needs a collision detection of interactions from the
    #outside of them, not the inside of them like Map objects
    def checkCollision(self, char):
        # solve for the edges of the character
        charTop = char.y - (char.radius)
        charLeft = char.x - (char.radius)
        charBottom = char.y + (char.radius)
        charRight = char.x + (char.radius)

        #solve to find the edges of the map
        edgeTop = self.y + 5
        edgeLeft = self.x + 5
        edgeBottom = self.x + self.width - 5
        edgeRight = self.y + self.length - 5

        #if as long as any map edge doesnt exceeds that of the char, return true
        if(charTop < edgeTop and charLeft < edgeLeft and charBottom > edgeBottom and charRight > edgeRight):
            return True
        else:
            return False

    def move(self, char):
        self.x += self.speedX
        self.y += self.speedY

        #move if there is no collision with map edges and character
        if (self.checkCollision(char)):
            x = 1
            #move the map


        else:
            x = 1
            # #bring the map and constructs back into to
            # #approved area after collision with character
            # if ((self.x + self.width) > char.x + 20):
            #     self.x += 1
            #
            # elif(self.x < char.x - 20):
            #     self.x -= 1
            #
            # elif((self.y + self.length) > char.y + 20):
            #     self.y += 1
            #
            # elif(self.y < char.x - 20):
            #     self.y -= 1

class Teleporters(Map):
    def __init__(self,x,y):
        self.x = x
        self.y = y





class Character(object):
    def __init__(self):
     self.x = 500/2
     self.y = 500/2
     self.radius = 10


    def displayChar(self,screen):
        pygame.draw.circle(
        screen,
        (176,68,44),
        (self.x,self.y),
         self.radius,
         0)


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
    con1 = Construct(120, 170)
    pit1 = Pit(280, 300)
    char1 = Character()


    # Game initialization
    stop_game = False
    while not stop_game:

    # Event handling
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_W: #UP
                    map1.speedY = 3
                    pit1.speedY = 3
                if event.key == KEY_A: #LEFT
                    map1.speedX = 3
                    pit1.speedX = 3
                if event.key == KEY_S: #DOWN
                    map1.speedY = -3
                    pit1.speedY = -3
                if event.key == KEY_D: #RIGHT
                    map1.speedX = -3
                    pit1.speedX = -3

            if event.type == pygame.KEYUP:
                # deactivate the corresponding speeds
                # when an arrow key is released
                if event.key == KEY_W:
                    map1.speedY = 0
                    pit1.speedy = 0
                elif event.key == KEY_A:
                    map1.speedX = 0
                    pit1.speedX = 0
                elif event.key == KEY_S:
                    map1.speedY = 0
                    pit1.speedY = 0
                elif event.key == KEY_D:
                    map1.speedX = 0
                    pit1.speedX = 0
            if event.type == pygame.QUIT:
                stop_game = True

    # Game logic
        map1.move(char1)
        pit1.move(char1)






    # Game displa
        #(0th layer)
        #create the background for the background screen
        screen.fill(green_color)

        #(1st layer)
        #display the map screen
        map1.displayMap(screen)

        #(2nd layer)
        #create constructs to place on the map


        con1.displayConst(screen)
        pit1.displayPit(screen)

            #call the method responsible for creating the shape

            #create the main character that it looks like you are "controlling"
        char1 = Character()
        char1.displayChar(screen)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
