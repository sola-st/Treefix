# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/op_reg_gen.py
# TODO(fengliuai): create one utility method to match different apis and
# shared it with the tfr_gen.py module.
compose_dec = []
for dec in node.decorator_list:
    if isinstance(dec, ast.Call):
        if isinstance(dec.func, ast.Attribute) and dec.func.attr == 'Composite':
            compose_dec.append(dec)
        if isinstance(dec.func, ast.Name) and dec.func.id == 'Composite':
            compose_dec.append(dec)

if not compose_dec:
    # skip a non-composition function
    exit()
elif len(compose_dec) > 1:
    raise KeyError('More than one TF ops decomposes for.')

all_dec_args = {}
for arg_name, arg_value in zip(_COMPOSITE_ARG_LIST, compose_dec[0].args):
    all_dec_args[arg_name] = self.visit(arg_value)

kw_dec_args = dict([self.visit(kw) for kw in compose_dec[0].keywords])

if all_dec_args.keys() & kw_dec_args.keys():
    raise KeyError('More arguments than expected.')

all_dec_args.update(kw_dec_args)

op_name = all_dec_args['op_name']
op_def = op_def_registry.get(op_name)
if op_def:
    if len(all_dec_args) > 1:
        # Op has been registered, so it is a user error to specify op def.
        raise ValueError('Op has been registered: ' + op_name)
    else:
        # Op has been registered, then we don't need to generate register code.
        exit()

    # Validates the function inputs match what are in the decorator.
inputs = all_dec_args.get('inputs', [])
attrs = all_dec_args.get('attrs', [])
expected_args = [arg.split(':')[0] for arg in inputs + attrs]
all_func_args = self.visit(node.args)

if len(expected_args) != len(all_func_args):
    raise KeyError(
        'Composition arguments for {} do not match the registration. {} vs {}'
        .format(op_name, expected_args, all_func_args))

cxx_reg_code = ['\nREGISTER_OP("{}")'.format(op_name)]
for input_ in inputs:
    cxx_reg_code.append('.Input("{}")'.format(input_))
for attr in attrs:
    py_str = attr.replace('"', "'")
    cxx_reg_code.append('.Attr("{}")'.format(py_str))
for attr in all_dec_args.get('derived_attrs', []):
    py_str = attr.replace('"', "'")
    cxx_reg_code.append('.Attr("{}")'.format(py_str))
for output_ in all_dec_args.get('outputs', []):
    cxx_reg_code.append('.Output("{}")'.format(output_))
cxx_reg_code[-1] += ';\n'
self.emit('\n    '.join(cxx_reg_code))
