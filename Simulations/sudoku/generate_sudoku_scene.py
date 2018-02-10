import bpy
from random import random
from math import floor, atan, pi
import sys
import time

class SudokuScene:
    def __init__(self, difficulty, errors, completion, res_x, res_y, solved, unsolved,frontal_view):
        self.images_hand = [["./fonts/blank.png","./fonts/handwritten/basin/1.png","./fonts/handwritten/basin/2.png","./fonts/handwritten/basin/3.png","./fonts/handwritten/basin/4.png","./fonts/handwritten/basin/5.png","./fonts/handwritten/basin/6.png","./fonts/handwritten/basin/7.png","./fonts/handwritten/basin/8.png","./fonts/handwritten/basin/9.png"],
                            ["./fonts/blank.png","./fonts/handwritten/BelindaType67/1.png","./fonts/handwritten/BelindaType67/2.png","./fonts/handwritten/BelindaType67/3.png","./fonts/handwritten/BelindaType67/4.png","./fonts/handwritten/BelindaType67/5.png","./fonts/handwritten/BelindaType67/6.png","./fonts/handwritten/BelindaType67/7.png","./fonts/handwritten/BelindaType67/8.png","./fonts/handwritten/BelindaType67/9.png"],
                            ["./fonts/blank.png","./fonts/handwritten/otto/1.png","./fonts/handwritten/otto/2.png","./fonts/handwritten/otto/3.png","./fonts/handwritten/otto/4.png","./fonts/handwritten/otto/5.png","./fonts/handwritten/otto/6.png","./fonts/handwritten/otto/7.png","./fonts/handwritten/otto/8.png","./fonts/handwritten/otto/9.png"]]
        self.images_font = ["./fonts/blank.png","./fonts/common/Arial/1.png","./fonts/common/Arial/2.png","./fonts/common/Arial/3.png","./fonts/common/Arial/4.png","./fonts/common/Arial/5.png","./fonts/common/Arial/6.png","./fonts/common/Arial/7.png","./fonts/common/Arial/8.png","./fonts/common/Arial/9.png"]
        self.complete_sudoku = eval(solved)
        print(type(self.complete_sudoku))
        self.unsolved_sudoku = eval(unsolved)
        self.completion = int(completion)
        self.difficulty = difficulty
        self.errors = int(errors)
        self.bgcolor = (1,0.9+random()*0.1,0.7+random()*0.3)
        self.groundtruth = [[],[],[]]
        for i in range(0,81):
            self.groundtruth[0].append(0)
            self.groundtruth[1].append(0)
            self.groundtruth[2].append(0)
        self.fields = []
        self.r_x = int(res_x)
        self.r_y = int(res_y)
        self.bgcolor = (1,0.9+random()*0.1,0.7+random()*0.3)
        self.frontal_view = int(frontal_view)
        self.cTex_hand = []
        self.cTex_font = []
        self.__load_fonts()
    
    def __load_fonts(self):
        for i in range(0,10):
            try:
                img = bpy.data.images.load(self.images_hand[floor(random()*3)][i])
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
        if self.frontal_view:
            movement_x = 0#random()*15-7.5
            movement_y = 0#random()*15-7.5
        else:
            movement_x = random()*15-7.5
            movement_y = random()*15-7.5
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
        filename_tmp = list(filename)
        filename_tmp[0] = "."
        filename = "".join(filename_tmp)
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
        
    def crumble(self,name):
        pass

if __name__ == '__main__':

    print("na immerhin")
    argv = sys.argv
    argv = argv[argv.index("--") + 1 :]

    for i in range(0,int(argv[argv.index("--num_images") + 1])):
        s = SudokuScene(argv[argv.index("--difficulty") + 1], argv[argv.index("--errors") + 1], argv[argv.index("--completion") + 1], argv[argv.index("--resolution") + 1], argv[argv.index("--resolution") + 2], argv[argv.index("--solved") + 1], argv[argv.index("--unsolved") + 1], argv[argv.index("--frontal_view") + 1])
        s.visualize()
        s.induce_errors()
        s.write("image%d"%i)
        #s.crumble("image")
