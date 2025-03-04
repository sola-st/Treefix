# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/print_selective_registration_header_test.py
default_ops = ''
graphs = [text_format.Parse(GRAPH_DEF_TXT_2, graph_pb2.GraphDef())]

expected = """// This file was autogenerated by %s
#ifndef OPS_TO_REGISTER
#define OPS_TO_REGISTER

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
    constexpr const char* kNecessaryOpKernelClasses[] = {
"BiasOp<CPUDevice, float>",
};
#define SHOULD_REGISTER_OP_KERNEL(clz) (find_in<sizeof(kNecessaryOpKernelClasses) / sizeof(*kNecessaryOpKernelClasses)>::f(clz, kNecessaryOpKernelClasses))

constexpr inline bool ShouldRegisterOp(const char op[]) {
  return false
     || isequal(op, "AccumulateNV2")
     || isequal(op, "BiasAdd")
  ;
}
#define SHOULD_REGISTER_OP(op) ShouldRegisterOp(op)

#define SHOULD_REGISTER_OP_GRADIENT false
#endif""" % self.script_name

header = selective_registration_header_lib.get_header(
    self.WriteGraphFiles(graphs), 'rawproto', default_ops)
print(header)
self.assertListEqual(expected.split('\n'), header.split('\n'))
