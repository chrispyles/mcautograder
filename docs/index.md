# `mcautograder` Documentation

[Home](index) | [Usage](usage) | [Tests](tests) | [Docs](docs) | [License](license) | [Help](help)

## What is `mcautograder`?

This library is a mutliple choice question autograding library for Python. It was developed to be packaged with Jupyter Notebooks in such a way that does not require any special setup on the part of the server.

## Installation

You can install `mcautograder` using pip.

```bash
pip install mcautograder
```

## Changelog

**v0.0.5:**

* Changed `mcautograder.py` to `notebook.py` for less confusion
* Changed `max_retakes` param to `max_attempts` for better understanding
* Upadted docstring format for sphinx autodoc

**v0.0.4:**

* Moved utils to separate file for documentation

**v0.0.3:**

* Changed structure of tests file to be more intuitive
* Added docstrings and better documentation