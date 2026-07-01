# config_weapons.py
# master dictionary for all player weapons.
# includes raw damage, crit chances, and weights for inventory sorting.
# still tweaking the damage values for late-game balancing.

weapons = {
    1: {
        'id': 1,
        'name': "Noob Stick",
        'min_level': 1,
        'raw_damage': 5,
        'crit_chance': 0.05,
        'weight': 2.0,
        'flavor_text': "literally just a stick i found in the backyard. it's kinda sticky and looks like it might snap if u hit a rock too hard but hey it's better than nothing i guess?"
    },
    2: {
        'id': 2,
                'name': "Rusty Butter Knife",
        'min_level': 2,
        'raw_damage': 8,
        'crit_chance': 0.08,
        'weight': 0.5,
        'flavor_text': "found this in a trash can behind the diner. it's super rusty and probably gives enemies tetanus if u actually manage to pierce their skin lol it's not even sharp."
    },
    3: {
        'id': 3,
        'name': "Cracked Branch",
                'min_level': 3,
        'raw_damage': 12,
        'crit_chance': 0.03,
        'weight': 3.0,
        'flavor_text': "this branch is slightly bigger than the noob stick but it has a huge crack down the middle. if it breaks it's basically game over for u but it hits pretty okay."
    },
    4: {
        'id': 4,
        'name': "Dull Pocketknife",
        'min_level': 4,
        'raw_damage': 15,
        'crit_chance': 0.12,
        'weight': 0.3,
        'flavor_text': "my grandpa gave me this for my birthday but i used it to cut open too many boxes so now it's dull as heck. u gotta really poke 'em hard to make it count."
    },
    5: {
        'id': 5,
        'name': "Cardboard Tube",
        'min_level': 5,
        'raw_damage': 18,
                'crit_chance': 0.02,
        'weight': 0.1,
        'flavor_text': "u know that sound a cardboard tube makes when u hit someone? THWACK. it's lowkey satisfying but it does zero penetration damage. mostly emotional damage."
    },
    6: {
        'id': 6,
        'name': "Old Broomstick",
        'min_level': 6,
        'raw_damage': 22,
        'crit_chance': 0.04,
        'weight': 1.5,
                'flavor_text': "stole this from the janitor closet. it's long so u can poke mobs from a distance but don't expect to be doing any major damage unless u hit their eyes."
    },
    7: {
        'id': 7,
        'name': "Chipped Hatchet",
        'min_level': 8,
        'raw_damage': 28,
        'crit_chance': 0.10,
        'weight': 4.5,
                'flavor_text': "it's missing a chunk of the blade which makes it look kinda scary but it's actually just bad craftsmanship. still chops better than a stick though!"
    },
    8: {
        'id': 8,
        'name': "Slightly Heavy Rock",
        'min_level': 10,
        'raw_damage': 35,
        'crit_chance': 0.01,
        'weight': 10.0,
                'flavor_text': "literally just a rock. it's heavy and hurts a lot if u drop it on ur toe. imagine what it does to a goblin's head lol. primitive style active."
    },
    9: {
        'id': 9,
        'name': "Squeegee of Justice",
        'min_level': 11,
        'raw_damage': 42,
        'crit_chance': 0.07,
        'weight': 1.2,
                'flavor_text': "clean up the streets literally. it's got a rubber edge that squeaks when u hit stuff. super annoying for enemies but helpful for morale."
    },
    10: {
        'id': 10,
        'name': "Iron Spork",
        'min_level': 12,
        'raw_damage': 48,
        'crit_chance': 0.15,
        'weight': 0.8,
                'flavor_text': "is it a spoon? is it a fork? it's an iron weapon of lunch-time destruction. the points are sharp enough to hurt and the spoon part is good for scooping out loot."
    },
    11: {
        'id': 11,
        'name': "Copper Cleaver",
        'min_level': 14,
        'raw_damage': 55,
        'crit_chance': 0.11,
        'weight': 5.0,        'flavor_text': "copper is soft so it dents a lot but it's heavy and wide. good for hacking through mobs that have low physical defense."
    },
    12: {
        'id': 12,
        'name': "Spiked Baseball Bat",
        'min_level': 15,
        'raw_damage': 62,
        'crit_chance': 0.18,
        'weight': 3.5,
        'flavor_text': "classic zombie apocalypse vibes. some rusted nails sticking out of a wooden bat. it's brutal and simple. exactly what u need for the mid-game grind."
    },
    13: {
        'id': 13,
        'name': "Mechanical Keyboard",
        'min_level': 16,
        'raw_damage': 70,
        'crit_chance': 0.25,
        'weight': 2.5,
                'flavor_text': "this mechanical keyboard has blue switches so it's super loud. every hit sounds like a click-clack and it probably does extra damage to anyone who hates typing sounds."
    },
    14: {
        'id': 14,
        'name': "Overpowered Scythe",
        'min_level': 18,
        'raw_damage': 85,
        'crit_chance': 0.14,
        'weight': 7.0,
                'flavor_text': "look at this thing. the blade is curved like a question mark because i couldnt draw a straight scythe properly lol but it slices good enough."
    },
    15: {
        'id': 15,
                'name': "Fancy Dagger",
                        'min_level': 19,
        'raw_damage': 95,
        'crit_chance': 0.40,
        'weight': 1.0,
                'flavor_text': "this dagger is so shiny it actually distracts enemies before u stab 'em. it's really fast too so u can get those quick stabs in."
    },
    16: {
        'id': 16,
        'name': "Jagged Slicer",
        'min_level': 20,
        'raw_damage': 110,
        'crit_chance': 0.22,
        'weight': 4.0,
                'flavor_text': "don't ask about the design, i was tired when i coded this one. it's got a weird jagged edge that makes it look like it's vibrating. kinda unsettling."
    },
    17: {
        'id': 17,
        'name': "Shadow Dirk",
        'min_level': 22,
                'raw_damage': 130,
        'crit_chance': 0.35,
        'weight': 0.9,
                'flavor_text': "super edgy black dagger. it's hard to see in the dark so u can sneak up on people. i wanted to make it turn u invisible but that was too hard to code lol."
    },
    18: {
        'id': 18,
        'name': "Titanium Crowbar",
        'min_level': 24,
        'raw_damage': 150,
        'crit_chance': 0.12,
        'weight': 6.5,
                'flavor_text': "half-life vibes. titanium makes it light but strong. good for prying open chests AND skulls. universal tool for a universal hero."
    },
    19: {
        'id': 19,
        'name': "Katana from the Mall",
        'min_level': 25,
        'raw_damage': 180,
        'crit_chance': 0.28,
        'weight': 3.2,
                'flavor_text': "looks cool in the store window but it's actually just cheap stainless steel. it'll probably snap if u hit something really hard but for now u look like a pro."
    },
    20: {
        'id': 20,
        'name': "Laser Pointer Wand",
        'min_level': 27,
        'raw_damage': 210,
        'crit_chance': 0.15,
        'weight': 0.4,
                'flavor_text': "it doesnt actually fire lasers it just points at things really precisely. but if u poke someone in the eye with it it hurts like crazy. super high accuracy."
    },
    21: {
        'id': 21,
        'name': "Massive Greatsword",
        'min_level': 30,
        'raw_damage': 250,
        'crit_chance': 0.08,
        'weight': 25.0,
                'flavor_text': "this sword is absolutely massive. it's extremely thick. u need like max strength just to lift it but when it hits it levels the whole area."
    },
    22: {
        'id': 22,
        'name': "Beta Tester's Club",
        'min_level': 31,
        'raw_damage': 280,
        'crit_chance': 0.10,
        'weight': 12.0,
                'flavor_text': "a mace made out of discarded beta test servers. it's full of bugs and glitches which somehow makes it do more damage? weird logic but whatever."
    },
    23: {
        'id': 23,
        'name': "Glitch Blade",
        'min_level': 33,
        'raw_damage': 320,
        'crit_chance': 0.30,
        'weight': 2.8,
                'flavor_text': "the blade keeps flickering in and out of existence. it's hard for mobs to block because they cant see where it is half the time. totally unintended feature."
    },
    24: {
        'id': 24,
        'name': "Phantom Rapier",
        'min_level': 35,
        'raw_damage': 380,
        'crit_chance': 0.45,
        'weight': 1.5,
                'flavor_text': "it's see-through and cold to the touch. it bypasses some armor because it's slightly ghostly. kinda spooky but really strong for late game."
    },
    25: {
        'id': 25,
        'name': "Quantum Claymore",
        'min_level': 38,
        'raw_damage': 450,
        'crit_chance': 0.15,
        'weight': 18.0,
                'flavor_text': "exists in multiple states at once. u never know if u hit 'em till u look at their health bar. physics are weird in the void abyss."
    },
    26: {
        'id': 26,
        'name': "Elite Avenger",
        'min_level': 41,
        'raw_damage': 520,
        'crit_chance': 0.25,
        'weight': 8.5,
                'flavor_text': "the ultimate weapon for the lead dev... i mean, for the top-tier player. it's perfectly balanced and does massive damage. only for the elites."
    },
    27: {
        'id': 27,
        'name': "Omega Obliterator",
        'min_level': 44,
        'raw_damage': 650,
        'crit_chance': 0.10,
        'weight': 35.0,
                'flavor_text': "this thing is so big it literally covers half the screen when u equip it. it obliterates everything in one hit usually. absolute unit of a weapon."
    },
    28: {
        'id': 28,
        'name': "Void Reaver",
                'min_level': 47,
        'raw_damage': 800,
        'crit_chance': 0.35,
        'weight': 5.0,
                'flavor_text': "made from the literal fabric of the game engine's memory leaks. it consumes data and enemies alike. super dangerous to even hold it."
    },
    29: {
        'id': 29,
        'name': "Chrono Carbine",
        'min_level': 49,
        'raw_damage': 1000,
        'crit_chance': 0.50,
        'weight': 3.0,
                'flavor_text': "a gun from the future i think? it fires bullets of pure time. i didnt know how to code projectiles so it just behaves like a really long sword lol."
    },
    30: {
        'id': 30,
        'name': "The Dev Sword",
        'min_level': 50,
        'raw_damage': 9999,
        'crit_chance': 1.0,
        'weight': 0.0,
                'flavor_text': "i literally gave myself admin powers with this one. it's invisible and weightless and kills anything in one frame. don't tell the players lol."
    }
}

# magic system postponed for now. parsing complex spell strings is taking
# too much time and it's better to focus on melee and items first.
# maybe add it back in a future patch once the core loop is rock solid.
#
# magic_wands = {
#     1: {"name": "Wood Wand", "mana": 10, "element": "None"},
#     2: {"name": "Fire Wand", "mana": 20, "element": "Fire"},
#     3: {"name": "Ice Stick", "mana": 20, "element": "Ice"},
#     4: {"name": "Zap Baton", "mana": 30, "element": "Lightning"},
#     5: {"name": "Dark Orb", "mana": 50, "element": "Shadow"},
#     6: {"name": "Holy Staff", "mana": 50, "element": "Light"},
#     7: {"name": "Earth Rod", "mana": 40, "element": "Earth"},
#     8: {"name": "Wind Fan", "mana": 35, "element": "Wind"},
#     9: {"name": "Elder Wand", "mana": 100, "element": "All"},
#     10: {"name": "The Stick of Truth", "mana": 999, "element": "OP"}
# }

