# Example file showing a basic pygame "game loop"
import pygame
from camera import Camera
from screen import Screen
from grid import Grid
from pygame.locals import *
from character import Character
from gameManager import GameManager

# pygame setup
pygame.init()
screen_settings = Screen()
screen = pygame.display.set_mode((screen_settings.get_width(), screen_settings.get_height()))
clock = pygame.time.Clock()

def main():

    running = True
    dt = 0
    camera_scale = 100
    camera = Camera(camera_scale) #passing default zoom value
    game = GameManager([],camera, screen)

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    grid = Grid()

    # add code to preload all characters to list
    meow = Character([0,0],'images/meowscarada.jpg')
    meow.transform(0*grid.get_cell_width(),2*grid.get_cell_height())

    thief = Character([0,0],'images/thief.jpg')

    game.add_character(meow)
    game.add_character(thief)

    # set initial scale for all characters
    for character in game.character_list:
        character.scale(grid.get_cell_width(),grid.get_cell_height())

    # meow.rotate(45)
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == MOUSEWHEEL:
                if(event.y == 1):
                    game.zoom_in() # game manager will know what size of sprites to show based on zoom level
                elif(event.y == -1):
                    game.zoom_out() # game manager will know what size of sprites to show based on zoom level
                    # meow.scale(grid.get_cell_width()*camera.get_zoom_percentage(),grid.get_cell_width()*camera.get_zoom_percentage())
                # can access properties with
                # proper notation(ex: event.y)
            elif event.type == MOUSEBUTTONDOWN:
                # need to add code later to see if clicking on a UI or game object. If selecting one of these do not enter pan mode
                camera.set_pan_mode(True)
            elif event.type == MOUSEBUTTONUP:
                camera.set_pan_mode(False)
            elif event.type == MOUSEMOTION:
                if camera.get_pan_mode() == True:
                    # take the relative change from the event and update camera position
                    camera.change_pos(event.rel[0] * camera.get_scroll_speed(), event.rel[1] * camera.get_scroll_speed())

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE

        # render the player grid
        for vert_line in range(grid.get_width()+1):
            pygame.draw.line(screen, "green",(camera.scale_transform(vert_line*grid.get_cell_width(),0)),(camera.scale_transform(vert_line*grid.get_cell_width(),grid.get_height()*grid.get_cell_height())),grid.get_thickness())
        for horz_line in range(grid.get_height()+1):
            pygame.draw.line(screen, "green",(camera.scale_transform(0,horz_line*grid.get_cell_height())),(camera.scale_transform(grid.get_width()*grid.get_cell_width(),horz_line*grid.get_cell_height())),grid.get_thickness())
        #pygame.draw.rect(screen, "blue",(200,200,400,400),300)
        pygame.draw.circle(screen, "red", camera.scale_transform(player_pos.x, player_pos.y), (40*camera.get_zoom_percentage()))

        # render all the background elements

        # render all characters on screen
        game.render_characters()
        # render the UI

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt * camera.get_zoom_percentage()
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt * camera.get_zoom_percentage()
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt * camera.get_zoom_percentage()
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt * camera.get_zoom_percentage()

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()
    
# Execute game:
if __name__=='__main__':
    main()