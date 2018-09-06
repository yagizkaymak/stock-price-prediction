#!/bin/bash
#
# This shell script runs the code developed by Yagiz Kaymak using Python 3 for the prediction validation project.
#
python ./src/average-prediction-error-calculation.py ./input/window.txt ./input/actual.txt ./input/predicted.txt ./output/comparison.txt
