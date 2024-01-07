import re
import json
import time
import openai
import libcst as cst
from ..Util import get_json_info, remove_lines_with_execution_error

openai.api_key = ''

class GPTValuePredictor:
    def __init__(self, model_id="gpt-3.5-turbo"):
        self.model_id = model_id
        
    def predict(self, code_snippet_file, undefined_variables):
        prompt = self.create_prompt(code_snippet_file, undefined_variables)
        print(prompt)
        raw_predictions = self.query_model(prompt)
        print(raw_predictions)
        predictions = self.post_process_predictions(raw_predictions)
        log_file = code_snippet_file.replace('.py', f'_{self.model_id}.json')
        self.save_log(log_file, prompt, raw_predictions, predictions)
        return predictions

    def create_prompt(self, code_snippet_file, undefined_variables):  
        undefined_variables = '\n'.join(undefined_variables)

        with open(code_snippet_file, "r") as file:
            src = ''.join(file.readlines()[1:])

        prompt = (
            'Provide self-contained and concrete Python values to initialize the undefined variables in the code snippet.\n\n'
            '# begin code snippet\n' 
            f'{src}\n'
            '# end code snippet\n\n'
            '# begin undefined variables\n'
            f'{undefined_variables}\n'
            '# end undefined variables\n\n'
            'Respond strictly with JSON. The JSON should be compatible with the TypeScript type `Response` from the following:\n\n'
            '```ts\n'
            'interface Response {\n'
            '// Python import statements needed in the initialization code. One string per import.\n'
            'imports: string[];\n'
            '// Python code to initialize the undefined variables. One string per undefined variable. The statements in the code snippet above are not part of the initialization of undefined variables. Therefore, their copy or modified versions should not be added here. The values should be self-contained and concrete, i.e. without assumptions or expected replacements.\n'
            'initialization: string[];\n'
            '}\n'
            '```'
        )
        
        return prompt
        
    def query_model(self, prompt):
        while True:
            try:
                response = openai.ChatCompletion.create(
                    model=self.model_id,
                    messages=[{'role': 'user', 'content': prompt}],
                )
                break
            except Exception as e:
                print(e)
                # Rate limit achieved
                time.sleep(60)
        return response.choices[0].message.content
    
    def post_process_predictions(self, raw_predictions):
        predictions = get_json_info(raw_predictions)

        # Imports
        imports = '\n'.join(
            [f'{import_} # pragma: no cover' for import_ in predictions['imports']]
        )
        imports = remove_lines_with_execution_error(imports)

        # Initialization
        initialization = '\n'.join(
            [f'{init} # pragma: no cover' for init in predictions['initialization']]
        )
        # TO DO: add imports from the original snippet?
        initialization_with_imports = '\n# AUX COMMENT: END IMPORTS AND BEGIN INITIALIZATION\n'.join(
            [imports, initialization]
        )
        initialization_with_imports = remove_lines_with_execution_error(initialization_with_imports)
        initialization = initialization_with_imports.split('\n# AUX COMMENT: END IMPORTS AND BEGIN INITIALIZATION\n')[-1]    

        return {
            'imports': imports,
            'initialization': initialization
        }
    
    def save_log(self, log_file, prompt, raw_predictions, predictions):
        with open(log_file, 'w') as fp:
            json.dump(dict(
                prompt=prompt, 
                raw_predictions=raw_predictions,
                predictions=predictions), fp, indent=4)
