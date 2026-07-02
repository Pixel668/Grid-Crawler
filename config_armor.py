# config_armor.py
# armor data with defense ratings and stamina penalties.
# stamina penalties added to balance high-tier heavy armor sets.

armor_sets = {
    1: {
        'id': 1,
        'armor_name': "Ragged T-Shirt",
        'defense_rating': 1,
        'stamina_penalty': 0,
        'min_level': 1,
        'description': "it's dirty and has holes in it. basically zero protection but at least u aren't naked while fighting slimes."
    },
    2: {
        'id': 2,
        'armor_name': "Soggy Hoodie",
        'defense_rating': 3,
        'stamina_penalty': 1,
        'min_level': 2,
        'description': "it rained and u didn't dry it. it's heavy and gross but the thick fabric stops some small scratches."
    },
    3: {
        'id': 3,
        'armor_name': "Bubble Wrap Vest",
        'defense_rating': 5,
        'stamina_penalty': 0,
        'min_level': 3,
        'description': "POP! every time u get hit it makes a sound. it's actually decent padding until all the bubbles are gone."
    },
    4: {
        'id': 4,
        'armor_name': "Cardboard Box Plate",
        'defense_rating': 8,
                'stamina_penalty': 2,
        'min_level': 4,
        'description': "u taped some shipping boxes together. it's surprisingly stiff but don't walk into any puddles or ur in trouble."
    },
    5: {
        'id': 5,
        'armor_name': "Trash Can Lid",
        'defense_rating': 12,
        'stamina_penalty': 5,
                'min_level': 5,
        'description': "u use it as a chestplate. it smells like old garbage and it's super clunky but it's metal so it works i guess."
    },
    6: {
        'id': 6,
        'armor_name': "Thick Winter Coat",
        'defense_rating': 15,
        'stamina_penalty': 8,
        'min_level': 7,
        'description': "it's like 90 degrees out but u need the defense. u might get heatstroke but at least the wolves cant bite thru it."
    },
    7: {
        'id': 7,
        'armor_name': "Worn Leather Jacket",
        'defense_rating': 20,
                'stamina_penalty': 3,
        'min_level': 9,      
         'description': "u look like a cool biker now. leather is actually good for armor. plus the zip works mostly."
    },
    8: {
        'id': 8,
        'armor_name': "Padded Sweatpants",
        'defense_rating': 25,
        'stamina_penalty': 2,
                'min_level': 10,
        'description': "super comfy and u stuffed some towels in the legs. stealthy because they don't make noise when u walk."
    },
    9: {
        'id': 9,
        'armor_name': "Chainmail Poncho",
        'defense_rating': 35,
        'stamina_penalty': 10,
        'min_level': 12,
        'description': "it's a poncho made of metal rings. it's weirdly fashionable and keeps the arrows out. heavy as heck tho."
    },
    10: {
        'id': 10,
        'armor_name': "Copper Chestpiece",
        'defense_rating': 45,
        'stamina_penalty': 15,
        'min_level': 14,
        'description': "bright orange and shiny. it'll turn green in a week if u don't clean it. solid physical defense for a beginner."
    },
    11: {
        'id': 11,
        'armor_name': "Reinforced Hockey Pads",
        'defense_rating': 55,
        'stamina_penalty': 8,
        'min_level': 16,
        'description': "u took high school hockey too seriously. these pads are designed for impacts. good for tanking hits from skeletons."
    },
    12: {
        'id': 12,
        'armor_name': "Riot Shield Vest",
        'defense_rating': 70,
        'stamina_penalty': 20,
        'min_level': 18,
        'description': "found this during a weird store clearance. it's bulletproof mostly. super heavy tho so u cant move fast."
    },
    13: {
                'id': 13,
        'armor_name': "Scrap Metal Pauldrons",
        'defense_rating': 85,
        'stamina_penalty': 12,
        'min_level': 20,
                'description': "u just bolted random metal parts to ur shoulders. looks crazy but it blocks a lot of damage from the sides."
    },
    14: {
        'id': 14,
        'armor_name': "Neon Cyber Windbreaker",
                'defense_rating': 100,
        'stamina_penalty': 2,
        'min_level': 22,
        'description': "it glows in the dark. that's bad for stealth but it has built-in forcefields... maybe? the dev hasn't coded forcefields yet so it's just high defense."
    },
    15: {
        'id': 15,
        'armor_name': "Gaming Cloak",
        'defense_rating': 120,
        'stamina_penalty': 0,
        'min_level': 25,
        'description': "it has RGB lights all over it. the fps on ur life goes up when u wear this. literally zero weight because it's mostly light."
    },
    16: {
        'id': 16,
        'armor_name': "Tactical Turtleneck",
        'defense_rating': 140,
        'stamina_penalty': 5,
        'min_level': 27,
        'description': "it's tactileneck! it's in a slightly darker black than the other one. high defense and very stealthy."
    },
    17: {
        'id': 17,
        'armor_name': "Iron Plated Tuxedo",
        'defense_rating': 180,
        'stamina_penalty': 15,
                'min_level': 30,
        'description': "fight the final boss in style. the tuxedo has iron plates sewn inside the lining. class and survival in one package."
    },
    18: {
        'id': 18,
        'armor_name': "Titanium Tracksuit",
        'defense_rating': 220,
        'stamina_penalty': 10,
        'min_level': 32,
        'description': "made for the fastest players. it's shiny and flexible but strong enough to stop a bullet. very expensive."
    },
        19: {
        'id': 19,
        'armor_name': "Kevlar Kimono",
        'defense_rating': 280,
        'stamina_penalty': 4,
        'min_level': 35,
        'description': "traditional style meets modern survival. it's light and looks cool in the wind. plus it's bulletproof (duh)."
        },
    20: {
        'id': 20,
        'armor_name': "Obsidian Overcoat",
        'defense_rating': 350,
        'stamina_penalty': 30,
        'min_level': 38,
                'description': "made of volcanic glass. it's sharp and heavy. if anyone tries to touch u they get cut but u also move like a snail."
    },
    21: {
        'id': 21,
                'armor_name': "Hardened Shell",
        'defense_rating': 450,
        'stamina_penalty': 5,
        'min_level': 40,
        'description': "the energy of a thousand players compressed into literal armor. it radiates a barrier that reduces incoming damage."
    },
    22: {
        'id': 22,
        'armor_name': "Matrix Trenchcoat",
        'defense_rating': 550,
        'stamina_penalty': 1,
        'min_level': 42,
        'description': "u can dodge bullets now... wait no that's a different feature i didnt code. but the armor value is high anyway."
    },
    23: {
        'id': 23,
        'armor_name': "Nano Mesh Jersey",
        'defense_rating': 700,
        'stamina_penalty': 0,
        'min_level': 44,
                'description': "tiny robots doing all the work to stop u from dying. it's super thin but stronger than diamond. feels like wearing nothing at all."
    },
    24: {
        'id': 24,
        'armor_name': "Quantum Parka",
        'defense_rating': 900,
        'stamina_penalty': 10,
        'min_level': 46,
        'description': "it exists in a state of being both hit and not hit simultaneously. most of the damage just passes thru u into another dimension."
    },
    25: {
        'id': 25,
        'armor_name': "Legendary Armor",
        'defense_rating': 1200,
        'stamina_penalty': 0,
        'min_level': 48,
        'description': "ur confidence is so high it literally forms a physical barrier. enemies are too stunned by ur presence to actually hurt u."
    },
    26: {
        'id': 26,
        'armor_name': "Bedrock Carapace",
        'defense_rating': 2000,
        'stamina_penalty': 100,
        'min_level': 49,
                'description': "u literally cant move anymore but nothing in this game can kill u. u are a mountain. u are bedrock. u are invincible."
    },
    27: {
        'id': 27,
        'armor_name': "Void Cloak",
        'defense_rating': 5000,
        'stamina_penalty': 0,
        'min_level': 50,
        'description': "made from deleted save files. it absorbs all light and all damage. u aren't even really there when u wear this."
    },
    28: {
        'id': 28,
        'armor_name': "Chrono Mail",
        'defense_rating': 8000,
        'stamina_penalty': 0,
        'min_level': 50,
        'description': "any damage u take is just sent to ur past self... wait let me check the math... yeah it means u don't die now lol."
    },
    29: {
        'id': 29,
        'armor_name': "The Admin Vest",
        'defense_rating': 99999,
        'stamina_penalty': -50,
        'min_level': 50,
                'description': "literally cheat code armor. i gave it negative stamina penalty so u can run forever. dev life is easy."
    },
    30: {
        'id': 30,
        'armor_name': "God Mode Sweatshirt",
        'defense_rating': 999999,
        'stamina_penalty': 0,
        'min_level': 50,
        'description': "if u managed to get this without being a dev then something is wrong. u are untouchable. u are the engine."
    }
}

def validate_armor_config():
    # check for negative defense ratings to prevent broken mitigation math.
    for aid in armor_sets:
        armor = armor_sets[aid]
        if armor['defense_rating'] < 0:
            print(f"yooo armor id {aid} is bugged!! negative defense??")
        else:
            # armor values look kinda valid i guess
            pass
    return True

# running the check just in case
validate_armor_config()

