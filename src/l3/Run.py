import re
import time
import argparse
import subprocess

from .LLMs.GPT import GPTValuePredictor
from .Prompt import Prompt
from .RuntimeStats import RuntimeStats
from .Util import code_executes, gather_files, get_undefined_variables, get_undefined_attributes_methods


parser = argparse.ArgumentParser()
parser.add_argument(
    "--files", help="Python files or .txt file with all file paths", nargs="+")
parser.add_argument(
    "--openai_api_key", help="API Key from OpenAI", default="")

prompt = Prompt()

def initiate_predictions(code, instrumented_code, code_file, predictor):
    runtime_stats = RuntimeStats('initial')
    start_time = time.time()
    
    undefined_variables = get_undefined_variables(code)
    undefined_attributes_methods = get_undefined_attributes_methods(code)

    updated_code = code
    imports = ""
    initialization = ""
    predictions = []
    successful_execution = False

    if undefined_variables or undefined_attributes_methods:
        # Predict undefined variables and attributes
        initial_prompt = prompt.initial(code, undefined_variables, undefined_attributes_methods)

        predictions = predictor.predict(initial_prompt, code_file)

        for prediction in predictions:
            imports = prediction['imports']
            imports = imports + '\n\n' if imports else imports

            updated_code = f'{imports}{code}'

            # Code with predicted imports only is not executable
            if not code_executes(updated_code):
                initialization = prediction['initialization']
                initialization = initialization + '\n\n' if initialization else initialization

                updated_code = f'{imports}{initialization}{code}'

                if code_executes(updated_code):
                    successful_execution = True
                    break
            
            else:
                successful_execution = True
                break

            runtime_stats.prediction_index += 1

    updated_file_path = code_file.replace('.py', '_initial.py')
    updated_code = f'{imports}{initialization}{instrumented_code}'
    with open(updated_file_path, "w") as f:
        f.write(updated_code)

    runtime_stats.measure_coverage(updated_file_path, predictor.__class__.__name__)
    runtime_stats.save(code_file, predictor.__class__.__name__, start_time)

    return predictions, successful_execution, imports, initialization

def refine_predictions(code, instrumented_code, code_file, predictor, predictions):
    runtime_stats = RuntimeStats('refine')
    start_time = time.time()

    updated_code = code
    imports = ""
    initialization = ""
    successful_execution = False

    for prediction in predictions:
        imports = prediction['imports']
        imports = imports + '\n\n' if imports else imports

        updated_code = f'{imports}{code}'

        # Code with predicted imports only is not executable
        if not code_executes(updated_code):
            initialization = prediction['initialization']
            initialization = initialization + '\n\n' if initialization else initialization

            updated_code = f'{imports}{initialization}{code}'

            if not code_executes(updated_code):
                runtime_stats.refine_attempt = 0

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
                        refined_predictions = predictor.predict(refine_prompt, code_file)

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

    updated_file_path = code_file.replace('.py', '_refine.py')
    updated_code = f'{imports}{initialization}{instrumented_code}'
    with open(updated_file_path, "w") as f:
        f.write(updated_code)

    runtime_stats.measure_coverage(updated_file_path, predictor.__class__.__name__)
    runtime_stats.save(code_file, predictor.__class__.__name__, start_time)

    return successful_execution, imports, initialization

if __name__ == "__main__":
    args = parser.parse_args()

    files = gather_files(args.files)

    for file in files:
        with open(file, "r") as f:
            code = ''.join(f.readlines())

        # Instrument
        subprocess.run(["python", "-m", "l3.Instrument", "--files", file, "--line_coverage_instrumentation"])

        with open(file, "r") as f:
            instrumented_code = ''.join(f.readlines())

        predictor = GPTValuePredictor(args.openai_api_key)
        
        initial_predictions, successful_execution, imports, initialization = initiate_predictions(code, instrumented_code, file, predictor)

        if not successful_execution:
            successful_execution, imports, initialization = refine_predictions(code, instrumented_code, file, predictor, initial_predictions)