# Testing Directory

This directory `tests` is used for `testing` purposes.  Here, we have written some unit tests, taking the help of **pytest fixtures** and **pytest**.

Some key points to remember here - 

* All the common pytest fixtures are present in the file `conftest.py`, which contains the common fixtures shared by all the test files.

* Pytest fixtures `provide data for testing`, and in that sense the data can be `passed as an argument to a testing module`. 

* The testing modules should be present in the `/tests` directory, with the name starting with `test_*`, so that pytest can automatically figure out which are the test scripts which need to be run. 

* The name of the function inside the `testing` scripts, which are used for testing should also be prefixed using `test_*`.

