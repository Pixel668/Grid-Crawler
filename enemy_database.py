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
         return {
                "name": "Basic Attack",
                "desc": f"{self.monster_name} throws a basic attack at you.",
                "dmg_mult": 1.0,
                "effect": None,
                "effect_chance": 0.0
         }
        
        # enemies below 30% HP have a chance to use their last move (usually most powe        hp_ratio = self.current_hp / self.max_hp
        if hp_ratio < 0.3 and len(self.move_pool) > 1:
            import random as r
            # 40% chance to spam their most dangerous move when desperate
            if r.random() < 0.4:
                return self.move_pool[-1]
        
        import random as r2
        return r2.choice(self.move_pool)
    
# move pools for every enemy.
# format: name, desc, dmg_mult, effect, effect_chance
# effect types: poison, burn, stun, bleed, freeze, None

_goblin_moves = [
    {"name": "Grubby Claw",     "desc": "The goblin scratches at you with its gross little nails.",           "dmg_mult": 0.7,  "effect": None,      "effect_chance": 0.0},
    {"name": "Headbutt",        "desc": "It just runs directly into you head-first. Hurts you both.",         "dmg_mult": 1.0,  "effect": "stun",    "effect_chance": 0.15},
    {"name": "Stolen Shiv",     "desc": "The goblin produces a slightly rusty shiv from somewhere.",           "dmg_mult": 1.3,  "effect": "bleed",   "effect_chance": 0.30},
]

_spider_moves = [
    {"name": "Venomous Bite",   "desc": "The spider sinks its fangs in. It burns.",                           "dmg_mult": 0.8,  "effect": "poison",  "effect_chance": 0.50},
    {"name": "Web Spit",        "desc": "A sticky mess of web hits your face. Disgusting.",                   "dmg_mult": 0.4,  "effect": "stun",    "effect_chance": 0.25},
    {"name": "Pounce",          "desc": "The spider leaps at you before you can react.",                       "dmg_mult": 1.2,  "effect": None,      "effect_chance": 0.0},
]

_troll_moves = [
    {"name": "Stack Overflow",  "desc": "The troll throws a pile of error logs at you.",                      "dmg_mult": 1.1,  "effect": "stun",    "effect_chance": 0.20},
    {"name": "Compile Smash",   "desc": "A devastating blow accompanied by a loud error sound.",              "dmg_mult": 1.5,  "effect": None,      "effect_chance": 0.0},
    {"name": "Syntax Shriek",   "desc": "An ear-splitting scream. Your thoughts get scrambled.",              "dmg_mult": 0.6,  "effect": "stun",    "effect_chance": 0.40},
]

_wraith_moves = [
    {"name": "Null Touch",      "desc": "Everything you're holding feels like it doesn't exist for a moment.", "dmg_mult": 1.0,  "effect": "stun",    "effect_chance": 0.35},
    {"name": 