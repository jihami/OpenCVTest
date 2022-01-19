import cv2

src = cv2.imread("Image/Mybin.jpg",cv2.IMREAD_COLOR)
height, width, channel = src.shape

dst = cv2.pyrUp(src, dstsize=(width*2, height*2), borderType=cv2.BORDER_DEFAULT) # pyrUp()이미지 확대 함수, borderType(테투리 외삽법)
# 테두리 외삽법은 이미지 밖의 픽셀을 외삽하는 데 사용되는 테두리 모드로, 외삽 방식 설정 -> 이미지 밖 회색 부분
dst2 = cv2.pyrDown(src) # pyrDown()이미지 2배 축소함수
# 외삽법 종류 https://076923.github.io/posts/Python-opencv-7/#%ED%94%BD%EC%85%80-%EC%99%B8%EC%82%BD%EB%B2%95-%EC%A2%85%EB%A5%98

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()