# Table of Contents
1. [Author](README.md#author)
1. [Introduction](README.md#introduction)
1. [Input](README.md#input)
1. [Output](README.md#output)
1. [Running The Code](README.md#running)
1. [Test Cases](README.md#running)
1. [Computational Complexity](README.md#complexity)
1. [Caveat](README.md#caveat)


## Author
This code has been developed by Yagiz Kaymak using Python 3 for the prediction validation project as a part of the Insight coding challenge.
The code is also accessible online by using the following link:
https://yagizkaymak@bitbucket.org/yagizkaymak/stock-price-prediction

## Introduction
This Python code calculates an average error of the stock price differences for a given time range using the actual and predicted prices of the stocks.

"actual.txt" is a time-ordered file listing the actual value of stocks at a given hour.
"predicted.txt" is a time-ordered file of the predicted value of certain stocks at a given hour.
"window.txt" holds a single integer value denoting the window size (in hours) for which you must calculate the average error.

Please refer to in-line comments in "./src/average-prediction-error-calculation.py" file for further details of the implementation.

## Input
Three input files can be found in "input" folder with the file names of "actual.txt", "predicted.txt", and "window.txt".
Each file has pipe-character-delimited lines in the following format: time|ticker|price.

"actual.txt" has lines corresponding to the actual price of a stock recorded at a time.
"predicted.txt" has lines corresponding to the predicted price of a stock for a specific time.
"window.txt" has only one value indicating the inclusive time range of the sliding window.


## Output
The code outputs a file consisting of pipe-character-delimited lines. The output file is saved to "output" folder with file name of "comparison.txt".

The format of the file is as follows: start_time_of_the_sliding_window|end_time_of_the_sliding_window|absolute_average_price_difference_in_the_sliding_window

If the sliding window value given in "window.txt" is equal to one, the output file only includes the hourly average errors. Therefore, its format becomes:
hour|absolute_average_price_difference_in_the_sliding_window


## Running The Code
In order to run the code provided in this repository, please use the shell script (run.sh) located in the root folder of this project.

./run.sh command should be run in the stock-price-prediction folder.


## Test Cases
Five test cases to test the code can be found in "insight_testsuite/tests" folder. "test_1" is the test case created by Insight Institute. "my_test_x" folders are the test cases created by Yagiz Kaymak.

To run the test cases please run "./run_tests.sh" shell script in the "insight_testsuite/tests" folder.

## Computational Complexity
The code includes three for loops. The first one iterates through the lines of "actual.txt". Therefore, the computational
complexity of this loop is O(a), if there are "a" number of rows in "actual.txt".
The second loop iterates through the lines of "predicted.txt". Therefore, the computational
complexity of the second loop is O(p), if there are "p" number of rows in "predicted.txt". Note that (a >= p).
The last loop iterates through the hour (i.e., time) values and it has an inner loop that iterates over the time range  (i.e., stride) of each sliding window. Therefore, the computational complexity of the last loop is O(hs), if there are "h" number of hours stock recordings is "actual.txt" and the stride value in the "window.txt" is s.
So, the total computational complexity of the code is O(a) + O(p) + O(hs).

## Caveat
Because of the average calculation, which outputs a float number, and the rounding operation of the average value, the code does not pass the test case provided by the Insight Institute.
There is only a +/-0.01 error for some sliding windows.
