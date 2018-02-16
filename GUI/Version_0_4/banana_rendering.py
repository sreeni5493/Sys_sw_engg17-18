import bpy
import math
import random
import numpy as np
import os
import sys

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
    bpy.context.scene.camera = bpy.data.objects['Camera']

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
    
def addobjects(banana_file_loc, banana_tex_loc, num = 1, fruit_stat = [1], render_gt = False):
    if render_gt ==  False:
        for i in range(0,num):
            if i == 0:
                imported_object = bpy.ops.import_scene.obj(filepath=banana_file_loc)
                bpy.data.objects['Banana'].location = [0.12, - 7.7, 2.63]
                bpy.data.objects['Banana'].rotation_euler = [80*math.pi/180 , -8*math.pi/180 , -70*math.pi/180]
                bpy.data.objects['Banana'].scale = [0.45, 0.45, 0.45]
                bpy.ops.material.new()
                bpy.data.materials['Material'].name = 'banana'
                bpy.data.objects['Banana'].active_material = bpy.data.materials['banana']
                bpy.data.materials['banana'].use_nodes = True
                nodetree = bpy.data.materials['banana'].node_tree
                nodes = bpy.data.materials['banana'].node_tree.nodes
                nodes.new('ShaderNodeBsdfPrincipled')
                nodes['Principled BSDF'].inputs['Specular'].default_value=0.1
                nodetree.links.new(nodes['Principled BSDF'].outputs['BSDF'],nodes['Material Output'].inputs['Surface'])
                print ('fine')
                bpy.data.images.load(filepath=os.path.join(banana_tex_loc+'/albedo'+str(int(fruit_stat[i]))+'.png'))
                nodes.new('ShaderNodeTexImage')
                nodes['Image Texture'].image=bpy.data.images['albedo'+str(int(fruit_stat[i]))+'.png']
                nodetree.links.new(nodes['Image Texture'].outputs['Color'],nodes['Principled BSDF'].inputs[0])
            else:
                imported_object = bpy.ops.import_scene.obj(filepath=banana_file_loc)
                bpy.data.objects['Banana'+'.00'+str(i)].location = [0.12 + i*pow(-1.0,i+1)*0.3, - 7.7, 2.63]
                bpy.data.objects['Banana'+'.00'+str(i)].rotation_euler = [80*math.pi/180 , -8*math.pi/180 , -70*math.pi/180]
                bpy.data.objects['Banana'+'.00'+str(i)].scale = [0.45, 0.45, 0.45]
                bpy.ops.material.new()
                bpy.data.materials['Material'].name = 'banana'+str(i)
                bpy.data.objects['Banana'+'.00'+str(i)].active_material = bpy.data.materials['banana'+str(i)]
                bpy.data.materials['banana'+str(i)].use_nodes = True
                nodetree = bpy.data.materials['banana'+str(i)].node_tree
                nodes = bpy.data.materials['banana'+str(i)].node_tree.nodes
                nodes.new('ShaderNodeBsdfPrincipled')
                nodes['Principled BSDF'].inputs['Specular'].default_value=0.1
                nodetree.links.new(nodes['Principled BSDF'].outputs['BSDF'],nodes['Material Output'].inputs['Surface'])
                bpy.data.images.load(filepath=os.path.join(banana_tex_loc+'/albedo'+str(int(fruit_stat[i]))+'.png'))
                nodes.new('ShaderNodeTexImage')
                nodes['Image Texture'].image=bpy.data.images['albedo'+str(int(fruit_stat[i]))+'.png']
                nodetree.links.new(nodes['Image Texture'].outputs['Color'],nodes['Principled BSDF'].inputs[0])
    
        #now we need to uv unwrap over the entire mesh
        #bpy.ops.object.mode_set(mode='EDIT')
        #bpy.ops.mesh.select_all(action='SELECT')
        #bpy.ops.uv.unwrap()
        #bpy.ops.mesh.select_all(action='DESELECT')
        #bpy.ops.object.mode_set(mode='OBJECT')
    else:
        removeexistingobjects()
        camerasettings()
        for i in range(0,num):
            if i == 0:
                imported_object = bpy.ops.import_scene.obj(filepath=banana_file_loc)
                bpy.data.objects['Banana'].location = [0.12, - 7.7, 2.63]
                bpy.data.objects['Banana'].rotation_euler = [80*math.pi/180 , -8*math.pi/180 , -70*math.pi/180]
                bpy.data.objects['Banana'].scale = [0.45, 0.45, 0.45]
                bpy.ops.material.new()
                bpy.data.materials['Material'].name = 'banana'
                bpy.data.objects['Banana'].active_material = bpy.data.materials['banana']
                bpy.data.materials['banana'].use_nodes = True
                nodetree = bpy.data.materials['banana'].node_tree
                nodes = bpy.data.materials['banana'].node_tree.nodes
                nodes.new('ShaderNodeEmission')
                nodetree.links.new(nodes['Emission'].outputs['Emission'], nodes['Material Output'].inputs['Surface'])
                if (fruit_stat[i]<=4):
                    nodes['Emission'].inputs['Color'].default_value=[0.0, 1.0, 0.0, 1.0]
                elif (fruit_stat[i]<=6 and fruit_stat[i]>4):
                    nodes['Emission'].inputs['Color'].default_value=[0.0, 0.0, 1.0, 1.0]
                else:
                    nodes['Emission'].inputs['Color'].default_value=[1.0, 0.0, 0.0, 1.0]
            else:
                imported_object = bpy.ops.import_scene.obj(filepath=banana_file_loc)
                bpy.data.objects['Banana'+'.00'+str(i)].location = [0.12 + i*pow(-1.0,i+1)*0.3, - 7.7, 2.63]
                bpy.data.objects['Banana'+'.00'+str(i)].rotation_euler = [80*math.pi/180 , -8*math.pi/180 , -70*math.pi/180]
                bpy.data.objects['Banana'+'.00'+str(i)].scale = [0.45, 0.45, 0.45]
                bpy.ops.material.new()
                bpy.data.materials['Material'].name = 'banana'+str(i)
                bpy.data.objects['Banana'+'.00'+str(i)].active_material = bpy.data.materials['banana'+str(i)]
                bpy.data.materials['banana'+str(i)].use_nodes = True
                nodetree = bpy.data.materials['banana'+str(i)].node_tree
                nodes = bpy.data.materials['banana'+str(i)].node_tree.nodes
                nodes.new('ShaderNodeEmission')
                nodetree.links.new(nodes['Emission'].outputs['Emission'], nodes['Material Output'].inputs['Surface'])
                if (fruit_stat[i]<=4):
                    nodes['Emission'].inputs['Color'].default_value=[0.0, 1.0, 0.0, 1.0]
                elif (fruit_stat[i]<=7 and fruit_stat[i]>4):
                    nodes['Emission'].inputs['Color'].default_value=[0.0, 0.0, 1.0, 1.0]
                else:
                    nodes['Emission'].inputs['Color'].default_value=[1.0, 0.0, 0.0, 1.0]


