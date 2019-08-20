# `mcautograder` Documentation

## What is `mcautograder`?

This library is a mutliple choice question autograding library for Python. It was developed to be packaged with Jupyter Notebooks in such a way that does not require any special setup on the part of the server.

## Installation

You can install `mcautograder` using pip.

```bash
pip install mcautograder
```

## Changelog

**v0.0.6:**

* Added state serialization to prevent dead kernels from resetting notebooks
* Added `".tests.py"` as default argument value for `Notebook` constructor
* Added `AssertionError` for scored notebooks with 0 points
* Added try/except statement for scored notebook identifiers without `"points"` key

**v0.0.5:**

* Changed `mcautograder.py` to `notebook.py` for less confusion
* Changed `max_retakes` param to `max_attempts` for better understanding
* Upadted docstring format for sphinx autodoc
* Added license field for setuptools

**v0.0.4:**

* Moved utils to separate file for documentation

**v0.0.3:**

* Changed structure of tests file to be more intuitive
* Added docstrings and better documentation

### Help

If you have an problems with `mcautograder`, please open an issue on this project's [Github repo](https://github.com/chrispyles/mcautograder).
