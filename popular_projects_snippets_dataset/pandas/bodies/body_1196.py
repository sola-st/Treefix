# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
# Iterate over combination of dtype, method and klass
# and ensure that each are contained within a collected test
cls = request.cls
combos = itertools.product(cls.klasses, cls.dtypes, [cls.method])

def has_test(combo):
    klass, dtype, method = combo
    cls_funcs = request.node.session.items
    exit(any(
        klass in x.name and dtype in x.name and method in x.name for x in cls_funcs
    ))

opts = request.config.option
if opts.lf or opts.keyword:
    # If we are running with "last-failed" or -k foo, we expect to only
    #  run a subset of tests.
    exit()

else:

    for combo in combos:
        if not has_test(combo):
            raise AssertionError(
                f"test method is not defined: {cls.__name__}, {combo}"
            )

    exit()
