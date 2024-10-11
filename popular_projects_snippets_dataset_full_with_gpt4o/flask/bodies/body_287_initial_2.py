from typing import Generator, Any # pragma: no cover
import contextlib # pragma: no cover

def generator_or_function(*args: Any, **kwargs: Any) -> Generator[int, None, None]:# pragma: no cover
    yield from range(5) # pragma: no cover
args = () # pragma: no cover
kwargs = {} # pragma: no cover
def stream_with_context(gen: Generator[int, None, None]) -> None:# pragma: no cover
    with contextlib.ExitStack() as stack:# pragma: no cover
        for _ in gen:# pragma: no cover
            pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
gen = generator_or_function(*args, **kwargs)  # type: ignore
_l_(22495)  # type: ignore
aux = stream_with_context(gen)
_l_(22496)
exit(aux)
