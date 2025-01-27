# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/gen_quantized_function_library.py
namespaces = _NAMESPACE.value.split('::')
src_files = _SRCS.value.split(' ')
file_prefix = 'quantized_function_library'
module_prefix = 'kQuantizedFunctionLibraryInMLIR'

modules = []

for src_file in src_files:
    with open(src_file, 'r') as f:
        content = f.read()

        # Skip the copyright in the source file.
        module_match = re.search(r'(^module\s\{)(.*)(^\})', content,
                                 re.MULTILINE | re.DOTALL)
        if module_match is None:
            raise ValueError("Couldn't find module in the function library")
        module = module_match.group()

        # Substitute all the function templates.
        out = re.split(file_prefix, src_file)
        if len(out) != 2:
            raise ValueError('The file name must start with {}'.format(file_prefix))
        tag = out[1][:-5]  # the last five values = ".mlir"
        module = _substitute_for_loop_template(module)
        module = _substitute_parameterization_template(module)
        module = _substitute_quantized_function_name_template(module)
        module = _substitute_impl_function_name_template(module)
        modules.append((tag, module))

with open(_OUTPUT_FILE.value, 'w') as f:
    f.write("""/* Copyright 2022 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#ifndef TENSORFLOW_COMPILER_MLIR_QUANTIZATION_TENSORFLOW_PASSES_QUANTIZED_FUNCTION_LIBRARY_H_
#define TENSORFLOW_COMPILER_MLIR_QUANTIZATION_TENSORFLOW_PASSES_QUANTIZED_FUNCTION_LIBRARY_H_
""")

    for namespace in namespaces:
        f.write('namespace {0} {{\n'.format(namespace))

    for tag, module in modules:
        f.write('constexpr char {0}[] ='.format(module_prefix + tag.upper()))

        for line in module.splitlines():
            f.write('\n  "')
            f.write(line.rstrip().replace('"', r'\"'))
            f.write('\\n"')

        f.write(';\n')

    for namespace in reversed(namespaces):
        f.write('}}  // namespace {0}\n'.format(namespace))

    f.write(
        '#endif  // TENSORFLOW_COMPILER_MLIR_QUANTIZATION_TENSORFLOW_PASSES_QUANTIZED_FUNCTION_LIBRARY_H_'
    )
