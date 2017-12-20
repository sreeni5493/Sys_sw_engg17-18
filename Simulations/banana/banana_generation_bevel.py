import bpy
from math import sqrt,pi

# Create banana object. size not used yet
def banana(origin, size):
    # Define curve coordinates
    coords = [(1.5,0,1.1), (1.5,0,1.1), (1.4,0,1.2), (1.3,0,1.3), (0.7,0,1.8), (0.4,0,2), (0,0,3), (0,0,4.5), (0.2,0,6.25), (1.2,0,7), (1.2,0,7)]

    # Create the curve datablock
    curveData = bpy.data.curves.new('myCurve', type='CURVE')
    curveData.dimensions = '3D'
    curveData.resolution_u = 2

    # Map coords to splines of curve
    polyline = curveData.splines.new('NURBS')
    polyline.points.add(len(coords)-1)
    for i, coord in enumerate(coords):
        x,y,z = coord
        polyline.points[i].co = (x, y, z, 1)
        print(polyline.points[i].co)
    
    # Change point radius to achieve banana profile
    polyline.points[0].radius = 0.3
    polyline.points[1].radius = 0.3
    polyline.points[2].radius = 0.3
    polyline.points[3].radius = 0.3
    polyline.points[4].radius = 0.1
    polyline.points[5].radius = 1.2
    polyline.points[6].radius = 1.2
    polyline.points[7].radius = 1.2
    polyline.points[8].radius = 1.4
    polyline.points[9].radius = 0.3
    polyline.points[10].radius = 0.3

    # Create Object
    curveOB = bpy.data.objects.new('myCurve', curveData)
    # Link object to scene
    bpy.context.scene.objects.link(curveOB)

    # Create the Hexagon Datablock
    hexagon = bpy.data.curves.new('myCurve', type='CURVE')
    hexagon.dimensions = '3D'
    hexagon.resolution_u = 2
    
    # Evaluate points
    verts,edges = create_hexagon(origin,0.5)
    verts.append(verts[0])  # close curve
    
    # Map coords to splines of curve
    polyline = hexagon.splines.new('NURBS')
    polyline.order_u = 2
    polyline.points.add(len(verts)-1)

    for i, coord in enumerate(verts):
        x,y,z = verts[i]
        polyline.points[i].co = (x, y, z, 1)
        print("verts["+str(i)+"]: "+str(verts[i]))
    
    # Create Object
    hexagonCurveOB = bpy.data.objects.new('hexagon', hexagon)
    # Link object to scene
    #bpy.context.scene.objects.link(hexagonCurveOB)
    
    # Create bevel object with closed caps
    curveOB.data.bevel_object = bpy.data.objects["hexagon"]
    curveOB.data.splines[0].use_endpoint_u = True
    curveOB.data.splines[0].order_u = 6
    curveOB.data.use_fill_caps = True
    curveOB.data.use_uv_as_generated = True
    curveOB.data.materials.append(bpy.data.materials.new(name="fresh_banana"))
    curveOB.data.materials[0].diffuse_color = (1, 0.85, 0)
    curveOB.active_material.use_nodes = True
    
    return curveOB

#Create hexagon with radius r around point origin
def create_hexagon(origin, r):
    verts = [(origin[0],origin[1]-r,origin[2]), 
            (origin[0]+r*sqrt(3)/2.0,origin[1]-r/2.0,origin[2]), 
            (origin[0]+r*sqrt(3)/2.0,origin[1]+r/2.0,origin[2]), 
            (origin[0],origin[1]+r,origin[2]), 
            (origin[0]-r*sqrt(3)/2.0,origin[1]+r/2.0,origin[2]), 
            (origin[0]-r*sqrt(3)/2.0,origin[1]-r/2.0,origin[2])]
    edges = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)]
    return verts,edges
    
if __name__ == '__main__':
    banana1 = banana((0,0,0),1)
    banana1.rotation_euler[1] = -pi/2
    banana1.rotation_euler[2] = pi/4
    banana1.location = (3.2,3.3,0.0)
    bpy.context.area.type = 'VIEW_3D'
    