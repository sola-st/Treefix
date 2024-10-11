# Extracted from ./data/repos/scrapy/scrapy/utils/misc.py
"""Temporarily set environment variables inside the context manager and
    fully restore previous environment afterwards
    """

original_env = {k: os.environ.get(k) for k in kwargs}
os.environ.update(kwargs)
try:
    exit()
finally:
    for k, v in original_env.items():
        if v is None:
            del os.environ[k]
        else:
            os.environ[k] = v
