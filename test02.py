from itertools import permutations

# เก็บข้อมูลยอดซื้อ
straight_sales = {f"{i:03}": 0 for i in range(1000)}  # เลขตรง
tod_sales = {f"{i:03}": 0 for i in range(1000)}       # เลขโต๊ด

def get_tod_group(number):
    """คืนชุดเลขโต๊ดจากเลข 3 หลัก เช่น 123 -> [123, 132, 213, 231, 312, 321]"""
    return set("".join(p) for p in permutations(number))

def buy_number():
    while True:
        print("\n📌 กด 1 = ซื้อเลข | 2 = ดูประวัติยอดซื้อเกิน 50 | 0 = ออกจากระบบ")
        choice = input("เลือกคำสั่ง: ").strip()

        if choice == '0':
            print("👋 ออกจากระบบเจ้ามือแล้วครับ")
            break

        elif choice == '1':
            number = input("กรอกเลขที่ต้องการซื้อ (000-999): ").strip()

            if number not in straight_sales:
                print("❌ เลขไม่ถูกต้อง ต้องเป็นเลข 000 ถึง 999 เท่านั้น")
                continue

            bet_type = input("เลือกประเภทการเดิมพัน: 'ตรง' หรือ 'โต๊ด': ").strip().lower()
            if bet_type not in ['ตรง', 'โต๊ด']:
                print("❌ ประเภทต้องเป็น 'ตรง' หรือ 'โต๊ด'")
                continue

            try:
                amount = int(input(f"กรอกจำนวนเงินที่ต้องการซื้อเลข {number} ({bet_type}): ").strip())
                if amount <= 0:
                    print("❌ จำนวนเงินต้องมากกว่า 0")
                    continue
            except ValueError:
                print("❌ กรุณากรอกจำนวนเงินเป็นตัวเลข")
                continue

            if bet_type == 'ตรง':
                straight_sales[number] += amount
                total = straight_sales[number]
                print(f"✅ ซื้อเลข {number} ตรง จำนวน {amount} บาท (รวมทั้งหมด: {total} บาท)")

                if total >= 50:
                    print(f"⚠️ เตือน: เลขตรง {number} ถูกซื้อรวม {total} บาท (≥ 50)")

            else:  # โต๊ด
                tod_sales[number] += amount
                group = get_tod_group(number)
                group_total = sum(tod_sales[n] for n in group)

                print(f"✅ ซื้อเลข {number} โต๊ด จำนวน {amount} บาท (ยอดรวมชุดโต๊ด: {group_total} บาท)")
                if group_total >= 50:
                    print(f"⚠️ เตือน: ชุดเลขโต๊ดของ {number} ถูกซื้อรวม {group_total} บาท (≥ 50)")

        elif choice == '2':
            print("\n📋 ประวัติเลขที่มียอดซื้อเกินหรือเท่ากับ 50 บาท:\n")

            found = False

            # ตรวจเลขตรง
            for num, total in straight_sales.items():
                if total >= 50:
                    print(f"🔸 เลขตรง {num} มียอดซื้อ {total} บาท")
                    found = True

            # ตรวจเลขโต๊ด (รวมทั้งกลุ่ม)
            checked_groups = set()
            for num in tod_sales:
                group = frozenset(get_tod_group(num))
                if group in checked_groups:
                    continue
                group_total = sum(tod_sales[n] for n in group)
                if group_total >= 50:
                    group_str = ', '.join(sorted(group))
                    print(f"🔹 เลขโต๊ดกลุ่ม {group_str} มียอดซื้อรวม {group_total} บาท")
                    found = True
                checked_groups.add(group)

            if not found:
                print("📭 ไม่มีเลขใดที่มียอดซื้อเกินหรือเท่ากับ 50 บาท")

        else:
            print("❌ คำสั่งไม่ถูกต้อง กรุณาเลือก 0, 1 หรือ 2")
buy_number()