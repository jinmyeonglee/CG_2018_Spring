import glfw
import numpy as np
from OpenGL.GL import *

primitive = GL_LINE_LOOP

def draw_shape():
    global primitive
    a = np.arange(0, 360, 30)
    x = np.cos(np.deg2rad(a))
    y = np.sin(np.deg2rad(a))
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(primitive)
    for i in range(12):
        glVertex2f(x[i], y[i])
    glEnd()

def key_callback(window, key, scancode, action, mods):
    global primitive
    if key >= glfw.KEY_0 and key <= glfw.KEY_9:
        if action == glfw.PRESS:
            primitive = {
                1: GL_POINTS,
                2: GL_LINES,
                3: GL_LINE_STRIP,
                4: GL_LINE_LOOP,
                5: GL_TRIANGLES,
                6: GL_TRIANGLE_STRIP,
                7: GL_TRIANGLE_FAN,
                8: GL_QUADS,
                9: GL_QUAD_STRIP,
                0: GL_POLYGON,
            }[key - 48]

def main():
   #Initialize the library
   if not glfw.init():
      return
   #Create a windowed mode window and its OpenGL context
   window = glfw.create_window(480,480,"Hello World",None,None)
   if not window:
      glfw.terminate()
      return
   #Make the window's context current
   glfw.set_key_callback(window, key_callback)
   glfw.make_context_current(window)

   #Loop until the user closes the window
   while not glfw.window_should_close(window):
      #Poll events
      glfw.poll_events()

      #Render here, e.g. using pyOpenGL
      draw_shape()

      #Swap front and back buffers
      glfw.swap_buffers(window)

   glfw.terminate()

if __name__ == "__main__":
   main()
