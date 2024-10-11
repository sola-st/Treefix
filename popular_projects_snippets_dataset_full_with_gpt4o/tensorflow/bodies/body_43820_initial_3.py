n1 = 5 # pragma: no cover
n2 = 4 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
from l3.Runtime import _l_
i = 0
_l_(15607)
l = tf.TensorArray(tf.int32, size=0, dynamic_size=True, element_shape=())
_l_(15608)
while i < n1:
    _l_(15616)

    j = 0
    _l_(15609)
    s = 0
    _l_(15610)
    while j < n2:
        _l_(15613)

        s = s * 10 + i * j
        _l_(15611)
        j += 1
        _l_(15612)
    l = l.write(i, s)
    _l_(15614)
    i += 1
    _l_(15615)
aux = l.stack()
_l_(15617)
exit(aux)
