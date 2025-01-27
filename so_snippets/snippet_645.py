# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/276052/how-to-get-current-cpu-and-ram-usage-in-python
from l3.Runtime import _l_
try:
    import os
    _l_(2604)

except ImportError:
    pass
try:
    import re
    _l_(2606)

except ImportError:
    pass

CUT_OFF = 90
_l_(2607)

def get_cpu_load():
    _l_(2616)

    cmd = "ps -Ao user,uid,comm,pid,pcpu --sort=-pcpu | head -n 2 | tail -1"
    _l_(2608)
    response = os.popen(cmd, 'r').read()
    _l_(2609)
    arr = re.findall(r'\S+', response)
    _l_(2610)
    print(arr)
    _l_(2611)
    needKill = float(arr[-1]) > CUT_OFF
    _l_(2612)
    if needKill:
        _l_(2615)

        r = os.popen(f"kill -9 {arr[-2]}")
        _l_(2613)
        print('kill:', r)
        _l_(2614)

if __name__ == '__main__':
    _l_(2618)

    # Test CPU with 
    # $ stress --cpu 1
    # crontab -e
    # Every 1 min
    # */1 * * * * sh dog.sh
    # ctlr o, ctlr x
    # crontab -l
    print(get_cpu_load())
    _l_(2617)

