import mola.core 

def importOBJMesh(filename):
    """Loads a Wavefront OBJ file. """
    mesh=Mesh()
    for line in open(filename, "r"):
        if line.startswith('#'): continue
        values = line.split()
        if not values: continue
        if values[0] == 'v':
            v = map(float, values[1:4])
            mesh.vertices.append(Vertex(v[0],v[1],v[2]))
        elif values[0] == 'f':
            face = Face([])
            for v in values[1:]:
                w = v.split('/')
                vertex=vertices[int(w[0])-1]
                face.vertices.append(vertex)
                mesh.faces.append(face)
    return mesh

def importOBJFaces(filename):
    """Loads a Wavefront OBJ file. """
    vertices = []
    faces = []
    for line in open(filename, "r"):
        if line.startswith('#'): continue
        values = line.split()
        if not values: continue
        if values[0] == 'v':
            v = map(float, values[1:4])
            vertices.append(Vertex(v[0],v[1],v[2]))
        elif values[0] == 'f':
            face = Face([])
            for v in values[1:]:
                w = v.split('/')
                vertex=vertices[int(w[0])-1]
                face.vertices.append(vertex)
                faces.append(face)
    return faces

def exportOBJMeshWithColors(mesh,fileNameOBJ,fileNameMTL):
    exportOBJFacesWithColors(mesh.faces,fileNameOBJ,fileNameMTL)

def exportOBJFacesWithColors(faces,fileNameOBJ,fileNameMTL):
    file = open(fileNameOBJ, "w")
    file.write("mtllib ./"+fileNameMTL+"\n");
    fileMTL = open(fileNameMTL, "w")
    vertexCount=0
    materials=set()
    vertices={}
    for face in faces:
        materials.add(face.color)
        file.write("usemtl material"+str(face.color)+"\n")
        faceString="f"
        for p in face.vertices:
            ptuple=(p[0],p[1],p[2])
            if ptuple in vertices:
                faceString+=" "+str(vertices[ptuple])
            else:
                vertexCount+=1
                faceString+=" "+str(vertexCount)
                vertices[ptuple]=vertexCount
                file.write("v "+str(p.x)+" "+str(p.y)+" "+str(p.z)+"\n")
        faceString+="\n"
        file.write(faceString)
    file.close()
    for mat in materials:
        fileMTL.write("newmtl material"+str(mat)+"\n");
        fileMTL.write("Kd "+str(mat[0])+" "+" "+str(mat[1])+" "+str(mat[2])+"\n");
    fileMTL.close()