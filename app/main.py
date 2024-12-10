from players.elves.elf_ranger import ElfRanger
from players.elves.druid import Druid
from players.dwarves.dwarf_warrior import DwarfWarrior
from players.dwarves.dwarf_blacksmith import DwarfBlacksmith

def calculate_team_total_rating(team):
    return sum(player.get_rating() for player in team)

def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()