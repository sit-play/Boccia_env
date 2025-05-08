import cv2
import numpy as np

# ฟังก์ชันสำหรับตรวจจับวัตถุสีน้ำเงินเข้ม
def detect_dark_blue_objects():
    # เริ่มต้นการจับภาพจากกล้อง
    cap = cv2.VideoCapture(0)
    
    while True:
        # อ่านภาพจากกล้อง
        ret, frame = cap.read()
        if not ret:
            break
            
        # แปลงภาพจาก BGR เป็น HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # กำหนดช่วงสีน้ำเงินเข้มใน HSV
        lower_blue = np.array([100, 150, 50])  # ค่าสีน้ำเงินเข้ม (H, S, V)
        upper_blue = np.array([140, 255, 255]) # ค่าสีน้ำเงินเข้ม
        
        # สร้าง mask สำหรับสีน้ำเงินเข้ม
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
        # ทำการกรอง noise ด้วย Gaussian Blur
        mask = cv2.GaussianBlur(mask, (5, 5), 0)
        
        # ค้นหา contours ใน mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # วาดกรอบรอบวัตถุที่ตรวจพบ
        for contour in contours:
            if cv2.contourArea(contour) > 500:  # กรอง contours ขนาดเล็ก
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # แสดงผลลัพธ์
        cv2.imshow('Original', frame)
        cv2.imshow('Mask', mask)
        
        # กด 'q' เพื่อออก
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # ปล่อยกล้องและปิดหน้าต่าง
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_dark_blue_objects()