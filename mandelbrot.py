import pygame
from pygame import gfxdraw
from sys import exit
import datetime

def mandelbrot(eltolX, eltoly, max_iteration, magnification):

    for i in range(int(-eltolX), int(xSize - eltolX)):
        for j in range(int(-eltoly), int(ySize - eltoly)):
            iteration = 0
            x = 0
            y = 0
            while x * x + y * y <= 4 and iteration < max_iteration:
                #
                temp = x * x - y * y + i / magnification
                y = 2 * x * y + j / magnification
                x = temp

                iteration = iteration + 1

            if iteration != 1:
                pygame.gfxdraw.pixel(screen, i + eltolX, j + eltoly, (int(iteration * 25000 % 255), int(iteration * 1000 % 255), 0))

        percent = (100/xSize) * (i + 1 + eltolX)
        percent = round(percent,2)
        if percent == 12.5 or percent == 25.0 or percent == 37.5 or percent == 50.0 or percent == 67.5 or percent == 75.0 or percent == 87.5 or percent == 100.0:
            pygame.display.update()
        print(str(i + 1 + eltolX) + " out of " + str(xSize) + " (" + str(percent) + "%)")

    pygame.display.flip()
    pygame.display.update()
    print("done")

pygame.init()

xSize = 1000
ySize = 1000
screen = pygame.display.set_mode((xSize, ySize))

screen.fill((255, 255, 255))
pygame.display.update()

max_iteration = 10
magnification = 101

eltolX=0
eltoly=0


mandelbrot(eltolX, eltoly, max_iteration, magnification)

while True:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                eltoly = eltoly - 100
                mandelbrot(eltolX, eltoly, max_iteration, magnification)

            if event.key == pygame.K_DOWN:
                eltoly = eltoly + 100
                mandelbrot(eltolX, eltoly, max_iteration, magnification)

            if event.key == pygame.K_LEFT:
                eltolX = eltolX - 100
                mandelbrot(eltolX, eltoly, max_iteration, magnification)

            if event.key == pygame.K_RIGHT:
                eltolX = eltolX + 100
                mandelbrot(eltolX, eltoly, max_iteration, magnification)

            if event.key == pygame.K_KP_PLUS:
                magnification = magnification + 50
                mandelbrot(eltolX, eltoly, max_iteration, magnification)

            if event.key == pygame.K_KP_MINUS:
                magnification = magnification - 50
                mandelbrot(eltolX, eltoly, max_iteration, magnification)

            if event.key == pygame.K_KP_MULTIPLY:
                max_iteration = max_iteration + 100
                mandelbrot(eltolX, eltoly, max_iteration, magnification)

            if event.key == pygame.K_KP_DIVIDE:
                max_iteration = max_iteration - 100
                mandelbrot(eltolX, eltoly, max_iteration, magnification)

            if event.key == pygame.K_SPACE:
                now = datetime.datetime.now()
                pygame.image.save(screen, str(now.hour) + str(now.minute) + "mandelbrot.png")

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
quit()
