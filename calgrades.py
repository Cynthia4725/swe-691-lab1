def calculate_grade(scores):
    # แก้ Bug ที่ 1: ตรวจสอบว่าลิสต์ว่างหรือไม่
    if not scores:
        return "No Data", 0  # หรือส่งค่า None กลับไปเพื่อบอกว่าไม่มีข้อมูล
    
    # การปรับปรุง: ใช้ sum() แทนการเขียน loop เอง (เร็วกว่าและสั้นกว่า)
    total = sum(scores)
    
    # คำนวณค่าเฉลี่ย
    average = total / len(scores)
    
    # การตัดเกรด (โครงสร้างเดิมถูกต้องแล้ว แต่ระวังเรื่องคะแนนที่เกิน 100)
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return grade, average

# --- ทดสอบการทำงาน ---

# กรณีปกติ
scores1 = [85, 92, 78, 88, 95]
print(f"ผลลัพธ์ปกติ: {calculate_grade(scores1)}")

# กรณีลิสต์ว่าง (เพื่อทดสอบการแก้ Bug)
scores2 = []
print(f"ผลลัพธ์เมื่อลิสต์ว่าง: {calculate_grade(scores2)}")
