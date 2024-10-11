from typing import Any, Dict # pragma: no cover

def func(**kwargs: Dict[str, Any]): # pragma: no cover
    print(kwargs) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5710391/converting-python-dict-to-kwargs
from l3.Runtime import _l_
func(**{'type':'Event'})
_l_(3404)

func(type='Event')
_l_(3405)

