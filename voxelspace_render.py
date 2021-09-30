import math

render_distance = 100
fov = 90 #The FOV of the camera. This, because of mathematical constraints involving triangles, can never be 180 or larger. Also, combinding a large FOV with a large render distance may result in unexpected behaviour, or graphical anomalies. This is because the calculated base distance of the horizontal virtual triangle may exceed the window's vertical pixel count, forcing multiple lines into the space of a single one. Therefore, resulting in unpredictable results.

window_x = 0 #window_x and window_y are placeholder variables for what will in future be the window dimensions in pixels.
window_y = 0

z_axis = [] #This will be used to allow for drawing lines from the front of the screen to the back.

aspect_ratio = (window_x / window_y) #The aspect ratio of the screen, calculated by dividing the horizontal resolution by the vertical resolution. This is redundant, and is never used.

pos = [0, 0, 0] #The player/camera position.

camera_rotation = 0

x_base_distance = ((math.tan(radians(fov / 2)) * render_distance) * 2) #Calculates the length of the base of the virtual triangle that is constructed when getting pixels.

y_base_distance = (window_y / window_x) * x_base_distance #Uses a (hopefully) clever trick with the aspect ratio of the screen to possibly save some time and maths in order to calculate the same number as above, but for the vertical, "side view", triangle base length.

def render_frame():

    rotated_points = [(0, 0), (0, 0)]

    z_axis = [] #Clears the Z buffer

    for loop in range(window_x): #Creates the correct number of spaces within the Z buffer. This makes things easier later on, as you can't directly add to or change a position in a list that isn't already occupied.
        z_axis.append(0)

    for y in range(render_distance): #Runs for every horizontal line between the camera/player and the furthest point away from them which they can see.
        rotated_points[0][0] = (math.cos(math.radians(camera_rotation)) * (((x_base_distance / render_distance) * (y + 1)) - (((x_base_distance / render_distance) * (y + 1)) / 2))) - (math.sin(math.radians(camera_rotation)) * (y + 1))
        rotated_points[0][1] = (math.sin(math.radians(camera_rotation)) * (((x_base_distance / render_distance) * (y + 1)) - (((x_base_distance / render_distance) * (y + 1)) / 2))) + (math.cos(math.radians(camera_rotation)) * (y + 1))

        rotated_points[1][0] = (math.cos(math.radians(camera_rotation)) * (((x_base_distance / render_distance) * (y+1)) / 2)) - (math.sin(math.radians(camera_rotation)) * (y + 1))
        rotated_points[1][0] = (math.sin(math.radians(camera_rotation)) * (((x_base_distance / render_distance) * (y+1)) / 2)) + (math.cos(math.radians(camera_rotation)) * (y + 1))
        for x in range((x_base_distance / render_distance) * (y+1)): #Runs for every pixel that should be checked between the edges of each horizontal line.
            get_point((pos[0] + (rotated_points[0][0] + ((rotated_points[0][0] - rotated_points[1][0]) * x))), (pos[2] + (rotated_points[0][1] + ((rotated_points[0][1] - rotated_points[1][1]) * x))

            pos[0] + (x - ((x_base_distance / render_distance) * (y+1) / 2)) #This will return the point that would be on the left side of the screen, relative to the camera/player position.
            pos[2] + (y + 1) #This returns the Y axis at which the line should be on, relative to the player position.

            pos[0] + (x + ((x_base_distance / render_distance) * (y+1) / 2)) #This line and the line below it are irrelevant, given that I have used loops. I am leaving them here simply because I cannot be bothered to remove them.
            pos[2] + (y + 1)




# OBJECTIVES FOR TOMORROW
#
# - Either:
# - - Have the line counting start at the back, instead of starting at the front. This would be easier and less complex to program for, but may be an inefficient method later on. This method is less flexible, but easier to understand and program for.
# - OR
# - - Implement a Z-axis of sorts. This method, although it would be complicated, has the possibility to be more efficient than the above method. It is also more flexible.
#
# - Implement view turning.
#
# - Test the goddamn thing
