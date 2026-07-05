# shop_system.py
# simple shop system using zone-based coordinates to trigger.
# uses a global inventory for now, maybe add unique vendors later.

import config_items

# list of coords where the shop menu is accessible.
SHOP_ZONE_COORDS = [
    (0, 4),   # The Suburbs - Entrance
    (0, 6),   # The Suburbs - Mall
    (1, 3),   # Forest of the Forgotten Login
    (2, 2),   # Sandy Coast - Shop
    (3, 0),   # The Ancient Highlands - Market
    (3, 3),   # The Nexus Crossroads
    (4, 2),   # The Industrial Wasteland - Black Market
]

# hardcoded prices for game balance.
SHOP_INVENTORY = {
    1: {"item_id": 1, "name": "Minor Health Potion",      "buy_price": 25,  "sell_price": 10},
    2: {"item_id": 2, "name": "Health Potion",             "buy_price": 60,  "sell_price": 25},
    3: {"item_id": 3, "name": "Major Health Potion",       "buy_price": 140, "sell_price": 60},
    4: {"item_id": 4, "name": "Full Restore",              "buy_price": 300, "sell_price": 120},
    5: {"item_id": 5, "name": "Emergency Bandage",         "buy_price": 40,  "sell_price": 15},
    6: {"item_id": 6, "name": "Antidote",                  "buy_price": 50,  "sell_price": 20},
    7: {"item_id": 7, "name": "Burn Ointment",             "buy_price": 50,  "sell_price": 20},
    8: {"item_id": 8, "name": "Freeze Thaw Kit",           "buy_price": 65,  "sell_price": 25},
    9: {"item_id": 9, "name": "Iron Will Tablet",          "buy_price": 80,  "sell_price": 35},
       10: {"item_id": 10, "name": "Attack Boost Powder",      "buy_price": 90,  "sell_price": 40},
11: {"item_id": 11, "name": "Defense Capsule",          "buy_price": 90,  "sell_price": 40},
   12: {"item_id": 12, "name": "Escape Smoke",             "buy_price": 35,  "sell_price": 12},
}

def is_shop_zone(x, y):
    return (x, y) in SHOP_ZONE_COORDS

def 