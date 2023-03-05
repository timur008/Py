import cv2
from PIL import Image
image_path = 'FELV-cat.jpg'
cat_face_cascade = cv2.CascadeClassifier \
    ('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)
cat = Image.open(image_path)
hat = Image.open('cap.png')
cat = cat.convert('RGBA')
hat = hat.convert('RGBA')
for (x,y,w,h) in cat_face:
    hat = hat.resize((w, int(h)))
    cat.paste(hat, (x, int(y + h-420)), hat)
    cat.save('cat_with_hat1.png')
    cat_with_hat1 = cv2.imread('cat_with_hat1.png')
    cv2.imshow("Cat_with_hat", cat_with_hat1)
    cv2.waitKey()

image_path = 'cat.jpg'
cat = Image.open(image_path)
hat = Image.open('straw.png')
cat = cat.convert('RGBA')
hat = hat.convert('RGBA')
for (x,y,w,h) in cat_face:
    hat = hat.resize((w*2, int(h)))
    cat.paste(hat, (x-190, int(y + h-450)), hat)
    cat.save('cat_with_hat2.png')
    cat_with_hat2 = cv2.imread('cat_with_hat2.png')
    cv2.imshow("Cat_with_hat", cat_with_hat2)
    cv2.waitKey()

image_path = 'cat3.jpg'
cat = Image.open(image_path)
hat = Image.open('hat.png')
cat = cat.convert('RGBA')
hat = hat.convert('RGBA')
for (x,y,w,h) in cat_face:
    hat = hat.resize((w-70, int(h/3)))
    cat.paste(hat, (x+60, int(y + h-300)), hat)
    cat.save('cat_with_hat3.png')
    cat_with_hat3 = cv2.imread('cat_with_hat3.png')
    cv2.imshow("Cat_with_hat", cat_with_hat3)
    cv2.waitKey()