def create_banana(number_imgs, num_fruits, fruits_states):
    if len(list(bpy.context.user_preferences.addons['cycles'].preferences.devices)) > 0:
        bpy.context.scene.cycles.device = 'GPU'
    # ensure that cycles engine is set for the basic scene.
    bpy.data.scenes['Scene'].render.engine = 'CYCLES'
    banana_file_loc = 'Banana.obj'
    banana_tex_loc = 'banana_textures'
    save_loc = './simulation_results'
    num_imgs = 1
    for num in range(num_imgs):
        removeexistingobjects()
        camerasettings()
        lightsource()
        meshsettings()
        bpy.data.scenes['Scene'].render.resolution_percentage = 25
        num_fruits = random.randint(2, 5)
        fruit_states = 9
        fruit_status = np.zeros(num_fruits)
        for k in range(num_fruits):
            fruit_status[k] = random.randint(1, fruit_states)
        addobjects(banana_file_loc, banana_tex_loc, num=num_fruits, fruit_stat=fruit_status, render_gt=False)
        bpy.data.scenes["Scene"].render.filepath = save_loc + '/render' + str(num + 1) + '.png'
        bpy.ops.render.render(write_still=True)
        bpy.data.scenes['Scene'].render.resolution_percentage = 25
        addobjects(banana_file_loc, banana_tex_loc, num=num_fruits, fruit_stat = fruit_status, render_gt = True)
        bpy.data.scenes["Scene"].render.filepath = save_loc+'/groundtruth'+str(num + 1)+'.png'
        bpy.ops.render.render( write_still=True)

def create_sample_banana():
    if len(list(bpy.context.user_preferences.addons['cycles'].preferences.devices)) > 0:
        bpy.context.scene.cycles.device = 'GPU'
    # ensure that cycles engine is set for the basic scene.
    bpy.data.scenes['Scene'].render.engine = 'CYCLES'
    banana_file_loc = 'Banana.obj'
    banana_tex_loc = 'banana_textures'
    save_loc = './simulation_results'
    num_imgs = 1
    for num in range(num_imgs):
        removeexistingobjects()
        camerasettings()
        lightsource()
        meshsettings()
        bpy.data.scenes['Scene'].render.resolution_percentage = 25
        num_fruits = random.randint(2, 5)
        fruit_states = 9
        fruit_status = np.zeros(num_fruits)
        for k in range(num_fruits):
            fruit_status[k] = random.randint(1, fruit_states)
        addobjects(banana_file_loc, banana_tex_loc, num=num_fruits, fruit_stat=fruit_status, render_gt=False)
        bpy.data.scenes["Scene"].render.filepath = save_loc + '/render' + str(num + 1) + '.png'
        bpy.ops.render.render(write_still=True)
        # bpy.data.scenes['Scene'].render.resolution_percentage = 25
        # addobjects(banana_file_loc, banana_tex_loc, num=num_fruits, fruit_stat = fruit_status, render_gt = True)
        # bpy.data.scenes["Scene"].render.filepath = save_loc+'/groundtruth'+str(num + 1)+'.png'
        # bpy.ops.render.render( write_still=True)


if __name__ == '__main__':
    argv = sys.argv
    argv = argv[argv.index("--") + 1 :]
    create_banana(argv[argv.index("--number_imgs") + 1], argv[argv.index("--number_fruits") + 1],
                    argv[argv.index("--fruit_states") + 1])
