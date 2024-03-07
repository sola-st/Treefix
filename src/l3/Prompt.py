class Prompt:
    def initial(self, src, undefined_vars, undefined_attrs_mets):
        src = '\n'.join(src.split('\n')[1:])
        undefined_vars = '\n'.join([var for var in undefined_vars])
        undefined_attrs_mets = '\n'.join([var for var in undefined_attrs_mets])
        prompt = (
            'Provide self-contained and concrete Python values to initialize the undefined variables in the code snippet.\n\n'
            '# begin code snippet\n' 
            f'{src}\n'
            '# end code snippet\n\n'
            '# begin undefined variables\n'
            f'{undefined_vars}\n'
            '# end undefined variables\n\n'
            '# begin undefined attributes and methods\n'
            f'{undefined_attrs_mets}\n'
            '# end undefined attributes and methods\n\n'
            'Respond strictly with JSON. The JSON should be compatible with the TypeScript type `Response` from the following:\n\n'
            '```ts\n'
            'interface Response {\n'
            '// Python import statements needed in the initialization code. One string per import.\n'
            'imports: string[];\n'
            '// Python code to initialize the undefined variables and make the code snippet executable. One string per undefined variable.'
            ' The statements in the code snippet above are not part of the initialization of undefined variables.'
            ' Therefore, their copy or modified versions should not be added here.'
            ' The values should be self-contained and concrete, i.e. without assumptions or expected replacements of any code that is not present in the code snippet.'
            ' In case there are undefined attributes or methods and the attribute or method base is not initialized, initialize the attribute or method base using type("Mock", bases, dict), where bases is a tuple containing the base classes that the Mock object inherits from, e.g. object, and dict is a dictionary containing the initialization of the undefined attributes and methods in the code snippet.\n'
            'initialization: string[];\n'
            '}\n'
            '```'
        )
        return prompt
    
    def refine(self, error):
        prompt = (
            'When trying to execute the code snippet with the provided imports and initialization, the following error happens:\n'
            '# begin error message\n'
            f'{error}\n'
            '# end error message\n\n'
            'Please, provide self-contained and concrete Python fixed values of the imports and initialization to solve the error and make the code snippet executable.\n'
            'Respond strictly with JSON. The JSON should be compatible with the TypeScript type `Response` from the following:\n\n'
            '```ts\n'
            'interface Response {\n'
            '// Python import statements needed in the initialization code. One string per import.\n'
            'imports: string[];\n'
            '// Python code to initialize the undefined variables and make the code snippet executable. One string per undefined variable.'
            ' The statements in the code snippet above are not part of the initialization of undefined variables.'
            ' Therefore, their copy or modified versions should not be added here.'
            ' The values should be self-contained and concrete, i.e. without assumptions or expected replacements of any code that is not present in the code snippet.'
            ' In case there are undefined attributes or methods and the attribute or method base is not initialized, initialize the attribute or method base using type("Mock", bases, dict), where bases is a tuple containing the base classes that the Mock object inherits from, e.g. object, and dict is a dictionary containing the initialization of the undefined attributes and methods in the code snippet.\n'
            'initialization: string[];\n'
            '}\n'
            '```'
        )
        return prompt
    
    def cover(self, src):
        prompt = (
            'When trying to execute the code snippet with the provided imports and initialization, the lines with # uncovered are not executed.\n\n'
            '# begin code snippet\n'
            f'{src}\n'
            '# end code snippet\n\n'
            'Please, provide self-contained and concrete Python modified values of the imports and initialization to execute one of the uncovered paths in the code snippet.\n'
            'Respond strictly with JSON. The JSON should be compatible with the TypeScript type `Response` from the following:\n\n'
            '```ts\n'
            'interface Response {\n'
            '// Python import statements needed in the initialization code. One string per import.\n'
            'imports: string[];\n'
            '// Python code to initialize the undefined variables and make the code snippet executable. One string per undefined variable.'
            ' The statements in the code snippet above are not part of the initialization of undefined variables.'
            ' Therefore, their copy or modified versions should not be added here.'
            ' The values should be self-contained and concrete, i.e. without assumptions or expected replacements of any code that is not present in the code snippet.'
            ' In case there are undefined attributes or methods and the attribute or method base is not initialized, initialize the attribute or method base using type("Mock", bases, dict), where bases is a tuple containing the base classes that the Mock object inherits from, e.g. object, and dict is a dictionary containing the initialization of the undefined attributes and methods in the code snippet.\n'
            'initialization: string[];\n'
            '}\n'
            '```'
        )
        return prompt