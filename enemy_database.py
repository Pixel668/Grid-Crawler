# enemy_database.py
# master list of mobs and their stats.
# includes level scaling logic and the move pools for combat.

class Enemy:
    def __init__(self, monster_id, monster_name, max_hp, base_damage, xp_drop, move_pool=None, gold_drop=10):
        self.monster_id = monster_id
        self.monster_name = monster_name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.base_damage = base_damage
        self.accuracy = 0.8
        self.evasion_rate = 0.1
        self.xp_drop = xp_drop
        self.gold_drop = gold_drop
        self.active_debuff_list = []
        if move_pool is None:
            self.move_pool = []
        else:
            self.move_pool = move_pool  # list of move dicts the enemy picks from
        print(f"spawned a {monster_name}! stay alert.")
        
    def take_damage(self, amount):
        self.current_hp -= amount
        if self.current_hp < 0:
            self.current_hp = 0
        print(f"{self.monster_name} took {amount:.1f} damage. remaining: {self.current_hp:.0f}/{self.max_hp}")
        
    def pick_move(self):
        # TODO: add smarter hp-based logic for boss patterns.
        import random
        if not self.move_pool:
            # fallback default attack
    