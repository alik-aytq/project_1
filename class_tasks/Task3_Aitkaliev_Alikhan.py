import cv2 as cv

car_img=cv.imread('mitsubishi_car.png')
logo_img=cv.resize(cv.imread('logo.png'),(120,120))

rows,cols,channels=logo_img.shape
roi=car_img[(480-rows):480,(800-cols):800]

logo2gray=cv.cvtColor(logo_img,cv.COLOR_BGR2GRAY)
ret,mask=cv.threshold(logo2gray,10,255,cv.THRESH_BINARY)
mask_inv=cv.bitwise_not(mask)

car_bg=cv.bitwise_and(roi,roi,mask=mask_inv)
logo_fg=cv.bitwise_and(logo_img,logo_img,mask=mask)

dst=cv.add(car_bg,logo_fg)
car_img[(480-rows):480,(800-cols):800]=dst

cv.imshow('Image',car_img)
cv.waitKey(0)

