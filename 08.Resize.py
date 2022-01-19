import cv2

src = cv2.imread("Image/Mybin.jpg", cv2.IMREAD_COLOR)

# dst = destination(목적지) -> 함수가 실행되고 도착할 곳
dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA) # resize() 이미지 크기 조절함수
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)
# dst = cv2.resize(src, dstSize, fx, fy, interpolation) -> 입력 이미지(src), 절대 크기(dstSize), 상대 크기(fx, fy), 보간법(interpolation)으로 출력 이미지(dst) 생성
# 상대크기는 절대크기(0,0)할당 후 상대크기 할당 -> fx,fy가 계산된 사이즈가 dsize에 할당
# dsize.width = round(fx X src.cols) | dsixe.height = round(fy X src.rows)
# fx = dsixe.width/src.cols | fy = dsize.height/src.rows
# 보간법 속성 https://076923.github.io/posts/Python-opencv-8/#%EC%B6%94%EA%B0%80-%EC%A0%95%EB%B3%B4
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()