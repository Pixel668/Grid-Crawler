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
    {"name": "Pointer Drain",   "desc": "It reaches through you and drains your life force.",                 "dmg_mult": 1.2,  "effect": None,      "effect_chance": 0.0},
    {"name": "Dereference",     "desc": "Takes a chunk of your soul. Also your stamina.",                     "dmg_mult": 0.9,  "effect": "stun",    "effect_chance": 0.30},
]

_lag_beast_moves = [
    {"name": "Timeout Slam",    "desc": "A slow but heavy hit. You couldn't dodge it, it just sat there.",   "dmg_mult": 0.9,  "effect": "stun",    "effect_chance": 0.20},
    {"name": "Packet Loss",     "desc": "The beast flickers. You miss. It doesn't.",                         "dmg_mult": 1.1,  "effect": None,      "effect_chance": 0.0},
    {"name": "Lag Spike",       "desc": "Suddenly hits you from three different directions at once.",          "dmg_mult": 1.4,  "effect": None,      "effect_chance": 0.0},
]

_slime_moves = [
    {"name": "Acid Splash",     "desc": "A wave of corrosive goop. Burns like crazy.",                       "dmg_mult": 0.8,  "effect": "burn",    "effect_chance": 0.45},
    {"name": "Engulf",          "desc": "The slime tries to absorb you. Partially succeeds.",                 "dmg_mult": 1.0,  "effect": "poison",  "effect_chance": 0.30},
    {"name": "Ooze Lunge",      "desc": "Gross. Just... gross.",                                              "dmg_mult": 0.7,  "effect": None,      "effect_chance": 0.0},
]

_golem_moves = [
    {"name": "Merge Crush",     "desc": "Slams both massive fists together on your head.",                    "dmg_mult": 1.6,  "effect": "stun",    "effect_chance": 0.30},
    {"name": "Conflict Roar",   "desc": "A deafening scream that shakes the ground.",                         "dmg_mult": 0.5,  "effect": "stun",    "effect_chance": 0.60},
    {"name": "Rock Throw",      "desc": "Tears out a chunk of itself and hurls it at you.",                   "dmg_mult": 1.3,  "effect": None,      "effect_chance": 0.0},
    {"name": "Ground Pound",    "desc": "Absolute devastation. You feel it in your bones.",                   "dmg_mult": 2.0,  "effect": "stun",    "effect_chance": 0.20},
]

_warrior_moves = [
    {"name": "Keyboard Frenzy", "desc": "Types extremely fast. Somehow this hurts.",                         "dmg_mult": 1.0,  "effect": None,      "effect_chance": 0.0},
    {"name": "Flaming Comment", "desc": "Sends you a toxic message. Causes burn damage.",                    "dmg_mult": 0.9,  "effect": "burn",    "effect_chance": 0.40},
    {"name": "Reply All",       "desc": "Hits everyone in range. Including you, twice.",                      "dmg_mult": 1.2,  "effect": "stun",    "effect_chance": 0.15},
]

_rat_moves = [
    {"name": "Nibble",          "desc": "A tiny bite. Embarrassing that it still hurts.",                     "dmg_mult": 0.5,  "effect": None,      "effect_chance": 0.0},
    {"name": "Diseased Bite",   "desc": "That thing is definitely not clean. Poison chance is real.",        "dmg_mult": 0.7,  "effect": "poison",  "effect_chance": 0.45},
    {"name": "Swarm Call",      "desc": "Somehow summons more rats from somewhere. Deals bonus damage.",      "dmg_mult": 1.1,  "effect": None,      "effect_chance": 0.0},
]

_ghost_moves = [
    {"name": "Haunting Touch",  "desc": "Cold fingers pass through your chest. Very uncomfortable.",          "dmg_mult": 1.1,  "effect": "freeze",  "effect_chance": 0.25},
    {"name": "Scream",          "desc": "A horrific wail. Deals damage and chance to stun.",                  "dmg_mult": 0.9,  "effect": "stun",    "effect_chance": 0.30},
    {"name": "Phase Strike",    "desc": "Hits from inside the wall. No right way to block it.",               "dmg_mult": 1.3,  "effect": None,      "effect_chance": 0.0},
        {"name": "Soul Drain",      "desc": "Drains your life into itself. It looks healthier than you.",          "dmg_mult": 1.0,  "effect": None,      "effect_chance": 0.0},
]

