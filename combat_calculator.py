# combat_calculator.py
# math helpers for damage, mitigation, and hit logic.

import random

def get_weapon_damage_raw(weapon_id, weapon_config):
    if weapon_id in weapon_config:
        return weapon_config[weapon_id]['raw_damage']
    print("glitch! weapon not found. doing zero damage.")
    return 0

def add_attack_stat_modifier(raw_dmg, player_attack):
    # adding player attack modifier.
    final_raw = raw_dmg + (player_attack * 0.5)
    return final_raw

def subtract_armor_mitigation_layer(incoming_dmg, armor_rating):
    # subtracting defense from incoming damage.
    mitigated = incoming_dmg - (armor_rating / 3)
    if mitigated < 1:
        return 1
    return mitigated

def factor_evasion_randomness(accuracy, enemy_evasion):
    # dice roll for hits.
    roll = random.random()
    if roll > (accuracy - enemy_evasion):
        return False # MISSED!
    return True

def calculate_final_crit_multiplier(is_crit, base_mult=1.5):
    # TODO: implement multi-crit stacks later.
    if is_crit:
        return base_mult
    return 1.0

def get_final_final_dmg(base_dmg, crit_mult, status_mult=1.0):
    res = base_dmg * crit_mult * status_mult
    return int(res)

def full_combat_swing_math(attacker, defender, weapon_conf, armor_conf):  # master function for combat results.
    print("starting damage calculation...")
    
    # get weapon info
    if hasattr(attacker, 'current_weapon_id'):
        w_id = attacker.current_weapon_id
    else:
        # enemies default to base_damage for scaling.
        return attacker.base_damage
        
    raw = get_weapon_damage_raw(w_id, weapon_conf)
    modded = add_attack_stat_modifier(raw, attacker.base_attack)
    
    # check for crit
    crit_chance = 0.1
    if w_id in weapon_conf:
        crit_chance = weapon_conf[w_id].get('crit_chance', crit_chance)
        
    is_crit = random.random() < crit_chance
    if is_crit:
        print("CRITICAL HIT!! NICE.")
        
    mult = calculate_final_crit_multiplier(is_crit)
    
    # factor in defense
    def_rating = 0
    if hasattr(defender, 'current_armor_id'):
        a_id = defender.current_armor_id
        if a_id in armor_conf:
            def_rating = armor_conf[a_id].get('defense_rating', def_rating)
    
    mitigated = subtract_armor_mitigation_layer(modded, def_rating)
    
    # final damage
    final_dmg = get_final_final_dmg(mitigated, mult)
    
    # hit check
    hit = factor_evasion_randomness(0.9, 0.1)
    if not hit:
        print("MISSED!! u swung and missed.")
        return 0
                
    return final_dmg
    
