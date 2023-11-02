import openai

# Initialize the LLM (Assuming GPT-4 with OpenAI API)
openai.api_key = 'YOUR_OPENAI_API_KEY'


class LLM_UnitTest_Generator:

    def __init__(self):
        self.cache = {}  # A dictionary to cache results for previously processed code snippets

    def determine_complexity(self, code_snippet):
        """
        Determines the complexity of the code snippet.
        This is just a basic example using line count; a more sophisticated metric can be used.
        """
        lines = code_snippet.strip().split("\n")
        if len(lines) <= 5:
            return "simple"
        elif len(lines) <= 15:
            return "medium"
        else:
            return "complex"

    def generate_test(self, code_snippet):
        """
        Use the LLM to generate a unit test for a given code snippet.
        """
        complexity = self.determine_complexity(code_snippet)

        # Check cache
        if code_snippet in self.cache:
            print("Using cached result")
            return self.cache[code_snippet]

        prompt = f"Generate a {complexity} unit test for the following Python code:\n\n{code_snippet}\n"

        response = openai.Completion.create(
            model="gpt-4.0-turbo",
            prompt=prompt,
            max_tokens=500  # You can adjust this based on requirements
        )

        generated_code = response.choices[0].text.strip()

        # Cache the result
        self.cache[code_snippet] = generated_code

        return generated_code

    def generate_tests_for_multiple_snippets(self, code_snippets):
        """
        Generate unit tests for multiple code snippets.
        """
        tests = {}
        for snippet in code_snippets:
            test = self.generate_test(snippet)
            tests[snippet] = test
        return tests


# Usage:

generator = LLM_UnitTest_Generator()

code_sample = """
def add(a, b):
    return a + b
"""

generated_test = generator.generate_test(code_sample)
print(generated_test)

multiple_samples = [
    """
def add(a, b):
    return a + b
    """,
    """
def subtract(a, b):
    return a - b
    """
]

generated_tests = generator.generate_tests_for_multiple_snippets(multiple_samples)
for code, test in generated_tests.items():
    print(f"For code:\n{code}\nGenerated test:\n{test}\n{'-' * 40}")
