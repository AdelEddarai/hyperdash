import face_alignment
from skimage import io

face = face_alignment.FaceAlignment(face_alignment.LandmarksType._3D, flip_input=False)
input = io.imread('adel.png')
pred = face.get_landmarks(input)