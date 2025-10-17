class Camera:
    def __init__(self, zoom):
        self.zoom = zoom
        self.zoom_min = 20
        self.zoom_max = 500
        self.pan_mode = False
        self.x = 0
        self.y = 0
        self.scroll_speed = 0.5

    def apply_transform(self,x,y):
        return (x+self.x, y+self.y)
    def scale_transform(self,x,y):
        return(x*self.zoom/100+self.x,y*self.zoom/100+self.y)
    def change_pos(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
    def set_x(self, x_pos):
        self.x = x_pos
    def change_x(self, delta_x):
        self.x += delta_x
    def set_y(self, y_pos):
        self.y = y_pos
    def change_y(self, delta_y):
        self.y += delta_y
    def get_pos(self):
        return (self.x,self.y)
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

    def set_zoom(self,zoom_modifier):
        temp_zoom = self.zoom
        temp_zoom += zoom_modifier
        round(temp_zoom,2)

        # discard the zoom valule if it bring it out of the zoom limits
        if(temp_zoom >= self.zoom_min and temp_zoom <= self.zoom_max):
            self.zoom = temp_zoom

    def get_zoom(self):
        return self.zoom
    
    def get_zoom_percentage(self):
        return (self.zoom / 100)
    
    def set_pan_mode(self,value):
        self.pan_mode = value

    def get_pan_mode(self):
        return self.pan_mode
    
    def set_scroll_speed(self, speed):
        self.scroll_speed = speed
    def get_scroll_speed(self):
        return self.scroll_speed