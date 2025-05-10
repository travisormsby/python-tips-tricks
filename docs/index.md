# Introduction

If you're anything like us, most of what you know about Python you learned by trial and error. Most geospatial professionals don't have much formal training in computer science or software engineering. And that's fine because we're mostly not computer scientists or sofware engineers. We don't have time to train in a whole new career just to write some automation scripts. But the downside of a purely practical education is that it can be easy to settle for suboptimal solutions because we're not aware of better practices that can improve the performance and readability of our code.

This session is designed to highlight some common code patterns that work OK, but for which a better approach exists.

* Instead of bracket notation, use more unpacking
* Instead of conditionals for validation, use try/except
* Instead of rolling your own solutions, use existing Python capabilities 
* Instead of writing setup and teardown code, use context managers 
* Instead of only writing documentation in separate files, use doc strings and type hints.
* Instead of always modeling data collections as lists, use more tuples and sets
* Instead of always looping over lists, use more iterators
* Instead of list comprehensions, use more generators
* Instead of guessing about inefficiencies, profile your code 

This workshop is focused on general patterns that you can use no matter what type of problem you are working on. Because these are general patterns, don't expect to be able to lift the code examples here and use them directly in your code. Do expect to take these strategies and apply them to your code. 

The code examples and exercises are written using Jupyter Notebooks. If you have a Google account, you can click the Open in Colab button at the top to run the notebooks using Google's Colab environment. Otherwise, you can click the download button for each notebook to download it to your local machine and run in a notebook environment (e.g. loading the notebook into ArcGIS Pro). 
