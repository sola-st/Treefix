# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter_test.py
opts = converter.ConversionOptions()
opts_ast = opts.to_ast()

template = '''
    def f():
      return opts_ast
    '''
opts_packed = templates.replace(template, opts_ast=opts_ast)

reparsed, _, _ = loader.load_ast(opts_packed)
fake_ag = imp.new_module('fake_ag')
fake_ag.ConversionOptions = converter.ConversionOptions
fake_ag.Feature = converter.Feature
reparsed.ag__ = fake_ag

reparsed_opts = reparsed.f()

self.assertEqual(opts.recursive, reparsed_opts.recursive)
self.assertEqual(opts.user_requested, False)
self.assertEqual(
    opts.internal_convert_user_code,
    reparsed_opts.internal_convert_user_code)
self.assertEqual(opts.optional_features, reparsed_opts.optional_features)
