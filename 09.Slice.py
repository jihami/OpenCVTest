import cv2

# src = cv2.imread("Image/Mybin.jpg", cv2.IMREAD_COLOR)
# dst = src[100:600, 200:700].copy()  # = 이런식으로 사용하면 원본이 망가져 .copy()를 이용해 깊은 복사(deep copy)를 사용
# # src 이미지에 src[높이(행), 너비(열)]로 관심 영역을 설정
# cv2.imshow("src", src)
# cv2.imshow("dst", dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

src = cv2.imread("Image/pawns.jpg", cv2.IMREAD_COLOR)

dst = src.copy()
roi = src[100:600, 200:700]
dst[0:500, 0:500] = roi
# dst[높이(행), 너비(열)] = roi를 이용해 dst 이미지 해당 영역 붙임

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()

#사진 사이즈 때문에 오류 났었음