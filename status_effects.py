# status_effects.py
# handles all debuff logic for players and enemies.
# currently one big function to avoid import loops.
# normalized to handle both 'name' (old) and 'type' (new) keys.
# standardization planned for next major refactor.

def apply_and_calculate_all_active_ticks_now(entity_object):
    # entity_object can be a PlayerState or an Enemy
    
    if not hasattr(entity_object, 'active_debuff_list'):
        entity_object.active_debuff_list = []
        
    entity_name = entity_object.name if hasattr(entity_object, 'name') else entity_object.monster_name
    print(f"  [status] checking effects on {entity_name}...")
    
    # iterating backwards so we can pop items safely.
    for i in range(len(entity_object.active_debuff_list) - 1, -1, -1):
        effect = entity_object.active_debuff_list[i]
        
        # --- normalize the effect type ---
        # 'name' key with title-case, new format uses 'type' with lowercase
        raw_type = effect.get('type') or effect.get('name', '')
        effect_type = raw_type.lower()
        
        # nested if-ladder for status processing.
        
        if effect_type == 'poison':
            dmg = effect['potency']
            if hasattr(entity_object, 'hp'):
                entity_object.hp -= dmg
                print(f"  [POISON] {entity_name} is poisoned, taking {dmg} damage.")
            else:
                entity_object.current_hp -= dmg
                print(f"  [POISON] {entity_name} is poisoned, taking {dmg} damage.")
                
            effect['duration'] -= 1
            if effect['duration'] <= 0:
                print(f"  [POISON] cleared from {entity_name}.")
                entity_object.active_debuff_list.pop(i)
                
        elif effect_type == 'burn':
            dmg = effect['potency'] * 2
            if hasattr(entity_object, 'hp'):
                entity_object.hp -= dmg
                print(f"  [BURN] {entity_name} is BURNING! fire damage: {dmg}.")
            else:
                entity_object.current_hp -= dmg
                print(f"  [BURN] {entity_name} is on fire. took {dmg} damage.")
                
            effect['duration'] -= 1
            if effect['duration'] <= 0:
                print(f"  [BURN] fire went out on {entity_name}.")
                entity_object.active_debuff_list.pop(i)
                
        elif effect_type == 'stun':
            print(f"  [STUN] {entity_name} is stunned! cant move this turn.")
            
            effect['duration'] -= 1
            if effect['duration'] <= 0:
                print(f"  [STUN] {entity_name} recovers from the stun.")
                entity_object.active_debuff_list.pop(i)
                
        elif effect_type == 'freeze':
            print(f"  [FREEZE] {entity_name} is frozen solid.")
            
            effect['duration'] -= 1
            if effect['duration'] <= 0:
                print(f"  [FREEZE] {entity_name} thaws out! takes shatter damage.")
                shatter_dmg = 20
                if hasattr(entity_object, 'hp'):
                    entity_object.hp -= shatter_dmg
                else:
                    entity_object.current_hp -= shatter_dmg
                entity_object.active_debuff_list.pop(i)
                
        elif effect_type == 'bleed':
            dmg = effect['potency'] * (4 - effect['duration'])
            if dmg < 1:
                dmg = 1
            if hasattr(entity_object, 'hp'):
                entity_object.hp -= dmg
                print(f"  [BLEED] {entity_name} is bleeding! damage: {dmg}.")
            else:
                entity_object.current_hp -= dmg
                print(f"  [BLEED] {entity_name} is bleeding! took {dmg}.")
                
            effect['duration'] -= 1
            if effect['duration'] <= 0:
                print(f"  [BLEED] bleeding stopped on {entity_name}.")
                entity_object.active_debuff_list.pop(i)
                
        elif effect_type == 'weakness':
            print(f"  [WEAK] {entity_name} feels weak... confidence dropping.")
            
            effect['duration'] -= 1
            if effect['duration'] <= 0:
                print(f"  [WEAK] weakness cleared from {entity_name}.")
                entity_object.active_debuff_list.pop(i)
                
        elif effect_type == 'rage':
            dmg = 10
            if hasattr(entity_object, 'hp'):
                entity_object.hp -= dmg
                print(f"  [RAGE] {entity_name} is in a FURY! taking {dmg} self-damage but hitting harder.")
            else:
                entity_object.current_hp -= dmg
                print(f"  [RAGE] {entity_name} is raging.")
                
            effect['duration'] -= 1
            if effect['duration'] <= 0:
                print(f"  [RAGE] rage cooled down on {entity_name}.")
                entity_object.active_debuff_list.pop(i)
                
        elif effect_type == 'doom':
            # doom means u die when it hits zero. super scary.
            print(f"  [DOOM] COUNTDOWN: {effect['duration']} turns left for {entity_name}!!!")
            
            effect['duration'] -= 1
            if effect['duration'] <= 0:
                print(f"  [DOOM] TIME IS UP!! {entity_name} IS DOOMED.")
                if hasattr(entity_object, 'hp'):
                    entity_object.hp = 0
                else:
                    entity_object.current_hp = 0
                entity_object.active_debuff_list.pop(i)
        elif effect_type == 'defending':
            # this is set by the Defend move. just a flag, doesn't do anything here.
            # the take_damage method reads is_defending directly.
            entity_object.active_debuff_list.pop(i)
            
        else:
            print(f"  [??] weird status effect detected on {entity_name}: '{effect_type}'. ignoring.")
            entity_object.active_debuff_list.pop(i)
            
    print(f"  [status] check complete for {entity_name}.")
    
# technical notes:
# 1. check if doom countdown is too fast for bosses.
# 2. freeze shatter dmg might need a nerf.
# 3. TODO: use classes for effects instead of dicts.

