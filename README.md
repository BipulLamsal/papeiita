# papeiita
regx based c++ function extractor, workable but is error prone. 

### Commands
```
usage: main.py [-h] [-f FILE] [-o OUTPUT] [--font FONT] [--size SIZE]
               [--style {abap,algol,algol_nu,arduino,autumn,ys...}]
Function Extractor for C++ file and generate codeblock images.
options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to the C++ file
  -o OUTPUT, --output OUTPUT
                        Output directory for images
  --font FONT           Path to the custom font file
  --size SIZE           Font size
  --style {abap,algol,algol_nu,arduino,autumn,ys...}
```

## Warning
The regex currently extract based on the content inside {}, it might generate error when there are multiple nested curly braces, using try, catch blocks or nested switch case or nested if else might also be extracted as function.
