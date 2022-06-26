from lib2to3.pytree import convert


def main():
    faces=input()
    face_convert=convert(faces)
    print(face_convert)
def convert(faces):
    face1=faces.replace(":)","🙂")
    face2=face1.replace(":(","☹️")
    face3=face2.replace("^_^","😊")
    return face3
main()