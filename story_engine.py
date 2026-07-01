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
    "certainty of a coordinate. But the Grid is not merely a 