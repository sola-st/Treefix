# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    # pylint: disable=invalid-name
    ABC = collections.namedtuple('ABC', ['a', 'b', 'c'])
    DEFGHI = collections.namedtuple('DEFGHI', ['d', 'e', 'f', 'g', 'h', 'i'])
    # pylint: enable=invalid-name
    a_val = 42.0
    b_val = None
    c_val = 44.0
    a = constant_op.constant(a_val)
    b = control_flow_ops.no_op()  # An op, not a tensor.
    c = constant_op.constant(c_val)
    test_dct = {'a': a.name, 'c': c, 'b': b}
    test_dct_types = [dict, frozendict, defaultdict]
    # List of lists, tuples, namedtuple, dict, frozendict, and defaultdict
    res = sess.run([
        [a, b, c],
        (a, b, c),
        ABC(a=a, b=b, c=c),
        dict(test_dct),
        frozendict(test_dct),
        defaultdict(str, test_dct),
    ])
    self.assertIsInstance(res, list)
    self.assertEqual(6, len(res))
    self.assertIsInstance(res[0], list)
    self.assertEqual(3, len(res[0]))
    self.assertEqual(a_val, res[0][0])
    self.assertEqual(b_val, res[0][1])
    self.assertEqual(c_val, res[0][2])
    self.assertIsInstance(res[1], tuple)
    self.assertEqual(3, len(res[1]))
    self.assertEqual(a_val, res[1][0])
    self.assertEqual(b_val, res[1][1])
    self.assertEqual(c_val, res[1][2])
    self.assertIsInstance(res[2], ABC)
    self.assertEqual(a_val, res[2].a)
    self.assertEqual(b_val, res[2].b)
    self.assertEqual(c_val, res[2].c)
    for expected_type, r in zip(test_dct_types, res[3:]):
        self.assertIsInstance(r, expected_type)
        self.assertEqual(3, len(r))
        self.assertEqual(a_val, r['a'])
        self.assertEqual(b_val, r['b'])
        self.assertEqual(c_val, r['c'])
    self.assertEqual(res[5].default_factory, str)
    # Tuple of lists, tuples, namedtuple, dict, frozendict, and defaultdict
    res = sess.run(([a, b, c], (a.name, b, c), ABC(a=a, b=b,
                                                   c=c), dict(test_dct),
                    frozendict(test_dct), defaultdict(str, test_dct)))
    self.assertIsInstance(res, tuple)
    self.assertEqual(6, len(res))
    self.assertIsInstance(res[0], list)
    self.assertEqual(3, len(res[0]))
    self.assertEqual(a_val, res[0][0])
    self.assertEqual(b_val, res[0][1])
    self.assertEqual(c_val, res[0][2])
    self.assertIsInstance(res[1], tuple)
    self.assertEqual(3, len(res[1]))
    self.assertEqual(a_val, res[1][0])
    self.assertEqual(b_val, res[1][1])
    self.assertEqual(c_val, res[1][2])
    self.assertIsInstance(res[2], ABC)
    self.assertEqual(a_val, res[2].a)
    self.assertEqual(b_val, res[2].b)
    self.assertEqual(c_val, res[2].c)
    for expected_type, r in zip(test_dct_types, res[3:]):
        self.assertIsInstance(r, expected_type)
        self.assertEqual(3, len(r))
        self.assertEqual(a_val, r['a'])
        self.assertEqual(b_val, r['b'])
        self.assertEqual(c_val, r['c'])
    self.assertEqual(res[5].default_factory, str)

    # Namedtuple of lists, tuples, namedtuples, dict, frozendict, defaultdict
    res = sess.run(
        DEFGHI(
            d=[a, b, c],
            e=(a, b, c),
            f=ABC(a=a.name, b=b, c=c),
            g=dict(test_dct),
            h=frozendict(test_dct),
            i=defaultdict(str, test_dct)))
    self.assertIsInstance(res, DEFGHI)
    self.assertIsInstance(res.d, list)
    self.assertEqual(3, len(res.d))
    self.assertEqual(a_val, res.d[0])
    self.assertEqual(b_val, res.d[1])
    self.assertEqual(c_val, res.d[2])
    self.assertIsInstance(res.e, tuple)
    self.assertEqual(3, len(res.e))
    self.assertEqual(a_val, res.e[0])
    self.assertEqual(b_val, res.e[1])
    self.assertEqual(c_val, res.e[2])
    self.assertIsInstance(res.f, ABC)
    self.assertEqual(a_val, res.f.a)
    self.assertEqual(b_val, res.f.b)
    self.assertEqual(c_val, res.f.c)
    self.assertIsInstance(res.g, dict)
    self.assertEqual(3, len(res.g))
    self.assertEqual(a_val, res.g['a'])
    self.assertEqual(b_val, res.g['b'])
    self.assertEqual(c_val, res.g['c'])
    self.assertIsInstance(res.h, frozendict)
    self.assertEqual(3, len(res.h))
    self.assertEqual(a_val, res.h['a'])
    self.assertEqual(b_val, res.h['b'])
    self.assertEqual(c_val, res.h['c'])
    self.assertIsInstance(res.i, defaultdict)
    self.assertEqual(3, len(res.i))
    self.assertEqual(a_val, res.i['a'])
    self.assertEqual(b_val, res.i['b'])
    self.assertEqual(c_val, res.i['c'])
    self.assertEqual(res.i.default_factory, str)
    # Dict of lists, tuples, namedtuples, dict, frozendict, defaultdict
    res = sess.run({
        'd': [a, b, c],
        'e': (a, b, c),
        'f': ABC(a=a, b=b, c=c),
        'g': dict(test_dct),
        'h': frozendict(test_dct),
        'i': defaultdict(str, test_dct),
    })
    self.assertIsInstance(res, dict)
    self.assertEqual(6, len(res))
    self.assertIsInstance(res['d'], list)
    self.assertEqual(3, len(res['d']))
    self.assertEqual(a_val, res['d'][0])
    self.assertEqual(b_val, res['d'][1])
    self.assertEqual(c_val, res['d'][2])
    self.assertIsInstance(res['e'], tuple)
    self.assertEqual(3, len(res['e']))
    self.assertEqual(a_val, res['e'][0])
    self.assertEqual(b_val, res['e'][1])
    self.assertEqual(c_val, res['e'][2])
    self.assertIsInstance(res['f'], ABC)
    self.assertEqual(a_val, res['f'].a)
    self.assertEqual(b_val, res['f'].b)
    self.assertEqual(c_val, res['f'].c)
    for expected_type, r_key in zip(test_dct_types, ('g', 'h', 'i')):
        r = res[r_key]
        self.assertIsInstance(r, expected_type)
        self.assertEqual(3, len(r))
        self.assertEqual(a_val, r['a'])
        self.assertEqual(b_val, r['b'])
        self.assertEqual(c_val, r['c'])
    self.assertEqual(res['i'].default_factory, str)
