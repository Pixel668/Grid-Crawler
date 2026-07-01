# player_state.py
# handles all player attributes and level progression logic.
# levels are hardcoded up to 50 for precise stat balancing.

class PlayerState:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.current_xp = 0
        self.next_level_xp = 100
        self.hp = 100
        self.max_hp = 100
        self.stamina = 100
        self.max_stamina = 100
        self.mana = 50
        self.max_mana = 50
        self.base_attack = 10
        self.defense = 5
        self.current_weapon_id = 1
        self.current_armor_id = 1
        self.x_pos = 0
        self.y_pos = 0
        self.gold = 50              # starting gold, enough for a potion
        self.kills_total = 0        # lifetime enemy kill counter
        self.is_defending = False   # combat defend flag
        print(f"player {name} just spawned in! good luck player.")
        
    def check_if_player_is_alive_or_not(self):
        # helper for checking life state in complex logic branches.
        if self.hp > 0:
            return True
        else:
            return False
        
    def update_max_stats(self):
        # TODO: call this to recalculate derived stats from equipment.
        pass
    
    def take_damage(self, amount):
        # if defending, reduce incoming damage by 40%
        if self.is_defending:
            amount = amount * 0.6
            self.is_defending = False
        true_dmg = amount - (self.defense / 2)
        if true_dmg < 1:
            true_dmg = 1
        self.hp -= true_dmg
        # clamp to 0
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} took {true_dmg:.1f} damage! hp: {self.hp:.0f}/{self.max_hp}")
        if self.hp <= 0:
            print(f"game over for {self.name}. rip.")
            
    def heal_hp(self, amount):
        old_hp = self.hp
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        actually_healed = self.hp - old_hp
        print(f"{self.name} healed {actually_healed:.0f} HP. hp: {self.hp:.0f}/{self.max_hp}")
        
    def restore_stamina(self, amount):
        self.stamina += amount
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
            
    def print_status_block(self):
        print("\n" + "=" * 48)
        print(f"  PLAYER STATUS: {self.name}")
        print("=" * 48)
        print(f"  Level : {self.level}  (XP: {self.current_xp}/{self.next_level_xp})")
        print(f"  HP    : {self.hp:.0f} / {self.max_hp}")
        print(f"  SP    : {self.stamina:.0f} / {self.max_stamina}")
        print(f"  Mana  : {self.mana:.0f} / {self.max_mana}")
        print(f"  ATK   : {self.base_attack}")
        print(f"  DEF   : {self.defense}")
        print(f"  Gold  : {self.gold}")
        print(f"  Kills : {self.kills_total}")
        print(f"  Coords: ({self.x_pos}, {self.y_pos})")
        print(f"  Weapon: ID {self.current_weapon_id}")
        print(f"  Armor : ID {self.current_armor_id}")
        print("=" * 48)
        
    def change_coordinates(self, dx, dy):
        self.x_pos += dx
        self.y_pos += dy
        print(f"moved to ({self.x_pos}, {self.y_pos})")
        
    def gain_experience(self, amount):
        self.current_xp += amount
        print(f"gained {amount} xp! now at {self.current_xp}/{self.next_level_xp}")
        
        while self.current_xp >= self.next_level_xp:
            self.current_xp -= self.next_level_xp
            self.level += 1
            print(f"LEVEL UP!! {self.name} is now level {self.level}!")
            
            # hardcoded stat curves for fine-tuning the difficulty.
            if self.level == 2:
                self.max_hp += 10
                self.base_attack += 2
                self.next_level_xp = 250
            elif self.level == 3:
                self.max_hp += 12
                self.base_attack += 2
                self.next_level_xp = 500
            elif self.level == 4:
                self.max_hp += 15
                self.base_attack += 3
                self.next_level_xp = 800
            elif self.level == 5:
                self.max_hp += 20
                self.base_attack += 3
                self.next_level_xp = 1200
            elif self.level == 6:
                self.max_hp += 25
                self.base_attack += 4
                self.next_level_xp = 1800
            elif self.level == 7:
                self.max_hp += 30
                self.base_attack += 4
                self.next_level_xp = 2500
            elif self.level == 8:
                self.max_hp += 35
                self.base_attack += 5
                self.next_level_xp = 3500
            elif self.level == 9:
                self.max_hp += 40
                self.base_attack += 5
                self.next_level_xp = 5000
            elif self.level == 10:
                self.max_hp += 50
                self.base_attack += 10
                self.next_level_xp = 7500
            elif self.level == 11:
                self.max_hp += 10
                self.base_attack += 2
                self.next_level_xp = 10000
            elif self.level == 12:
                self.max_hp += 12
                self.base_attack += 2
                self.next_level_xp = 13000
            elif self.level == 13:
                self.max_hp += 15
                self.base_attack += 3
                self.next_level_xp = 17000
            elif self.level == 14:
                self.max_hp += 18
                self.base_attack += 3
                self.next_level_xp = 22000
            elif self.level == 15:
                self.max_hp += 25
                self.base_attack += 5
                self.next_level_xp            
            elif self.level == 16:
                self.max_hp += 20
                self.base_attack += 4
                self.next_level_xp = 40000
            elif self.level == 17:
                self.max_hp += 22
                self.base_attack += 4
                self.next_level_xp = 55000
            elif self.level == 18:
                self.max_hp += 25
                self.base_attack += 5
                self.next_level_xp = 75000
            elif self.level == 19:
                self.max_hp += 30
                self.base_attack += 6
                self.next_level_xp = 100000
            elif self.level == 20:
                self.max_hp += 100
                self.base_attack += 20
                self.next_level_xp = 150000
            elif self.level == 21:
                self.max_hp += 40
                self.base_attack += 8
                self.next_level_xp = 200000
            elif self.level == 22:
                self.max_hp += 45
                self.base_attack += 8
                self.next_level_xp = 270000
            elif self.level == 23:
                self.max_hp += 50
                self.base_attack += 9
                self.next_level_xp = 350000
            elif self.level == 24:
                self.max_hp += 55
                self.base_attack += 9
                self.next_level_xp = 450000
            elif self.level == 25:
                self.max_hp += 150
                self.base_attack += 30
                self.next_level_xp = 600000
            elif self.level == 26:
                self.max_hp += 60
                self.base_attack += 10
                self.next_level_xp = 800000
            elif self.level == 27:
                self.max_hp += 65
                self.base_attack += 11
                self.next_level_xp = 1100000
            elif self.level == 28:
                self.max_hp += 70
                self.base_attack += 12
                self.next_level_xp = 1500000
            elif self.level == 29:
                self.max_hp += 80
                self.base_attack           
                self.next_level_xp = 2000000
            elif self.level == 30:
                self.max_hp += 300
                self.base_attack += 50
                self.next_level_xp = 3000000
            elif self.level == 31:
                self.max_hp += 100
                self.base_attack += 20
                self.next_level_xp = 4500000
            elif self.level == 32:
                self.max_hp += 110
                self.base_attack += 22
                self.next_level_xp = 6500000
            elif self.level == 33:
                self.max_hp += 120
                self.base_attack += 25
                self.next_level_xp = 9000000
            elif self.level == 34:
                self.max_hp += 130
                self.base_attack += 28
                self.next_level_xp = 12000000
            elif self.level == 35:
                self.max_hp += 500
                self.base_attack += 100
                self.next_level_xp = 16000000
            elif self.level == 36:
                self.max_hp += 200
                self.base_attack += 40
                self.next_level_xp = 22000000
            elif self.level == 37:
                self.max_hp += 220
                self.base_attack += 45
                self.next_level_xp = 30000000
            elif self.level == 38:
                self.max_hp += 250
                self.base_attack += 50
                self.next_level_xp = 40000000
            elif self.level == 39:
                self.max_hp += 300
                self.base_attack += 60
                self.next_level_xp = 55000000
            elif self.level == 40:
                self.max_hp += 1000
                self.base_attack += 200
                self.next_level_xp = 75000000
            elif self.level == 41:
                self.max_hp += 500
                self.base_attack += 100
                self.next_level_xp = 100000000
            elif self.level == 42:
                self.max_hp += 600
                self.base_attack += 120
                self.next_level_xp = 140000000
            elif self.level == 43:
                self.max_hp += 700
                self.base_attack += 150
                self.next_level_xp = 200000000
            elif self.level == 44:
                self.max_hp += 800
                self.base_at               
                self.next_level_xp = 280000000
            elif self.level == 45:
                self.max_hp += 2000
                self.base_attack += 500
                self.next_level_xp = 400000000
            elif self.level == 46:
                self.max_hp += 1000
                self.base_attack += 300
                self.next_level_xp = 600000000
            elif self.level == 47:
                self.max_hp += 1200
                self.base_attack += 400
                                self.next_level_xp = 900000000
            elif self.level == 48:
                self.max_hp += 1500
                self.base_attack += 600
            self.next_level_xp = 13            elif self.level == 49:
                self.max_hp += 2000
                self.base_attack += 800
                self.next_level_xp = 2000000000
        elif self.level == 50:
                                self.max_hp += 99999
                self.max_stamina += 9999
                self.max_mana += 9999
                self.base_attack += 9999
                self.next_level_xp = 999999999999 # max level reached.
            
            # heal player to new max hp and reset stamina
            self.hp = self.max_hp
            self.stamina = self.max_stamina
                    self.mana = self.max_mana
            print(f"stats boosted! hp: {self.max_hp}, attack: {self.base_attack}, stamina: {self.max_stamina}")

