import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self,location,path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.image_small = pygame.transform.scale(self.image, (70,70))
        self.image_smallest = pygame.transform.scale(self.image, (40,40))
    
    def flip (self, y=False,x=False):
        self.image = pygame.transform.flip(self.image,y,x)
    
    def scale(self,x,y):
        self.image = pygame.transform.scale(self.image, (x,y))
    
    def rotate(self,angle):
        self.image = pygame.transform.rotate(self.image,angle)

    def transform(self,xPos,yPos):
        self.rect.left = xPos
        self.rect.top = yPos