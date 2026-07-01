# story_engine.py
# narrative triggers for the game. checks player level and zone coords
# to show typewriter chapters. using proper prose for the story content.

import string_helpers
import time

OPENING_NARRATIVE = [
    "",
    "========================================================================",
    "  T H E   G R I D :   A N   E X I S T E N T I A L   T R A V E R S A L  ",
    "========================================================================",
    "",
    "Before the memory was cold, there was only the Grida sterile, infinite",
    ttice of logic and light. Six columns. Seven rows. A coordinate system",
    "designed to contain the chaos of a nascent universe.",
    "",
    "The ancients called it 'The Origin'. They built their lives around the",
    "predictability of the (x, y) axes, finding comfort in the absolute",
    "certainty of a coordinate. But the Grid is not merely a map; it is a",
        "living organism, and it does not take kindly to intruders.",
    "",
        "Monsters manifested as the first logic errors began to ripple through",
    "the source code. The Deadlock Dragon was the first born of an infinite",
    "loop; the Quantum Glitch God, a manifestation of a thousand race",
    "conditions. They wait at the edges of your perception, hungry for",
        "unallocated memory.",
    "",
    "You have been initialized at (0,0). You are the latest iteration in",
    "a long line of failed processes. The Grid is watching. It remembers",
        "every step you take.",
    "",
    "Good luck, Process. You will need more than logic to survive this.",
    "",
    "========================================================================",
    "",
]

chapter_markers = {
    ("level", 5): [
        "\n[ CHAPTER I: THE FRAGILE ORIGIN ]",
              "The Beginner Meadows no longer offer the sanctuary they once did.",
                      "The air has turned cold, and the binary chirping of the insects has",
        "flattened into a persistent, unsettling hum. Something to the east",
                "stirsa corruption deep within the swamp. Old Man Greg watches you",
        "with eyes that have seen a thousand deletions. He does not speak,",
        "but his silence is a heavy warning. You are no longer just a visitor.",
    ],
    ("level", 10): [
        "\n[ CHAPTER II: THE WEIGHT OF THE AXES ]",
        "Reaching the tenth level is a milestone the Grid recognizes. The",
                "coordinates feel heavier now, as if the very geometry of the world",
        "is pressing against your skin. The danger ratings are no longer",
        "theoretical values; they are promises of violence. You are a known",
        "entity now, and the system is recalibrating its defenses.",
    ],
    ("level", 20): [
        "\n[ CHAPTER III: THROUGH THE LOOKING GLASS ]",
                "You have traversed half the known world. The Legacy Code Lich still",
        "shrieks in the swamp, and the Deadlock Dragon waits at the horizon,",
        "but you are no longer the frightened process that spawned in the",
        "meadows. The Grid hums with a new frequency. Something ancient and",
        "terrible is stirring at (5,6), sensing your growing footprint.",
    ],
        ("level", 30): [
        "\n[ CHAPTER IV: THE UNMAPPED VOID ]",
        "Level thirty. You have survived longer than 99% of the processes",
        "that came before you. The Quantum Glitch God has turned its gaze",
        "toward you, its many eyes flickering like corrupted pixels. The",
        "northern edge of the map is no longer a border; it is a challenge.",
                "Be carefulthe code is starting to fray where you 