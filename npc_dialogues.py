# npc_dialogues.py
# scripted NPC encounters mapped to zone coordinates.


npc_encounter_map = {
    (0, 0): {
        "npc_name": "Greg, the Weathered System-Scribe",
        "lines": [
            "Ah, a fresh process initialized at the Origin. It has been quite some time.",
            "I have occupied this meadow since the kernel was first compiled.",
            "Take heed, wanderer: the path north is a deceptive one. Many who seek",
            "glory at the edge find only an unforgiving termination by the Compiler Troll.",
            "Steel your spirit within these meadows before you test the higher danger ratings.",        "hint": "ADVICE: The 'status' command will reveal your internal attributes. Monitor them closely."
    },
        (0, 1): {
        "npc_name": "Kel, the Ethereal Merchant",
        "lines": [
            "Hush. Do you hear that? The static in the wind is particularly loud today.",
            "I deal in artifactsthings salvaged from the wreckage of failed builds.",
            "The merchants in the Suburb Mall are mere peddlers of mass-produced gear.",
            "If you survive the swamp to the east, perhaps we shall trade again.",
        ],
        "hint": "ADVICE: Typing 'shop' in established hubs will open the interface for trade."
        },
    (0, 3): {
        "npc_name": "Kira, the Data-Drifter",
        "lines": [
                        "Stop. You're real, aren't you? Not just another phantom projection?",
            "I've been calculating my way through this path for solar-cycles. I found",
            "a physical input device earlier, but the circuitry had completely oxidised.",
            "The forest to the east... they call it the Forest of the Forgotten Login.",
            "The trees themselves attempt to parse your credentials. Stay vigilant.",
        ],
        "hint": "ADVICE: The Muddy Swamp lies to the east. Its danger rating is a promise of pain."
    },
    (1, 2): {
        "npc_name": "Doz, the Swamp-Hermit",
        "lines": [
            "This dwelling is private. The sign was not a suggestion.",
            "...",
            "However, since you have waded through the muck to reach me... listen.",
            "Something ancient remains buried beneath the sediment of the Great Leak.",
            "The Legacy Code Lich guards the debts of the past. Defeat it, and the",
                        "murk may finally begin to recede. Until then, expect only more mud.",
        ],
        "hint": "ADVICE: Liches and specters possess higher drop rates for ancient artifacts."
    },
    (2, 0): {
        "npc_name": "Tomek, the Bastion Sentinel",
        "lines": [
            "Halt, Wanderer. You stand at the precipice of the Coastal Cliffs Arena.",
            "Here, your rank and history do not matter. Only the efficiency of your code.",
           "Type 'fight_mob' to issue a challenge. If you can survive three consecutive",
            "executions, you may find the Grid has more to offer than just binary dust.",
        ],
        "hint": "ADVICE: Victorious combat in the Arena yields substantial experience yields."
    },
    (2, 3): {
        "npc_name": "Yuna, the Harmonic Alchemist",
        "lines": [
            "A traveler! Thank the stars. I feared I would be erased in the next patch.",
                        "My elixirs are crafted from the pure, unrefracted light of the Crystal River.",
            "...but the Firewall Falcons have plundered my stores. I am rebuilding.",
            "Should you discover any raw components in your travels, return them hither.",
        ],
        "hint": "ADVICE: Command 'use' or 'heal' to consume restorative items during your journey."
    },
    (3, 0): {
        "npc_name": "Bron, the Retired Admin",
        "lines": [
            "You have that lookthe expression of one who has finally mapped the grid",
            "only to realize how small the drawing truly is.",
            "I once faced the Deadlock Dragon with a kernel-patch and a prayer. I lost.",
            "The second time, I possessed maxed defense and a heart full of rage. I triumphed.",
            "The secret to the dragon: do not panic when it freezes your thread. Wait.",
        ],
                "hint": "ADVICE: Use 'Freezing Shock' to interrupt the dragon's most devastating loops."
    },
    (3, 3): {
        "npc_name": "The Prophet of the Axis",
        "lines": [
            "You stand at the Nexus. The center of all things (x) and (y).",
            "Four corners. Four elemental corruptions. They grow stronger as you know them.",
            "Ice in the north, fire in the south, ruin in the east, and something in the",
            "west that the developer chose to never define. Avoid coordinate (5,6).",
            "It is the Terminus. The beginning of the end.",
        ],
        "hint": "ADVICE: Zone (5,6) is the Void Abyss. It is recommended only for the level 50 elite."
    },
    (4, 5): {
                "npc_name": "The Entity 404",
        "lines": [
          "SYSTEM ERROR. SCANNING... SCAN COMPLETE. Greetings, User.",
            "My presence here is a violation of the current map-schema. I migrated",
                        "from an unallocated block when the developer forgot to define (4,4).",
            "I possess assembly-level knowledge. The Quantum Glitch God is not a bug",
            "it is a feature that was never meant to be enabled. It is already aware of you.",
        ],
        "hint": "ADVICE: The Quantum Glitch God at (5,5) is a supreme threat. Prepare your healing."
    },
    (5, 6): {
        "npc_name": "THE FINAL WARDEN",
        "lines": [
            "The simulation ends here.",
            "You have navigated the lattice with unexpected efficiency.",
            "The gate beyond leads to the Final Boss. Your thread of existence",
            "is nearing its termination point. Are you prepared to execute?",
        ],
        "hint": "WARNING: This is the endgame. Ensure your attributes are maxed before entry."
    },
}

