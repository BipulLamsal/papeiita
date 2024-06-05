import re
def extract_functions(content):
    # Regular expression to match function signatures without bodies
    function_signature_pattern = re.compile(r'''
        ([\w\s*&:<>]+)      # Return type (including templates)
        \s+(\w+::\w+|\w+)   # Function name
        \s*\(([^)]*)\)      # Parameters
        \s*{                # Opening brace of function body
    ''', re.VERBOSE)

    matches = function_signature_pattern.finditer(content)
    extracted_functions = []

    for match in matches:
        return_type, name, parameters = match.groups()
        start = match.end() - 1
        body, end = extract_body(content, start)
        combined_function = f"{return_type.strip()} {name.strip()}({parameters.strip()}) {body.strip()}"
        extracted_functions.append((name, combined_function))
    
    return extracted_functions

def extract_body(content, start):
    stack = []
    end = start
    for i in range(start, len(content)):
        if content[i] == '{':
            stack.append('{')
        elif content[i] == '}':
            stack.pop()
            if not stack:
                end = i + 1
                break
    return content[start:end], end
