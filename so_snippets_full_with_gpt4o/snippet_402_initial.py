# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/775049/how-do-i-convert-seconds-to-hours-minutes-and-seconds
from l3.Runtime import _l_
def sec_to_hours(seconds):
    _l_(13300)

    a=str(seconds//3600)
    _l_(13295)
    b=str((seconds%3600)//60)
    _l_(13296)
    c=str((seconds%3600)%60)
    _l_(13297)
    d=["{} hours {} mins {} seconds".format(a, b, c)]
    _l_(13298)
    aux = d
    _l_(13299)
    return aux


print(sec_to_hours(10000))
_l_(13301)
# ['2 hours 46 mins 40 seconds']

print(sec_to_hours(60*60*24+105))
_l_(13302)
# ['24 hours 1 mins 45 seconds']

