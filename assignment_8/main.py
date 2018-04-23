from OpenGL.GLU import *
from OpenGL.GL import *
import numpy as np
import glfw

camAng = 0
gComposedM = np.array([[1.,0.,0.,0.],
                       [0.,1.,0.,0.],
                       [0.,0.,1.,0.],
                       [0.,0.,0.,1.]])

def render(camAng):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    glOrtho(-1,1, -1,1, -1,1)

    gluLookAt(.1*np.sin(camAng),.1,.1*np.cos(camAng), 0,0,0, 0,1,0)

    # draw coordinates
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([1.,0.,0.]))
    glColor3ub(0, 255, 0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([0.,1.,0.]))
    glColor3ub(0, 0, 255)
    glVertex3fv(np.array([0.,0.,0]))
    glVertex3fv(np.array([0.,0.,1.]))
    glEnd()
    ##############################
    # edit here
    glColor3ub(255, 255, 255)
    glMultMatrixf(gComposedM.T)
    drawTriangle()

def drawTriangle():
    glBegin(GL_TRIANGLES)
    glVertex3fv(np.array([.0,.5,0.]))
    glVertex3fv(np.array([.0,.0,0.]))
    glVertex3fv(np.array([.5,.0,0.]))
    glEnd()

def key_callback(window, key, scancode, action, mods):
    global camAng
    global gComposedM
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_1:
            camAng = np.radians(-10) + camAng
        elif key == glfw.KEY_3:
            camAng = np.radians(10) + camAng
        elif key == glfw.KEY_Q:
            gComposedM = gComposedM @ np.array([[1.,0.,0.,-0.1],
                                             [0.,1.,0.,0.],
                                             [0.,0.,1.,0.],
                                             [0.,0.,0.,1.]])
        elif key == glfw.KEY_E:
            gComposedM = gComposedM @ np.array([[1.,0.,0.,0.1],
                                             [0.,1.,0.,0.],
                                             [0.,0.,1.,0.],
                                             [0.,0.,0.,1.]])
        elif key == glfw.KEY_A:
            th = np.radians(-10)
            gComposedM = gComposedM @ np.array([[np.cos(th),0.,np.sin(th), 0.],
                                             [0.,1.,0.,0.],
                                             [-np.sin(th),0.,np.cos(th), 0.],
                                             [0.,0.,0.,1.]])
        elif key == glfw.KEY_D:
            th = np.radians(10)
            gComposedM = gComposedM @ np.array([[np.cos(th),0.,np.sin(th), 0.],
                                             [0.,1.,0.,0.],
                                             [-np.sin(th),0.,np.cos(th), 0.],
                                             [0.,0.,0.,1.]])
        elif key == glfw.KEY_W:
            th = np.radians(-10)
            gComposedM = gComposedM @ np.array([[1.,0.,0.,0.],
                                             [0.,np.cos(th),-np.sin(th),0.],
                                             [0.,np.sin(th),np.cos(th),0.],
                                             [0.,0.,0.,1.]]) 
        elif key == glfw.KEY_S:
            th = np.radians(10)
            gComposedM = gComposedM @ np.array([[1.,0.,0.,0.],
                                             [0.,np.cos(th),-np.sin(th),0.],
                                             [0.,np.sin(th),np.cos(th),0.],
                                             [0.,0.,0.,1.]])

def main():
    global camAng
    if not glfw.init():
        return
    window = glfw.create_window(480,480,"2016024975", None,None)
    if not window:
        glfw.terminate()
        return
    glfw.set_key_callback(window, key_callback)
    glfw.make_context_current(window)
    glfw.swap_interval(1)
    while not glfw.window_should_close(window):
        glfw.poll_events()

        render(camAng)

        glfw.swap_buffers(window)
    glfw.terminate()


if __name__ == "__main__":
    main()
