# =====================================================
# weapon_shop/show_catalog.py — คนรับผิดชอบ: PETCHYPRETTYBOY
# =====================================================
from data import weapons_catalog

def show_catalog ():
    print("SHOW WEAPONS : ")
    for order in weapons_catalog:
        weapon = weapons_catalog[order]
        print (f"[{order}] {weapon['name']} | ราคา: {weapon['price']} พลัง: {weapon['bonus']}")


# if name == "main":
#     show_catalog()