# Testing Phonetic Matching

This repo has some code for using a python phonetic matching package to match words. Should mean "Jon" and "John" match! Perhaps this can be used to do better person name matching?

## Usage

Uses Python 3. To try it out, use a [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) and load in the requirements.txt file.

```
python3 -m venv ./.venv
source ./.venv/bin/activate (works on Mac, other OS might differ)
python3 -m pip install -r requirements.txt
```

You might need to need to [restart the virtual environment](https://stackoverflow.com/a/54597424) to run the tests - something like `deactivate && source .venv/bin/activate` will do that. Then just running `pytest` will run the tests.

To use it from the console, put the inputs into the `inputs.csv` file and from this directory run `python main.py` - the results will be written to `outputs.csv`