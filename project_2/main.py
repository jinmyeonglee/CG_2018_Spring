import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

count = .0

# draw a cube of side 2, centered at the origin.
def drawCube():
	glBegin(GL_QUADS)
	glVertex3f( 1.0, 1.0,-1.0)
	glVertex3f(-1.0, 1.0,-1.0)
	glVertex3f(-1.0, 1.0, 1.0)
	glVertex3f( 1.0, 1.0, 1.0)
	glVertex3f( 1.0,-1.0, 1.0)
	glVertex3f(-1.0,-1.0, 1.0)
	glVertex3f(-1.0,-1.0,-1.0)
	glVertex3f( 1.0,-1.0,-1.0)
	glVertex3f( 1.0, 1.0, 1.0)
	glVertex3f(-1.0, 1.0, 1.0)
	glVertex3f(-1.0,-1.0, 1.0)
	glVertex3f( 1.0,-1.0, 1.0)
	glVertex3f( 1.0,-1.0,-1.0)
	glVertex3f(-1.0,-1.0,-1.0)
	glVertex3f(-1.0, 1.0,-1.0)
	glVertex3f( 1.0, 1.0,-1.0)
	glVertex3f(-1.0, 1.0, 1.0)
	glVertex3f(-1.0, 1.0,-1.0)
	glVertex3f(-1.0,-1.0,-1.0)
	glVertex3f(-1.0,-1.0, 1.0)
	glVertex3f( 1.0, 1.0,-1.0)
	glVertex3f( 1.0, 1.0, 1.0)
	glVertex3f( 1.0,-1.0, 1.0)
	glVertex3f( 1.0,-1.0,-1.0)
	glEnd()

def drawSphere(numLats=12, numLongs=12):
	for i in range(0, numLats + 1):
		lat0 = np.pi * (-0.5 + float(float(i - 1) / float(numLats)))
		z0 = np.sin(lat0)
		zr0 = np.cos(lat0)
		
		lat1 = np.pi * (-0.5 + float(float(i) / float(numLats)))
		z1 = np.sin(lat1)
		zr1 = np.cos(lat1)
	# Use Quad strips to draw the sphere
		glBegin(GL_QUAD_STRIP)
	
		for j in range(0, numLongs + 1):
			lng = 2 * np.pi * float(float(j - 1) / float(numLongs))
			x = np.cos(lng)
			y = np.sin(lng)
			glVertex3f(x * zr0, y * zr0, z0)
			glVertex3f(x * zr1, y * zr1, z1)
		glEnd()

def drawFrame():
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

def drawFinger(num):
	add = .0
	location = -0.5
	if num == 2:
		add += 20
		location = -0.22
	elif num == 3:
		add += 40
		location = 0.06
	elif num == 4:
		add += 50
		location = 0.34

	glPushMatrix()
	glTranslatef(location, .0, 0)
	glPushMatrix()
	glRotatef((np.sin(np.radians(count + add)) + 1) * 45, 1, 0, 0)
	glTranslatef(.08, 0, 0)

	#draw first red sphere
	glPushMatrix()
	glTranslatef(0, .1, .0)
	glScalef(.1, .1, .1)
	glColor3ub(255, 0, 0)
	drawSphere()
	glPopMatrix()

	# draw first green rectangle
	glPushMatrix()
	glTranslatef(0, .4, 0)
	glScalef(.08, .2, .1)
	# drawFrame()
	glColor3ub(0, 255, 0)
	drawCube()
	glPopMatrix()######

	# draw second sphere
	glPushMatrix()
	glTranslatef(0, .7, 0)
	glScalef(.1, .1, .1)
	glColor3ub(255, 0, 0)
	drawSphere()
	glPopMatrix()

	# save the second rotate matrix
	glPushMatrix()
	glTranslatef(0, .8, 0)
	# drawFrame()
	glRotatef((np.sin(np.radians(count + 10 + add)) + 1) * 45, 1, 0, 0)

	# draw second green rectangle
	glPushMatrix()
	glTranslatef(0, .2, 0)
	glScalef(.08, .2, .1)
	glColor3ub(0, 255, 0)
	drawCube()
	glPopMatrix()

	# draw the third red sphere
	glPushMatrix()
	glTranslatef(0, .5, 0)
	glScalef(.1, .1, .1)
	glColor3ub(255, 0, 0)
	drawSphere()
	glPopMatrix()

	# draw last green rectangle
	glPushMatrix()
	glTranslatef(0, .7, 0)
	glRotatef((np.sin(np.radians(count + 20 + add)) + 1) * 45, 1, 0, 0)
	glPushMatrix()
	glScalef(.08, .1, .1)
	glColor3ub(0, 255, 0)
	drawCube()
	glPopMatrix()
	glPopMatrix()

	glPopMatrix()
	glPopMatrix()
	glPopMatrix()

def render():
	global count
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glEnable(GL_DEPTH_TEST)
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
	glLoadIdentity()
	glOrtho(-1.7,1.7, -1.7,1.7, -1.7,1.7)
	
	gluLookAt(.1*np.sin(np.radians(20)), .1,.1*np.cos(np.radians(20)), 0,0,0, 0,1,0)
	# drawFrame()

	glPushMatrix() # Identity matrix is pushed
	# blue base drawing
	glTranslatef(0, -.5, 0)
	glScalef(.5, .5, .2)
	glColor3ub(0, 0, 255)
	drawCube()
	glPopMatrix()

	# draw thumb
	glPushMatrix()

	glPushMatrix()
	glTranslatef(-.6, -.5, 0)
	glScalef(.1, .1, .1)
	glColor3ub(255, 0, 0)
	drawSphere()
	glPopMatrix()

	glPushMatrix()
	glTranslatef(-.7, -.5, 0)
	glRotatef((np.sin(np.radians(count)) + 1) * 45, 0, 1, 0)
	# drawFrame()

	glPushMatrix() # store rotate matrix
	# draw first green
	glPushMatrix()
	glTranslatef(-.2, 0, 0)
	glScalef(.2, .12, .1)
	glColor3ub(0, 255, 0)
	drawCube()
	glPopMatrix()

	# draw second red
	glPushMatrix()
	glTranslatef(-.5, 0, 0)
	glScalef(.1, .1, .1)
	glColor3ub(255, 0, 0)
	drawSphere()
	glPopMatrix()

	# draw second green
	glPushMatrix()
	glTranslatef(-.6, 0, 0)
	glRotatef((np.sin(np.radians(count + 20)) + 1) * 45, 0, 1, 0)
	# drawFrame()
	glPushMatrix()
	glTranslatef(-.2, 0, 0)
	glScalef(.2, .12, .1)
	glColor3ub(0, 255, 0)
	drawCube()
	glPopMatrix()
	glPopMatrix()


	glPopMatrix()
	glPopMatrix()
	glPopMatrix()

	# draw rest four fingers
	for i in range(4):
		drawFinger(i + 1)

def main():
	global count
	if not glfw.init():
		return
	window = glfw.create_window(720,720,'2016024975', None, None)
	if not window:
		glfw.terminate()
		return
	glfw.make_context_current(window)
	
	while not glfw.window_should_close(window):
		count += 1.5
		glfw.poll_events()
		render()
		glfw.swap_buffers(window)

	glfw.terminate()

if __name__ == "__main__":
   main()