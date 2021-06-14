# File Creator

## Motivation
Every time when I need to create a python file, I need to add:
- `#!/usr/bin/env ipython3` (shebang), most of the time
- or `#!/usr/bin/python3`
- Date
- User
- `if __name__ == "__main__":`

Then I need to change the mode of the file to 744 to make it executable.

This is a tedious process and I want to automate this. The python script in this repo enables this.


## Usage

1. Clone the repo.

2. Setup
```
cd file_creator
./setup_symbolic_link.sh

cf -h
```

cf stands is short for create_file

## Example
- Create a python file with 744

  `cf python python_file.py`

- Create a python file with 644

  `cf python python_file.py -m 644`

- Create a c file

  `cf c c_file.c`

- Create a bash script with 744

  `cf python bash_file.py`
