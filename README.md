# Introduction to Quantitative Finance

## Setup instructions for the impatient

For this course you will need:

* *Python 2.7* and *Anaconda*
* *Plotly* and *Requests* (install via pip)

Download the files from this repository into an appropriate folder, open Jupyter notebook and you're ready to go.

## Complete setup instructions

In order to follow this course you need to install the following software on
your machine:

* *Python 2.7*: Unfortunately, version compatibility in Python is still an issue
and  Python 3.x may not work.
* *Anaconda* (for `Python 2.7`) which you can get [here](https://docs.continuum.io/anaconda/install):
A package manager for Python which includes some of the packages you need for
this course (`pip`, `numpy`, `scipy`, `pandas`) as well as `jupyter`. If you want to manage your
Python environment in your own way, make sure you have those installed.
* *plotly* (`pip install plotly`): A library you will use to plot data.
* *requests* (`pip install requests`): A library you will use to retrieve information from a website (we will use it to retrieve quotes from Yahoo Finance).

Finally, you need to download the file `cca_imc_library.py` from
this repository.
We recommend you place it in a fresh directory, say `introQF`, where all your code for this course is going to live.

You're now ready to go: open a terminal in the `introQF` directory and use the command `jupyter notebook` to start a new notebook. You can then open the skeleton notebook `introQF.ipynb` (also available in this repository) and get started with the course.

## Remarks

* If you have never used Jupyter notebooks, [this tutorial](http://jupyter.readthedocs.io/en/latest/running.html) gets you running very quickly. Essentially, cells contain short chunks of code that can be executed pressing `MAJ+ENTER`.
* If your Python is a bit rusty of if you have never really coded in Python, please go through the Python warm-up notebook `introQF_pythonWarmup.ipynb` also available in the repository. This notebook will walk you very quickly through the main tools you will use in the workshop (basic types, control statements, functions, lambdas, a bit of `numpy`, `plotly` and `matplotlib`).
