import bpy
import sys
import os
import random

i = 0
x= 0
graphe = []
graphe.append(bpy.ops.curve.primitive_bezier_curve_add(radius=10, enter_editmode=False, align='WORLD', location=(0, 0, 0), rotation=(random.randint(0, 30), 90, random.randint(0, 30))))
for i in range(random.randint(5, 15)):
    graphe.append(bpy.ops.curve.primitive_bezier_curve_add(radius=10, enter_editmode=False, align='WORLD', location=(0, 0, 10), rotation=(0, random.randint(0, 180), random.randint(0, 180))))
    x += 2
bpy.ops.object.parent_set(type='OBJECT')
