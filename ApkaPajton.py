import pygame as pg
import time



def main():

    pg.init()
    pg.display.set_caption("Apka Pajton")

    screen = pg.display.set_mode((1920,180))

    running = True

    y = 50

    w = pg.image.load("kliknij w mordo.png")
    player = pg.image.load("szczała.png")

    screen.fill((100,100,100))
    screen.blit(w, (50,3))
    pg.display.flip()

    time.sleep(3)

    def play(y):
        screen.fill((100,100,100))
        screen.blit(player, (50,y))
        pg.display.flip()

    play(100)

    while running:

        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                   play(50)
                   time.sleep(1)
                   play(100)
                   time.sleep(1)



if __name__=="__main__":
    main()