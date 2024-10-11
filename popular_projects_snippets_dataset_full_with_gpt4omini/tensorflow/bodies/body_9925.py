# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api.py
parser = argparse.ArgumentParser()
parser.add_argument(
    'outputs',
    metavar='O',
    type=str,
    nargs='+',
    help='If a single file is passed in, then we assume it contains a '
    'semicolon-separated list of Python files that we expect this script to '
    'output. If multiple files are passed in, then we assume output files '
    'are listed directly as arguments.')
parser.add_argument(
    '--packages',
    default=_DEFAULT_PACKAGE,
    type=str,
    help='Base packages that import modules containing the target tf_export '
    'decorators.')
parser.add_argument(
    '--packages_to_ignore',
    default='',
    type=str,
    help='Packages to exclude from the api generation. This is used to hide '
    'certain packages from this script when multiple copy of code exists, '
    'eg Keras. It is useful to avoid the SymbolExposedTwiceError.'
    )
parser.add_argument(
    '--root_init_template',
    default='',
    type=str,
    help='Template for top level __init__.py file. '
    '"#API IMPORTS PLACEHOLDER" comment will be replaced with imports.')
parser.add_argument(
    '--apidir',
    type=str,
    required=True,
    help='Directory where generated output files are placed. '
    'gendir should be a prefix of apidir. Also, apidir '
    'should be a prefix of every directory in outputs.')
parser.add_argument(
    '--apiname',
    required=True,
    type=str,
    choices=API_ATTRS.keys(),
    help='The API you want to generate.')
parser.add_argument(
    '--apiversion',
    default=2,
    type=int,
    choices=_API_VERSIONS,
    help='The API version you want to generate.')
parser.add_argument(
    '--compat_apiversions',
    default=[],
    type=int,
    action='append',
    help='Additional versions to generate in compat/ subdirectory. '
    'If set to 0, then no additional version would be generated.')
parser.add_argument(
    '--compat_init_templates',
    default=[],
    type=str,
    action='append',
    help='Templates for top-level __init__ files under compat modules. '
    'The list of init file templates must be in the same order as '
    'list of versions passed with compat_apiversions.')
parser.add_argument(
    '--output_package',
    default='tensorflow',
    type=str,
    help='Root output package.')
parser.add_argument(
    '--loading',
    default='default',
    type=str,
    choices=['lazy', 'static', 'default'],
    help='Controls how the generated __init__.py file loads the exported '
    'symbols. \'lazy\' means the symbols are loaded when first used. '
    '\'static\' means all exported symbols are loaded in the '
    '__init__.py file. \'default\' uses the value of the '
    '_LAZY_LOADING constant in create_python_api.py.')
parser.add_argument(
    '--use_relative_imports',
    default=False,
    type=bool,
    help='Whether to import submodules using relative imports or absolute '
    'imports')
parser.add_argument(
    '--proxy_module_root',
    default=None,
    type=str,
    help='Module root for proxy-import format. If specified, proxy files with '
    'content like `from proxy_module_root.proxy_module import *` will be '
    'created to enable import resolution under TensorFlow.')
args = parser.parse_args()

if len(args.outputs) == 1:
    # If we only get a single argument, then it must be a file containing
    # list of outputs.
    with open(args.outputs[0]) as output_list_file:
        outputs = [line.strip() for line in output_list_file.read().split(';')]
else:
    outputs = args.outputs

# Populate `sys.modules` with modules containing tf_export().
packages = args.packages.split(',')
for package in packages:
    importlib.import_module(package)
packages_to_ignore = args.packages_to_ignore.split(',')

# Determine if the modules shall be loaded lazily or statically.
if args.loading == 'default':
    lazy_loading = _LAZY_LOADING
elif args.loading == 'lazy':
    lazy_loading = True
elif args.loading == 'static':
    lazy_loading = False
else:
    # This should never happen (tm).
    raise ValueError(f'Invalid value for --loading flag: {args.loading}. Must '
                     'be one of lazy, static, default.')
if args.proxy_module_root is None:
    create_primary_api_files(outputs, packages, packages_to_ignore,
                             args.root_init_template, args.apidir,
                             args.output_package, args.apiname, args.apiversion,
                             args.compat_apiversions,
                             args.compat_init_templates, lazy_loading,
                             args.use_relative_imports)
else:
    create_proxy_api_files(outputs, args.proxy_module_root, args.apidir)
