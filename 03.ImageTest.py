import cv2
image = cv2.imread("Image/Mybin.jpg", cv2.IMREAD_ANYCOLOR)
#이미지 함수(cv2.imread)를 통해 로컬경로 이미지 읽기
# cv2.IMREAD_ANYCOLOR = 원본사용 = falages : 이미지 불러올때 적용 상태(다른 플래그는 검색 ㄱㄱ 종류 多)
cv2.imshow("bin",image) # 이미지 표시 함수(cv2.imshow), bin은 윈도우 타이틀
cv2.waitKey() # 키 입력 대기 함수(cv2.waitkey) -> 키입력시 종료
cv2.destroyAllWindows() # 모든 창 제거 함수(cv2.destroyAllWindows)

height, width, channel = image.shape
print(height, width, channel) #높이, 너비, 채널->색상정보
#채널 1 : 단색(흑백), 3 : 다색(RGB)