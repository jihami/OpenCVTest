import cv2
src = cv2.imread("Image/Mybin.jpg", cv2.IMREAD_COLOR)
dst = cv2.flip(src, 0) #cv2.flip()대칭함수로 이미지 대칭가능
# flipCode < 0 : XY축 (상하좌우)
# flipCode = 0 : X축 (상하)
# flipCode > 0 : Y축 (좌우)

cv2.imshow("src",src)
cv2.imshow("dst", dst) # cv2.imshow()함수는 동일한 이미지여도 여러개 ㅆㄱㄴ

cv2.waitKey() # 키 입력대기
cv2.destroyAllWindows() # 키 입력되면 모든창 닫음