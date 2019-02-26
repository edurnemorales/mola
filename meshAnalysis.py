import math

def determinant(a,b,c,d,e,f,g,h,i):
	return (a * e * i - a * f * h - b * d * i + b * f * g + c * d * h - c * e * g)

def getTriangleArea3D(a,b,c):
	return getTriangleArea3DCoords(a.x,a.y,a.z,b.x,b.y,b.z,c.x,c.y,c.z)

def getTriangleArea3DCoords(xa,ya,za,xb,yb,zb,xc,yc,zc):
	return 0.5 * math.sqrt(math.pow(determinant(xa, xb, xc, ya, yb, yc, 1, 1, 1), 2) + math.pow(determinant(ya, yb, yc, za, zb, zc, 1, 1, 1), 2) + math.pow(determinant(za, zb, zc, xa, xb, xc, 1, 1, 1), 2))

def getFaceArea(face):
	if(len(face.vertices) == 3):
		return getTriangleArea3D(face.vertices[0],face.vertices[1],face.vertices[2])
	else:
		return getTriangleArea3D(face.vertices[0],face.vertices[1],face.vertices[2]) + getTriangleArea3D(face.vertices[1],face.vertices[2],face.vertices[3])

def getFacePerimeter(face):
	sum = 0;
	for i in range(len(face.vertices)):
		v1 = face.vertices[i]
		v2 = face.vertices[(i+1)%len(face.vertices)]
		sum += vec.VectorDistance(v1,v2)
	return sum

def getFaceVerticality(face):
	normal = vec.VectorNormalFromVertices(face.vertices)
	return math.atan2(normal[1] * normal[1], normal[0] * normal[0])