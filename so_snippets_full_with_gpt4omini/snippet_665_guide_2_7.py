import sys # pragma: no cover
import subprocess # pragma: no cover
import pkg_resources # pragma: no cover
from pkg_resources import DistributionNotFound, VersionConflict # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12332975/installing-python-module-within-code
from l3.Runtime import _l_
try:
    import sys
    _l_(994)

except ImportError:
    pass
try:
    import subprocess
    _l_(996)

except ImportError:
    pass
try:
    import pkg_resources
    _l_(998)

except ImportError:
    pass
try:
    from pkg_resources import DistributionNotFound, VersionConflict
    _l_(1000)

except ImportError:
    pass

def should_install_requirement(requirement):
    _l_(1007)

    should_install = False
    _l_(1001)
    try:
        _l_(1005)

        pkg_resources.require(requirement)
        _l_(1002)
    except (DistributionNotFound, VersionConflict):
        _l_(1004)

        should_install = True
        _l_(1003)
    aux = should_install
    _l_(1006)
    return aux


def install_packages(requirement_list):
    _l_(1015)

    try:
        _l_(1014)

        requirements = [
            requirement
            for requirement in requirement_list
            if should_install_requirement(requirement)
        ]
        _l_(1008)
        if len(requirements) > 0:
            _l_(1011)

            subprocess.check_call([sys.executable, "-m", "pip", "install", *requirements])
            _l_(1009)
        else:
            print("Requirements already satisfied.")
            _l_(1010)

    except Exception as e:
        _l_(1013)

        print(e)
        _l_(1012)

requirement_list = ['requests', 'httpx==0.18.2']
_l_(1016)
install_packages(requirement_list)
_l_(1017)

