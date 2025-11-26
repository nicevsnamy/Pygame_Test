from camera import Camera
from screen import Screen

class GameManager:
    def __init__(self,character_list = [],camera: Camera = None, screen: Screen = None):
        self.character_list = character_list
        self.camera = camera
        self.screen = screen
        self.zoom_level = 3
    def add_character(self,character):
        self.character_list.append(character)

    def render_characters(self):
        for character in self.character_list:
            if self.zoom_level == 3:
                self.screen.blit(character.image,self.camera.scale_transform(character.rect[0],character.rect[1]))
            if self.zoom_level == 2:
                self.screen.blit(character.image_small,self.camera.scale_transform(character.rect[0],character.rect[1]))
            if self.zoom_level ==1:
                self.screen.blit(character.image_smallest,self.camera.scale_transform(character.rect[0],character.rect[1]))
        return
    def zoom_out(self):

        # check to see if there is the ability to zoom, if so do the zoom proceedure
        if self.camera.zoom == self.camera.zoom_min:
            return
        else:
            self.camera.set_zoom(-30)
            self.zoom_level -= 1
        print(f'zooming out: {self.camera.zoom} zoom level: {self.zoom_level}')

    def zoom_in(self):
        # check to see if there is the ability to zoom, if so do the zoom proceedure
        if self.camera.zoom == self.camera.zoom_max:
            return
        else:
            self.camera.set_zoom(30)
            self.zoom_level += 1
            
        print(f'zooming in: {self.camera.zoom} zoom level: {self.zoom_level}')