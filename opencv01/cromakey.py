import cv2
import numpy as np

dog = cv2.imread('dog.jpg')
dog = cv2.resize(dog, (512, 512))
lena = cv2.imread('lena.jpg')
lena = cv2.resize(lena, (512, 512))

# ㅡㅡㅡㅡ 마스크 설정 ㅡㅡㅡㅡ
# 차원 분리
hsv = cv2.cvtColor(dog, cv2.COLOR_BGR2HSV)

# 범위 설정
low_green = np.array([25, 25, 25])
high_green = np.array([90, 255, 255])

mask = cv2.inRange(hsv, low_green, high_green)

# 색상 반전
invert = cv2.bitwise_not(mask)

# 대상 추출
result1 = cv2.bitwise_and(dog, dog, mask=invert)
cv2.imshow('result 1', result1)

result2 = cv2.bitwise_and(lena, lena, mask=mask)
cv2.imshow('result 2', result2)


# ㅡㅡㅡㅡ 영상 합성 ㅡㅡㅡㅡ
result3 = cv2.add(result1, result2)
cv2.imshow('result 3', result3)


cv2.waitKey()
cv2.destroyAllWindows()