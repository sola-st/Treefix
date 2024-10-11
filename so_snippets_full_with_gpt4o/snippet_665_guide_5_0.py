import sys # pragma: no cover
import subprocess # pragma: no cover
import pkg_resources # pragma: no cover
from pkg_resources import DistributionNotFound, VersionConflict # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12332975/installing-python-module-within-code
from l3.Runtime import _l_
try:
    import sys
    _l_(12169)

except ImportError:
    pass
try:
    import subprocess
    _l_(12171)

except ImportError:
    pass
try:
    import pkg_resources
    _l_(12173)

except ImportError:
    pass
try:
    from pkg_resources import DistributionNotFound, VersionConflict
    _l_(12175)

except ImportError:
    pass

def should_install_requirement(requirement):
    _l_(12182)

    should_install = False
    _l_(12176)
    try:
        _l_(12180)

        pkg_resources.require(requirement)
        _l_(12177)
    except (DistributionNotFound, VersionConflict):
        _l_(12179)

        should_install = True
        _l_(12178)
    aux = should_install
    _l_(12181)
    return aux


def install_packages(requirement_list):
    _l_(12190)

    try:
        _l_(12189)

        requirements = [
            requirement
            for requirement in requirement_list
            if should_install_requirement(requirement)
        ]
        _l_(12183)
        if len(requirements) > 0:
            _l_(12186)

            subprocess.check_call([sys.executable, "-m", "pip", "install", *requirements])
            _l_(12184)
        else:
            print("Requirements already satisfied.")
            _l_(12185)

    except Exception as e:
        _l_(12188)

        print(e)
        _l_(12187)

requirement_list = ['requests', 'httpx==0.18.2']
_l_(12191)
install_packages(requirement_list)
_l_(12192)

