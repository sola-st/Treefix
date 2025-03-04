# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/selective_registration_header_lib.py
"""Returns a header for use with tensorflow SELECTIVE_REGISTRATION.

  Args:
    ops_and_kernels: a set of (op_name, kernel_class_name) pairs to include.
    include_all_ops_and_kernels: if True, ops_and_kernels is ignored and all op
      kernels are included.

  Returns:
    the string of the header that should be written as ops_to_register.h.
  """
ops_and_kernels = sorted(ops_and_kernels)
ops = set(op for op, _ in ops_and_kernels)
result_list = []

def append(s):
    result_list.append(s)

_, script_name = os.path.split(sys.argv[0])
append('// This file was autogenerated by %s' % script_name)
append('#ifndef OPS_TO_REGISTER')
append('#define OPS_TO_REGISTER')

if include_all_ops_and_kernels:
    append('#define SHOULD_REGISTER_OP(op) true')
    append('#define SHOULD_REGISTER_OP_KERNEL(clz) true')
    append('#define SHOULD_REGISTER_OP_GRADIENT true')
else:
    line = """
    namespace {
      constexpr const char* skip(const char* x) {
        return (*x) ? (*x == ' ' ? skip(x + 1) : x) : x;
      }

      constexpr bool isequal(const char* x, const char* y) {
        return (*skip(x) && *skip(y))
                   ? (*skip(x) == *skip(y) && isequal(skip(x) + 1, skip(y) + 1))
                   : (!*skip(x) && !*skip(y));
      }

      template<int N>
      struct find_in {
        static constexpr bool f(const char* x, const char* const y[N]) {
          return isequal(x, y[0]) || find_in<N - 1>::f(x, y + 1);
        }
      };

      template<>
      struct find_in<0> {
        static constexpr bool f(const char* x, const char* const y[]) {
          return false;
        }
      };
    }  // end namespace
    """
    line += 'constexpr const char* kNecessaryOpKernelClasses[] = {\n'
    for _, kernel_class in ops_and_kernels:
        if kernel_class is None:
            continue
        line += '"%s",\n' % kernel_class
    line += '};'
    append(line)
    append('#define SHOULD_REGISTER_OP_KERNEL(clz) '
           '(find_in<sizeof(kNecessaryOpKernelClasses) '
           '/ sizeof(*kNecessaryOpKernelClasses)>::f(clz, '
           'kNecessaryOpKernelClasses))')
    append('')

    append('constexpr inline bool ShouldRegisterOp(const char op[]) {')
    append('  return false')
    for op in sorted(ops):
        append('     || isequal(op, "%s")' % op)
    append('  ;')
    append('}')
    append('#define SHOULD_REGISTER_OP(op) ShouldRegisterOp(op)')
    append('')

    append('#define SHOULD_REGISTER_OP_GRADIENT ' +
           ('true' if 'SymbolicGradient' in ops else 'false'))

append('#endif')
exit('\n'.join(result_list))
