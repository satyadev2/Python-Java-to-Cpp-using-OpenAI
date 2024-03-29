# Python to C++ Converter using OpenAI Codex 

This script converts Python code to C++ using OpenAI Codex. It utilizes the GPT-3.5 Turbo Instruct model to transpile Python code into equivalent C++ code.

## Configuration

Before running the script, ensure you have set up your OpenAI API key in a `.env` file located in the root directory of the project. The `.env` file should contain the following, it might show import error but once you install dependency given below, it will work fine, so don't worry and go with the flow :)

```csharp
[openai]
api_key = 'YOUR_OPENAI_API_KEY'
```

Replace `'YOUR_OPENAI_API_KEY'` with your actual OpenAI API key. If you don't have an API key, you can register for OpenAI Codex [Copy](https://file+.vscode-resource.vscode-cdn.net/home/kush_satyadev/py2cpp/# "#").

Just Login there and there will be api option, just generate an api key from there and paste in .env file, keep instution as default.

## How to Run

I suppose you must have python , if not, please install it before going below doc-

check whether you have installed it successfully -

`pyhton -v`

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies by running:

<pre><div class="white bg-white-950 rounded-md"><div class="p-4 overflow-y-auto"><code class="">
pip install openai
pip install os
pip install dotenv
</code></div></div></pre>


4. Create the `.env` file in the root directory and add your OpenAI API key.
5. Run the script using Python 3:

<pre><div class="dark bg-gray-950 rounded-md"><div class="p-4 overflow-y-auto"><code class="">python3 python2cppconverter.py
</code></div></div></pre>

6. Follow the prompts and instructions provided by the script.
7. Once completed, check the generated C++ file in the same directory.

## Notes

* The script iterates to find a compilable C++ solution, with a maximum of 3 iterations.
* It warns about control reaching the end of a non-void function during C++ compilation, which may require additional handling in the generated code.

## Show Your Support giving it a ⭐

If you find this project helpful or valuable, we'd appreciate it if you could give it a star! It helps us know that our efforts are appreciated and motivates us to continue improving the project for you and others in the community. Thank you for your support!
