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
        
        # update state
        self.player.change_coordinates(dx, dy)
        self.player.restore_stamina(10) # walking restores a bit more now
        
        # UI update
        self.redraw_ui(zone_verbose=True)
        
        # story / NPC triggers
        story_engine.check_and_show_chapter("zone", (self.player.x_pos, self.player.y_pos))
        
        coords = (self.player.x_pos, self.player.y_pos)
                if coords in npc_dialogues.npc_encounter_map and coords not in self.npc_talked_zones:
                        print(f"\n  [ ALERT: Unknown entity detected. Source ID: {npc_dialogues.npc_encounter_map[coords]['npc_name']} ]")
            print("  [ Action: Type 'talk' to initiate communication. ]")
        
        return True
    
    def check_current_zone(self, verbose=False):
        coords = (self.player.x_pos, self.player.y_pos)
        if coords in world_conf.world_map:
            zone = world_conf.world_map[coords]
            string_helpers.print_zone_header(zone['zone_name'], zone['danger_rating'])
            if verbose:
                print("\n  [ DESCRIPT                string_helpers.typewriter_print(f"  {zone['entry_announcement']}", speed=0.01)
                if 'lore_e                    print("\n  [ LOG DETAILS ]")
                    string_helpers.typewriter_print(f"  {zone['lore_entry']}", speed=0.008)
        else:
            print("  !! SYSTEM FAULT: Location out of sync. Teleporting to Origin.")
                        self.player.x_pos = 0
            self.player.y_pos = 0

    def trigger_npc_encounter(self):
        coords = (self.player.x_pos, self.player.y_pos)
        if coords not in npc_dialogues.npc_encounter_map:
            print("  >> Scanning... No communicative entities found in this sector.")
            return
            
        npc = npc_dialogues.npc_encounter_map[coords]
        self.npc_talked_zones.add(coords)
        
        print(f"\n   {npc['npc_name']} ")
        for line in npc['lines']:
            string_helpers.typewriter_print(f" {line}", speed=0.015)
            time.sleep(0.2)
        print(f"  ")
        if npc.get('hint'):
            print(f"\n  [ ENCRYPTED HINT: {npc['hint']} ]")
            
    def print_help_menu(self):
        print("\n" + "=" * 60)
        print("  SYSTEM DIRECTIVES (COMMANDS)")
        print("=" * 60)
        print("  NAVIGATION:  n (north), s (south), e (east), w (west), map")
        print("  ACTIONS   :  look, talk, fight, shop")
        print("  VITALS    :  status, bag, use (heal)")
        print("  SYSTEM    :  help, quit")
        print("=" * 60)
        
    def _use_item(self):
        used = self.inventory.use_healing_item()
        if used:
            self.player.heal_hp(35)
        else:
            print("  !! WARNING: Restoration stock depleted.")
            
    def trigger_random_encounter(self, manual=True):
        coords = (self.player.x_pos, self.player.y_pos)
        zone = world_conf.world_map[coords]
        m_id = random.choice(zone['spawnable_monster_ids'])
        enemy = spawn_mob_by_id_and_level_scale(m_id, (self.player.level / 5) + 0.5)
        
        session = CombatSession(self.player, enemy)
        
        string_helpers.clear_screen()
        print(f"\n  [ CRITICAL ALERT: Hostile Entity Manifested ]")
        print(f"  ID: {enemy.monster_name}")
        print(f"  \"{self._get_encounter_taunt(enemy.monster_name)}\"")
        time.sleep(1.0)
        
        while True:
            action = get_player_combat_choice_manual() if manual else "attack"
            res = session.execute_round(action)
            
            if res == "win":
                story_engine.check_and_show_chapter("level", self.player.level)
                break
            elif res == "loss":
                print("\n  !! FATAL ERROR: Process core destroyed. Game Over. !!")
                self.game_running = False
                break
            elif res == "fled":
                break
            elif res != "ongoing":
                            break
        
        self.redraw_ui()
        
    def _get_encounter_taunt(self, enemy_name):
            taunts = [
            f"The {enemy_name} blocks your logic            f"A violent {enemy_name} emerges from a memory leak.",
            f"The {enemy_name} is already calculating your demise.",
            f"You have entered the detection range of a {enemy_name}.",
            ]
        return random.choice(taunts)
        
    def execute_mock_command_stream(self, commands):
        # helper for automated tests to run a series of strings.
        for cmd in commands:
            if not self.game_running:
                break
            self.process_command(cmd, manual=False)
            
    def run_interactive_loop(self):
        story_engine.show_opening_narrative()
        try:
            name_input = input("  ENTER PROCESS DESIGNATION: ").strip()
            if name_input:
                self.player.name = name_in      except (EOFError, KeyboardInterrupt):
            pass
            
        self.redraw_ui()
        
        while self.game_running:
            try:
                prompt = f"\n  {self.player.name} @ ({self.player.x_pos},{self.player.y_pos}) > "
                user_input = input(prompt).lower().strip()
                if not user_input:
                    continue
                self.process_command(user_input, manual=True)
            except (EOFError, KeyboardInterrupt):
                break
                
if __name__ == "__main__":
    engine = GridCrawlerEngine()
    #print("\n  [1] Automated Stability Simulation")
    #print("  [2] Execute Interactive Session")
    #mode = input("\n  Selection > ").strip()
    
    #if mode == "1":
    #    engine.run_interactive_loop() # simulation support is legacy for now
    #else:
    # directly starting the interactive session to bypass the dev menu.
    engine.run_interactive_loop()
    
