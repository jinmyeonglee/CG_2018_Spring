import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

gComposedM = np.array([[1.,0.],
                       [0.,1.]])

def render(T):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    # draw cooridnate
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0, 255, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()
    # draw triangle
    glBegin(GL_TRIANGLES)
    glColor3ub(255, 255, 255)
    glVertex2fv(T @ np.array([0.0,0.5]))
    glVertex2fv(T @ np.array([0.0,0.0]))
    glVertex2fv(T @ np.array([0.5,0.0]))
    glEnd()

def key_callback(window, key, scancode, action, mods):
    global gComposedM
    if key == glfw.KEY_1:
        gComposedM = np.array([[1.,0.],
                               [0.,1.]])
    elif key == glfw.KEY_W:
        gComposedM = np.array([[.9,0.],
                               [0,1.]]) @ gComposedM
    elif key == glfw.KEY_E:
        gComposedM = np.array([[1.1,0.],
                               [0,1.]]) @ gComposedM
    elif key == glfw.KEY_S:
        th = np.radians(10)
        gComposedM = np.array([[np.cos(th), -np.sin(th)],
                               [np.sin(th), np.cos(th)]]) @ gComposedM
    elif key == glfw.KEY_D:
        th = np.radians(-10)
        gComposedM = np.array([[np.cos(th), -np.sin(th)],
                               [np.sin(th), np.cos(th)]]) @ gComposedM
    elif key == glfw.KEY_X:
        gComposedM = np.array([[1.,-0.1],
                               [0.,1.]]) @ gComposedM
    elif key == glfw.KEY_C:
        gComposedM = np.array([[1.,0.1],
                               [0.,1.]]) @ gComposedM
    elif key == glfw.KEY_R:
        gComposedM = np.array([[1.,0.],
                               [0.,-1.]]) @ gComposedM


def main():
    global gComposedM
    if not glfw.init():
        return
    window = glfw.create_window(480,480,"2016024975", None,None)
    if not window:
        glfw.terminate()
        return
    glfw.set_key_callback(window, key_callback)
    glfw.make_context_current(window)
    glfw.swap_interval(1)
    count = 0
    while not glfw.window_should_close(window):
        glfw.poll_events()
        #sx = (count % 10) * .1
        #sy = sx * 2
        #th = np.radians(count % 360)
        #T = np.array([[np.cos(th), -np.sin(th)],
        #               [np.sin(th),  np.cos(th)]])
        #T = np.array([[sx, 0.],
        #              [0., sy]])
        #a = (count % 10) * .2
        #T = np.array([[-1.,a],
        #              [0.,1.]])
        #render(T)
        #count += 1

        render(gComposedM)
        glfw.swap_buffers(window)
    glfw.terminate()
if __name__ == "__main__":
    main()
