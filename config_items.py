# config_items.py
# consumable item data for the inventory and shop systems.
# each item has a potency multiplier 
# healers are so expensive in this game.
consumables = {
    1: {
        'id': 1,
        'item_name': "Health Juice",
        'item_type': "healing",
        'potency_multiplier': 1.2,
        'cooldown_ticks': 3,
        'slang_alert_text': "clutched the heal! health juice is working."
    },
    2: {
        'id': 2,
        'item_name': "Recovery Potion",
        'item_type': "healing",
        'potency_multiplier': 1.5,
        'cooldown_ticks': 5,
        'slang_alert_text': "feeling better! hp looking decent now."
    },
    3: {
        'id': 3,
        'item_name': "Guelph Elixir",
        'item_type': "buff",
        'potency_multiplier': 1.3,
        'cooldown_ticks': 10,
        'slang_alert_text': "elixir buff active! u feel stronger already."
    },
    4: {
        'id': 4,
        'item_name': "Super Soda",
        'item_type': "buff",
                'potency_multiplier': 2.0,
        'cooldown_ticks': 15,
        'slang_alert_text': "pro mode unlocked! damage output is high."
    },
    5: {
        'id': 5,
        'item_name': "Strange Mushroom",
        'item_type': "buff",
        'potency_multiplier': 3.0,
        'cooldown_ticks': 20,
        'slang_alert_text': "kinda weird... but the buff is huge!"
    },
    6: {
        'id': 6,
        'item_name': "Coffee Recharge",
        'item_type': "healing",
        'potency_multiplier': 1.8,
        'cooldown_ticks': 6,
        'slang_alert_text': "break time! energy restored and feeling fresh."
    },
    7: {
        'id': 7,
        'item_name': "Giant Slurp",
        'item_type': "healing",
        'potency_multiplier': 2.5,
        'cooldown_ticks': 12,
        'slang_alert_text': "health bar is basically overflowing now."
    },
    8: {
        'id': 8,
        'item_name': "Energy Slop",
        'item_type': "buff",
        'potency_multiplier': 1.1,
                'cooldown_ticks': 2,
        'slang_alert_text': "it tastes like static but it works i guess."
    },
    9: {
        'id': 9,
        'item_name': "Overclock Chip",
        'item_type': "buff",
        'potency_multiplier': 1.7,
        'cooldown_ticks': 8,
        'slang_alert_text': "system overclocked! speed is through the roof!"
    },
    10: {
        'id': 10,
        'item_name': "Charisma Serum",
        'item_type': "buff",
        'potency_multiplier': 1.5,
        'cooldown_ticks': 10,
        'slang_alert_text': "confidence peaking! enemies are backing off."
    },
    11: {
        'id': 11,
        'item_name': "Aura Booster",
        'item_type': "buff",
        'potency_multiplier': 1.4,
        'cooldown_ticks': 7,
        'slang_alert_text': "barrier active! huge defense boost for now."
    },
    12: {
        'id': 12,
        'item_name': "Gamer Fuel",
        'item_type': "buff",
        'potency_multiplier': 2.2,
        'cooldown_ticks': 18,
                'slang_alert_text': "energy drink vibes! twitch reflexes active."
    },
    13: {
        'id': 13,
        'item_name': "System Patch",
        'item_type': "debuff_cleaner",
                'potency_multiplier': 1.0,
        'cooldown_ticks': 5,
        'slang_alert_text': "system patched! all weird effects are gone."
    },
    14: {
        'id': 14,
        'item_name': "Spicy Ramen",
        'item_type': "buff",
        'potency_multiplier': 1.6,
                'cooldown_ticks': 9,
        'slang_alert_text': "TOO HOT! fire damage added to ur next hit."
    },
    15: {
        'id': 15,
        'item_name': "Ice Coffee",
        'item_type': "buff",
        'potency_multiplier': 1.3,
        'cooldown_ticks': 4,
        'slang_alert_text': "brain freeze but fast! speed up!"
    },
    16: {
        'id': 16,
        'item_name': "Antidote Slime",
        'item_type': "debuff_cleaner",
        'potency_multiplier': 1.0,
        'cooldown_ticks': 4,
                'slang_alert_text': "it's gross and sticky but the poison is gone."
    },
    17: {
        'id': 17,
        'item_name': "Burn Cream",
        'item_type': "debuff_cleaner",
        'potency_multiplier': 1.0,
        'cooldown_ticks': 4,
        'slang_alert_text': "fire damage stopped! cooling down now."
    },
    18: {
        'id': 18,
        'item_name': "Detox Tea",
        'item_type': "debuff_cleaner",
        'potency_multiplier': 1.0,
        'cooldown_ticks': 6,
        'slang_alert_text': "cleaning out the system! feeling pure again."
    },
    19: {
        'id': 19,
        'item_name': "Focus Mint",
        'item_type': "buff",
        'potency_multiplier': 1.25,
        'cooldown_ticks': 5,
        'slang_alert_text': "fresh breath and better accuracy."
    },
    20: {
        'id': 20,
        'item_name': "Rage Beans",
        'item_type': "buff",
        'potency_multiplier': 2.8,
        'cooldown_ticks': 25,
                'slang_alert_text': "BEANS OF FURY! damage is double! watch out."
    },
    21: {
        'id': 21,
        'item_name': "Doom Counter Pill",
        'item_type': "debuff_cleaner",
        'potency_multiplier': 1.0,
        'cooldown_ticks': 20,
        'slang_alert_text': "death delayed! doom status is cleared."
    },
    22: {
        'id': 22,
        'item_name': "Stamina Cookie",
        'item_type': "buff",
        'potency_multiplier': 1.4,
        'cooldown_ticks': 3,
                'slang_alert_text': "sugar rush! stamina penalties reduced."
    },
    23: {
        'id': 23,
        'item_name': "Phoenix Feather",
        'item_type': "healing",
        'potency_multiplier': 5.0,
        'cooldown_ticks': 50,
        'slang_alert_text': "BACK FROM THE DEAD! full health restored."
    },
    24: {
        'id': 24,
        'item_name': "Gold Apple",
        'item_type': "buff",
        'potency_multiplier': 10.0,
        'cooldown_ticks': 100,
                'slang_alert_text': "POWER LEVEL OVER 9000! every stat is boosted."
    },
    25: {
      'id': 25,
        'item_name': "Midas Touch Paste",
        'item_type': "buff",
  'potency_multiplier': 1.5,
        'cooldown_ticks': 15,
        'slang_alert_text': "everything u hit turns to loot! cash money."
    }
}

