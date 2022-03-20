### Note: Convertion of image(s) to pencil sketch ###

import cv2     # import cv2 module to handle image manipulation

# Enter your image file here and run
# File to convert has the same location with the python code location
img_var = 'image_filename_here.jpg'

# Load the image and display the image to be converted
image1 = cv2.imread(img_var, cv2.IMREAD_UNCHANGED)     # Load the image from variable
frame1_title = 'Original image : '+str(img_var)        # window frame title
cv2.imshow(frame1_title, image1)                       # display the image from variable

# convert the image to gray scale
img2gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
img_new = cv2.bitwise_not(img2gray)
blur = cv2.GaussianBlur(img_new, (21, 21), 0)        # smoothens image with GaussianBlur()
# blur = cv2.bilateralFilter(img_new, 9, 75, 75)     # smoothens image with bilateralFilter()
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(img2gray, invertedblur, scale = 256.0)

fname=input("\nType in file name to save: ")
new_var = str(fname)+'.png'                           # store new file to variable
print("Saved to file name "+new_var)
cv2.imwrite(new_var, sketch)                          # save the image to new image file
image2 = cv2.imread(new_var)                          # read the new image file
frame2_title = 'Sketch image : '+str(new_var)         # new window frame title

# display the new image
cv2.imshow(frame2_title, image2)                      # display the sketched new image
cv2.waitKey(0)                                        # use waitkey() to prevent Python kernel to crash
cv2.destroyAllWindows()                               # close all windows
