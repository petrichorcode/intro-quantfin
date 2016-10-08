# Introduction to Quantitative Finance: Setup Instructions

In order to follow this course you need to install the following software on
your machine:

* *Python 2.7*: Unfortunately, version compatibility in Python is a big issue
and  Python 3.x may not work.
* *Anaconda*
(link:https://docs.continuum.io/anaconda/install[docs.continuum.io/anaconda/install]):
A package manager for Python which includes some of the packages you need for
this course (`pip`, `numpy`, `scipy`, `pandas`). If you want to manage your
Python environment in your own way, make sure you have those installed.
* *plotly* (`pip install plotly`): A library you will use to plot data.
* *requests* (`pip install requests`): A library you will use to extract
information from Yahoo Finance.

Finally, you need to get the file `cca_imc_library.py` from
this repository. We recommend you place it in a fresh
directory, say `introQF`, where all your code for this course is going to live.

You're now ready to go: open a terminal in the `introQF` directory and use the
command `jupyter notebook` to start a new notebook. At the beginning of your
notebook, write

[source,python]
----
from cca_imc_library import *
----

in order to load the necessary libraries – it might take a few seconds – as
well as some other functions to retrieve financial data from the web.
A skeleton notebook `introQF.ipynb` is also available in the repository and will be useful for the course.

.Remarks
****

* If you have never used Jupyter notebooks, link:http://jupyter.readthedocs.io/en/latest/running.html[jupyter.readthedocs.io/en/latest/running.html] is a tutorial that gets you running very quickly.
* If your Python is a bit rusty of if you have never really coded in Python, please go through the Python warm-up notebook [red]#*TODO:PUT_ADDRESS_HERE*# which walks you very quickly through the main tools you will use in this workshop (basic types, control statements, functions, lambdas and a bit of `numpy`).
* The figures of this document are displayed as generated with `Matplotlib+Seaborn`. The figures you will generate with `Plotly` in your notebook are interactive. They will also look a bit different.
