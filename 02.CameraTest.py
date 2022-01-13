import cv2

capture = cv2.VideoCapture(0) # 내장카메라는 0, 외장 카메라는 1~n
# capture.set(propid, value)-> 카메라 속성(propid), 값(value) 설정 메서드
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # propid -> 카메라 설정 , value -> 값
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480) # 가로 640, 세로 240

# 어떤키라도 입력되기 전까지 33ms마다 반복문 실행함
while cv2.waitKey(33)<0: # 프레임을 지속적으로 받아옴 | cv2.waitKey() -> 키입력 대기함 : 지정된 시간동안 키입력이 있을때까지 프로그램지연
                         # 입력된 키의 아스키코드 반환
    ret, frame = capture.read() # capture.read() 프레임 읽기 메스드로 카메라 상태,프레임 받아옴, ret:카메라 상태저장, 정상(True), 작동안할때(false), frame:현재시점 프레임 저장
    cv2.imshow("카메라다아ㅏ", frame) # 이미지 표시 함수 cv2.imshow(), 창 제목(winname)과 이미지(mat)할당
                                    # winname : 문자열 표시, 문자열은 변수와 비슷한 역할 | mat : 위도우 창에 할당할 이미지 의미
# elay가 0일 경우, 지속적으로 키 입력을 검사하여 프레임 안넘어감
# while cv2.waitKey(33) != ord('q'):으로 사용할 경우, q가 입력될 때 while문을 종료


capture.release() # 메모리 해제 메서드(카메라 장치에서 받아몬 메모리 해제ㄹ)
cv2.destroyAllWindows() # 모든 위도우 창 닫음
# 특정 윈도우 창만 닫는다면, cv2.destroyWindow(winname)