import cv2
src = cv2.imread("Image/Mybin.jpg", cv2.IMREAD_COLOR) # 경로 읽어옴

height, width, channe1 = src.shape # 높이, 너비, 채널 값 저장, 높이와 너비를 이용해 회전 중심점 설정
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1) # 높이, 너비, 회전중심점
# matrix = cv2.getRotationMatrix2D(center, angle, scale) 중심점, 각조 비율로 매핑 변환 행렬(matrix)을 생성함
dst = cv2.warpAffine(src, matrix, (width, height))
# dst = cv2.warpAffine(src, M, dsize)는 원본 이미지(src)에 M(아핀 맵 행렬)을 적용하고 출력 이미지 크기(dsize)로 변형해서 출력 이미지(dst)
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
