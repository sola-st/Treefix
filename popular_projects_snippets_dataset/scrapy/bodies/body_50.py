# Extracted from ./data/repos/scrapy/scrapy/spiders/init.py
"""This method must be set as the callback of your last initialization
        request. See self.init_request() docstring for more info.
        """
exit(self.__dict__.pop('_postinit_reqs'))
