import pygame
from sys import exit
from random import randint
from pygame.locals import *
import math


#   #   #Initialising
pygame.init()
WINDOW_SIZE = (800,800)
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
WINDOW = pygame.Surface((800,800))


CLOCK = pygame.time.Clock()
pygame.display.set_caption("Particle Editor")


#   #   #Variables
radius = 10
direction_x_1 = -4
direction_x_2 = 4
direction_y_1 = -4
direction_y_2 = 4
shrink_rate = 0.2
emission_rate = 50




#Text
FONT =  pygame.font.Font("data/Pixeltype.ttf", 30)
FONT2 =  pygame.font.Font("data/Pixeltype.ttf", 40)

Text_radius = FONT.render("Radius: ", False , (255,255,255))
Text_radius_rect = Text_radius.get_rect(center = (60, 630))

Text_radius_number = FONT2.render(str(radius), False , (255,255,255))
Text_radius_number_rect = Text_radius_number.get_rect(topleft = (142, 619))

Text_direction = FONT.render("Direction: ", False , (255,255,255))
Text_direction_rect = Text_radius.get_rect(center = (60, 670)) # ahhhh wrong rect - will fix if time (works fine without just incorrect)

Text_shrink_rate = FONT.render("Shrink Rate: ", False , (255,255,255))
Text_shrink_rate_rect = Text_shrink_rate.get_rect(center = (390, 630))

Text_shrink_rate_number = FONT2.render(str(shrink_rate), False , (255,255,255))
Text_shrink_rate_number_rect = Text_shrink_rate.get_rect(center = (555, 630))

Text_emission_rate = FONT.render("Emission Rate: ", False , (255,255,255))
Text_emission_rate_rect = Text_emission_rate.get_rect(center = (400, 670))

Text_emission_rate_number = FONT2.render(str(emission_rate), False , (255,255,255))
Text_emission_rate_number_rect = Text_emission_rate.get_rect(center = (580, 670))




#x
Text_direction_x = FONT.render("X: ", False , (255,255,255))
Text_direction_x_rect = Text_radius.get_rect(center = (60, 700)) # ahh wrong rect

Text_direction_x_number_1 = FONT2.render(str(direction_x_1), False , (255,255,255))
Text_direction_x_number_1_rect = Text_direction_x_number_1.get_rect(center = (100, 703))

Text_direction_x_divide = FONT2.render("-", False , (255,255,255))
Text_direction_x_divide_rect = Text_direction_x_divide.get_rect(center = (180, 704))

Text_direction_x_number_2 = FONT2.render(str(direction_x_2), False , (255,255,255))
Text_direction_x_number_2_rect = Text_direction_x_number_2.get_rect(center = (255, 703))

#y
Text_direction_y = FONT.render("Y: ", False , (255,255,255))
Text_direction_y_rect = Text_radius.get_rect(center = (60, 740)) # ahh wrong rect

Text_direction_y_number_1 = FONT2.render(str(direction_y_1), False , (255,255,255))
Text_direction_y_number_1_rect = Text_direction_y_number_1.get_rect(center = (100, 743))

Text_direction_y_divide = FONT2.render("-", False , (255,255,255))
Text_direction_y_divide_rect = Text_direction_y_divide.get_rect(center = (180, 744))

Text_direction_y_number_2 = FONT2.render(str(direction_y_2), False , (255,255,255))
Text_direction_y_number_2_rect = Text_direction_y_number_2.get_rect(center = (255, 743))




#Menu
menubar = pygame.image.load("data/menubar.png").convert_alpha()

subtraction = pygame.image.load("data/subtract.png").convert_alpha()
addition = pygame.image.load("data/addition.png").convert_alpha()

radius_subtract_rect = subtraction.get_rect(topleft = (105, 617))
radius_add_rect = addition.get_rect(topleft = (180, 617))

direction_x_1_subtract_rect = subtraction.get_rect(topleft = (50, 687))
direction_x_1_add_rect = addition.get_rect(topleft = (135, 687))

direction_x_2_subtract_rect = subtraction.get_rect(topleft = (200, 687))
direction_x_2_add_rect = addition.get_rect(topleft = (285, 687))

direction_y_1_subtract_rect = subtraction.get_rect(topleft = (50, 727))
direction_y_1_add_rect = addition.get_rect(topleft = (135, 727))

direction_y_2_subtract_rect = subtraction.get_rect(topleft = (200, 727))
direction_y_2_add_rect = addition.get_rect(topleft = (285, 727))

shrink_rate_subtract_rect = subtraction.get_rect(topleft = (460, 617))
shrink_rate_add_rect = addition.get_rect(topleft = (545, 617))

