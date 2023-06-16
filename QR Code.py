import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer
from qrcode.image.styles.colormasks import SquareGradiantColorMask
import cv2
from PIL import Image


#####    CREATING A QR-Code OBJECT     #####
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,
)


#####    TAKING USER INPUT    #####
flag=1
while(flag!=0):
    choice=int(input("Enter 1- To enter manual data. \n      2- To enter website address. "))
    
    if(choice==1):
        flag=0
        Name=input("\nEnter the name of person- ")
        Email=input("Enter the email address- ")
        Ph=input("Enter phone number- ")
        data= "\nThe Details inside are---\nNAME- {}\nEmail ID- {}\nPhone Number- {}".format(Name,Email,Ph)
    elif(choice==2):
        flag=0
        data=input("\nEnter website address:- ")
    else:
        print("Enter correct choice.")


#####    CREATING QR-code(Adding Data & Styling) & a LOCATION(png/svg format) TO SAVE QR-CODE IMAGE    #####
path="QR-code.png"
qr.add_data(data=data)
qr.make(fit=True)

# qr_img= qr.make_image(fill_color="black",back_color="white")               #-->> If only QR-code generated with 2 colors                            

qr_img = qr.make_image(image_factory=StyledPilImage,module_drawer=CircleModuleDrawer(),color_mask=SquareGradiantColorMask(back_color=(255,255,255),center_color=(102,178,255),edge_color=(0,0,255)))                                                  #-->> If QR-Code generated with Styling applied

qr_img.save(path)


#####   SHOWING THE QR-CODE IMAGE IN Pop-Up WINDOW   #####
qr=Image.open(path)                                                           #-->> QR-Code saved file opened
img=Image.open("linkedin-logo-linkedin-icon-transparent-free-png.webp")
img.thumbnail((150,150))
img.save("linkedin-logo-linkedin-icon-transparent-free-png_100.webp")         #-->> Overlap icon saved with new dimensions
qr=qr.convert("RGBA")
img=img.convert("RGBA")
width=(qr.width-img.width)//2
height=(qr.height-img.height)//2
qr.paste(img,(width,height),img)                                  #-->> Overlappng image added above the QR-code generated
qr.save(path,fromat="png")
qr.show()


#####    DECODING THE QR-CODE AGAIN TO FETCH DETAILS    #####
qr_img=cv2.imread(path)
detect=cv2.QRCodeDetector()
val,pts,st_code=detect.detectAndDecode(qr_img)
print("The details inside are:-\n",val)