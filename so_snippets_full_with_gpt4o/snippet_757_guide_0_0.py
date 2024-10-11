import sys # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4675728/redirect-stdout-to-a-file-in-python
from l3.Runtime import _l_
class out_to_lt():
    _l_(14374)

    def __init__(self, lt):
        _l_(14362)

        if type(lt) == list:
            _l_(14361)

            self.lt = lt
            _l_(14359)
        else:
            raise Exception("Need to pass a list")            
            _l_(14360)            
    def __enter__(self):
        _l_(14369)

        try:
            import sys
            _l_(14364)

        except ImportError:
            pass
        self._sys = sys
        _l_(14365)
        self._stdout = sys.stdout
        _l_(14366)
        sys.stdout = self
        _l_(14367)
        aux = self
        _l_(14368)
        return aux
    def write(self,txt):
        _l_(14371)

        self.lt.append(txt)    
        _l_(14370)    
    def __exit__(self, type, value, traceback):
        _l_(14373)

        self._sys.stdout = self._stdout
        _l_(14372)

lt = []
_l_(14375)
with out_to_lt(lt) as o:
    _l_(14378)

    print("Test 123\n\n")
    _l_(14376)
    print(help(str))
    _l_(14377)

class out_to_lt():
    _l_(14384)

    ...
    _l_(14379)
    def isatty(self):
        _l_(14381)

        aux = True #True: You're running in a real terminal, False:You're being piped, redirected, cron
        _l_(14380) #True: You're running in a real terminal, False:You're being piped, redirected, cron
        return aux #True: You're running in a real terminal, False:You're being piped, redirected, cron
    def flush(self):
        _l_(14383)

        pass
        _l_(14382)

