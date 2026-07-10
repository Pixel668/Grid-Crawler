# GridCrawler Engine
<img width="601" height="218" alt="image" src="https://github.com/user-attachments/assets/ec307fec-f5ff-4d3c-8ae6-5dc853208886" />

yo! welcome to **GridCrawler**. this is a massive, headless, text-driven RPG simulation engine i've been working on. it's basically a backend for a super complex RPG game, but without the flashy graphics.

## what even is this?
it's a python-based engine that handles everything a real RPG needs:
- **massive world**: a 6x7 grid (42 zones!) each with their own monsters and descriptions.
- **combat system**: turn-based battles with crits, misses, and scaling enemies.
- **status effects**: poison, burn, freeze, bleed, and even a "doom" counter that kills u instantly if u don't clear it.
- **inventory manager**: carry up to 20 items and sort them with my custom (and slightly slow) bubble sort algorithm.
- **gear galore**: 30 unique weapons and 30 armor sets. 

## stuff u can do
- [x] move around the grid with simple commands.
- [x] fight mobs that scale with ur level (don't get too confident).
- [x] level up all the way to 50.
- [x] use items to heal or buff ur stats.
- [x] wear cool gear like a "Gaming Cloak" or a "Tactical Turtleneck".

### how to run it

**easiest way (just download & play):**
- grab the **GridCrawler.exe** file from the release
- double click it, ur in the grid

**if u wanna run from source:**
first, make sure u have requirements installed:
```bash
pip install -r requirements.txt
```
to see the engine in action:
```bash
python game_simulation_engine.py
```
**when u start it**
u should see this and just follow the prompts:


<img width="392" height="447" alt="image" src="https://github.com/user-attachments/assets/936e9a26-2517-4155-97cd-52581a4677c2" />

## commands u can use

once ur in the game, here's what u can do:

**moving around:**
- `n` - go north
- `s` - go south
- `e` - go east
- `w` - go west
- `map` - check out the full grid map

**fighting stuff:**
- `fight` or `attack` - pick a random mob in ur current zone and fight them (they scale with ur level)

**talking to people:**
- `talk` or `npc` - chat with NPCs if they're hanging around. they might have hints.

**managing ur stuff:**
- `bag` or `inventory` - check what u got (u can carry max 20 items)
- `use` or `consume` or `heal` - use a healing item from ur inventory
- `shop` or `store` - buy and sell gear if there's a shop nearby

**checking ur status:**
- `status` or `stats` - see ur HP, XP, level, all that good stuff
- `look` or `inspect` - get a detailed description of where u are

**other:**
- `help` - shows this list of commands (same one ur reading)
- `quit` or `exit` - peace out, end the game

### testing everything
i spent way too much time writing tests (38 of them!!) to make sure nothing explodes. u can run them with:
```bash
python -m pytest tests/
```

anyway, hope u like it!



