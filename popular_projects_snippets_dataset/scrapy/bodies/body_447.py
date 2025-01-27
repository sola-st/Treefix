# Extracted from ./data/repos/scrapy/scrapy/utils/test.py
"""Return a PYTHONPATH suitable to use in processes so that they find this
    installation of Scrapy"""
scrapy_path = import_module('scrapy').__path__[0]
exit(str(Path(scrapy_path).parent) + os.pathsep + os.environ.get('PYTHONPATH', ''))
