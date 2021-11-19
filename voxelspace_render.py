import math
import turtle

render_distance = 100
fov = 90
#The FOV of the camera. This, because of mathematical constraints involving triangles, can never be 180 or larger.
#The larger the FOV, the larger the 'x_base_distance' will be with the same render distance.
#
#Also, combinding a large FOV with a large render distance may result in unexpected behaviour, or graphical anomalies.
#This is because the calculated base distance of the horizontal virtual triangle may exceed the window's vertical pixel count, forcing multiple lines into the space of a single one. Therefore, resulting in unpredictable results.

window_x = 0 #window_x and window_y are placeholder variables for what will in future be the window dimensions in pixels.
window_y = 0

z_axis = [] #This will be used to allow for drawing lines from the front of the screen to the back.

try:
    aspect_ratio = (window_x / window_y) #The aspect ratio of the screen, calculated by dividing the horizontal resolution by the vertical resolution. This is redundant, and is never used.
except ZeroDivisionError:
    aspect_ratio = 0

pos = [0, 0, 0] #The player/camera position.

camera_rotation = 0

x_base_distance = ((math.tan(math.radians(fov / 2)) * render_distance) * 2) #Calculates the length of the base of the virtual triangle that is constructed when getting pixels.

try:
    y_base_distance = (window_y / window_x) * x_base_distance #Uses a (hopefully) clever trick with the aspect ratio of the screen to possibly save some time and maths in order to calculate the same number as above, but for the vertical, "side view", triangle base length.
except ZeroDivisionError:
    y_base_distance = 0

background_colour = [0.53, 0.603, 0.776] #Due to the way the turtle library works, the background colour is split up into 3 values of red, green, and blue, each ranging from 0 to 1.

def window_init():
    screen = turtle.Screen()
    screen.bgcolor(background_colour)

    linedraw = turtle.Turtle()
    linedraw.hideturtle()
    linedraw.pensize(1)

def draw_vertical_line(height, y_axis):
    linedraw.penup()

    linedraw.goto(-(window_y / 2), (-(window_x / 2) + y_axis))
    linedraw.pendown()
    linedraw.goto((-(window_y / 2) + height), (-(window_x / 2) + y_axis))

def render_frame():
    window_x = screen.window_width()
    window_y = screen.window_height()

    linedraw.clear()

    try:
        aspect_ratio = (window_x / window_y)
    except ZeroDivisionError:
        print("An error has occurred, as a window has most likely not been created. Make sure that you did not close any windows that may have appeared, as that may be the cause of the issue. Otherwise, report this as a bug.")
        print("ERROR: 'window_x' and/or 'window_y' are empty.")

    x_base_distance = ((math.tan(radians(fov / 2)) * render_distance) * 2) #Calculates the length of the base of the virtual triangle that is constructed when getting pixels.

    y_base_distance = (window_y / window_x) * x_base_distance #Uses a (hopefully) clever trick with the aspect ratio of the screen to possibly save some time and maths in order to calculate the same number as above, but for the vertical, "side view", triangle base length.


    rotated_points = [(0, 0), (0, 0)]

    z_axis = [] #Clears the Z buffer

    for loop in range(window_x): #Creates the correct number of spaces within the Z buffer. This makes things easier later on, as you can't directly add to or change a position in a list that isn't already occupied.
        z_axis.append(0)

    for y in range(render_distance): #Runs for every horizontal line between the camera/player and the furthest point away from them which they can see.
        rotated_points[0][0] = (math.cos(math.radians(camera_rotation)) * (((x_base_distance / render_distance) * (y + 1)) - (((x_base_distance / render_distance) * (y + 1)) / 2))) - (math.sin(math.radians(camera_rotation)) * (y + 1)) #This line records the X co-ordinate of the starting position of the rendering line, after rotating.
        rotated_points[0][1] = (math.sin(math.radians(camera_rotation)) * (((x_base_distance / render_distance) * (y + 1)) - (((x_base_distance / render_distance) * (y + 1)) / 2))) + (math.cos(math.radians(camera_rotation)) * (y + 1)) #This line records the Y co-ordinate of the starting position of the rendering line, after rotating.

        rotated_points[1][0] = (math.cos(math.radians(camera_rotation)) * (((x_base_distance / render_distance) * (y+1)) / 2)) - (math.sin(math.radians(camera_rotation)) * (y + 1)) #This line records the X co-ordinate of the ending position of the rendering line, after rotating.
        rotated_points[1][0] = (math.sin(math.radians(camera_rotation)) * (((x_base_distance / render_distance) * (y+1)) / 2)) + (math.cos(math.radians(camera_rotation)) * (y + 1)) #This line records the Y co-ordinate of the ending position of the rendering line, after rotating.
        for x in range((x_base_distance / render_distance) * (y+1)): #Runs for every pixel that should be checked between the edges of each horizontal line.
            #for loop1 in range(math.ceil((x_base_distance / render_distance) * (y+1))): Temporary placeholder code until I can implement proper functions for getting pixels and drawing lines on the screen.

            get_point((pos[0] + (rotated_points[0][0] + ((rotated_points[0][0] - rotated_points[1][0]) * x))), (pos[2] + (rotated_points[0][1] + ((rotated_points[0][1] - rotated_points[1][1]) * x)))) #Gets the point on the heightmap/colourmap corresponding to the current rendering point.



            pos[0] + (x - ((x_base_distance / render_distance) * (y+1) / 2)) #This will return the point that would be on the left side of the screen, relative to the camera/player position.
            pos[2] + (y + 1) #This returns the Y axis at which the line should be on, relative to the player position.

            pos[0] + (x + ((x_base_distance / render_distance) * (y+1) / 2)) #This line and the line below it are irrelevant, given that I have used loops. I am leaving them here simply because I cannot be bothered to remove them.
            pos[2] + (y + 1)




# OBJECTIVES
#
# - Complete Z-buffer implementation.
# - Trial using turtle to display frames to ensure that the turtle is not too slow to be used as the line renderer.
# - Ensure appropriate behavior based on screen resolution, so line rendering can be ensured to cover the whole screen.
# - Test the goddamn thing.
