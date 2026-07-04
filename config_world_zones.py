# config_world_zones.py
# master world map. each coordinate hash has its own lore, entry text,
# danger rating, and list of monsters that can spawn there.

world_map = {
    (0, 0): {
        'zone_name': "The Origin Meadows - Genesis",
        'entry_announcement': "Soft, emerald blades of grass sway in a gentle, algorithmic breeze. The air is remarkably clear, carrying the scent of fresh rain and uncompiled potential.",
        'lore_entry': "This is the Genesis Coordinatethe point from which all existence in the Grid is derived. It is said that the first iteration of life began here as a simple 'Hello World' broadcast into the void.",
        'danger_rating': 1,
        'spawnable_monster_ids': [1, 1, 2, 3, 4]
        (0, 1): {
        'zone_name': "The Origin Meadows - North",
        'entry_announcement': "The rolling hills continue toward the horizon, punctuated by clusters of binary wildflowers that flicker with a soft, neon glow.",
                'lore_entry': "Gamer Goblins often migrate through these northlands, preying on nascent processes. The soil here is rich with the discarded data-packets of those who failed to navigate the first axis.",
        'danger_rating': 1,
        'spawnable_monster_ids': [1, 2, 2, 3, 5]
        },
    (0, 2): {
        'zone_name': "The Origin Meadows - Fraying Edge",
        'entry_announcement': "The lush vegetation begins to give way to jagged outcroppings of grey, untextured stone. A low-frequency hum vibrates through the ground.",
        'lore_entry': "You stand at the boundary where the Meadows merge with the urban sprawl. The logic of the flora is beginning to break down, replaced by the cold, rigid geometry of the Suburbs.",
        'danger_rating': 2,
        'spawnable_monster_ids': [2, 3, 4, 5, 6]
    },
    (0, 3): {
        'zone_name': "Way of the Forsaken Input",
                'entry_announcement': "The path is littered with the rusted remains of physical hardware. A shattered monitor reflects the pale light of a distant, dying server.",
        'lore_entry': "Named in memory of 'NoobSlayer99', a legendary process who attempted to brute-force the Grid using only a primitive mechanical keyboard. His failure is a lesson in the necessity of efficient algorithms.",
        'danger_rating': 2,
        'spawnable_monster_ids': [3, 4, 6, 7, 8]
    },
    (0, 4): {
        'zone_name': "The Suburbs - Gated Entrance",
        'entry_announcement': "Rows of identical, pristine houses stretch into a lingering grey fog. The silence is absolute, save for the rhythmic clicking of a thousand smart-locks.",
        'lore_entry': "The Suburbs were synthesized during the Epoch of Expansion. They represent a forced attempt at structural order, though the absence of inhabitants suggests a deeper systemic failure.",
        'danger_rating': 3,
                'spawnable_monster_ids': [5, 6, 8, 9, 10]
    },
    (0, 5): {
        'zone_name': "The Suburbs - Still Cul-de-sac",
        'entry_announcement': "The pavement terminates at a circular drive. A child's tricycle sits abandoned in the center, its wheels slowly rotating in the stagnant air.",
        'lore_entry': "Local folklore speaks of a rogue developer who sought to simulate a perfect domestic life here, before being purged during a midnight deployment. The lingering melancholy is palpable.",
        'danger_rating': 3,
        'spawnable_monster_ids': [6, 7, 9, 10, 11]
    },
    (0, 6): {
        'zone_name': "The Suburbs - Derelict Mall",
        'entry_announcement': "Flickering neon signs cast long, distorted shadows across the cracked plaza. The fountain in the center pumps a viscous, iridescent liquid.",
                'lore_entry': "Once the economic heart of the first quadrant, the Mall now serves as a graveyard for commercial assets. It is a place where currency flows slowly and danger hides behind every sale sign.",
        'danger_rating': 4,
        'spawnable_monster_ids': [8, 9, 11, 12, 13]
    },
    (1, 0): {
        'zone_name': "The Muddy Swamp - Western Reach",
        thick with the scent of stagnant data and decaying logic. Every step into the dark slurry results in a wet, heavy suction.",
        'lore_entry': "The Swamp was formed when a gargantuan database overflow saturated the lower sectors. The muck is composed of millions of unindexed records, forever trapped in a state of slow decay.",
        'danger_rating': 3,
        'spawnable_monster_ids': [4, 5, 7, 8, 9]
    },
    (1, 1): {
        'zone_name': "The Muddy Swamp - Sunken Center",
                'entry_announcement': "Visibility is reduced to a few meters by a shroud of toxic, green vapor. The sounds of unseen creatures splashing in the deep mire echo through the trees.",
        'lore_entry': "This is the absolute nadir of the swamp. It is a sector where the 'Clean Code' philosophy was long ago abandoned in favor of messy, recursive survival.",
        'danger_rating': 4,
        'spawnable_monster_ids': [7, 8, 10, 11, 12]
    },
    (1, 2): {
        'zone_name': "The Muddy Swamp - Hermit's Respite",
                'entry_announcement': "A weathered shack perched on rotting stilts emerges from the mist. A flickering lantern hangs from the porch, casting a dim, jittery light.",
        'lore_entry': "Home to the Swamp Hermit, an ancient process who retreated from the Grid's society to study the underlying assembler code of the muck. He claims the swamp is sentient.",
        'danger_rating': 4,
        'spawnable_monster_ids': [9, 10, 12, 13, 14]
    },
    (1, 3): {
                'zone_name': "Forest of the Forgotten Login",
        'entry_announcement': "Shadowy trees with interconnected branches form a canopy that resembles a complex neural network. The wind carries the faint sound of whispered passwords.",
        'lore_entry': "The forest acts as a psychological filter for the Grid. It preys upon the insecurities of processes, manifesting their lost credentials as tangling vines and obscured paths.",
        'danger_rating': 3,
        'spawnable_monster_ids': [5, 6, 7, 8, 10]
    },
    (1, 4): {
        'zone_name': "Forest of the Forgotten Login - Deadlock",
        'entry_announcement': "The density of the timber becomes overwhelming. The trees here are locked in a perpetual embrace, their trunks fused by centuries of failed synchronization.",
        'lore_entry': "Rumors persist of a 'Legacy Support' division that attempted to map this sector using only outdated documentation. They were eventually absorbed by the forest itself.",
                'danger_rating': 4,
        'spawnable_monster_ids': [8, 9, 11, 12, 14]
    },
    (1, 5): {
        'zone_name': "The Crystal River - Pristine Bank",
        'entry_announcement': "The water is a flowing stream of liquid crystal, reflecting the blue light of the upper-system with startling fidelity.",
        'lore_entry': "The River is the Grid's primary garbage collection mechanism. It effectively flushes unreferenced objects and orphaned pointers toward the Great Null in the north.",
        'danger_rating': 5,
        'spawnable_monster_ids': [10, 11, 13, 14, 15]
    },
    (1, 6): {
        'zone_name': "The Crystal River - Arched Bridge",
                'entry_announcement': "A stone bridge, carved with intricate geometric patterns, spans the rushing data. Its surface is worn smooth by the passage of a million previous iterations.",
                        'lore_entry': "The bridge is a marvel of ancient engineering. It remains one of the few structures that has survived every major system refactor since the Second Epoch.",
        'danger_rating        'spawnable_monster_ids': [11, 12, 14, 15, 16]
    },
    (2, 0): {
        'zone_name': "The Glitch Dungeon - Fractured Entry",
        'entry_announcement': "The walls are composed of unrendered textures and flickering purple polygons. The air vibrates with the sound of a thousand persistent system errors.",
        'lore_entry': "This sector was intended to be the Grid's capital city, before a catastrophic 'Optimisation' patch corrupted the very foundations of the local geometry.",
        'danger_rating': 6,
        'spawnable_monster_ids': [12, 13, 15, 16, 17]
    },
    (2, 1): {
        'zone_name': "The Glitch Dungeon - Binary Hall",
                'entry_announcement': "Long, narrow corridors pulse with scrolling strings of binary code. The floor beneath your feet feels inconsistent, as if it might de-allocate at any second.",
        'lore_entry': "Every interaction in this hall is a gamble against the underlying logic. It is a place where race conditions and off-by-one errors are the primary laws of physics.",
        'danger_rating': 6,
        'spawnable_monster_ids': [13, 14, 16, 17, 18]
    },
    (2, 2): {
        'zone_name': "The Glitch Dungeon - Core Server Room",
        'entry_announcement': "Massive, glowing towers of light hum with immense power. The heat is stifling, and the smell of ozone is thick in the air.",
        'lore_entry': "The true heart of the dungeon. It is here that the regional lag originates, radiating outward from a central GPU that has been running at 100% capacity for decades.",
        'danger_rating': 7,
        'spawnable_monster_ids': [15, 16, 18, 19, 20]
    },
    (2, 3): {
                'zone_name': "The Glitch Dungeon - Egress Conduit",
        'entry_announcement': "A dark, slippery pipe leading back toward the surface. Cool air occasionally rushes down from the exit, carrying the scent of sanity.",
        'lore_entry': "The primary escape route for those who find the logic of the dungeon too taxing for their buffers. It is a humble exit for a humbling experience.",
        'danger_rating': 6,
        'spawnable_monster_ids': [14, 15, 17, 18, 19]
    },
    (2, 4): {
        'zone_name': "Compiler's Canyon - Rugged Pass",
        'entry_announcement': "Sheer cliffs of grey logic-stone rise on either side. The wind howls through the narrow pass, sounding like a thousands of simultaneous syntax errors.",
        'lore_entry': "The canyon was carved by the persistent flow of uncompiled source-code during the Great Integration. The stone is remarkably brittle and prone to sudden collapse.",
        'danger_rating': 5,
                'spawnable_monster_ids': [10, 11, 13, 14, 16]
    },
    (2, 5): {
        'zone_name': "Compiler's Canyon - Semicolon Wall",
        'entry_announcement': "An impassable barrier of stone blocks the path. It is covered in an intricate mosaic of semicolons and curly brackets.",
        'lore_entry': "Symbolic of the final check before a build is complete. Many processes have spent eternity staring at this wall, searching for the one missing character that would allow them to pass.",
        'danger_rating': 5,
        'spawnable_monster_ids': [11, 12, 14, 15, 17]
    },
    (2, 6): {
        'zone_name': "The Beta Testing Grounds - T-Pose Plains",
        'entry_announcement': "The horizon is filled with T-posing figures and untextured cubes. A giant, translucent overlay reading 'DEVELOPMENT BUILD' covers the sky.",
                'lore_entry': "A surreal landscape where the laws of immersion are suspended. It is a place of infinite possibility and zero polish, where the developer's whims are made manifest in 3D space.",
        'danger_rating': 6,
        'spawnable_monster_ids': [13, 14, 16, 17, 19]
    },
    (3, 0): {
        'zone_name': "Summit of the Admin - Ascent",
        'entry_announcement': "The air grows thin and cold. You feel the constant, heavy gaze of an unseen observer monitoring your every register change.",
        'lore_entry': "This mountain was grafted onto the map during a particularly manic weekend of development. Its slopes are steep because the developer forgot to implement a staircase.",
        'danger_rating': 7,
        'spawnable_monster_ids': [16, 17, 19, 20, 21]
    },
    (3, 1): {
        'zone_name': "Summit of the Admin - Overlook",
                'entry_announcement': "From this height, the entire Grid is visible as a pattern of glowing green lines against a backdrop of absolute nothingness.",
        'lore_entry': "The View Distance here is set to 'Maximum'. You can see the very edges of the simulation, and the flickering data-shadows of entities that have not yet been spawned.",
        'danger_rating': 8,
        'spawnable_monster_ids': [18, 19, 21, 22, 23]
    },
    (3, 2): {
        'zone_name': "The Great Rift - Gorge",
        'entry_announcement': "A gargantuan fissure in the earth reveals the blue background-color of the cosmos below. The edges of the rift are perfectly sharp and vertical.",
        'lore_entry': "A permanent scar from the 'Refactor of '21'. The developer attempted to delete a single unused variable and accidentally null-terminated the regional terrain.",
        'danger_rating': 7,
        'spawnable_monster_ids': [17, 18, 20, 21, 22]
    },
    (3, 3): {
                'zone_name': "The Great Rift - Suspension Bridge",
        'entry_announcement': "A narrow bridge of rope and planks sways violently in the wind. Every step is an 'if' statement that might return false.",
        'lore_entry': "The bridge is held together by three lines of uncommented code and a single 'TODO: Fix this' sticky note. Cross with extreme caution.",
        'danger_rating': 8,
        'spawnable_monster_ids': [19, 20, 22, 23, 24]
    },
    (3, 4): {
        'zone_name': "Valley of the 404 - Echo",
        'entry_announcement': "The terrain flickers in and out of phase. Your compass is spinning wildly, unable to find a stable North in this non-existent space.",
        valley of unreferenced indices. It is a pocket of space that the system failed to index, making it a natural haven for glitches and outcasts.",
        'danger_rating': 6,
        'spawnable_monster_ids': [14, 15, 17, 18, 20]
    },
    (3, 5): {
                'zone_name': "Valley of the 404 - Data Cache",
        'entry_announcement': "A hidden cave filled with the discarded remnants of previous game versions. You find a pile of 'Congratulations' messages and broken textures.",
                'lore_entry': "One of the few places where the history of the Grid is preserved. Someone has scrawled 'MADHAV WAS HERE' in 12pt Comic Sans on the far wall. It is truly chilling.",
        'danger_rating': 7,
                'spawnable_monster_ids': [16, 17, 19, 20, 22]
    },
    (3, 6): {
        'zone_name': "The Elite Arena - Proving Grounds",
        'entry_announcement': "Warriors in high-fidelity armor spar with phantoms of the past. The sound of clashing steel and triggered events constant and deafening.",
        'lore_entry': "The ultimate proving ground for the Grid's warriors. Most of the enemies here were originally designed as player-class archetypes before they were corrupted by greed.",
        'danger_rating': 9,
                'spawnable_monster_ids': [20, 21, 23, 24, 25]
    },
    (4, 0): {
        'zone_name': "Wasteland of the Abandoned Assets",
        'entry_announcement': "Toppled statues of forgotten heroes lie half-buried in the grey dust. Their low-polygon faces are frozen in expressions of permanent confusion.",
        'lore_entry': "A graveyard of discarded ideas. You can find the original 2D sprites of the Gamer Goblins here, if you are willing to dig through the untextured debris.",
        'danger_rating': 7,
        'spawnable_monster_ids': [15, 16, 18, 19, 21]
    },
    (4, 1): {
        'zone_name': "Wasteland of the Abandoned Assets - The Pit",
        'entry_announcement': "A gargantuan crater filled with the deafening sound of a thousand overlapping 'OOF' sound effects.",
        'lore_entry': "The system's literal 'Trash Bin'. Anything that is deleted without a confirmation dialog eventually washes into this gravity well.",
        'danger_rating': 8,
                'spawnable_monster_ids': [17, 18, 20, 21, 23]
    },
    (4, 2): {
        'zone_name': "The Lag Lagoon - Shallow Bank",
        'entry_announcement': "The water is thick and viscous, its surface rippling with the colors of unoptimized shaders. Every movement feels sluggish and delayed.",
        'lore_entry': "The lagoon is the primary source of the system's frame-rate drops. The water is actually a complex series of nested 