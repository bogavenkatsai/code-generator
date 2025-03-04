import random

def generate_random_code(language, length=10):
    """Generates random code snippets in a given language."""

    if language == "python":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_+-*/%&|^~<>=!(),[]{}:; "
        code = "".join(random.choice(characters) for _ in range(length))
        # Add a bit of structure (very basic)
        if random.random() < 0.3:
            code = f"def my_func():\n    return {code}"
        elif random.random() < 0.5:
            code = f"print({code})"
        return code

    elif language == "javascript":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_+-*/%&|^~<>=!(),[]{}; "
        code = "".join(random.choice(characters) for _ in range(length))
        if random.random() < 0.3:
            code = f"function myFunction() {{\n  return {code};\n}}"
        elif random.random() < 0.5:
            code = f"console.log({code});"
        return code

    elif language == "c++":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_+-*/%&|^~<>=!(),[]{};<># "
        code = "".join(random.choice(characters) for _ in range(length))
        if random.random() < 0.3:
            code = f"#include <iostream>\nint main() {{\n  std::cout << {code} << std::endl;\n  return 0;\n}}"
        return code

    else:
        return "Language not supported."

def main():
    """Main function to demonstrate code generation."""

    language = input("Enter programming language (python, javascript, c++): ").lower()
    length = int(input("Enter code length: "))

    generated_code = generate_random_code(language, length)
    print("\nGenerated Code:\n")
    print(generated_code)

if __name__ == "__main__":
    main()