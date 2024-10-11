# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11941817/how-to-avoid-runtimeerror-dictionary-changed-size-during-iteration-error
from l3.Runtime import _l_
dicti = {
"k0_l0":{
    "k0_l1": {
        "k0_l2": {
                "k0_0":None,
                "k1_1":1,
                "k2_2":2.2
                }
        },
        "k1_l1":None,
        "k2_l1":"not none",
        "k3_l1":[]
    },
    "k1_l0":"l0"
}
_l_(12918)

def pop_nested_nulls(dicti):
    _l_(12925)

    for k in list(dicti):
        _l_(12923)

        if isinstance(dicti[k], dict):
            _l_(12922)

            dicti[k] = pop_nested_nulls(dicti[k])
            _l_(12919)
        elif not dicti[k]:
            _l_(12921)

            dicti.pop(k)
            _l_(12920)
    aux = dicti
    _l_(12924)
    return aux

{'k0_l0': {'k0_l1': {'k0_l2': {'k1_1': 1,
                               'k2_2': 2.2}},
           'k2_l1': 'not '
                    'none'},
 'k1_l0': 'l0'}
_l_(12926)

