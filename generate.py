import bpy
from bpy import data as D
from bpy import context as C
from mathutils import *
from math import *

fp = "/home/ramon/projects/LegoBrickClassification/ldraw/parts/9.dat"
ldrawpath = "/home/ramon/projects/LegoBrickClassification/ldraw/"
imagepath = "/home/ramon/projects/LegoBrickClassification/test.png"

pby.object.delete(bpy.data.objects)

#TODO remove white square element
#add white background to the scene
bpy.ops.mesh.primitive_plane_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0))



bpy.ops.import_scene.importldraw(filepath=fp, ldrawPath=ldrawpath)
bpy.context.scene.render.filepath = "/home/ramon/projects/LegoBrickClassification/"

for scene in bpy.data.scenes:
    scene.render.resolution_x = 160
    scene.render.resolution_y = 160
    scene.render.resolution_percentage = 70
    scene.render.use_border = False

im_i = 0
scene.render.image_settings.file_format = "PNG"

import math


for euler_x in range(0, 4):
    for euler_y in range(0,1):
        for euler_z in range(0,1):
            bpy.context.scene.render.filepath = "/home/ramon/projects/LegoBrickClassification/test" + str(im_i) + ".png"
            bpy.context.active_object.rotation_euler[0] = math.radians(euler_x * 45)
            bpy.context.active_object.rotation_euler[1] = math.radians(euler_y * 45)
            bpy.context.active_object.rotation_euler[2] = math.radians(euler_z * 45)
            bpy.ops.render.render(write_still=True)
            im_i += 1

