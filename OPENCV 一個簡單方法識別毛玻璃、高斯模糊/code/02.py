import cv2
def variance_of_laplacian(image):
  return cv2.Laplacian(image, cv2.CV_64F).var()

imagePath = “test.jpg”
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fm = variance_of_laplacian(gray)
if fm < 100:
    print("Blurry")