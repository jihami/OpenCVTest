import cv2

capture = cv2.VideoCapture("Image/KnowMe(ft.DEAN).mp4") # cv2.VideoCapture(비디오 출력)
while cv2.waitKey(33)<0:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0) #0->false
    # 비디오 속성 반환 메서드(capture.get)으로 속성 반환
    # 현재 프레임수(cv2.CAP_PROP_POS_FRAME) 와 총 프레임수(cv2.CAP_PROP_FRAME_COUNT)를 받아옴 둘이 같다면 현재 재생프레임은 가장 마지막 프레임이됨

    ret, frame = capture.read()
    cv2.imshow("Video ze long", frame)

capture.release() # 장치를 닫고 메모리 해제
cv2.destroyAllWindows()