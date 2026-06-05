Web VPython 3.2
import random

a = box(pos = vec(0,1,0),size = vec(3,0.1,1))
b = box(pos = vec(1.5,-0.45,0),size = vec(0.1,3,1))
c = box(pos = vec(-1.5,-0.45,0),size = vec(0.1,3,1))
d = box(pos = vec(0,-1,0),size = vec(3,0.1,1))
e = box(pos = vec(0,-0.05,0),size = vec(3,0.1,1))
f = box(pos = vec(0,-1.89,0),size = vec(3,0.1,1))

text(text='book shelf', align='center',pos = vec(0,1.7,0),height = 1,axis = vec(1,0,0))
text(text='book truck', align='center',pos = vec(6,7,4),height = 1,axis = vec(1,0,0))
# text(text='Wonder', align='center',pos = vec(6,7,4),height = 1,axis = vec(0,1,0))
randomlist = [1,2,3]
random.shuffle(randomlist)

r = box(pos = vec(5,6.5,6),size = vec(0.7,0.9,0.7))
rp = box(pos = vec(5,6.5,6),size = vec(0.7,0.9,0.7),opacity = 0.5)
v = box(pos = vec(6,6.5,6),size = vec(0.7,0.9,0.7))
vp = box(pos = vec(6,6.5,6),size = vec(0.7,0.9,0.7),opacity = 0.5)
o = box(pos = vec(7,6.5,6),size = vec(0.7,0.9,0.7))
op = box(pos = vec(7,6.5,6),size = vec(0.7,0.9,0.7),opacity = 0.5)
gp = box(pos = vec(-1,0.5,0),size = vec(0.7,0.9,0.7),opacity = 0.5)
ip = box(pos = vec(0,0.5,0),size = vec(0.7,0.9,0.7),opacity = 0.5)
np = box(pos = vec(1,0.5,0),size = vec(0.7,0.9,0.7),opacity = 0.5)
tp = box(pos = vec(-2,0.5,0),size = vec(0.7,0.9,0.7),opacity = 0.5)


boxes=[r,v,o]

m = randomlist[0]
p = randomlist[1]
l = randomlist[2]

if l == 1:
    r.color = color.cyan
if p == 1:
    v.color = color.cyan
if m == 1:
    o.color = color.cyan


ix = 0
    



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

while True :
    rate(100)
    k = keysdown()
    if 'd' in k :
        o.pos.x = o.pos.x + 0.1
        #boxes[ix].pos.x = boxes[ix].pos.x + 0.1
    if 'a' in k :
        o.pos.x = o.pos.x - 0.1
    if 'w' in k :
        o.pos.y = o.pos.y + 0.1
    if 's' in k :
        o.pos.y = o.pos.y - 0.1
    if 'q' in k : 
        o.pos.z = o.pos.z + 0.1
    if 'e' in k : 
        o.pos.z = o.pos.z - 0.1
#    if ' ' in k :
        rate(10)
        ix = (ix + 1) % 3
    if mag(r.pos - gp.pos) < 1 : 
        r.color = color.red
        rp.color = color.green
    if mag(v.pos - ip.pos) < 1 : 
        v.color = color.red
        vp.color = color.green
    if mag(o.pos - np.pos) < 1 : 
        o.color = color.red
        op.color = color.green
        
        
