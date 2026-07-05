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

def display_shop_menu(player_gold):
    print("\n" + "=" * 55)
    print("  SHOP -- Welcome traveler. Gold is the only language here.")
    print(f"  Your gold: {player_gold} G")
    print("=" * 55)
    print(f"  {'#':<4} {'Item':<28} {'Buy':>6}  {'Sell':>6}")
    print("-" * 55)
    for slot_id, item in SHOP_INVENTORY.items():
         print(f"  {slot_id:<4} {item['name']:<28} {item['buy_price']:>5}G  {item['sell_price']:>5}G")
    print("=" * 55)
    print("  Commands: 'buy <number>', 'sell <number>', 'leave'")
    print("=" * 55)
    
def handle_shop_session(player, inventory_manager):
    # runs a shop loop. player can buy/sell until they type 'leave'.
    # player needs gold attribute. inventory manager handles adding iTEMS.
    
    if not hasattr(player, 'gold'):
        print("somehow ur player has no gold attribute. that's a bug. sorry.")
        return
    
    coords = (player.x_pos, player.y_pos)
    if not is_shop_zone(player.x_pos, player.y_pos):
        print("there's no shop here. try heading to a town zone.")
        return
        
    display_shop_menu(player.gold)
    
    while True:
        try:
            raw = input("\nshop > ").lower().strip()
        except (EOFError, KeyboardInterrupt):
            print("\nleaving shop.")
            break
        
        if raw == "leave" or raw == "exit" or raw == "back":
            print("you leave the shop. the shopkeeper gives you a neutral nod.")
            break
        
        elif raw.startswith("buy "):
            parts = raw.split()
            if len(parts) < 2:
                print("buy what? type 'buy <number>'.")
                continue
            try:
                slot = int(parts[1])
            except ValueError:
                print("that's not a valid number lol.")
                continue
            
            if slot not in SHOP_INVENTORY:
                print(f"slot {slot} doesn't exist. look at the menu again.")
                continue
            
            chosen = SHOP_INVENTORY[slot]
            cost = chosen["buy_price"]
            
            if player.gold < cost:
                                print(f"u only have {player.gold}G. that costs {cost}G. not enough.")
                cont            # try to add to inve            added = inventory_manager.add_item_to_bag(chosen["item_id"], chosen["name"])
            if added:
                player.gold -= cost
                print(f"bought {chosen['name']} for {cost}G. gold remaining: {player.gold}G")
            else:
                print("ur bag is full. use or drop something first.")
        
        elif raw.startswith("sell "):
            # selling items. i'll refine the inventory manager hook later.
            parts = raw.split()
            if len(parts) < 2:
                print("sell what? type 'sell <inventory slot number>'.")
                continue
            try:
                inv_slot = int(parts[1])
            except ValueError:
             print("not a number.")
                continue
            
            removed = inventory_manager.remove_item_from_bag(inv_slot)
            if removed:
                # find sell price from shop inventory, or default to 10
                sell_val = 10
                                for s_item in SHOP_INVENTORY.values():
                      if s_item["item_id"] == removed:
                        sell_val = s_item["sell_price"]
                        break
                player.gold += sell_val
        