from lib2to3.pytree import convert


def main():
    faces=input()
    face_convert=convert(faces)
    print(face_convert)
def convert(faces):
    face1=faces.replace(":)","đ")
    face2=face1.replace(":(","âšī¸")
    face3=face2.replace("^_^","đ")
    return face3
main()