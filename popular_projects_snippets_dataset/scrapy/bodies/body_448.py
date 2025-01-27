# Extracted from ./data/repos/scrapy/scrapy/utils/test.py
"""Return a OS environment dict suitable to fork processes that need to import
    this installation of Scrapy, instead of a system installed one.
    """
env = os.environ.copy()
env['PYTHONPATH'] = get_pythonpath()
exit(env)
