# Extracted from https://stackoverflow.com/questions/492519/timeout-on-a-function-call
@killer_call(timeout=4)
bar(10)
Traceback (most recent call last):
  ...
__main__.TimeoutError: function 'bar' timed out after 4s

bar(2)
2

import multiprocessing as mp
import multiprocessing.queues as mpq
import functools
import dill

from typing import Tuple, Callable, Dict, Optional, Iterable, List, Any

class TimeoutError(Exception):

    def __init__(self, func: Callable, timeout: int):
        self.t = timeout
        self.fname = func.__name__

    def __str__(self):
            return f"function '{self.fname}' timed out after {self.t}s"


def _lemmiwinks(func: Callable, args: Tuple, kwargs: Dict[str, Any], q: mp.Queue):
    """lemmiwinks crawls into the unknown"""
    q.put(dill.loads(func)(*args, **kwargs))


def killer_call(func: Callable = None, timeout: int = 10) -> Callable:
    """
    Single function call with a timeout

    Args:
        func: the function
        timeout: The timeout in seconds
    """

    if not isinstance(timeout, int):
        raise ValueError(f'timeout needs to be an int. Got: {timeout}')

    if func is None:
        return functools.partial(killer_call, timeout=timeout)

    @functools.wraps(killer_call)
    def _inners(*args, **kwargs) -> Any:
        q_worker = mp.Queue()
        proc = mp.Process(target=_lemmiwinks, args=(dill.dumps(func), args, kwargs, q_worker))
        proc.start()
        try:
            return q_worker.get(timeout=timeout)
        except mpq.Empty:
            raise TimeoutError(func, timeout)
        finally:
            try:
                proc.terminate()
            except:
                pass
    return _inners

if __name__ == '__main__':
    @killer_call(timeout=4)
    def bar(x):
        import time
        time.sleep(x)
        return x

    print(bar(2))
    bar(10)

