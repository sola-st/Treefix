n1 = 5 # pragma: no cover
n2 = 3 # pragma: no cover

n1 = 5 # pragma: no cover
n2 = 3 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
from l3.Runtime import _l_
i = 0
_l_(4310)
l = tf.TensorArray(tf.int32, size=0, dynamic_size=True, element_shape=())
_l_(4311)
while i < n1:
    _l_(4319)

    j = 0
    _l_(4312)
    s = 0
    _l_(4313)
    while j < n2:
        _l_(4316)

        s = s * 10 + i * j
        _l_(4314)
        j += 1
        _l_(4315)
    l = l.write(i, s)
    _l_(4317)
    i += 1
    _l_(4318)
aux = l.stack()
_l_(4320)
exit(aux)
