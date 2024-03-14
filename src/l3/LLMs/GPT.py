import csv
import os
import json
import time
import openai
import tiktoken
import pandas as pd

from ..Util import get_json_info, install_dependencies, remove_lines_with_execution_error


class GPTValuePredictor:
    def __init__(self, openai_api_key, model_id="gpt-3.5-turbo-0125"):
        openai.api_key = openai_api_key
        self.model_id = model_id
        self.conversation_history = [{
            "role": "system", 
            "content": "You are an exceptionally useful value predictor that consistently predicts accurate and reliable responses to user instructions."
        }]
        self.conversation_history_size = self.count_tokens(self.conversation_history)
        self.latest_predictions = {}
    
    def predict(self, prompt, prompt_type, code_snippet_file, prediction_index=0):
        self.prompt_type = prompt_type
        self.code_snippet_file = code_snippet_file

        if self.prompt_type == 2:
            prediction_with_error = self.latest_predictions[prediction_index]
            self.conversation_history.append({
                    "role": prediction_with_error.message.role,
                    "content": prediction_with_error.message.content
                })
            self.conversation_history_size += self.count_tokens([self.conversation_history[-1]])

        prompt_msg = {
            "role": "user",
            "content": prompt
        }
        self.conversation_history.append(prompt_msg)
        self.conversation_history_size += self.count_tokens([prompt_msg])

        self.manage_conversation_history()

        raw_predictions = self.query_model()
        self.latest_predictions = raw_predictions
        raw_predictions, predictions = self.post_process_predictions(raw_predictions)
        log_file = code_snippet_file.replace('.py', f'_{self.model_id}.csv')
        self.save_log(log_file, prompt, raw_predictions, predictions)
        return predictions

    def query_model(self):
        while True:
            print(self.conversation_history)
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
        predictions = []
        post_processed_predictions = []
        for raw_prediction in raw_predictions:
            # Add predictions to conversation history
            if self.prompt_type == 3:
                self.conversation_history.append({
                    "role": raw_prediction.message.role,
                    "content": raw_prediction.message.content
                })
                self.conversation_history_size += self.count_tokens([self.conversation_history[-1]])

            prediction = get_json_info(raw_prediction.message.content)
            predictions.append(prediction)

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

        return predictions, post_processed_predictions
    
    def manage_conversation_history(self):
        # output tokens limit
        max_tokens = 4096
        # context size limit: input + output tokens
        context_length = 16385
        while self.conversation_history_size + max_tokens > context_length:
            removed_messages = []

            if self.prompt_type == 2:
                removed_messages.append(self.conversation_history.pop(2))
                removed_messages.append(self.conversation_history.pop(3))
            elif self.prompt_type == 3:
                for i in range(1, 12):
                    removed_messages.append(self.conversation_history.pop(i))
                    print(removed_messages)
                    print(len(removed_messages))

            self.conversation_history_size -= self.count_tokens(removed_messages)

    def count_tokens(self, messages):
        encoding = tiktoken.encoding_for_model(self.model_id)
        num_tokens = 0
        for message in messages:
            num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
        num_tokens += 2  # every reply is primed with <im_start>assistant
        return num_tokens
    
    def save_log(self, log_file, prompt, raw_predictions, predictions):
        processed_predictions = []
        for prediction in predictions:
            processed_predictions.append({
                'imports': prediction['imports'].split('\n'),
                'initialization': prediction['initialization'].split('\n')
            })
        # Create CSV file and add header if it doesn't exist
        if not os.path.isfile(log_file):
            columns = ['prompt', 'raw_predictions', 'predictions']

            with open(log_file, 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(columns)

        df = pd.read_csv(log_file)
        df_new_data = pd.DataFrame({
            'prompt': [prompt],
            'raw_predictions': [json.dumps(raw_predictions, indent = 4)],
            'predictions': [json.dumps(processed_predictions, indent = 4)]
        })
        df = pd.concat([df, df_new_data])
        df.to_csv(log_file, index=False)