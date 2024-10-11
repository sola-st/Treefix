from contextlib import contextmanager # pragma: no cover
from typing import Generator # pragma: no cover

def generator_or_function(*args, **kwargs) -> Generator[str, None, None]: return (f"Generated value {i}" for i in range(5)) # pragma: no cover
args = [1, 2, 3] # pragma: no cover
kwargs = {'key': 'value'} # pragma: no cover
@contextmanager# pragma: no cover
def stream_with_context(generator): yield generator() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
gen = generator_or_function(*args, **kwargs)  # type: ignore
_l_(4321)  # type: ignore
aux = stream_with_context(gen)
_l_(4322)
exit(aux)
