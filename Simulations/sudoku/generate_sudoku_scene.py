import bpy
from random import random, shuffle
from math import floor, atan, pi
import sys
sys.path.append("C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku")
import sudoku
import copy
import time
from itertools import chain

class Sudoku:
    def __init__(self, difficulty, errors = 0, completion = 1, res_x = 1920, res_y = 1080):
        self.cTex_hand = []
        self.cTex_font = []
        self.__load_fonts()
        self.precreated_sudoku_dict = {"Easy" : [[1, 5, 2, 6, 4, 3, 7, 9, 8, 9, 3, 7, 1, 5, 8, 2, 6, 4, 8, 4, 6, 9, 7, 2, 5, 1, 3, 3, 9, 8, 5, 6, 4, 1, 2, 7, 4, 6, 5, 2, 1, 7, 3, 8, 9, 2, 7, 1, 3, 8, 9, 6, 4, 5, 5, 8, 9, 7, 2, 6, 4, 3, 1, 6, 1, 3, 4, 9, 5, 8, 7, 2, 7, 2, 4, 8, 3, 1, 9, 5, 6],\
                                           [6, 3, 4, 1, 8, 9, 7, 5, 2, 7, 9, 8, 5, 2, 6, 4, 1, 3, 1, 2, 5, 7, 4, 3, 8, 9, 6, 8, 4, 6, 9, 7, 2, 1, 3, 5, 9, 5, 7, 3, 1, 8, 6, 2, 4, 3, 1, 2, 6, 5, 4, 9, 7, 8, 2, 6, 1, 4, 3, 7, 5, 8, 9, 5, 8, 9, 2, 6, 1, 3, 4, 7, 4, 7, 3, 8, 9, 5, 2, 6, 1]],\
                                "Medium" : [[5, 1, 3, 8, 2, 7, 4, 9, 6, 4, 6, 7, 1, 9, 5, 8, 2, 3, 2, 8, 9, 6, 3, 4, 5, 7, 1, 7, 2, 1, 9, 5, 6, 3, 4, 8, 8, 9, 5, 3, 4, 1, 7, 6, 2, 6, 3, 4, 7, 8, 2, 9, 1, 5, 1, 4, 6, 5, 7, 3, 2, 8, 9, 9, 5, 2, 4, 6, 8, 1, 3, 7, 3, 7, 8, 2, 1, 9, 6, 5, 4],\
                                            [6, 1, 8, 3, 2, 7, 9, 4, 5, 5, 3, 9, 6, 4, 1, 8, 2, 7, 7, 2, 4, 9, 8, 5, 6, 3, 1, 3, 5, 1, 7, 6, 4, 2, 9, 8, 8, 6, 2, 1, 9, 3, 5, 7, 4, 9, 4, 7, 8, 5, 2, 3, 1, 6, 4, 8, 3, 2, 7, 6, 1, 5, 9, 1, 9, 5, 4, 3, 8, 7, 6, 2, 2, 7, 6, 5, 1, 9, 4, 8, 3]],\
                                "Hard" : [[8, 5, 2, 6, 1, 7, 9, 4, 3, 4, 3, 9, 2, 8, 5, 7, 6, 1, 6, 7, 1, 3, 9, 4, 5, 2, 8, 9, 1, 3, 7, 6, 2, 4, 8, 5, 7, 6, 5, 8, 4, 3, 2, 1, 9, 2, 8, 4, 9, 5, 1, 6, 3, 7, 5, 4, 6, 1, 3, 9, 8, 7, 2, 3, 2, 8, 5, 7, 6, 1, 9, 4, 1, 9, 7, 4, 2, 8, 3, 5, 6],\
                                       [2, 1, 4, 7, 8, 3, 9, 6, 5, 5, 3, 6, 4, 2, 9, 7, 1, 8, 8, 9, 7, 1, 6, 5, 2, 4, 3, 7, 2, 8, 6, 5, 1, 3, 9, 4, 3, 6, 9, 2, 7, 4, 8, 5, 1, 4, 5, 1, 9, 3, 8, 6, 2, 7, 6, 4, 2, 8, 1, 7, 5, 3, 9, 9, 7, 3, 5, 4, 2, 1, 8, 6, 1, 8, 5, 3, 9, 6, 4, 7, 2]],\
                               "Insane" : [[8, 9, 4, 7, 3, 1, 5, 6, 2, 7, 2, 1, 4, 6, 5, 8, 9, 3, 6, 5, 3, 9, 8, 2, 1, 7, 4, 3, 6, 2, 5, 7, 8, 9, 4, 1, 5, 4, 8, 1, 2, 9, 6, 3, 7, 1, 7, 9, 6, 4, 3, 2, 5, 8, 2, 1, 5, 3, 9, 4, 7, 8, 6, 9, 3, 7, 8, 1, 6, 4, 2, 5, 4, 8, 6, 2, 5, 7, 3, 1, 9],\
                                            [6, 3, 7, 9, 1, 4, 8, 2, 5, 2, 4, 9, 8, 7, 5, 1, 3, 6, 5, 1, 8, 2, 6, 3, 4, 7, 9, 4, 5, 1, 7, 9, 8, 3, 6, 2, 9, 8, 6, 3, 5, 2, 7, 4, 1, 7, 2, 3, 1, 4, 6, 9, 5, 8, 8, 9, 5, 6, 3, 7, 2, 1, 4, 3, 6, 2, 4, 8, 1, 5, 9, 7, 1, 7, 4, 5, 2, 9, 6, 8, 3]]}
        self.precreated_unsolved_sudoku_dict =  {"Easy" : [[0, 0, 0, 0, 4, 0, 7, 0, 0, 9, 0, 0, 0, 0, 8, 0, 0, 4, 8, 4, 0, 9, 0, 0, 0, 1, 0, 3, 9, 0, 5, 0, 0, 0, 2, 0, 4, 0, 5, 0, 1, 7, 3, 8, 0, 2, 7, 0, 0, 8, 0, 6, 4, 5, 5, 0, 0, 0, 2, 6, 0, 3, 0, 6, 1, 0, 4, 9, 5, 8, 7, 2, 7, 2, 4, 0, 0, 0, 0, 5, 0],
                                           [6, 0, 0, 1, 8, 9, 7, 0, 0, 0, 0, 8, 0, 0, 6, 4, 0, 3, 0, 2, 5, 7, 4, 3, 0, 9, 0, 8, 4, 0, 9, 7, 2, 1, 3, 5, 9, 5, 0, 0, 1, 0, 0, 2, 0, 3, 1, 2, 6, 5, 0, 9, 7, 8, 2, 6, 1, 4, 3, 0, 5, 8, 9, 5, 8, 9, 2, 0, 0, 3, 0, 0, 4, 7, 0, 8, 9, 0, 0, 6, 1]],
                                 "Medium" : [[0, 0, 3, 8, 0, 0, 0, 0, 6, 4, 0, 0, 0, 9, 0, 0, 0, 0, 2, 0, 9, 6, 3, 0, 0, 7, 0, 7, 2, 0, 9, 5, 6, 0, 4, 8, 0, 0, 5, 0, 4, 1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 3, 2, 0, 0, 9, 0, 0, 4, 6, 0, 0, 0, 7, 0, 0, 8, 0, 0, 0, 6, 5, 0],
                                            [6, 0, 0, 0, 2, 7, 9, 0, 5, 5, 0, 9, 6, 0, 1, 0, 2, 7, 0, 0, 0, 9, 8, 0, 6, 3, 1, 0, 5, 0, 7, 0, 0, 0, 9, 0, 0, 0, 0, 1, 0, 0, 0, 0, 4, 0, 4, 0, 8, 5, 0, 0, 1, 0, 4, 8, 0, 2, 0, 6, 1, 5, 0, 0, 9, 5, 4, 0, 8, 7, 6, 0, 0, 0, 6, 5, 1, 9, 4, 8, 0]],
                                "Hard" : [[0, 0, 0, 0, 0, 7, 9, 0, 3, 0, 0, 9, 0, 0, 5, 7, 0, 0, 6, 7, 0, 3, 0, 4, 5, 0, 0, 0, 1, 0, 7, 0, 0, 0, 0, 0, 0, 6, 0, 8, 0, 3, 0, 1, 9, 0, 0, 4, 9, 0, 0, 6, 0, 0, 5, 4, 0, 0, 0, 0, 0, 0, 0, 3, 2, 0, 5, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 8, 3, 0, 6],
                                       [0, 1, 0, 0, 0, 0, 0, 0, 5, 0, 3, 0, 4, 0, 9, 0, 0, 0, 0, 9, 0, 0, 0, 0, 2, 0, 0, 7, 0, 8, 6, 0, 1, 3, 9, 0, 0, 6, 9, 0, 7, 0, 8, 5, 0, 4, 0, 0, 9, 3, 8, 6, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 9, 0, 7, 3, 0, 4, 2, 0, 8, 6, 0, 8, 0, 0, 0, 6, 0, 7, 0]],
                                "Insane" : [[0, 9, 0, 7, 3, 0, 5, 0, 0, 7, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 6, 2, 0, 0, 0, 0, 4, 0, 5, 0, 0, 0, 0, 9, 0, 0, 7, 0, 0, 0, 0, 4, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 8, 0, 6, 0, 0, 0, 0, 8, 0, 2, 5, 0, 3, 0, 9],
                                           [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 4, 0, 8, 7, 0, 0, 0, 6, 0, 1, 8, 2, 0, 3, 4, 7, 0, 0, 0, 0, 0, 9, 8, 0, 0, 2, 0, 0, 0, 3, 0, 2, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 5, 0, 8, 0, 0, 0, 0, 7, 2, 1, 0, 0, 6, 0, 4, 0, 0, 0, 0, 7, 0, 0, 4, 0, 2, 0, 0, 0, 3]]}
        r = floor(random()*len(self.precreated_sudoku_dict[difficulty]))
        self.complete_sudoku = self.precreated_sudoku_dict[difficulty][r]
        self.unsolved_sudoku = self.precreated_unsolved_sudoku_dict[difficulty][r]
        self.completion = completion
        self.difficulty = difficulty
        self.errors = errors
        self.bgcolor = (1,0.9+random()*0.1,0.7+random()*0.3)
        self.groundtruth = [[],[],[]]
        for i in range(0,81):
            self.groundtruth[0].append(0)
            self.groundtruth[1].append(0)
            self.groundtruth[2].append(0)
        self.fields = []
        self.r_x = res_x
        self.r_y = res_y
        
    def __load_fonts(self):
        self.images_hand = ["C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\blank.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\1.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\2.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\3.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\4.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\5.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\6.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\7.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\8.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\handwritten\\basin\\9.png"]
        self.images_font = ["C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\blank.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\1.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\2.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\3.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\4.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\5.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\6.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\7.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\8.png","C:\\Users\\JonasSimon\\Documents\\sys_sw_eng\\Sys_sw_engg17-18\\Simulations\\sudoku\\fonts\\common\\Arial\\9.png"]
        for i in range(0,10):
            try:
                img = bpy.data.images.load(self.images_hand[i])
            except:
                raise NameError("Cannot load image %s" % self.images_hand[i])
            # Create image texture from image
            cTex = bpy.data.textures.new('ColorTexHand%d'%i, type = 'IMAGE')
            cTex.image = img
            self.cTex_hand.append(cTex)
            
        for i in range(0,10):
            try:
                img = bpy.data.images.load(self.images_font[i])
            except:
                raise NameError("Cannot load image %s" % self.images_font[i])
            # Create image texture from image
            cTex = bpy.data.textures.new('ColorTexFont%d'%i, type = 'IMAGE')
            cTex.image = img
            self.cTex_font.append(cTex)
    
    def randomize_sudoku(self):
        r = floor(random()*len(self.precreated_sudoku_dict[self.difficulty]))
        self.complete_sudoku = self.precreated_sudoku_dict[self.difficulty][r]
        self.unsolved_sudoku = self.precreated_unsolved_sudoku_dict[self.difficulty][r]
        blocksize = 9
        r = random()
        permutation_list = [i for i in range(0,81)]
        for i in range(0,3):
            blocks = [permutation_list[i:i+blocksize] for i in range(i*3*blocksize,(i+1)*3*blocksize,blocksize)]
            print(blocks)
            shuffle(blocks)
            permutation_list[i*3*blocksize:(i+1)*3*blocksize] = [b for bs in blocks for b in bs]
        # Flip sudoku to shuffle former lines
        blocks = [permutation_list[i:i+blocksize] for i in range(0,len(permutation_list),blocksize)]
        blocks = zip(*blocks)
        permutation_list = list(chain(*blocks))
        for i in range(0,3):
            print(permutation_list)
            print(blocksize)
            blocks = [permutation_list[i:i+blocksize] for i in range(i*3*blocksize,(i+1)*3*blocksize,blocksize)]
            print("blocks" + str(blocks))
            shuffle(blocks)
            permutation_list[i*3*blocksize:(i+1)*3*blocksize] = [b for bs in blocks for b in bs]
        # Maybe flip back
        if (random() < 0.5):
            blocks = [permutation_list[i:i+blocksize] for i in range(0,len(permutation_list),blocksize)]
            blocks = zip(*blocks)
            permutation_list[0:len(permutation_list)] = [b for bs in blocks for b in bs]
        # Reorder sudokus
        tmp_complete_sudoku = []
        tmp_unsolved_sudoku = []
        for i in range(0,81):
            tmp_complete_sudoku.append(self.complete_sudoku[permutation_list[i]])
            tmp_unsolved_sudoku.append(self.unsolved_sudoku[permutation_list[i]])
        self.complete_sudoku = tmp_complete_sudoku
        self.unsolved_sudoku = tmp_unsolved_sudoku
        del tmp_complete_sudoku,tmp_unsolved_sudoku
        #permutation_list = zip(*permutation_list)
        #for i in range(0,3):
        #    blocks = [permutation_list[i:i+blocksize] for i in range(i*3*blocksize,(i+1)*3*blocksize,blocksize)]
        #    print(blocks)
        #    shuffle(blocks)
        #    permutation_list[i*3*blocksize:(i+1)*3*blocksize] = [b for bs in blocks for b in bs]
            
    def visualize(self):
        bpy.ops.object.select_all(action='TOGGLE')
        bpy.ops.object.select_all(action='TOGGLE')
        bpy.ops.object.delete(use_global=False)

        #------------------
        #  Sudoku planes
        #------------------
        # Create background plane
        ground_plane = bpy.ops.mesh.primitive_plane_add(radius=20, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.context.object.data.materials.append(bpy.data.materials.new(name="background_color"))
        bpy.context.object.data.materials[0].diffuse_color = self.bgcolor

        # Create black sudoku border and grid
        border_obj = bpy.ops.mesh.primitive_cube_add(radius=5, view_align=False, enter_editmode=False, location=(0, 0, 0.001), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.ops.transform.resize(value=(1, 1, 0.0005), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.context.object.data.materials.append(bpy.data.materials.new(name="border_color"))
        bpy.context.object.data.materials[0].diffuse_color = (0, 0, 0)
        # TODO: allow changing grid color

        start = time.time()

        # Create entry fields
        counter = 0
        for i in [4.4,3.3,2.2,1.1,0,-1.1,-2.2,-3.3,-4.4]:
            for j in [-4.4,-3.3,-2.2,-1.1,0,1.1,2.2,3.3,4.4]:
                if self.unsolved_sudoku[counter] != 0:
                    print(self.images_font[self.complete_sudoku[counter]])
                    self.__create_number_field(j, i, "font", self.complete_sudoku[counter])
                    self.groundtruth[0][counter] = self.complete_sudoku[counter]
                else:
                    r = random()
                    if (self.completion == 0 or (self.completion == 1 and r < 0.5)):
                        self.__create_number_field(j, i, "hand", 0)   # Create empty field
                    else:
                        self.__create_number_field(j, i, "hand", self.complete_sudoku[counter])
                        self.groundtruth[1][counter] = self.complete_sudoku[counter]
                counter += 1
        end = time.time()
        print("field drawing took ",end - start," seconds")
        
        #------------------
        #       Light
        #------------------
        # Create lamp if none exists and move it anywhere in the parallel z=12-plane above the surface.
        try:
            lamp = bpy.data.objects["Lamp"]
        except:
            lamp_data = bpy.data.lamps.new(name="Lamp", type='POINT')
            lamp_object = bpy.data.objects.new(name="Lamp", object_data=lamp_data)
            bpy.context.scene.objects.link(lamp_object)
            lamp = bpy.data.objects["Lamp"]
        lamp.location = (-4+random()*8, -4+random()*8, 12)
        lamp.data.energy = 0+random()*2.5
        
        bpy.ops.object.lamp_add(type='SUN', view_align=False, location=(-5+random()*10, -5+random()*10, 30), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.context.object.data.use_specular = False
        bpy.context.object.data.energy = random()*0.1 + 0.25

        #------------------
        #      Camera
        #------------------
        # Create camera if non exist and move it above surface.
        try:
            camera = bpy.data.objects["Camera"]
        except:
            camera_data = bpy.data.cameras.new(name="Camera")
            camera_object = bpy.data.objects.new(name="Camera", object_data=camera_data)
            bpy.context.scene.objects.link(camera_object)
            camera = bpy.data.objects["Camera"]
        bpy.context.scene.camera = camera
        movement_x = 0#random()*15-7.5
        movement_y = 0#random()*15-7.5
        camera.location = (movement_x, movement_y, 22)
        camera.rotation_euler[0] = -atan(movement_y/22.0)
        camera.rotation_euler[1] = atan(movement_x/22.0)
        camera.rotation_euler[2] = 0
        
        #TODO: Move and rotate camera slightly randomly.

    def __create_number_field(self,x,y,type,field_value):
        # Create plane
        bpy.ops.mesh.primitive_plane_add(radius=0.5, view_align=False, enter_editmode=False, location=(x, y, 0.02), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.ops.transform.resize(value=(1, 1, 1), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            
        mat = bpy.data.materials.new('TexMat')
        mat.preview_render_type = 'FLAT'
        mat.diffuse_color = self.bgcolor

        # Add texture slot for color texture
        mtex = mat.texture_slots.add()
        if type == "hand":
            mtex.texture = self.cTex_hand[field_value]
        else:
            mtex.texture = self.cTex_font[field_value]
        mtex.texture_coords = 'UV'
        mtex.mapping = 'FLAT'
        
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)
        bpy.ops.object.editmode_toggle()

        bpy.context.object.data.materials.append(mat)

    def create_new_sudoku(self):
        start = time.time()

        # Create sudoku data
        # Create a solved and an unsolved sudoku, the different is the handwritten input.
        condition = False   # The sudokus are created and the difficulty is checked afterwards. So we create sudokus (which is rather fast) until we have a sudoku of given difficulty.
        while (condition == False):
            new_complete_sudoku = sudoku.perfectSudoku()
            unsolved_sudoku_result = sudoku.puzzleGen(copy.deepcopy(new_complete_sudoku))
            print(unsolved_sudoku_result[2])
            if unsolved_sudoku_result[2] == self.difficulty:
                condition = True

        for i in range(0,81,1):
            self.complete_sudoku[i] = new_complete_sudoku[i].returnPossible()[0]
            if len(unsolved_sudoku_result[0][i].returnPossible())<2:
                self.unsolved_sudoku[i] = unsolved_sudoku_result[0][i].returnPossible()[0]
            else:
                self.unsolved_sudoku[i] = 0
                
        end = time.time()
        print("sudoku generation took ",end - start," seconds")

    def induce_errors(self):
        for i in range(0,self.errors,1):
            print("inducing error %d" % i)
            x = floor(random()*81)
            if x+1 < 10:
                error_plane = bpy.data.objects["Plane.00%d" % (x+1)]
            else:
                error_plane = bpy.data.objects["Plane.0%d" % (x+1)]
            correct_val = self.complete_sudoku[x]
            while 1:
                r = floor(random()*9)+1
                if r != correct_val:
                    break
            error_plane.data.materials[0].texture_slots[0].texture = self.cTex_hand[r]
            #error_plane.data.materials[0].diffuse_color = (1,0,0)
            print("%d: %d -> %d" % (x+1,correct_val,r))
            print("x: %d, y: %d" % (floor(x/9)+1,9-(x%9)))
            self.groundtruth[2][x] = 1
            self.groundtruth[1][x] = r
    
    def write(self,filename):
        bpy.data.scenes['Scene'].render.filepath = '%s.png'%filename
        bpy.context.scene.render.resolution_x = self.r_x
        bpy.context.scene.render.resolution_y = self.r_y
        bpy.ops.render.render( write_still=True ) 
        solution = ""
        errors = ""
        font = ""
        handwritten = ""
        f = open('%s.csv'%filename,'w')
        f.write("solution\n")
        for i in range(0,9):
            for j in range(0,8):
                solution = solution + str(self.complete_sudoku[j+i*9]) + ", "
            f.write(solution + str(self.complete_sudoku[8+i*9]) + "\n")
            solution = ""
        f.write("printed numbers\n")
        for i in range(0,9):
            for j in range(0,8):
                font = font + str(self.groundtruth[0][j+i*9]) + ", "
            f.write(font + str(self.groundtruth[0][8+i*9]) + "\n")
            font = ""
        f.write("handwritten numbers \n")
        for i in range(0,9):
            for j in range(0,8):
                handwritten = handwritten + str(self.groundtruth[1][j+i*9]) + ", "
            f.write(handwritten + str(self.groundtruth[1][8+i*9]) + "\n")
            handwritten = ""
        f.write("errors\n")
        for i in range(0,9):
            for j in range(0,8):
                errors = errors + str(self.groundtruth[2][j+i*9]) + ", "
            f.write(errors + str(self.groundtruth[2][8+i*9]) + "\n")
            errors = ""
        f.close()
        

if __name__ == '__main__':
    argv = sys.argv
    argv = argv[argv.index("--") + 1 :]
    #argv = ["--difficulty","Easy","--errors","0","--completion","0"]
    if "--difficulty" in argv:
        difficulty = argv[argv.index("--difficulty") + 1]
        if difficulty not in ["Easy","Medium","Hard","Insane"]:
            raise Exception("Difficulty "+difficulty+" not defined. Please choose from \"Easy\", \"Medium\", \"Hard\" and \"Insane\".")
    else:
        raise Exception('--difficulty argument missing.') 
    if "--errors" in argv:
        errors = int(argv[argv.index("--errors") + 1])
    else:
        raise Exception('--errors argument missing.') 
    if "--completion" in argv:
        completion = int(argv[argv.index("--completion") + 1])
        if completion == 0:
            completion_str = "unsolved"
        elif completion == 1:
            completion_str = "partially_solved"
        else:
            completion_str = "solved"
    else:
        raise Exception('--completion argument missing.')
    if "--name" in argv:
        name = int(argv[argv.index("--name") + 1])
    else:
        raise Exception('--name argument missing.')
    for i in range(0,2):
        if "--resolution" in argv:
            res_x = int(argv[argv.index("--resolution") + 1])
            res_y = int(argv[argv.index("--resolution") + 2])
            s = Sudoku(difficulty, errors, completion, res_x, res_y)
        else:
            s = Sudoku(difficulty, errors, completion)
        #s.randomize_sudoku()
        s.create_new_sudoku()
        s.visualize()
        if completion > 0:
            s.induce_errors()
        s.write(name)#'/sudoku_dataset/' + difficulty + '/errors_%d/' % errors + completion_str + '/frontal_%d' % i)