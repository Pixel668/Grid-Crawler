# game_simulation_engine.py
# main orchestrator. i've added screen clearing and better UI flow.
# every move now clears the screen so the map and status stay clean.
# narrative beats now wait for player input so they aren't missed.
# keep in mind code is messy because i'm human but the story is proper.

import time
import random
from player_state import PlayerState
from inventory_manager import InventoryManager
from enemy_database import spawn_mob_by_id_and_level_scale
from combat_loop import CombatSession, get_player_combat_choice_manual
import config_world_zones as world_conf
import string_helpers
import story_engine
import npc_dialogues
import shop_system
class GridCrawlerEngine:
    def __init__(self, player_name="Process_01"):
        string_helpers.clear_screen()
        print(string_helpers.get_splash_screen())
        self.player = PlayerState(player_name)
        self.inventory = InventoryManager()
        self.game_running = True
        self.global_ticks = 0
        self.npc_talked_zones = set()
        print("[SYSTEM] LATTICE INITIALIZED. AWAITING INPUT.")
        time.sleep(1.0)
        
    def redraw_ui(self, zone_verbose=True):
        # clears and draws the current state.
        string_helpers.clear_screen()
        self.check_current_zone(verbose=zone_verbose)
        string_helpers.draw_mini_map(self.player.x_pos, self.player.y_pos, world_conf.world_map)
        
        neighbors = string_helpers.get_neighbor_zone_names(self.player.x_pos, self.player.y_pos, world_conf.world_map)
        print("\n  ADJACENT NODES:")
        for direction, zone_name in neighbors.items():
            print(f"    {direction:<6}: {zone_name}")
            
    def process_command(self, cmd, manual=False):
        clean_cmd = string_helpers.sanitize_command_string(cmd)
        self.global_ticks += 1
        
        # navigation logic
        moved = False
        if clean_cmd in ("n", "north", "move_north"):
            moved = self._try_move(0, 1)
        elif clean_cmd in ("s", "south", "move_south"):
            moved = self._try_move(0, -1)
        elif clean_cmd in ("e", "east", "move_east"):
            moved = self._try_move(1, 0)
        elif clean_cmd in ("w", "west", "move_west"):
            moved = self._try_move(-1, 0)
        
        elif clean_cmd in ("look", "inspect_room", "inspect"):
            self.redraw_ui(zone_verbose=True)
            string_helpers.press_enter_to_continue()
        
        elif clean_cmd == "map":
            string_helpers.draw_mini_map(self.player.x_pos, self.player.y_pos, world_conf.world_map)
            string_helpers.press_enter_to_continue()
            
        elif clean_cmd in ("status", "stats"):
            self.player.print_status_block()
            string_helpers.press_enter_to_continue()
            
        elif "fight" in clean_cmd or clean_cmd == "attack":
            self.trigger_random_encounter(manual=manual)
            
        elif clean_cmd in ("npc", "talk"):
            self.trigger_npc_encounter()
            string_helpers.press_enter_to_continue()
            
        elif clean_cmd in ("shop", "store"):
            shop_system.handle_shop_session(self.player, self.inventory)
            self.redraw_ui()
            
        elif "consume" in clean_cmd or clean_cmd in ("heal", "use"):
            self._use_item()
            time.sleep(1.0)
            self.redraw_ui()
            
        elif clean_cmd in ("check_bag", "bag", "inventory"):
            self.inventory.debug_print_inventory()
            string_helpers.press_enter_to_continue()
            
        elif clean_cmd == "help":
            self.print_help_menu()
            string_helpers.press_enter_to_continue()
            
        elif clean_cmd in ("quit", "exit"):
            print("\n  >> Termination sequence initiated. Goodbye, Process.")
            self.game_running = False
        
        else:
            print(f"  !! ERROR: Unknown directive '{clean_cmd}'.")
            time.sleep(0.5)
            
        # if we just moved, we already redrew in _try_move.
        # if not, we might need a refresh depending on the command.
        if not moved and self.game_running and clean_cmd not in ("map", "status", "stats", "bag", "help", "npc", "talk", "look"):
            self.redraw_ui(zone_verbose=False)
    def _try_move(self, dx, dy):
        new_x = self.player.x_pos + dx
        new_y = self.player.y_pos + dy
        
        if (new_x, new_y) not in world_conf.world_map:
            print(f"\n  !! BLOCKED: Coordinate ({new_x}, {new_y}) is beyond the de-allocated boundary.")
            time.sleep(0.8)
            return False
        
