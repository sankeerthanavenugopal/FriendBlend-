import numpy as np
import cv2 as cv
import os

dir = os.path.dirname(__file__)
cat = cv.imread(dir+"\\..\\data\\inputs\\cat.jpg")

cat_hls = cv.cvtColor(cat, cv.COLOR_BGR2HLS)
cat_hls[:,:,0] = (cat_hls[:,:,0] + 120)%360
cat_2 = cv.cvtColor(cat_hls, cv.COLOR_HLS2BGR)

cv.imshow("cat", cat)
cv.imshow("cat_hls", cv.cvtColor(cat_hls, cv.COLOR_HLS2BGR))


# Blends between columns start and end
def alpha_blend(img_left, img_right, start, end):
    end = end+1  # Include the last column in computation
    step_size = 1.0/(end-start)
    img_left_cut = img_left[:,start:end,:]
    img_right_cut = img_right[:,start:end,:]
    
    alpha = np.arange(0, end-start)*step_size
    alpha = np.reshape(alpha,(1,-1,1))

    out_mid = img_left_cut*(1-alpha) + img_right_cut*(alpha)
    
    out = img_left.copy()
    out[:,start:end,:] = out_mid
    out[:,end:,:] = img_right[:,end:,:]

    return out

blended = alpha_blend(cat, cat_2, 200, 400)

cv.imshow("blended", blended)

cv.waitKey(0)
cv.destroyAllWindows()
