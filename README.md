# Table of Contents
1. [Copyright](README.md#copyright)
1. [Introduction](README.md#introduction)
1. [Running The Code](README.md#running)

## Copyright
This code has been developed by Yagiz Kaymak using Python 3 for the prediction validation project as a part of Insight coding challenge.

Copyright 2018 Yagiz Kaymak

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Introduction
This Python code calculates an average error of the differences between the actual and the predicted stock prices.

 Two different files, one (actual.txt) provides the actual value of each stock every hour and the second (predicted.txt) lists the predicted value of various stocks at a certain hour during the same time period.

This code obtains the average error by calculating the average difference between the actual stock prices and the predicted values over a specified sliding time window.

## Running The Code
In order to run the code provided in this repository, please use the shell script (run.sh) in the root folder of this project.

<b>./run.sh</b> command should be run in the stock-price-prediction folder.
