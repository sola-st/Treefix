# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4697882/how-can-i-find-all-matches-to-a-regular-expression-in-python
from l3.Runtime import _l_
re.findall( r'all (.*?) are', 'all cats are smarter than dogs, all dogs are dumber than cats')
_l_(2855)
# Output: ['cats', 'dogs']

[x.group() for x in re.finditer( r'all (.*?) are', 'all cats are smarter than dogs, all dogs are dumber than cats')]
_l_(2856)
# Output: ['all cats are', 'all dogs are']

