import json
import time
import openai
from ..Util import get_undefined_elements

openai.api_key = ''

class GPTValuePredictor:
    def __init__(self, code_snippet_file, model_id="gpt-3.5-turbo"):
        self.code_snippet_file = code_snippet_file
        self.model_id = model_id
        self.log_file = code_snippet_file.replace('.py', f'_{model_id}.json')
        prompt = self.create_prompt(code_snippet_file)
        self.predictions = self._query_model(prompt)

    def _query_model(self, prompt):
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

        with open(self.log_file, 'w') as fp:
            json.dump(dict(prompt=prompt, response=response), fp, indent=4)

        return response.choices[0].message.content

    def create_prompt(self, code_snippet_file):
        undefined_elements = '=\n'.join(
            list(get_undefined_elements(code_snippet_file)))

        with open(code_snippet_file, "r") as file:
            src = file.read()

        prompt = (
            'Provide concrete values to initialize the undefined elements in the code snippet.\n\n'
            '# begin code snippet\n'
            f'{src}\n'
            '# end code snippet\n\n'
            '# begin initialization\n'
            f'{undefined_elements}\n'
            '# end initialization')

        return prompt
