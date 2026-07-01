# combat_loop.py
# battle orchestration. i've added screen clearing and brief pauses
# to make the text combat feel like it's actually "animating".
# the code is still a mess of if-statements but it's human-written so...
# properly grammatic story text is now used during combat.

import random
import time
from combat_calculator import full_combat_swing_math
from status_effects import apply_and_calculate_all_active_ticks_now
import config_weapons
import config_armor
import config_player_moves as moves_conf
import string_helpers

def print_combat_hud(player, enemy, turn):
    # a clean, screen-cleared HUD for the fight.
    print(f"  [ BATTLE: ROUND {turn} ] ")
    print("")
    string_helpers.draw_hp_bar(player.hp, player.max_hp, 22, label=player.name[:8])
    string_helpers.draw_hp_bar(player.stamina, player.max_stamina, 22, label="Stamina")
    print("  " + " " * 58)
    string_helpers.draw_hp_bar(enemy.current_hp, enemy.max_hp, 22, label=enemy.monster_name[:8])
    print("  " + " " * 58)

class CombatSession:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.turn_count = 1
        
    def execute_round(self, action_string):
        # execute a single round of combat.
        
        # 1. status check
        print_combat_hud(self.player, self.enemy, self.turn_count)
        print("  [ SYSTEM: Validating entity integrity... ]")
        time.sleep(0.3)
        apply_and_calculate_all_active_ticks_now(self.player)
        apply_and_calculate_all_active_ticks_now(self.enemy)
        
        if self.player.hp <= 0 or self.enemy.current_hp <= 0:
            return self.check_winner()
        
        # 2. player choice
        print_combat_hud(self.player, self.enemy, self.turn_count)
        result = self._resolve_player_action(action_string)
        if result in ("fled", "win", "loss"):
            return result
        
        # 3. enemy turn
        if self.enemy.current_hp > 0:
            time.sleep(0.6) # minor pause so player can read their own move result
            enemy_move = self.enemy.pick_move()
            self._resolve_enemy_action(enemy_move)
            time.sleep(1.0) # wait before next round clears screen
            
        if self.player.hp <= 0:
            return "loss"
        
        self.turn_count += 1
        return "ongoing"
    
    def _resolve_player_action(self, action_string):
        if action_string == "attack":
            dmg = full_combat_swing_math(self.player, self.enemy, config_weapons.weapons, config_armor.armor_sets)
            self.enemy.take_damage(dmg)
            if self.enemy.current_hp <= 0:
                self.player.gain_experience(self.enemy.xp_drop)
                self.player.gold += self.enemy.gold_drop
                self.player.kills_total += 1
                return "win"
            return "ongoing"
        
        if action_string == "flee" or action_string == "15":
            if random.random() < 0.5:
                print("\n  >> You pivot and sprint into the darkness. The Grid allows your escape.")
                time.sleep(1.0)
                return "fled"
            else:
                print("\n  >> Your attempt to flee is truncated by a swift movement from the enemy.")
                return "ongoing"
            
        if action_string == "inspect" or action_string == "13":
            print(f"\n  [ ANALYSIS: {self.enemy.monster_name} ]")
            print(f"  Threat Level: {self.enemy.base_damage}")
            print(f"  Capabilities: {', '.join([m['name'] for m in self.enemy.move_pool])}")
            string_helpers.press_enter_to_continue()
            return "ongoing"
        
        if action_string == "use_item" or action_string == "14":
            print(f"\n  >> You initiate a restoration sequence mid-combat.")
            self.player.heal_hp(30)
            return "ongoing"
        
        # move resolution
        move_id = moves_conf.move_name_to_id.get(action_string.lower().strip())
        if move_id is None:
            print(f"\n  !! ERROR: Unknown command sequence '{action_string}'. turn truncated.")
            return "ongoing"
        
        chosen_move = moves_conf.player_move_list[move_id]
        
        if self.player.stamina < chosen_move['stamina_cost']:
            print(f"\n  !! WARNING: Insufficient stamina to execute {chosen_move['name']}.")
            return "ongoing"
        
        # commit action
        self.player.stamina -= chosen_move['stamina_cost']
        
        if chosen_move.get('effect') == 'defending':
            self.player.is_defending = True
            print(f"\n  >> {self.player.name} executes: {chosen_move['name']}")
            string_helpers.typewriter_print(f"     \"{chosen_move['desc']}\"", speed=0.01)
            return "ongoing"
        
        # lunge logic
        extra_mult = 1.0
        if move_id == 6 and (self.player.hp / self.player.max_hp) < 0.3:
            extra_mult = 1.8
            print("  !! LOGIC OVERRIDE: Desperate Lunge synergy active !!")
            
        # combat math
        hit_chance = 0.85 + chosen_move['acc_mod']
        print(f"\n  >> {self.player.name} executes: {chosen_move['name']}")
        string_helpers.typewriter_print(f"     \"{chosen_move['desc']}\"", speed=0.01)
        
        if random.random() > hit_chance:
            print(f"  >> MISS. The calculation failed to converge.")
            return "ongoing"
        
        base_dmg = self.player.base_attack * chosen_move['dmg_mult'] * extra_mult
        crit_label = ""
        if random.random() < 0.12:
            base_dmg *= 2.0
            crit_label = " [ CRITICAL HIT ]"
        final_dmg = base_dmg * random.uniform(0.9, 1.1)
        self.enemy.take_damage(final_dmg)
        print(f"     Impact resulted in {final_dmg:.1f} kinetic displacement.{crit_label}")
        # status effects
        if chosen_move['effect'] and chosen_move['effect'] != 'defending':
            if random.random() < chosen_move['effect_chance']:
                self.enemy.active_debuff_list.append({
                    "type": chosen_move['effect'],
                    "duration": 3,
                    "potency": 5
                })
                print(f"     Secondary effect applied: {chosen_move['effect'].upper()}.")
                
        if self.enemy.current_hp <= 0:
            print(f"\n  >> The {self.enemy.monster_name} has been de-allocated from the lattice.")
            self.player.gain_experience(self.enemy.xp_drop)
            self.player.gold += self.enemy.gold_drop
            self.player.kills_total += 1
            string_helpers.press_enter_to_continue()
            return "win"
        
        return "ongoing"
    
    def _resolve_enemy_action(self, enemy_move):
        print(f"\n  >> {self.enemy.monster_name} executes: {enemy_move['name']}")
        string_helpers.typewriter_print(f"     \"{enemy_move['desc']}\"", speed=0.01)
        
        if random.random() > self.enemy.accuracy:
            print(f"  >> The attack was miscounted and missed.")
            return
        
        raw_dmg = self.enemy.base_damage * enemy_move['dmg_mult'] * random.uniform(0.85, 1.15)
        self.player.take_damage(raw_dmg)
        
        if enemy_move.get('effect') and random.random() < enemy_move['effect_chance']:
            self.player.active_debuff_list.append({
                "type": enemy_move['effect'],
                "duration": 3,
                "potency": 4
            })
            print(f"     Anomalous data detected: {self.player.name} is afflicted by {enemy_move['effect'].upper()}.") 