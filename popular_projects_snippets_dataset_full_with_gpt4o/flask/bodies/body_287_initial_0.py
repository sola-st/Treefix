from typing import Generator, Any, Callable # pragma: no cover

def generator_or_function(*args: Any, **kwargs: Any) -> Generator[int, None, None]: # pragma: no cover
    yield 1 # pragma: no cover
    yield 2 # pragma: no cover
    yield 3 # pragma: no cover
args = () # pragma: no cover
kwargs = {} # pragma: no cover
def stream_with_context(gen: Callable[[], Generator[int, None, None]]) -> None: # pragma: no cover
    gen_instance = gen() # pragma: no cover
    for item in gen_instance: # pragma: no cover
        print(item) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
gen = generator_or_function(*args, **kwargs)  # type: ignore
_l_(22495)  # type: ignore
aux = stream_with_context(gen)
_l_(22496)
exit(aux)
