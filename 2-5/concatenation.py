import cv2

try:
    img_1 = cv2.imread('./001_001.jpg')
    img_2 = cv2.imread('./002_001.jpg')
    img_3 = cv2.imread('./003_001.jpg')
    img_4 = cv2.imread('./004_001.jpg')
    img_5 = cv2.imread('./005_001.jpg')

    images = cv2.vconcat([img_1, img_2, img_3, img_4, img_5])

    cv2.imwrite('images.jpg', images)
except Exception as e:
    print(e)
