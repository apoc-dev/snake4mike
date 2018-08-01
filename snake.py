import pygame
import time
import random

#start lenght
start_leng = 0

#colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


#window size
ww = 300
wh = 300


class app(object):
    
    
    def __init__(self):
        self.ww = ww
        self.wh = wh
        self.on_init()
        self.snake = snake(self.window, self.myfont)
        self.food = food(self.window)
        self.on_exec()

    def on_init(self):
        pygame.init()
        pygame.display.set_caption('snake vs mike')
                
        self.window = pygame.display.set_mode((ww, wh))
        self.gameclock = pygame.time.Clock()

        self.myfont = pygame.font.SysFont("monospace", 15)



    def on_render(self):
        self.window.fill(BLACK)
        self.snake.score()
        self.snake.draw()
        self.food.spawn()

        
    def on_exec(self):
        stopped = False

        #create snake object
        
        print("starting main loop")


        while stopped == False:
            self.window

            #Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                keys_pressed = pygame.key.get_pressed()

                if keys_pressed[pygame.K_ESCAPE]:
                    pygame.quit()
                    quit()
                if keys_pressed[pygame.K_LEFT]:
                    self.snake.move_left()
                if keys_pressed[pygame.K_RIGHT]:
                    self.snake.move_right()
                if keys_pressed[pygame.K_UP]:
                    self.snake.move_up()
                if keys_pressed[pygame.K_DOWN]:
                    self.snake.move_down()

            #render everything
            self.on_render()

            #food logic
            if self.snake.get_pos() == self.food.get_pos():
                self.snake.pop = False
                self.food.food_on_table = False
            
            #Collision Detection - Wall
            if self.snake.get_pos()[0] >= 300 or self.snake.get_pos()[0] < 0 or self.snake.get_pos()[1] >= 300 or self.snake.get_pos()[1] < 0:
                pygame.quit()
                quit()

            #Collision Detection - Snake
            for i in self.snake.parts[1:]:
                if i == self.snake.get_pos():
                    pygame.quit()
                    quit()

            
            #update snake position
            self.snake.move()
            
            pygame.display.flip()
            self.gameclock.tick(15)
            
class snake(object):

    def __init__(self, window, myfont):
        self.window = window
        self.myfont = myfont
        self.block = 10
        self.x = ww/2
        self.y = wh/2

        self.speed = self.block
        self.direc = "up"

        self.leng = start_leng

        self.parts = []
        
        for i in range(0, self.leng):
            self.parts.append((-10,-10))
        self.pop = True
           
    def move(self):
        if self.direc == "up":
            self.y -= self.speed

        elif self.direc == "down":
            self.y += self.speed

        elif self.direc == "left":
            self.x -= self.speed
            
        elif self.direc == "right":
            self.x += self.speed
        return
    
    def get_pos(self):
        self.getx = self.x
        self.gety = self.y
        return self.getx, self.gety

    def get_leng(self):
        self.get_leng = len(self.parts)

        return self.get_leng

    
    def score(self):
        self.get_leng = len(self.parts)
        label = self.myfont.render("Score: {}".format(self.get_leng), 1, (255,255,0))
        self.window.blit(label, (0, 0))

        return
    
    def move_left(self):
        if self.direc != "right":
            self.direc = "left"
        return

    def move_right(self):
        if self.direc != "left":
            self.direc = "right"
        return

    def move_up(self):
        if self.direc != "down":
            self.direc = "up"
        return

    def move_down(self):
        if self.direc != "up":
            self.direc = "down"
        return

    def draw(self):
        #draw the snake and logic behind snake
        self.parts.insert(0, (self.x, self.y))

        for i in range(0, len(self.parts)):
            pygame.draw.rect(self.window, RED, [self.parts[i][0], self.parts[i][1], self.block, self.block])
        if self.pop:
            self.parts.pop()
        else:
            self.pop = True

class food(object):
    def __init__(self, window):
        self.food_on_table = False
        self.window = window
        self.x = 0
        self.y = 0
        
    def spawn(self):
        if not self.food_on_table:
            self.x = random.randrange(0, ww, 10)
            self.y = random.randrange(0, wh, 10)
            self.food_on_table = True

        pygame.draw.rect(self.window, WHITE, [self.x, self.y, 10, 10])
        
    def get_pos(self):
        return self.x, self.y


if __name__ == '__main__':
    app()
