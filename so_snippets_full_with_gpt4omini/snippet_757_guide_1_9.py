import sys # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4675728/redirect-stdout-to-a-file-in-python
from l3.Runtime import _l_
class out_to_lt():
    _l_(2663)

    def __init__(self, lt):
        _l_(2651)

        if type(lt) == list:
            _l_(2650)

            self.lt = lt
            _l_(2648)
        else:
            raise Exception("Need to pass a list")            
            _l_(2649)            
    def __enter__(self):
        _l_(2658)

        try:
            import sys
            _l_(2653)

        except ImportError:
            pass
        self._sys = sys
        _l_(2654)
        self._stdout = sys.stdout
        _l_(2655)
        sys.stdout = self
        _l_(2656)
        aux = self
        _l_(2657)
        return aux
    def write(self,txt):
        _l_(2660)

        self.lt.append(txt)    
        _l_(2659)    
    def __exit__(self, type, value, traceback):
        _l_(2662)

        self._sys.stdout = self._stdout
        _l_(2661)

lt = []
_l_(2664)
with out_to_lt(lt) as o:
    _l_(2667)

    print("Test 123\n\n")
    _l_(2665)
    print(help(str))
    _l_(2666)

class out_to_lt():
    _l_(2673)

    ...
    _l_(2668)
    def isatty(self):
        _l_(2670)

        aux = True #True: You're running in a real terminal, False:You're being piped, redirected, cron
        _l_(2669) #True: You're running in a real terminal, False:You're being piped, redirected, cron
        return aux #True: You're running in a real terminal, False:You're being piped, redirected, cron
    def flush(self):
        _l_(2672)

        pass
        _l_(2671)

