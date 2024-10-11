from typing import Any, List # pragma: no cover

class MockInnerConcrete:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.captured_inputs = []# pragma: no cover
# pragma: no cover
    def _call_flat(self, args: List[Any], captured_inputs: List[Any]) -> None:# pragma: no cover
        return 'Executed with args: ' + str(args) + ' and captured: ' + str(captured_inputs)# pragma: no cover
# pragma: no cover
inner_concrete = MockInnerConcrete() # pragma: no cover
args = [1, 2, 3] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_serialization.py
from l3.Runtime import _l_
aux = inner_concrete._call_flat(args, inner_concrete.captured_inputs)  # pylint:disable=protected-access
_l_(4823)  # pylint:disable=protected-access
exit(aux)  # pylint:disable=protected-access
