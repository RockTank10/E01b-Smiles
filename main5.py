#!/usr/bin/env python3

import utils, open_color, arcade #gets all outside sources needed

utils.check_version((3,7))  #makes sure you are on the right python version

SCREEN_WIDTH = 800  #sets the width
SCREEN_HEIGHT = 600 #sets the height
SCREEN_TITLE = "Smiley Face Example"    #names the screen

class Faces(arcade.Window): #makes the class
    """ Our custom Window Class"""  #gives class description

    def __init__(self): #sets up the class
        """ Initializer """ 
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)#calls for information outside the class

        # Show the mouse cursor
        self.set_mouse_visible(True)#lets you see mouse curser

        self.x = SCREEN_WIDTH / 2   #sets x to half the screen width
        self.y = SCREEN_HEIGHT / 2  #sets y to half the screen height

        arcade.set_background_color(open_color.white)   #makes background white

    def on_draw(self): #defines the face
        """ Draw the face """ #says what it does
        arcade.start_render()   #starts the render
        face_x,face_y = (self.x,self.y) #centers face
        smile_x,smile_y = (face_x + 0,face_y - 10)  #sets smile
        eye1_x,eye1_y = (face_x - 30,face_y + 20)   #sets eye1
        eye2_x,eye2_y = (face_x + 30,face_y + 20)   #sets eye2
        catch1_x,catch1_y = (face_x - 25,face_y + 25)   #sets pupil1
        catch2_x,catch2_y = (face_x + 35,face_y + 25)   #sets pupil2

        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3)#draws face
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4)#draws outline of face
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black)#draws eye1
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black)#draws eye2
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2)#draws pupil1
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2)#draws pupil2
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4)#draws smile


    def on_mouse_motion(self, x, y, dx, dy):#defines what happens when there is mouse movement
        """ Handle Mouse Motion """#says what it does
        self.x = x#sets x to x
        self.y = y#sets y to y



window = Faces()#opens window
arcade.run()#has arcade run