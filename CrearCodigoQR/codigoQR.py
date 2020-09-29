#pip install pillow qrcode 
#primero se debe intalar la siguietne libreria, para ubunto es sudo pip install pillow qrcode
from PIL import Image, ImageDraw
import qrcode
data="tE amo pinky"
img = qrcode.make(data)
img.save("./CrearCodigoQR/Test.png")    
