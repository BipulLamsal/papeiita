import argparse
import threading
from utils.extractor import extract_functions
from utils.codeblock import process_code_blocks 
from utils.codeblock import loading_animation 
from pygments.styles import get_all_styles

def main():
    available_styles = list(get_all_styles()) 
    parser = argparse.ArgumentParser(description="Function Extractor for C++ file and generate codeblock images.")
    parser.add_argument("-f","--file", help="Path to the C++ file")
    parser.add_argument("-o", "--output", help="Output directory for images", default=".")
    parser.add_argument("--font", default="JetBrainsMono-Regular.ttf", help="Path to the custom font file")
    parser.add_argument("--size", type=int, default=12, help="Font size")
    parser.add_argument("--style", choices=available_styles, default="github-dark", help="Pygments style")
    # Parse arguments
    args = parser.parse_args()

    try:
        with open(args.file, 'r') as file:
            content = file.read()
            if content:
                event = threading.Event()
                loading_thread = threading.Thread(target=loading_animation, args=(event,))
                loading_thread.start()
                
                functions = extract_functions(content)
                process_code_blocks(functions, args.output, args.font, args.size, args.style)
                # triggers completion
                event.set()
                print("Extracted Code Snippets! on ", args.output)

                # Wait for the loading animation thread to complete
                loading_thread.join()
                
    except FileNotFoundError:
        print("Error: File not found.")

if __name__ == "__main__":
    main()

