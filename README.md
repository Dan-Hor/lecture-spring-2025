# Lecture Spring 2025 - Homework assignment 1
Copyright 2025 Daniel Horvath

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is released under an MIT LICENSE.

This is a homework assignment for the lecture "Open-Source Energy System Modeling" by [danielhuppmann](https://github.com/danielhuppmann/), TU Wien.
It aims to calculate the [pvlib](https://pvlib-python.readthedocs.io/en/stable/) shading factor for a utility-scale PV power plant for a whole year in 5 minute steps. The inputs to define the timespan, the geometry and the position of the PV plant are written inside the main.ipynb file. The output is a graph shown in the main.ipynb file. The newplot.py has a plot function to make a plot in one line of code. The utils.py has a is_valid_date function to check if the start and end dates are given correctly.
Beware: the comments and variables are in german.

Currently there are 2 workflows on this repo: a ruff check and a pytest for the is_valid_date function of utils.
