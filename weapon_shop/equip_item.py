# =====================================================
#  weapon_shop/equip_item.py — คนรับผิดชอบ: PETCHYPRETTYBOY
# =====================================================

def equip_item(person, weapon):
    if person["money"] < weapon["price"]:
        return {"status": False, "message":("ซื้อไม่ได้เงิน ไม่พอ")}
    elif person["equipment"]!= "ไม่มี" :
        return {"status": False, "message":("ใส่เพิ่มไม่ได้ มีอาวุธแล้ว")}
    else:
        person["money"] -= weapon["price"]
        person["equipment"] = weapon["name"]
        person["power"] += weapon["bonus"]
        return {"status": True, "message": "ซื้อเส้รจแล้ว"}



# ทดสอบ: python -m weapon_shop.equip_item
if __name__ == "__main__":
    vito = {"name": "Vito", "money": 60000, "power": 5, "equipment": "ไม่มี"}
    gun = {"name": "ปืนพก 9mm", "price": 50000, "bonus": 5}

    # print(equip_item(vito, gun))   # ต้องได้ status True
    print(vito)                    # เงินเหลือ 10000, power เป็น 10, equipment เป็นปืน
    print(equip_item(vito, gun))   # ครั้งที่สองต้องได้ status False (มีอาวุธแล้ว)
    print(vito)    