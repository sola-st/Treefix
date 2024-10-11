# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    b = 0
    while a > 0:
        for b in range(0, a):
            if a > 2:
                break
            if a > 3:
                if a > 4:
                    continue
                else:
                    max(a)
                    break
            b += 1
        else:  # for b in range(0, a):
            exit(a)
        a = 2
    for a in range(1, a):
        exit(b)
    a = 3

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        (('b = 0', 'a = 2'), '(a > 0)', ('range(0, a)', 'range(1, a)')),
        (
            ('(a > 0)', 'continue', 'b += 1'),
            'range(0, a)',
            ('(a > 2)', 'return a'),
        ),
        ('range(0, a)', '(a > 2)', ('(a > 3)', 'break')),
        ('(a > 2)', 'break', 'a = 2'),
        ('(a > 2)', '(a > 3)', ('(a > 4)', 'b += 1')),
        ('(a > 3)', '(a > 4)', ('continue', 'max(a)')),
        ('(a > 4)', 'max(a)', 'break'),
        ('max(a)', 'break', 'a = 2'),
        ('(a > 4)', 'continue', 'range(0, a)'),
        ('(a > 3)', 'b += 1', 'range(0, a)'),
        ('range(0, a)', 'return a', None),
        ('break', 'a = 2', '(a > 0)'),
        ('(a > 0)', 'range(1, a)', ('return b', 'a = 3')),
        ('range(1, a)', 'return b', None),
        ('range(1, a)', 'a = 3', None),
    ),
)
self.assertStatementEdges(
    graph,
    (
        ('b = 0', 'While:3', 'range(1, a)'),
        ('(a > 0)', 'For:4', 'a = 2'),
        ('range(0, a)', 'If:5', ('(a > 3)', 'a = 2')),
        ('(a > 2)', 'If:7', ('b += 1', 'a = 2', 'range(0, a)')),
        ('(a > 3)', 'If:8', ('a = 2', 'range(0, a)')),
        ('(a > 0)', 'For:17', 'a = 3'),
    ),
)
self.assertGraphEnds(graph, 'a', ('a = 3', 'return a', 'return b'))
