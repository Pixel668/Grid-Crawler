# config_player_moves.py
# combat moves for the player. handles damage, accuracy, and status effects.
# i've tweaked these multipliers to try and make combat feel balanced.

# each move has:
#   name - what to display
#   key - what player types (1-12 or the name)
#   desc - flavor text shown in combat
#   dmg_mult - multiplier on base_attack
#   acc_mod - modifier to hit chance (0.0 to 1.0 added to base 0.85)
#   stamina_cost - how much stamina it drains
#   effect - status to apply, or None
#   effect_chance - 0.0 to 1.0 chance of applying the effect

player_move_list = {
    1: {
        "name": "Quick Strike",
        "key": "quick strike",
        "desc": "A fast jab. Nothing flashy, just gets the job done.",
        "dmg_mult": 0.8,
        "acc_mod": 0.12,
        "stamina_cost": 5,
        "effect": None,
        "effect_chance": 0.0
    },
    2: {
        "name": "Heavy Slash",
        "key": "heavy slash",
        "desc": "You wind up and put everything into it. Might miss, but it hurts when it lands.",
        "dmg_mult": 1.6,
        "acc_mod": -0.15,
        "stamina_cost": 15,
        "effect": None,
        "effect_chance": 0.0
    },
    3: {
        "name": "Shield Bash",
        "key": "shield bash",
                "desc": "You slam your shield into the enemy. Low damage but might stun them.",
        "dmg_mult": 0.5,
        "acc_mod": 0.05,
        "stamina_cost": 10,
        "effect": "stun",
        "effect_chance": 0.35
    },
    4: {
        "name": "Reckless Smash",
        "key": "reckless smash",
                "desc": "Absolutely zero technique. Just pure violence. Leaves you wide open tho.",
        "dmg_mult": 2.0,
        "acc_mod": -0.20,
        "stamina_cost": 20,
        "effect": None,
        "effect_chance": 0.0
    },
    5: {
        "name": "Focused Strike",
        "key": "focused strike",
        "desc": "You slow down, breathe, aim carefully. It never misses. Just moderate damage.",
        "dmg_mult": 1.0,
        "acc_mod": 0.50,
        "stamina_cost": 12,
        "effect": None,
        "effect_chance": 0.0
    },
    6: {
        "name": "Desperate Lunge",
        "key": "desperate lunge",
        "desc": "A gamble. Deals massive bonus damage when ur nearly dead. Risky as anything.",
        "dmg_mult": 2.5,
        "acc_mod": -0.10,
        "stamina_cost": 25,
        "effect": None,
        "effect_chance": 0.0
    },
    7: {
        "name": "Bleed Cut",
        "key": "bleed cut",
                "desc": "A careful slice aimed at the tendons. Doesn't hurt much now but they'll bleed for a few turns.",
        "dmg_mult": 0.7,
        "acc_mod": 0.05,
                "stamina_cost": 10,
        "effect": "bleed",
        "effect_chance": 0.65
    },
    8: {
        "name": "Burning Palm",
        "key": "burning palm",
        "desc": "You channel some weird heat into ur 