emission_rate_subtract_rect = subtraction.get_rect(topleft = (470, 655))
emission_rate_add_rect = addition.get_rect(topleft = (575, 655))

white = pygame.image.load("data/white.png").convert_alpha()
aqua = pygame.image.load("data/aqua.png").convert_alpha()

export = pygame.image.load("data/export.png").convert_alpha()
export2 = pygame.image.load("data/export2.png")
export_rect = export.get_rect(topleft = (590, 750))

logo = pygame.image.load("data/logo.png")
pygame.display.set_icon(logo)

#   #   #Functions
def func_export():
    Code = f"""class Particle:
    def __init__(self):
        self.particles = []
    def emit(self): # Moves and draws particles
        if self.particles:
            self.remove_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][1]
                particle[0][0] += particle[2][0]
                particle[1] -= {shrink_rate}
                pygame.draw.circle(WINDOW, (255,255,255), particle[0],int(particle[1]))


    def add_particles(self): #Adds particles
        pos_x = 400
        pos_y = 300
        direction_x = random.randint({direction_x_1},{direction_x_2})
        direction_y = random.randint({direction_y_1},{direction_y_2})


        particle_circle = [[pos_x, pos_y], {radius}, [direction_x, direction_y]]
        self.particles.append(particle_circle)




    def remove_particles(self): #Removes particles*
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy


particle = Particle()

PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, {emission_rate})

"""
    with open('particle.txt', 'w') as f:
        f.write(Code)







#   #   #Classes
class Particle:
    def __init__(self):
        self.particles = []
    def emit(self, shrink_rate): # Moves and draws particles
        if self.particles:
            self.remove_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][1]
                particle[0][0] += particle[2][0]
                particle[1] -= shrink_rate
                pygame.draw.circle(WINDOW, (255,255,255), particle[0],int(particle[1])) #Radius must be int


    def add_particles(self, radius, x1, x2, y1, y2): #Adds particles
        pos_x = 400
        pos_y = 300
        direction_x = randint(x1,x2)
        direction_y = randint(y1,y2)


        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)




    def remove_particles(self): #Removes particles
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy



particle = Particle()

PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, emission_rate)


#Exporting File:

radius = 10
direction_x_1 = -4
direction_x_2 = 4
direction_y_1 = -4
direction_y_2 = 4
shrink_rate = 0.2
emission_rate = 50






#   #   #Main loop

