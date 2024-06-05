import re

def extract_functions(content):
    # regex based on c++ syntex 
    function_pattern = re.compile(r'''
    ([\w\s*&:]+)      # Return type
        \s+(\w+::\w+|\w+) # Function name
        \s*\(([^\)]*)\)   # Parameters
        \s*({(?:[^{}]*{[^{}]*})*[^{}]*})  # Function body
    ''', re.VERBOSE)

    functions = function_pattern.findall(content)
    extracted_functions = []

    for func in functions:
        return_type, name, parameters, body = func
        combined_function = f"{return_type.strip()} {name.strip()}({parameters.strip()}) {body.strip()}"
        extracted_functions.append((name,combined_function))
    
    return extracted_functions;  
