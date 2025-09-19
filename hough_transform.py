import cv2
import numpy as np

# 1. 빈 이미지 생성
img = np.zeros((400, 400), dtype=np.uint8)

# 2. 흰 직선 몇 개 그리기
cv2.line(img, (50, 300), (350, 300), 255, 2)  #수평
cv2.line(img, (200, 50), (200, 350), 255, 2)  #수직
cv2.line(img, (50, 50), (350, 350), 255, 2)  #수평

# 3. Canny Edge 검출(Hough 변환 입력으로 사용)
edges = cv2.Canny(img, 50, 150, apertureSize=3)

# 4. 표준 Hough 변환
lines = cv2.HoughLines(edges, 1, np.pi/180, 150)

color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for rho, theta in lines[:,0]:
        a, b = np.cos(theta), np.sin(theta)
        x0, y0 = a*rho, b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(x0 - 1000*(a))
        cv2.line(color_img, (x1, y1), (x2, y2), (0, 0, 255), 1)
        
# 5. 확률적 Hough 변환
linesP = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=80, minLineLength=50, maxLineGap=10)

if linesP is not None:
    for x1, y1, x2, y2 in linesP[:,0]:
        cv2.line(color_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
# 6. 결과 출력
cv2.imshow("Input (with drawn lines)", img)
cv2.imshow("Edges", edges)
cv2.imshow("Detected Lines", color_img)
cv2.waitKey(0)
cv2.destroyAllWindows()