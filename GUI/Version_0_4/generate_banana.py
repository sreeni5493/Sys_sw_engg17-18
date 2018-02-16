import subprocess


def call_banana_render(num_imgs = 1, num_fruits = 1, fruit_states = 9):
    string_call = '/home/m3/Testing/gui/GUI_Sudoku_Testing/blender-2.79-linux-glibc219-x86_64/blender'
    subprocess.call(
        [string_call, "-b","--python",'./banana_rendering.py',"--","--number_imgs","%d"%num_imgs,
         "--number_fruits","%d"%num_fruits,"--fruit_states","%d"%fruit_states])
    return True


if __name__ == '__main__':
    call_banana_render()