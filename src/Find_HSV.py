import cv2
import numpy as np

# ฟังก์ชันที่ไม่ทำอะไร (จำเป็นสำหรับ trackbars)
def nothing(x):
    pass

# สร้างหน้าต่างสำหรับ trackbars
cv2.namedWindow('Trackbars')
cv2.createTrackbar('HMin', 'Trackbars', 0, 179, nothing)
cv2.createTrackbar('SMin', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('VMin', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('HMax', 'Trackbars', 179, 179, nothing)
cv2.createTrackbar('SMax', 'Trackbars', 30, 255, nothing)
cv2.createTrackbar('VMax', 'Trackbars', 255, 255, nothing)

# เปิดกล้อง
cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()
    if not ret:
        print("ไม่สามารถอ่านภาพจากกล้องได้")
        break
    
    # แปลงภาพเป็น HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # อ่านค่าจาก trackbars
    h_min = cv2.getTrackbarPos('HMin', 'Trackbars')
    s_min = cv2.getTrackbarPos('SMin', 'Trackbars')
    v_min = cv2.getTrackbarPos('VMin', 'Trackbars')
    h_max = cv2.getTrackbarPos('HMax', 'Trackbars')
    s_max = cv2.getTrackbarPos('SMax', 'Trackbars')
    v_max = cv2.getTrackbarPos('VMax', 'Trackbars')
    
    # กำหนดขีดจำกัด HSV
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    
    # สร้าง mask
    mask = cv2.inRange(hsv, lower, upper)
    
    # แสดงภาพต้นฉบับและ mask
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    
    # ออกจากโปรแกรมเมื่อกด 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(f"Lower HSV: [{h_min}, {s_min}, {v_min}]")
        print(f"Upper HSV: [{h_max}, {s_max}, {v_max}]")
        break

# ปิดกล้องและหน้าต่าง
cap.release()
cv2.destroyAllWindows()