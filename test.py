# เจ้ามือหวยใต้ดินเวอร์ชันพื้นฐาน

# สร้าง dictionary เพื่อเก็บยอดซื้อเลข 000-999
lotto_sales = {f"{i:03}": 0 for i in range(1000)}

def buy_number():
    while True:
        number = input("กรอกเลขที่ต้องการซื้อ (000-999 หรือ 'exit' เพื่อออก): ").strip()

        if number.lower() == 'exit':
            print("ออกจากระบบแล้วครับ")
            break

        # ตรวจสอบว่าเป็นเลข 3 หลัก
        if number not in lotto_sales:
            print("❌ เลขไม่ถูกต้อง ต้องเป็นเลข 000 ถึง 999 เท่านั้น")
            continue

        try:
            amount = int(input(f"กรอกจำนวนเงินที่ต้องการซื้อเลข {number}: ").strip())
            if amount <= 0:
                print("❌ จำนวนเงินต้องมากกว่า 0")
                continue
        except ValueError:
            print("❌ กรุณากรอกจำนวนเงินเป็นตัวเลข")
            continue

        # บวกยอดซื้อ
        lotto_sales[number] += amount

        if lotto_sales[number] >= 50:
            print(f"⚠️ เตือน: เลข {number} มียอดซื้อรวม {lotto_sales[number]} บาท ซึ่งเกินหรือเท่ากับ 100 บาทแล้ว")
        else:
            print(f"✅ ซื้อเลข {number} จำนวน {amount} บาท เรียบร้อย (ยอดรวม: {lotto_sales[number]} บาท)")

# เรียกใช้งานฟังก์ชัน
buy_number()