Web VPython 3.2
a = box(pos = vec(0,1,0),size = vec(3,0.1,1))
b = box(pos = vec(1.5,-0.45,0),size = vec(0.1,3,1))
c = box(pos = vec(-1.5,-0.45,0),size = vec(0.1,3,1))
d = box(pos = vec(0,-1,0),size = vec(3,0.1,1))
e = box(pos = vec(0,-0.05,0),size = vec(3,0.1,1))
f = box(pos = vec(0,-1.89,0),size = vec(3,0.1,1))
text(text='Wonder', align='center',pos = vec(0,2,0),height = 0.5,axis = vec(1,0,0))
t = box(pos = vec(-2,0.5,0),size = vec(0.7,0.9,0.7))
stack = compound([a,b,c,d,e,f])
stack.axis = vec(1,0,0)
stack.pos.x = stack.pos.x + 6
stack.pos.y = stack.pos.y + 6
stack.pos.z = stack.pos.z + 6

box(pos = vec(0,1,0),size = vec(5,0.1,1))
box(pos = vec(2.5,-0.45,0),size = vec(0.1,3,1))
box(pos = vec(-2.5,-0.45,0),size = vec(0.1,3,1))
box(pos = vec(0,-1,0),size = vec(5,0.1,1))
box(pos = vec(0,-0.05,0),size = vec(5,0.1,1))
box(pos = vec(0,-1.89,0),size = vec(5,0.1,1))
