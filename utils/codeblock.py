import os
import threading
import time
import sys
from pygments import lexers
from pygments.formatters import ImageFormatter
from pygments import highlight 

def loading_animation(event):
    animation = '|/-\\'
    idx = 0
    while not event.is_set():
        sys.stdout.write('\r' + animation[idx % len(animation)] + ' ')
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)

def process_code_blocks(blocks, output, font_path, font_size, style):
    threads = []
    for block in blocks:
        filename, code = block
        thread = threading.Thread(target=generate_code_block_image, args=(filename, code, output, font_path, font_size, style))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def generate_code_block_image(filename, code, output, font_path, font_size, style):
    lexer = lexers.get_lexer_by_name("cpp")
    formatter = ImageFormatter(font_name=font_path, font_size=font_size, line_numbers=True, style=style)
    highlighted_code = highlight(code, lexer, formatter)
    if not os.path.exists(output):
        os.makedirs(output)
    with open(f"{output}/{filename}.png", 'wb') as f:
        f.write(highlighted_code)
