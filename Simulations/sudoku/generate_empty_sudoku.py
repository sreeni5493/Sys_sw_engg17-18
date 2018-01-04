import bpy
from random import random
from math import floor

def create_number_field(x,y):
    # Create plane
    bpy.ops.mesh.primitive_plane_add(radius=0.5, view_align=False, enter_editmode=False, location=(x, y, 0.02), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.resize(value=(1, 1, 0.1), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
    images_hand = ["C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\0.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\1.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\2.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\3.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\4.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\5.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\6.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\7.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\8.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\9.png"]
    images_font = ["C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\0.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\1.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\2.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\3.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\4.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\5.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\6.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\7.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\8.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\9.png"]
    image_id = floor(random()*10)

    try:
        r1 = random()
        if (r1 < 0.25):
            img = bpy.data.images.load(images_hand[image_id])
        else:
            try:
                if (r1 < 0.5):
                    img = bpy.data.images.load(images_font[image_id])
                else:
                    img = bpy.data.images.load("C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\blank.png")                
            except:
                raise NameError("Cannot load image %s" % images_font[image_id])
    except:
        raise NameError("Cannot load image %s" % images_hand[image_id])
        
    # Create image texture from image
    cTex = bpy.data.textures.new('ColorTex', type = 'IMAGE')
    cTex.image = img
    
    mat = bpy.data.materials.new('TexMat')
    #mat.use_shadeless = True
    mat.preview_render_type = 'FLAT'
    mat.diffuse_color = (2, 2, 2)

    # Add texture slot for color texture
    mtex = mat.texture_slots.add()
    mtex.texture = cTex
    mtex.texture_coords = 'UV'
    mtex.mapping = 'FLAT'
    
    bpy.ops.object.editmode_toggle()
    bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)
    bpy.ops.object.editmode_toggle()

    bpy.context.object.data.materials.append(mat)

def create_sudoku():
    #------------------
    #  Sudoku planes
    #------------------
    # Create background plane
    ground_plane = bpy.ops.mesh.primitive_plane_add(radius=10, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.context.object.data.materials.append(bpy.data.materials.new(name="background_color"))
    bpy.context.object.data.materials[0].diffuse_color = (2, 2, 2)

    # Create black sudoku border and grid
    border_obj = bpy.ops.mesh.primitive_cube_add(radius=5, view_align=False, enter_editmode=False, location=(0, 0, 0.001), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.resize(value=(1, 1, 0.0005), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.context.object.data.materials.append(bpy.data.materials.new(name="border_color"))
    bpy.context.object.data.materials[0].diffuse_color = (0, 0, 0)

    # Create entry fields
    for i in [-4.4,-3.3,-2.2,-1.1,0,1.1,2.2,3.3,4.4]:
        for j in [-4.4,-3.3,-2.2,-1.1,0,1.1,2.2,3.3,4.4]:
            create_number_field(i, j)

    #------------------
    #      Camera
    #------------------
    # Create camera if non exist and move it above surface
    try:
        camera = bpy.data.objects["Camera"]
    except:
        camera_data = bpy.data.cameras.new(name="Camera")
        camera_object = bpy.data.objects.new(name="Camera", object_data=camera_data)
        bpy.context.scene.objects.link(camera_object)
        camera = bpy.data.objects["Camera"]    
    camera.location = (0.0, 0.0, 22)
    camera.rotation_euler[0] = 0
    camera.rotation_euler[1] = 0
    camera.rotation_euler[2] = 0

    #------------------
    #       Light
    #------------------
    # Create lamp if none exists and move it anywhere in the parallel plane above the surface
    try:
        lamp = bpy.data.objects["Lamp"]
    except:
        lamp_data = bpy.data.lamps.new(name="Lamp", type='POINT')
        lamp_object = bpy.data.objects.new(name="Lamp", object_data=lamp_data)
        bpy.context.scene.objects.link(lamp_object)
        lamp = bpy.data.objects["Lamp"]
    lamp.location = (random()*4, random()*4, 12)
    
if __name__ == '__main__':
    create_sudoku()