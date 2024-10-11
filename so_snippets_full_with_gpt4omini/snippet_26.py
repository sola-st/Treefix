# Extracted from https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
import collections
Player = collections.namedtuple('Player', 'score name')
d = {'John':5, 'Alex':10, 'Richard': 7}

worst = sorted(Player(v,k) for (k,v) in d.items())

best = sorted([Player(v,k) for (k,v) in d.items()], reverse=True)

player = best[1]
player.name
    'Richard'
player.score
    7

