class MockNamespace: pass # pragma: no cover
namespace = MockNamespace() # pragma: no cover
option_strings = ['--test'] # pragma: no cover
dest = 'test_flag' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
from l3.Runtime import _l_
class FlagAction(argparse.Action):
    _l_(11935)

    # From http://bugs.python.org/issue8538

    def __init__(self, option_strings, dest, default=None,
                 required=False, help=None, metavar=None,
                 positive_prefixes=['--'], negative_prefixes=['--no-']):
        _l_(11930)

        self.positive_strings = set()
        _l_(11919)
        self.negative_strings = set()
        _l_(11920)
        for string in option_strings:
            _l_(11927)

            assert re.match(r'--[A-z]+', string)
            _l_(11921)
            suffix = string[2:]
            _l_(11922)
            for positive_prefix in positive_prefixes:
                _l_(11924)

                self.positive_strings.add(positive_prefix + suffix)
                _l_(11923)
            for negative_prefix in negative_prefixes:
                _l_(11926)

                self.negative_strings.add(negative_prefix + suffix)
                _l_(11925)
        strings = list(self.positive_strings | self.negative_strings)
        _l_(11928)
        super(FlagAction, self).__init__(option_strings=strings, dest=dest,
                                         nargs=0, const=None, default=default, type=bool, choices=None,
                                         required=required, help=help, metavar=metavar)
        _l_(11929)

    def __call__(self, parser, namespace, values, option_string=None):
        _l_(11934)

        if option_string in self.positive_strings:
            _l_(11933)

            setattr(namespace, self.dest, True)
            _l_(11931)
        else:
            setattr(namespace, self.dest, False)
            _l_(11932)

