import bpy
import math
def removeexistingobjects():
    check = bpy.data.objects is not None
    # remove pre-existing objects from blender
    if check == True:
        for object in bpy.data.objects:
            object.select = True
            bpy.ops.object.delete()
            # clear mesh and material data. removing objects alone is not necessary
            for mesh in bpy.data.meshes:
                bpy.data.meshes.remove(mesh, do_unlink=True)
            for material in bpy.data.materials:
                bpy.data.materials.remove(material, do_unlink=True)
            for camera in bpy.data.cameras:
                bpy.data.cameras.remove(camera, do_unlink=True)
            for lamp in bpy.data.lamps:
                bpy.data.lamps.remove(lamp, do_unlink=True)
                
def camerasettings():
    # add camera
    bpy.ops.object.camera_add()
    # location of camera
    bpy.data.objects['Camera'].location = (-0.2567, -12.208, 4.98)
    # rotation of camera. x axis rotation is 105.125 degrees in this example
    bpy.data.objects['Camera'].rotation_euler = [ 70.*math.pi/180, -2.44*math.pi/180, -5.14*math.pi/180]
    # scale of camera usually unaltered.
    bpy.data.objects['Camera'].scale = [1.0, 1.0, 1.0]
    bpy.data.cameras['Camera'].lens = 35.00
    # by default camera type is perspective. uncomment below line for changing camera to orthographic.
    #bpy.data.cameras['Camera'].type='ORTHO'     #PERSP for perspective. default orthographic scale is 7.314

def lightsource():
    # add lamp
    bpy.ops.object.lamp_add(type='AREA')
    # change sun location.
    bpy.data.objects['Area'].location = [0.60,-7.2,5.30]
    bpy.data.objects['Area'].rotation_euler = [-10*math.pi/180, 0.0, 0.0]

    # you can modify object names. example given below. uncomment if needed.
    # if uncommented upcoming commands should also be modified accordingly
    #bpy.data.lamps[0].name = 'Sun'
    #bpy.data.objects['Sun'].name = 'Sun'
    # you can add more light sources. uncomment below line for example light source
    #bpy.ops.object.lamp_add(type='POINT')

    # change rotation of sun's direction vector.
    #bpy.data.objects['Sun'].rotation_euler = [59*math.pi/180, 0.0, 0.0]
    # in order to change color, strength of sun, we have to use nodes.
    # also node editing is quite useful for designing layers to your rendering
    bpy.data.lamps['Area'].use_nodes = True
    # in the above statement we used 'Lamp' instead of index 0.
    # The default name of lamps is 'Lamp' as described in the above comments.

    # set color and strength value of sun using nodes.
    #bpy.data.lamps['Area'].node_tree.nodes['Emission'].inputs['Color'].default_value = [1.0, 1.0, 1.0, 1.0]
    bpy.data.lamps['Area'].node_tree.nodes['Emission'].inputs['Strength'].default_value = 50.0

def meshsettings():
    bpy.ops.mesh.primitive_plane_add(location=(0.3, -7.0, 2.5))
    bpy.data.objects['Plane'].scale = [4.0, 3.0, 2.0]
    bpy.ops.mesh.primitive_plane_add(location=(1.75, -7.0, 4.2))
    bpy.data.objects['Plane.001'].scale = [2.0, 3.0, 2.0]
    bpy.data.objects['Plane.001'].rotation_euler = [0.0, -90*math.pi/180, 0.0]
    bpy.ops.mesh.primitive_plane_add(location=(0.1, -7.0, 5.4))
    bpy.data.objects['Plane.002'].scale = [3.0, 2.0, 2.0]
    bpy.ops.mesh.primitive_plane_add(location=(-1.5, -7.0, 4.2))
    bpy.data.objects['Plane.003'].scale = [2.0, 3.0, 2.0]
    bpy.data.objects['Plane.003'].rotation_euler = [0.0, -90*math.pi/180, 0.0]
    bpy.ops.mesh.primitive_plane_add(location=(0.1, -7.0, 4.4))
    bpy.data.objects['Plane.004'].scale = [2.0, 3.0, 2.0]
    bpy.data.objects['Plane.004'].rotation_euler = [0.0, 90*math.pi/180, -90*math.pi/180]
    
def addobjects(banana_file_loc,num = 1):
    for i in range(0,num):
        if i == 0:
            imported_object = bpy.ops.import_scene.obj(filepath=banana_file_loc)
            bpy.data.objects['Banana'].location = [0.12, - 7.7, 2.63]
            bpy.data.objects['Banana'].rotation_euler = [80*math.pi/180 , -8*math.pi/180 , -70*math.pi/180]
            bpy.data.objects['Banana'].scale = [0.45, 0.45, 0.45]
        else:
            imported_object = bpy.ops.import_scene.obj(filepath=banana_file_loc)
            bpy.data.objects['Banana'+'.00'+str(i)].location = [0.12 + i*pow(-1.0,i+1)*0.3, - 7.7, 2.63]
            bpy.data.objects['Banana'+'.00'+str(i)].rotation_euler = [80*math.pi/180 , -8*math.pi/180 , -70*math.pi/180]
            bpy.data.objects['Banana'+'.00'+str(i)].scale = [0.45, 0.45, 0.45]

#ensure that cycles engine is set for the basic scene.
bpy.data.scenes['Scene'].render.engine = 'CYCLES'    
banana_file_loc = '/mnt/sdb1/repositories/Sys_sw_engg17-18/Simulations/banana/Banana.obj'
removeexistingobjects()
camerasettings()
lightsource()
meshsettings()
addobjects(banana_file_loc, num=5)