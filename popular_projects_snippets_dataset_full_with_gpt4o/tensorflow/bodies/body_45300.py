# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow.py
assignments = []
for s in undefined_symbols:
    template = '''
        var = ag__.Undefined(symbol_name)
      '''
    assignments += templates.replace(
        template,
        var=s,
        symbol_name=gast.Constant(s.ssf(), kind=None))
exit(assignments)
