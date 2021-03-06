# Introduction to Quantitative Finance

<!---
[**Link to competition files**](http://beta.cambridgespark.com/courses/public/students.zip)

(if you're reading this comment before the event, those links will become live on the day.)

[comment]: <> [**Link to content**](http://beta.cambridgespark.com/courses/public/html/index.html)
--->

## Setup instructions for the impatient

* clone this repository
* install [*Anaconda*](https://docs.continuum.io/anaconda/install)
* run `pip install plotly requests`

Then, if your Python is rusty, open Jupyter (Terminal: `jupyter notebook`) and go through the `introQF_pythonWarmup.ipynb` notebook.

## Complete setup instructions

In order to follow this course you need to install the following software on
your machine:

* *Python 2.7* (recommended) or *Python 3.5*. You may already have Python on your system, to check this, in your terminal write

    ```bash
    python -V
    ```

    if it fails, you should [*install Python*](https://www.python.org/downloads/), if it returns `Python 2.7.x` or `Python 3.x` you're fine.
* [*Anaconda*](https://docs.continuum.io/anaconda/install):
a package manager for Data Science libraries in Python which includes some of the packages you need for
this course (`pip`, `numpy`, `scipy`, `pandas`) as well as `Jupyter`. Make sure you install the right version (Anaconda  4.1 for Python 2.7.x and 4.2 for Py3.x). If you want to manage your
Python environment in your own way, make sure you have those installed.
* *Plotly* and *requests* two Python libraries, the first one to plot data interactively, the second to retrieve informations from a website (e.g., quotes from Yahoo Finance). To install those two, you can use `pip` in your terminal:

    ```bash
    pip install plotly requests
    ```

Finally, you need to download the files `introQF_library.py` and `introQF_skeleton.ipynb` from this repository as well as the data files `pdata_AAPL_2005_2013.csv` and `pdata_GOOG_2005_2013.csv`.
We recommend you place them in a fresh directory, say `introQF`, where all your code for this course is going to live.

You're now ready to go: open a terminal in the `introQF` directory and use the command `jupyter notebook` to start a new notebook. You can then open the skeleton notebook `introQF.ipynb` and get started with the course.

## Remarks

* If you have never used Jupyter notebooks, [this tutorial](http://jupyter.readthedocs.io/en/latest/running.html) gets you running very quickly. Essentially, cells contain short chunks of code that can be executed pressing `MAJ+ENTER`.
* If your Python is rusty of if you have never coded in Python, we **strongly encourage** you to go through the Python warm-up notebook `introQF_pythonWarmup.ipynb` also available in the repository. This notebook will walk you very quickly through the main tools you will use in the workshop (basic types, control statements, functions, lambdas, a bit of `numpy`, `plotly` and `matplotlib`).