_snake_moves = [
    {"name": "Constrict",       "desc": "Wraps around you and squeezes. Bleed chance.",                      "dmg_mult": 1.0,  "effect": "bleed",   "effect_chance": 0.35},
    {"name": "Venom Bite",      "desc": "Sinks fangs deep. The poison is already moving through you.",        "dmg_mult": 0.9,  "effect": "poison",  "effect_chance": 0.65},
    {"name": "Tail Whip",       "desc": "A fast tail swipe. Hard to dodge.",                                  "dmg_mult": 0.8,  "effect": None,      "effect_chance": 0.0},
]

_ogre_moves = [
    {"name": "Feature Add",     "desc": "Adds more weight to an already bloated attack.",                    "dmg_mult": 1.2,  "effect": "stun",    "effect_chance": 0.25},
    {"name": "Scope Expansion", "desc": "A massive sweeping attack. Hits you from further away than expected.", "dmg_mult": 1.5,  "effect": None,      "effect_chance": 0.0    {"name": "Deadline Panic",  "desc": "Frenzied attacks from nowhere. Multiple hits.",                      "dmg_mult": 1.8,  "effect": "bleed",   "effect_chance": 0.30},
    {"name": "Backlog Crush",   "desc": "Buries you under accumulated problems. Critical hit chance.",         "dmg_mult": 2.2,  "effect": "stun",    "effect_chance": 0.15},
]

_lich_moves = [
    {"name": "Debt Curse",      "desc": "Curses you with decades of technical debt. Feel the poison.",        "dmg_mult": 1.0,  "effect": "poison",  "effect_chance": 0.70},
    {"name": "Undocumented Method", "desc": "Attacks from an unknown function. You cannot predict the damage.", "dmg_mult": 1.6,  "effect": None,      "effect_chance": 0.0},
    {"name": "Deprecated Drain", "desc": "Pulls your life force. Draining.",                                  "dmg_mult": 1.2,  "effect": "bleed",   "effect_chance": 0.40},
    {"name": "Memory Haunt",    "desc": "Fills ur head with corrupted memories. Stuns.",                     "dmg_mult": 0.8,  "effect": "stun",    "effect_chance": 0.50},
]

_hell_hound_moves = [
    {"name": "Dependency Bite", "desc": "Bites through every layer of your armor.",                          "dmg_mult": 1.1,  "effect": "bleed",   "effect_chance": 0.35},
    {"name": "Conflict Howl",   "desc": "A howl that causes the ground to fracture beneath you.",            "dmg_mult": 0.9,  "effect": "stun",    "effect_chance": 0.30},
    {"name": "Package Install", "desc": "Summons more hounds. Deals bonus damage for each one.",             "dmg_mult": 1.4,  "effect": None,      "effect_chance": 0.0},
]

_bat_moves = [
    {"name": "Buffer Bite",     "desc": "Fangs overflow your buffer. Memory corruption detected.",           "dmg_mult": 0.8,  "effect": "poison",  "effect_chance": 0.30},
    {"name": "Wing Slash",      "desc": "Razor wing cuts across your arm.",                                   "dmg_mult": 0.9,  "effect": "bleed",   "effect_chance": 0.25},
    {"name": "Echolocation Pulse", "desc": "A concentrated beam of sound. Your ears are ringing.",           "dmg_mult": 0.7,  "effect": "stun",    "effect_chance": 0.20},
]

_specter_moves = [
    {"name": "Stack Peek",      "desc": "Looks through you like you're a debugger window.",                  "dmg_mult": 1.0,  "effect": "stun",    "effect_chance": 0.25},
    {"name": "Trace Strike",    "desc": "Follows every movement precisely. Hard to avoid.",                  "dmg_mult": 1.2,  "effect": None,      "effect_chance": 0.0},
    {"name": "Error Propagation", "desc": "Sends cascading damage through your whole body.",                 