import cv2
import numpy as np
from copy import deepcopy

def main(args=None):
    file_name = "./camera.png"
    img = cv2.imread(file_name)
    original_image = deepcopy(img)
    cv2.imshow("original", original_image)
    
    src_list = np.float32([
        [488, 192],
        [580, 192],
        [142, 373],
        [820, 373]    ])
    
    dst_list = np.float32([
     [0, 0],
     [480, 0],
     [0, 480],
     [480, 480]   
    ])
    
    M =cv2.getPerspectiveTransform(src_list, dst_list)
    warp_img = cv2.warpPerspective(img, M, (480, 480), flags=cv2.INTER_LINEAR)
    cv2.imshow("warapped imaged", warp_img)
    cv2.waitKey(0)

    return 0    

if __name__ == '__main__':
    main()