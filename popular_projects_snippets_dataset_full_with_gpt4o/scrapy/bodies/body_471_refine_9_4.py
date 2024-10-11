from importlib import import_module # pragma: no cover
from pkgutil import iter_modules # pragma: no cover

path = 'example_module' # pragma: no cover
def walk_modules(path):# pragma: no cover
    return ['module1', 'module2'] # pragma: no cover

from importlib import import_module # pragma: no cover
from pkgutil import iter_modules # pragma: no cover

path = 'scrapy.utils' # pragma: no cover
def walk_modules(path):# pragma: no cover
    return [scrapy.utils._compression, scrapy.utils.asyncgen, scrapy.utils.benchserver, scrapy.utils.boto, scrapy.utils.conf, scrapy.utils.console, scrapy.utils.curl, scrapy.utils.datatypes, scrapy.utils.decorators, scrapy.utils.defer, scrapy.utils.deprecate, scrapy.utils.display, scrapy.utils.engine, scrapy.utils.ftp, scrapy.utils.gz, scrapy.utils.httpobj, scrapy.utils.iterators, scrapy.utils.job, scrapy.utils.log, scrapy.utils.misc, scrapy.utils.ossignal, scrapy.utils.project, scrapy.utils.python, scrapy.utils.reactor, scrapy.utils.request, scrapy.utils.response, scrapy.utils.serialize, scrapy.utils.signal, scrapy.utils.sitemap, scrapy.utils.spider, scrapy.utils.ssl, scrapy.utils.template, scrapy.utils.test, scrapy.utils.testproc, scrapy.utils.testsite, scrapy.utils.trackref, scrapy.utils.url, scrapy.utils.versions] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/misc.py
from l3.Runtime import _l_
"""Loads a module and all its submodules from the given module path and
    returns them. If *any* module throws an exception while importing, that
    exception is thrown back.

    For example: walk_modules('scrapy.utils')
    """

mods = []
_l_(18419)
mod = import_module(path)
_l_(18420)
mods.append(mod)
_l_(18421)
if hasattr(mod, '__path__'):
    _l_(18428)

    for _, subpath, ispkg in iter_modules(mod.__path__):
        _l_(18427)

        fullpath = path + '.' + subpath
        _l_(18422)
        if ispkg:
            _l_(18426)

            mods += walk_modules(fullpath)
            _l_(18423)
        else:
            submod = import_module(fullpath)
            _l_(18424)
            mods.append(submod)
            _l_(18425)
aux = mods
_l_(18429)
exit(aux)
