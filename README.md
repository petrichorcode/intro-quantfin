# Introduction to Quantitative Finance

@REVIEWERS for the dry run:

please write your comments [*here* (google doc)](https://goo.gl/BnnBpe)

## Setup instructions for the impatient

* clone this repo
* install [*Anaconda*](https://docs.continuum.io/anaconda/install)
* `pip install plotly requests`

## Complete setup instructions

In order to follow this course you need to install the following software on
your machine:

* *Python 2.7* (recommended) or *Python 3.5*. You may already have Python on your system, to check this, in your terminal write

```bash
python -V
```

if it fails, you should [*install Python*](https://www.python.org/downloads/), if it returns `Python 2.7.x` you're fine, if it returns `Python 3.x` you should be fine but may encounter problems running the game so we recommend also installing `Python 2.7`.

* [*Anaconda*](https://docs.continuum.io/anaconda/install):
a package manager for Data Science libraries in Python which includes some of the packages you need for
this course (`pip`, `numpy`, `scipy`, `pandas`) as well as `Jupyter`. If you want to manage your
Python environment in your own way, make sure you have those installed.
* *Plotly* and *requests* two Python libraries, the first one to plot data interactively, the second to retrieve informations from a website (e.g., quotes from Yahoo Finance). To install those two, you can use `pip` in your terminal:

```bash
pip install plotly requests
```

Finally, you need to download the files `introQF_library.py` and `introQF_skeleton.ipynb` from this repository.
We recommend you place them in a fresh directory, say `introQF`, where all your code for this course is going to live.

You're now ready to go: open a terminal in the `introQF` directory and use the command `jupyter notebook` to start a new notebook. You can then open the skeleton notebook `introQF.ipynb` and get started with the course.

## Remarks

* If you have never used Jupyter notebooks, [this tutorial](http://jupyter.readthedocs.io/en/latest/running.html) gets you running very quickly. Essentially, cells contain short chunks of code that can be executed pressing `MAJ+ENTER`.
* If your Python is a bit rusty of if you have never really coded in Python, please go through the Python warm-up notebook `introQF_pythonWarmup.ipynb` also available in the repository. This notebook will walk you very quickly through the main tools you will use in the workshop (basic types, control statements, functions, lambdas, a bit of `numpy`, `plotly` and `matplotlib`).
