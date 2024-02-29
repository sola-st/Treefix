import csv
import os
import json
import time
import openai
import pandas as pd
from ..Util import get_json_info, install_dependencies, remove_lines_with_execution_error


class GPTValuePredictor:
    def __init__(self, openai_api_key, model_id="gpt-3.5-turbo-0125"):
        openai.api_key = openai_api_key
        self.model_id = model_id
        self.conversation_history = [
            {
                "role": "system", 
                "content": "You are an exceptionally useful value predictor that consistently predicts accurate and reliable responses to user instructions."
            }
        ]
    
    def predict(self, prompt, code_snippet_file):
        self.code_snippet_file = code_snippet_file
        self.conversation_history.append({
            "role": "user",
            "content": prompt
        })
        raw_predictions = self.query_model()
        predictions = self.post_process_predictions(raw_predictions)
        log_file = code_snippet_file.replace('.py', f'_{self.model_id}.csv')
        self.save_log(log_file, prompt, raw_predictions, predictions)
        return predictions

    def query_model(self):
        while True:
            try:
                response = openai.ChatCompletion.create(
                    model=self.model_id,
                    messages=self.conversation_history,
                    response_format={ "type": "json_object" },
                    n=10
                )
                break
            except Exception as e:
                print(e)
                # Rate limit achieved
                time.sleep(60)
        return response.choices
    
    def post_process_predictions(self, raw_predictions):
        post_processed_predictions = []
        for raw_prediction in raw_predictions:
            # Add predictions to conversation history
            self.conversation_history.append({
                "role": raw_prediction.message.role,
                "content": raw_prediction.message.content
            })

            prediction = get_json_info(raw_prediction)

            # Add comment to avoid counting predictions during line coverage calculation
            try:
                imports = prediction['imports']
                imports = [import_.replace("\n", "# pragma: no cover\n") for import_ in imports]
                imports = '\n'.join(
                    [f'{import_} # pragma: no cover' for import_ in imports]
                )
            except:
                imports = ""

            try:
                initializations = prediction['initialization']
                initializations = [initialization.replace("\n", "# pragma: no cover\n") for initialization in initializations]
                initialization = '\n'.join(
                    [f'{initialization} # pragma: no cover' for initialization in initializations]
                )
            except:
                initialization = ""

            # Install missing dependencies
            dependencies_dir_path = os.path.dirname(os.path.realpath(self.code_snippet_file))
            install_dependencies(dependencies_dir_path, f'{imports}\n{initialization}')

            # Remove lines with execution errors
            imports = remove_lines_with_execution_error(imports)
            initialization_with_imports = '\n# AUX COMMENT: END IMPORTS AND BEGIN INITIALIZATION\n'.join(
                [imports, initialization]
            )
            initialization_with_imports = remove_lines_with_execution_error(initialization_with_imports)
            if imports:
                initialization = initialization_with_imports.split('\n# AUX COMMENT: END IMPORTS AND BEGIN INITIALIZATION\n')[-1] 
            else:
                initialization = initialization_with_imports.replace('\n# AUX COMMENT: END IMPORTS AND BEGIN INITIALIZATION\n', '')  

            post_processed_predictions.append({
                'imports': imports,
                'initialization': initialization
            })

        return post_processed_predictions
    
    def save_log(self, log_file, prompt, raw_predictions, predictions):
        predictions = {
            'imports': predictions['imports'].split('\n'),
            'initialization': predictions['initialization'].split('\n')
        }
        # Create CSV file and add header if it doesn't exist
        if not os.path.isfile(log_file):
            columns = ['prompt', 'raw_predictions', 'predictions']

            with open(log_file, 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(columns)

        df = pd.read_csv(log_file)
        df_new_data = pd.DataFrame({
            'prompt': [prompt],
            'raw_predictions': [raw_predictions],
            'predictions': [json.dumps(predictions, indent = 4)]
        })
        df = pd.concat([df, df_new_data])
        df.to_csv(log_file, index=False)