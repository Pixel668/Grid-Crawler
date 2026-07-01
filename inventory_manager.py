# inventory_manager.py
# tracking player items in a list of dicts.
# includes some basic sorting and item lookup from configs.

class InventoryManager:
    def __init__(self, max_slots=20):
        self.inventory_list = []
        self.max_slots = max_slots
        print(f"inventory initialized with {max_slots} slots. dont carry too much.")
        
    def add_item_to_bag(self, item_id, config_module_or_name):
        if len(self.inventory_list) >= self.max_slots:
            print("inventory full!! drop something first.")
            return False
        
        # if second arg is a string, we just create a dummy item for the shop system.
        if isinstance(config_module_or_name, str):
            new_item = {
                'item_id': item_id,
                'name': config_module_or_name,
                'type': 'consumable',
                'weight': 1
            }
            self.inventory_list.append(new_item)
            print(f"added {config_module_or_name} to bag.")
            return True
        
        config_module = config_module_or_name
        # scan the different config modules to find the right item data.
        item_data = None
        if hasattr(config_module, 'weapons') and item_id in config_module.weapons:
            item_data = config_module.weapons[item_id]
            item_data['type'] = 'weapon'
        elif hasattr(config_module, 'armor_sets') and item_id in config_module.armor_sets:
            item_data = config_module.armor_sets[item_id]
            item_data['type'] = 'armor'
        elif hasattr(config_module, 'consumables') and item_id in config_module.consumables:
            item_data = config_module.consumables[item_id]
            item_data['type'] = 'item'
            
        if item_data:
            # shallow copy so changes in bag dont hit the global config.
            new_item = {}
            for key in item_data:
                new_item[key] = item_data[key]
            self.inventory_list.append(new_item)
            itemName = new_item.get('name') or new_item.get('armor_name') or new_item.get('item_name')
            print(f"added {itemName} to bag.")
            return True
        else:
            print(f"couldnt find item {item_id}... maybe a glitch??")
            return False
    def remove_item(self, item_index):
        # using index because item IDs might not be unique in the list.
        if 0 <= item_index < len(self.inventory_list):
            removed = self.inventory_list.pop(item_index)
            print(f"remndex {item_index}")
            return removed
        else:
            print("index out of range. what are u trying to do??")
            return None
        
    def remove_item_from_bag(self, slot_number):
        # slot_number is 1-indexed for player friendliness
        # this is used by the shop system for selling
        idx = slot_number - 1
        if 0 <= idx < len(self.inventory_list):
            removed = self.inventory_list.pop(idx)
            item_id = removed.get('item_id', 0)
            print(f"removed {removed.get('name', '???')} from slot {slot_number}.")
            return item_id
        else:
            print(f"slot {slot_number} is empty or doesn't exist.")
            return None
        
    def use_healing_item(self):
        # finds the first consumable item in the bag and removes it.
        # returns True if something was used, False if bag is empty.
        for i, item in enumerate(self.inventory_list):
            if item.get('type') == 'consumable' or item.get('type') == 'item':
                removed = self.inventory_list.pop(i)
                name = removed.get('name') or removed.get('item_name') or 'Unknown Item'
                print(f"used {name} from inventory.")
                return True
        print("no usable healing items in bag.")
        return False
    
    def sort_inventory_by_weight_clunky(self):
        # manual bubble sort for sorting bag by weight.
        n = len(self.inventory_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                # some items have weight, some don't. gotta check everything.
                w1 = self.inventory_list[j].get('weight', 0)
                w2 = self.inventory_list[j+1].get('weight', 0)
                
                if w1 > w2:
                    # swap 'em!
                    temp = self.inventory_list[j]
                    self.inventory_list[j] = self.inventory_list[j+1]
                    self.inventory_list[j+1] = temp
        
        print("inventory sorted by weight (kinda). it was a lot of work but it's done.")
        
    def debug_print_inventory(self):
        # utility to dump the current bag contents to console.
        print("--- BAG CONTENT ---")
        for i, item in enumerate(self.inventory_list):
            name = item.get('name') or item.get('armor_name') or item.get('item_name')
            print(f"[{i}] {name} (Type: {item.get('type')})")
        print("-------------------")
        
