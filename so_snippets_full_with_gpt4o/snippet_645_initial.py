# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/276052/how-to-get-current-cpu-and-ram-usage-in-python
from l3.Runtime import _l_
try:
    import os
    _l_(15100)

except ImportError:
    pass
try:
    import re
    _l_(15102)

except ImportError:
    pass

CUT_OFF = 90
_l_(15103)

def get_cpu_load():
    _l_(15112)

    cmd = "ps -Ao user,uid,comm,pid,pcpu --sort=-pcpu | head -n 2 | tail -1"
    _l_(15104)
    response = os.popen(cmd, 'r').read()
    _l_(15105)
    arr = re.findall(r'\S+', response)
    _l_(15106)
    print(arr)
    _l_(15107)
    needKill = float(arr[-1]) > CUT_OFF
    _l_(15108)
    if needKill:
        _l_(15111)

        r = os.popen(f"kill -9 {arr[-2]}")
        _l_(15109)
        print('kill:', r)
        _l_(15110)

if __name__ == '__main__':
    _l_(15114)

    # Test CPU with 
    # $ stress --cpu 1
    # crontab -e
    # Every 1 min
    # */1 * * * * sh dog.sh
    # ctlr o, ctlr x
    # crontab -l
    print(get_cpu_load())
    _l_(15113)

