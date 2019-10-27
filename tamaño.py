from PIL import Image
img = Image.open("acromior.JPEG")
img.save("acromior2.PNG")
new_img=img.resize((480,640))
new_img.save("acromior2.PNG","PNG")
