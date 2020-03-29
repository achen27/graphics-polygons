import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    pass

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    ax = polygons[i+1][0] - polygons[i][0]
    ay = polygons[i+1][1] - polygons[i][1]
    az = polygons[i+1][2] - polygons[i][2]
    a = [ax,ay,az]

    bx = polygons[i+2][0] - polygons[i][0]
    by = polygons[i+2][1] - polygons[i][1]
    bz = polygons[i+2][2] - polygons[i][2]
    b = [bx,by,bz]

    x = a[1]*b[2]-a[2]*b[1]
    y = a[2]*b[0]-a[0]*b[2]
    z = a[0]*b[1]-a[1]*b[0]
    return [x,y,z]
