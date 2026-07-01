# GridCrawler Engine

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

## how to run it
first, make sure u have requirements installed:
```bash
pip install -r requirements.txt
```
to see the engine in action (it runs a mock simulation stream):
```bash
python game_simulation_engine.py
```

### testing everything
i spent way too much time writing tests (38 of them!!) to make sure nothing explodes. u can run them with:
```bash
python -m pytest tests/
```

anyway, hope u like it!



