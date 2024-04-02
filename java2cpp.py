import os
import configparser
import sys
import openai

# File paths
API_KEYS_LOCATION = "/home/kush_satyadev/codex_py2cpp/.env"
JAVA_FILE_TO_CONVERT = "Main.java"

# Function to create a template .env file if it doesn't exist


def create_template_ini_file():
    if not os.path.isfile(API_KEYS_LOCATION):
        with open(API_KEYS_LOCATION, 'w') as f:
            f.write('[openai]\n')
            f.write('api_key=\n')

        print('OpenAI API config file created at {}'.format(API_KEYS_LOCATION))
        print('Please edit it and add your API key')
        print('If you do not yet have an API key, register for OpenAI Codex at:\n'
              'https://openai.com/blog/openai-codex/')
        sys.exit(1)

# Initialize the OpenAI API


def initialize_openai_api():
    create_template_ini_file()
    config = configparser.ConfigParser()
    config.read(API_KEYS_LOCATION)

    # Initialize the client object with the API key
    openai.api_key = config['openai']['api_key'].strip('"').strip("'")
    return openai

# Generate input prompt from Java file


def create_input_prompt(length=3000):
    input_prompt = ''
    filename = JAVA_FILE_TO_CONVERT
    with open(filename) as f:
        input_prompt += '\n===================\n# Java to C++: \n'
        input_prompt += '# Java:\n'
        input_prompt += f.read() + '\n'

    input_prompt = input_prompt[:length]
    input_prompt += '\n\n===================\n// ' + 'C++:' + '\n'
    return input_prompt

# Generate completion from OpenAI Codex


def generate_completion(input_prompt, num_tokens):
    temperature = 0.0
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=input_prompt,
        max_tokens=num_tokens,
        temperature=temperature,
        stop=['===================\n'],
        n=1,
        stream=False
    )
    return response.choices[0].text.strip()

# Write transpiled C++ code to file


def write_cpp_file(text_response):
    file_name = JAVA_FILE_TO_CONVERT.split(".")[0] + ".cpp"
    with open(file_name, "w") as f:
        f.write(text_response)
    print(f"Transpiled to C++: {file_name}")

# Check if the generated file is compilable


def test_cpp_compilation(cpp_file):
    exe_file = cpp_file.split(".")[0] + ".exe"
    return os.system(f"g++ {cpp_file} -o {exe_file} &> /dev/null") == 0

# Iterate to find a compilable C++ solution


def iterate_for_compilable_solution(prompt, max_iterations):
    print('Codex is looking for a compilable C++ solution ...')
    for it in range(max_iterations):
        text_response = generate_completion(prompt, num_tokens=1000)
        write_cpp_file(text_response)
        is_solution_compilable = test_cpp_compilation(
            JAVA_FILE_TO_CONVERT.split(".")[0] + ".cpp")
        if is_solution_compilable:
            print(f"Found a compilable solution after {it+1} iterations")
            print(
                f"Compiled Executable: {JAVA_FILE_TO_CONVERT.split('.')[0]}.exe")
            break
        if it == max_iterations - 1:
            print('Unfortunately CODEX did not find a compilable solution. '
                  f'Still you can find the generated code in the file: {JAVA_FILE_TO_CONVERT.split(".")[0]}.cpp')


if __name__ == "__main__":
    openai = initialize_openai_api()
    prompt = create_input_prompt()
    iterate_for_compilable_solution(prompt, max_iterations=3)
