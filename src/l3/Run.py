import re
import time
import argparse
import subprocess
import pandas as pd
from .LLMs.GPT import GPTValuePredictor
from .Prompt import Prompt
from .RuntimeStats import RuntimeStats
from .Util import code_executes, gather_files, get_undefined_variables, get_undefined_attributes_methods

parser = argparse.ArgumentParser()
parser.add_argument(
    "--files", help="Python files or .txt file with all file paths", nargs="+")
parser.add_argument(
    "--openai_api_key", help="API Key from OpenAI", default="")

if __name__ == "__main__":
    args = parser.parse_args()

    files = gather_files(args.files)

    prompt = Prompt()

    for file in files:
        with open(file, "r") as f:
            code = ''.join(f.readlines())
            updated_code = code

        predictor = GPTValuePredictor(args.openai_api_key)
        successful_execution = code_executes(updated_code)

        runtime_stats = RuntimeStats()

        start_time = time.time()
        
        undefined_variables = get_undefined_variables(code)
        undefined_attributes_methods = get_undefined_attributes_methods(code)

        # TO DO: discard duplicate values from imports and initialization

        if undefined_variables or undefined_attributes_methods:
            # Predict undefined variables and attributes
            var_prompt = prompt.generate_var(code, undefined_variables, undefined_attributes_methods)

            predictions = predictor.predict(var_prompt, file)

            for prediction in predictions:
                imports = prediction['imports']
                imports = imports + '\n\n' if imports else imports

                updated_code = f'{imports}{code}'

                runtime_stats.refine_attempt = 0

                # Code with predicted imports only is not executable
                if not code_executes(updated_code):
                    initialization = prediction['initialization']
                    initialization = initialization + '\n\n' if initialization else initialization

                    updated_code = f'{imports}{initialization}{code}'

                    # Refine predictions
                    while not successful_execution and runtime_stats.refine_attempt < 10:
                        with open("temp.py", "w") as f:
                            f.write(updated_code)
                        try:
                            process = subprocess.run(["python3", "temp.py"], capture_output=True, text=True, check=True, timeout=30)
                            successful_execution = True
                        except subprocess.CalledProcessError as e:
                            lines = e.stderr.splitlines()
                            for line in lines:
                                match = re.search(r'temp.py\", line (\d+)', line)
                                if match:
                                    line_number = int(match.group(1))

                            line_code_and_error_msg = '\n'.join(lines[-2:])
                            cleaned_error_msg = f'Execution error at line {line_number}:\n{line_code_and_error_msg}'
                        
                            refine_prompt = prompt.refine(cleaned_error_msg)
                            refined_predictions = predictor.predict(refine_prompt, file)

                            runtime_stats.refined_prediction_index = 0

                            for refined_prediction in refined_predictions:
                                refined_imports = refined_prediction['imports']
                                refined_imports = refined_imports + '\n\n' if refined_imports else refined_imports

                                imports = imports + refined_imports

                                updated_code = f'{imports}{code}'

                                # Code with predicted imports only is not executable
                                if not code_executes(updated_code):
                                    refined_initialization = refined_prediction['initialization']
                                    refined_initialization = refined_initialization + '\n\n' if refined_initialization else refined_initialization

                                    initialization = initialization + refined_initialization

                                    updated_code = f'{imports}{initialization}{code}'

                                    if code_executes(updated_code):
                                        successful_execution = True
                                        break
                                else:
                                    successful_execution = True
                                    break

                                runtime_stats.refined_prediction_index += 1

                        except subprocess.TimeoutExpired:
                            break

                        runtime_stats.refine_attempt += 1
                        subprocess.run(["rm", "temp.py"])

                if successful_execution:
                    break

                runtime_stats.prediction_index += 1

        runtime_stats.save(file, predictor.__class__.__name__, start_time)

        updated_file_path = file.replace('.py', '_updated.py')
        with open(updated_file_path, "w") as f:
            f.write(updated_code)


