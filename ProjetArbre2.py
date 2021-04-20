import bpy
import sys
import os
import random

x=0
y=0

bpy.ops.curve.primitive_bezier_circle_add(radius=0.5,enter_editmode=False, align='WORLD', location=(0, 5, 10), scale=(1, 1, 1))
bpy.context.object.name = "Ep_branches"

bpy.ops.curve.primitive_bezier_circle_add(enter_editmode=False, align='WORLD', location=(0, 10, 10), scale=(1, 1, 1))


bpy.ops.curve.primitive_bezier_curve_add(radius=10, enter_editmode=False, align='WORLD', location=(0, 0, 10), rotation=(random.randint(0, 30), 90, random.randint(0, 30)))
bpy.context.object.name = "Tronc"
bpy.context.object.data.bevel_object = bpy.data.objects["BezierCircle"]
bpy.context.object.data.bevel_mode = 'OBJECT'
bpy.context.object.data.use_fill_caps = True


bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.object.constraint_add(type='CLAMP_TO')
bpy.context.object.constraints["Clamp To"].target = bpy.data.objects["Tronc"]
bpy.context.object.constraints["Clamp To"].main_axis = 'CLAMPTO_Z'



for i in range(random.randint(15, 30)):
    bpy.ops.curve.primitive_bezier_curve_add(radius=10, enter_editmode=False, align='WORLD', location=(0, 0, 10), rotation=(0, random.randint(0, 180), random.randint(0, 180)))
    bpy.ops.object.constraint_add(type='COPY_LOCATION')
    bpy.context.object.constraints["Copy Location"].target = bpy.data.objects["Empty"]
    bpy.context.object.data.bevel_object = bpy.data.objects["Ep_branches"]
    bpy.context.object.data.bevel_mode = 'OBJECT'
    bpy.context.object.data.use_fill_caps = True
    bpy.context.object.name = x
    
    bpy.ops.object.select_all(action='DESELECT')
    
    full_path_to_file = "/home/tgnsi_nicolas/Documents/BlenderProjet/feuille.obj"
    bpy.ops.import_scene.obj(filepath=full_path_to_file)
    bpy.context.object.name = y
    
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
    bpy.ops.object.modifier_add(type='ARRAY')
    bpy.context.object.modifiers["Array"].count = 4
    bpy.ops.object.modifier_add(type='CURVE')
    bpy.context.object.modifiers["Curve"].object = bpy.data.objects[x]
    x = x+1
    y = y+1
    
    #bpy.ops.object.convert(target='MESH')

bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.join()
bpy.context.object.name = "Branches"

bpy.ops.object.select_all(action='DESELECT')

bpy.ops.object.select_pattern(pattern="Ep_branches")
bpy.ops.object.delete(use_global=False)

