import cv2
import numpy as np

canvas = np.full((512, 512, 3), 255, dtype=np.uint8)
old_x, old_y = -1, -1


def mouse_callback(event, x, y, flags, param):
    global old_x, old_y

    # 마우스 클릭 시 이전 좌표 생성
    if event == cv2.EVENT_LBUTTONDOWN:
        old_x, old_y = x, y
    
    # 마우스 이동 시
    elif event == cv2.EVENT_MOUSEMOVE:
        # 마우스가 눌린 상태일때
        if flags & cv2.EVENT_FLAG_LBUTTON:
            # 이 전 좌표가 있을 때만 그리기
            if old_x != -1 and old_y != -1 :
                cv2.line(canvas, (old_x, old_y), (x, y), (0, 0, 0), 2)
                old_x, old_y = x, y
                cv2.imshow('canvas', canvas)

    elif event == cv2.EVENT_LBUTTONUP:
        old_x, old_y = -1, -1


cv2.namedWindow('canvas')
cv2.setMouseCallback('canvas', mouse_callback)


while True :
    cv2.imshow('canvas', canvas)
    key = cv2.waitKey(1) & 0xFF

    # (0, 0) ~ (end, end) 전부 흰색으로 다시 채우기
    if key == ord('c') or key == ord('C') :
        canvas[:] = 255

    elif key == ord('q') or key == ord('Q') or key == 27 :
        break


cv2.destroyAllWindows()