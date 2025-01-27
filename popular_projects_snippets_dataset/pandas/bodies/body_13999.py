# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_css.py
resolve = CSSResolver()
inherited_props = resolve(inherited)
style_props = resolve(style, inherited=inherited_props)
equiv_props = resolve(equiv)
assert style_props == equiv_props