while True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           exit()
        if event.type == MOUSEBUTTONDOWN:
            if radius_subtract_rect.collidepoint(mouse_pos) and radius:
                radius -= 1
                Text_radius_number = FONT2.render(str(radius), False , (255,255,255))
            if radius_add_rect.collidepoint(mouse_pos) and radius < 99:
                radius += 1
                Text_radius_number = FONT2.render(str(radius), False , (255,255,255))

            if direction_x_1_subtract_rect.collidepoint(mouse_pos):
                direction_x_1 -= 1
                Text_direction_x_number_1 = FONT2.render(str(direction_x_1), False , (255,255,255))
            if direction_x_1_add_rect.collidepoint(mouse_pos) and direction_x_1 < direction_x_2:
                direction_x_1 += 1
                Text_direction_x_number_1 = FONT2.render(str(direction_x_1), False , (255,255,255))
            if direction_x_2_subtract_rect.collidepoint(mouse_pos) and direction_x_1 < direction_x_2:
                direction_x_2 -= 1
                Text_direction_x_number_2 = FONT2.render(str(direction_x_2), False , (255,255,255))
            if direction_x_2_add_rect.collidepoint(mouse_pos):
                direction_x_2 += 1
                Text_direction_x_number_2 = FONT2.render(str(direction_x_2), False , (255,255,255))

            if direction_y_1_subtract_rect.collidepoint(mouse_pos):
                direction_y_1 -= 1
                Text_direction_y_number_1 = FONT2.render(str(direction_y_1), False , (255,255,255))
            if direction_y_1_add_rect.collidepoint(mouse_pos) and direction_y_1 < direction_y_2:
                direction_y_1 += 1
                Text_direction_y_number_1 = FONT2.render(str(direction_y_1), False , (255,255,255))
            if direction_y_2_subtract_rect.collidepoint(mouse_pos) and direction_y_1 < direction_y_2:
                direction_y_2 -= 1
                Text_direction_y_number_2 = FONT2.render(str(direction_y_2), False , (255,255,255))
            if direction_y_2_add_rect.collidepoint(mouse_pos):
                direction_y_2 += 1
                Text_direction_y_number_2 = FONT2.render(str(direction_y_2), False , (255,255,255))

            if shrink_rate_add_rect.collidepoint(mouse_pos):
                shrink_rate += .1
                shrink_rate = round(shrink_rate, 1)
                Text_shrink_rate_number = FONT2.render(str(shrink_rate), False , (255,255,255))
                Text_shrink_rate_number = FONT2.render(str(shrink_rate), False , (255,255,255))
            if shrink_rate_subtract_rect.collidepoint(mouse_pos) and shrink_rate > 0:
                shrink_rate -= .1
                shrink_rate = round(shrink_rate, 1)
                Text_shrink_rate_number = FONT2.render(str(shrink_rate), False , (255,255,255))

            if emission_rate_add_rect.collidepoint(mouse_pos):
                if emission_rate < 10:
                    emission_rate += 1
                elif emission_rate < 100:
                    emission_rate += 10
                elif emission_rate >= 100:
                    emission_rate += 100
                pygame.time.set_timer(PARTICLE_EVENT, emission_rate)
                Text_emission_rate_number = FONT2.render(str(emission_rate), False , (255,255,255))
            if emission_rate_subtract_rect.collidepoint(mouse_pos) and emission_rate > 1:
                if emission_rate <= 10:
                    emission_rate -= 1
                elif emission_rate <= 100:
                    emission_rate -= 10
                elif emission_rate > 100:
                    emission_rate -= 100

                pygame.time.set_timer(PARTICLE_EVENT, emission_rate)
                Text_emission_rate_number = FONT2.render(str(emission_rate), False , (255,255,255))
            if export_rect.collidepoint(mouse_pos):
                func_export()






        if event.type == PARTICLE_EVENT:
            particle.add_particles(radius, direction_x_1, direction_x_2, direction_y_1, direction_y_2)






    WINDOW.fill((30,30,30))
    particle.emit(shrink_rate)
    #Menu
    WINDOW.blit(menubar, (0,600))
    WINDOW.blit(subtraction, radius_subtract_rect)
    WINDOW.blit(addition, radius_add_rect)
    WINDOW.blit(subtraction, direction_x_1_subtract_rect)
    WINDOW.blit(addition, direction_x_1_add_rect)
    WINDOW.blit(subtraction, direction_x_2_subtract_rect)
    WINDOW.blit(addition, direction_x_2_add_rect)
    WINDOW.blit(subtraction, direction_y_1_subtract_rect)
    WINDOW.blit(addition, direction_y_1_add_rect)
    WINDOW.blit(subtraction, direction_y_2_subtract_rect)
    WINDOW.blit(addition, direction_y_2_add_rect)
    WINDOW.blit(subtraction, shrink_rate_subtract_rect)
    WINDOW.blit(addition, shrink_rate_add_rect)
    WINDOW.blit(subtraction, emission_rate_subtract_rect)
    WINDOW.blit(addition, emission_rate_add_rect)

    #Text
    WINDOW.blit(Text_radius, Text_radius_rect)
    WINDOW.blit(Text_radius_number, Text_radius_number_rect)

    WINDOW.blit(Text_direction, Text_direction_rect)
    WINDOW.blit(Text_direction_x, Text_direction_x_rect)
    WINDOW.blit(Text_direction_y, Text_direction_y_rect)

    WINDOW.blit(Text_direction_x_number_1, Text_direction_x_number_1_rect)
    WINDOW.blit(Text_direction_x_divide, Text_direction_x_divide_rect)
    WINDOW.blit(Text_direction_x_number_2, Text_direction_x_number_2_rect)
    WINDOW.blit(Text_direction_y_number_1, Text_direction_y_number_1_rect)
    WINDOW.blit(Text_direction_y_divide, Text_direction_y_divide_rect)
    WINDOW.blit(Text_direction_y_number_2, Text_direction_y_number_2_rect)

    WINDOW.blit(Text_shrink_rate, Text_shrink_rate_rect)
    WINDOW.blit(Text_shrink_rate_number, Text_shrink_rate_number_rect)

    WINDOW.blit(Text_emission_rate, Text_emission_rate_rect)
    WINDOW.blit(Text_emission_rate_number, Text_emission_rate_number_rect)

    if export_rect.collidepoint(mouse_pos):
        WINDOW.blit(export2, export_rect)
    else:
        WINDOW.blit(export, export_rect)











    #pygame.draw.polygon(WINDOW, (0, 255, 255), ((0,150),(150,0),(300,150)))






    #Everything is "blitted" onto a seperate surface and then scaled and displayed
    surface = pygame.transform.scale(WINDOW, WINDOW_SIZE)
    SCREEN.blit(surface, (0,0))

    pygame.display.update()
    CLOCK.tick(60)
