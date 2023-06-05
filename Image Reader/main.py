import cv2 as cv

#------------

def rescaleFrame(frame, scale=0.15):

    #convert to int
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    #resize frame to a particular dimension
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


#read image
img = cv.imread('Images/image_1.jpg')
img_resize = rescaleFrame(img)

#display image
cv.imshow('image_1', img_resize)

cv.waitKey(0)

