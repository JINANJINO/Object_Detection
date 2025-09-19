############################################################
# Author : jinhanlee
# Date   : 2025-09-19
############################################################

import cv2
import numpy as np

def lane_detection():
    file_name = "./camera.png"
    img = cv2.imread(file_name)
    if img is None:
        print("이미지 파일을 찾을 수 없습니다. 경로를 확인하세요.")
        return

    # 원본 이미지 출력
    cv2.imshow("Original", img)

    # BEV transform
    src_list = np.float32([
        [488, 192], [580, 192], [142, 373], [820, 373]
    ])
    dst_list = np.float32([
        [0, 0], [480, 0], [0, 480], [480, 480]
    ])
    M = cv2.getPerspectiveTransform(src_list, dst_list)
    bev = cv2.warpPerspective(img, M, (480, 480), flags=cv2.INTER_LINEAR)
    cv2.imshow("BEV", bev)

    # ================= Canny Edge Detection =================
    gray_bev = cv2.cvtColor(bev, cv2.COLOR_BGR2GRAY)
    
    blurred_bev = cv2.GaussianBlur(gray_bev, (5, 5), 0)
    edges = cv2.Canny(blurred_bev, 50, 150)
    cv2.imshow('Edges (BEV)', edges)

    # ================= Hough Transform =================
    lines = cv2.HoughLines(edges, 1, np.pi/180, 150)  
    edges_hough = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR) 
    if lines is not None:
        for rho, theta in lines[:,0]:
            a, b = np.cos(theta), np.sin(theta)
            x0, y0 = a*rho, b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            cv2.line(edges_hough, (x1, y1), (x2, y2), (0, 0, 255), 2)
            
    linesP = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=25, minLineLength=20, maxLineGap=60)
    if linesP is not None:
        for x1, y1, x2, y2 in linesP[:,0]:
            cv2.line(edges_hough, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imshow('Detected Lanes', edges_hough)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

lane_detection()
