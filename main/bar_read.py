import cv2
import pyzbar.pyzbar as pyzbar
from django.conf import settings

def bar_read(path):
    img = cv2.imread(path)

    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    decoded = pyzbar.decode(imgray)

    for d in decoded:
        cv2.rectangle(img, (d.rect[0], d.rect[1]), (d.rect[0]+d.rect[2], d.rect[1]+d.rect[3]), (0,0,255), 2)
        return d.data.decode('utf-8')
    cv2.imwrite(path, img)
    

# print(bar_read("C:/Users/User/Desktop/private/Practice_code/images/test_bar1.jpg"))

# img = cv2.imread("C:/Users/User/Desktop/private/Practice_code/images/test_bar1.jpg")

# imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# decoded = pyzbar.decode(imgray)

# print(decoded)

# for d in decoded:
#     print(d.data.decode('utf-8'))
#     print(d.type)
    
#     cv2.rectangle(img, (d.rect[0], d.rect[1]), (d.rect[0]+d.rect[2], d.rect[1]+d.rect[3]), (0,0,255), 2)


# cv2.imshow("imgray", img)
# cv2.waitKey(0)


# cnt = 2
# def bar_reading():
#     img_file = "C:/Users/User/Desktop/private/Practice_code/images/test" + str(cnt) + '.jpg'
#     image = cv2.imread(img_file)
#     cv2.imshow("img"+str(cnt), image)
#     cv2.waitKey(0)
#     cnt += 1

# bar_reading()
# bar_reading()