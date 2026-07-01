# string_helpers.py
# utility functions for handling strings and terminal UI.
# uses os.system for clearing screen and a custom typewriter print.
# includes box drawing for health bars, combat menu, and mini-map.

import os
import time
import sys

def clear_screen():
    # standard way to clear the terminal depending on the OS
    # cls for windows, clear for everything else.
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def typewriter_print(text, speed=0.012, end="\n"):
    # prints text character by character. 
    # makes the narrative feel more like a vintage RPG.
    # -- added TTY check so tests dont drag on forever.
    is_interactive = sys.stdout.isatty()
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if is_interactive:
            time.sleep(speed)
    sys.stdout.write(end)
    sys.stdout.flush()
    
def press_enter_to_continue():
    # just a helper so story text doesnt scroll away immediately.
    # -- added TTY check so headless tests dont hang.
    if sys.stdout.isatty():
        print("\n[ Press ENTER to continue... ]")
        try:
            input()
        except:
            pass
        
def clean_input_string(text):
    return text.strip().lower()

def sanitize_command_string(cmd):
    temp = cmd.strip()
    return temp.lower()

def draw_divider(style="="):
    print(style * 72)
    
def draw_hp_bar(current_hp, max_hp, width=22, label="HP"):
    if current_hp < 0:
        current_hp = 0
    if max_hp <= 0:
        max_hp = 1
    
    ratio = current_hp / max_hp
    filled = int(ratio * width)
    empty = width - filled
    
    bar = "[" + ("" * filled) + ("" * empty) + "]"    # manual "colors" via intensity
    if ratio <= 0.25:
        health_status = "  !! CRITICAL !!"
    elif ratio <= 0.5:
        health_status = "  ! LOW"
    else:
        health_status = ""
    
    print(f"  {label:<6} {bar} {int(current_hp)}/{int(max_hp)}{health_status}")
    
def draw_combat_menu(move_dict):
    print("\n ACTION")
    for move_id, move_data in move_dict.items():
        cost = move_data['stamina_cost']
        cost_str = f"(SP:{cost})" if cost > 0 else "(free)"
        short_desc = move_data['desc']
        if len(short_desc) > 38:
            short_desc = short_desc[:35] + "..."
        print(f"    [{move_id:>2}] {move_data['name']:<18} {cost_str:<9} {short_desc}")
    print("    [13] Inspect Enemy  [14] Use Item        [15] Flee      ")
    print("  ")
    
def draw_mini_map(player_x, player_y, world_map):
    print("\n   NAVIGATI")
    print("           N                             ")
    for row_y in range(6, -1, -1):
        row_str = "    "
        for col_x in range(7):
            if col_x == player_x and row_y == player_y:
                row_str += "[P]"
            elif (col_x, row_y) in world_map:
                row_str += "[ ]"
            else:
                row_str += "[?]"
        row_str += "  "
        print(row_str)
    print("           S                             ")
    print("  ")
    print(f"  COORDINATES: ({player_x}, {player_y})")
    
def get_neighbor_zone_names(player_x, player_y, world_map):
    neighbors = {}
    directions = [("North", 0, 1), ("South", 0, -1), ("East", 1, 0), ("West", -1, 0)]
    for d_name, dx, dy in directions:
        coord = (player_x + dx, player_y + dy)
        if coord in world_map:
            neighbors[d_name] = world_map[coord]["zone_name"]
        else:
            neighbors[d_name] = "BOUNDARY"
    return neighbors
        
def get_splash_screen():
    splash = """
#####################################################################################
#                                                                                   #
#    GGGGGG   RRRRRR   IIIIII  DDDDDD      CCCCCCC  RRRRRR    AAAAA   W   W  L L    #
#   G         R     R    II    D     D    C         R     R  A     A  W   W  L L    #
#   G  GGG    RRRRRR     II    D     D    C         RRRRRR   AAAAAAA  W W W  L L    #
#   G    G    R   R      II    D     D    C         R   R    A     A  W W W  L LLLL #
#    GGGGGG   R    R   IIIIII  DDDDDD      CCCCCCC  R    R   A     A   W W   LLLLLL #
#                                                                                   #
#                                                                                   #
#                                                                                   #
#####################################################################################
#                                                                                   #
#                                  [Have Fun]                                       #
#                                                                                   #
#####################################################################################
    """
    return splash

def print_zone_header(zone_name, danger_lvl):
    danger_bar = "!" * danger_lvl
    print("\n" + " " * 50 + "")
    print(f"  LOCALE: {zone_name:<39} ")
    # manual spacing to ensure alignment in some terminals.
    print(f"  THREAT: {danger_bar:<10} ({danger_lvl}/10)                   ")
    print(f"" + "" * 50 + 