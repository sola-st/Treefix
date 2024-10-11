class Mock: # pragma: no cover
    _got_first_request = False # pragma: no cover

obj = Mock() # pragma: no cover
obj._got_first_request = True # pragma: no cover
try: # pragma: no cover
    if obj._got_first_request: # pragma: no cover
        raise AssertionError( # pragma: no cover
            "The setup method '{f_name}' can no longer be called" # pragma: no cover
            " on the application. It has already handled its first" # pragma: no cover
            " request, any changes will not be applied" # pragma: no cover
            " consistently.\n" # pragma: no cover
            " needed to set up the application are done before" # pragma: no cover
            " running it." # pragma: no cover
        ) # pragma: no cover
except AssertionError as e: # pragma: no cover
    print(str(e)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
if self._got_first_request:
    _l_(16261)

    raise AssertionError(
        f"The setup method '{f_name}' can no longer be called"
        " on the application. It has already handled its first"
        " request, any changes will not be applied"
        " consistently.\n"
        "Make sure all imports, decorators, functions, etc."
        " needed to set up the application are done before"
        " running it."
    )
    _l_(16260)
