import sys # This library is used to get the command line arguments when the application runs.

# Method that creates the sliding windows, with a given sliding window time range as "stride".
# Please call this method with an itirable input parameter, such as a list,
# and a stride value that corresponds to the value in "window.txt."
# The output of this method is a generator that generates all the sliding windows.
def create_sliding_windows(input_list, stride=4):
    iterator = iter(input_list)
    window = []

    for index in range(0, stride):
        window.append(next(iterator))
    yield window

    for index in iterator:
        window = window[1:] + [index]
        yield window
# end of create_sliding_windows method.


### Main python function starts here. ###

# Open the "window.txt" located in "./input" folder as the second command line argument.
sliding_window_fd = open(sys.argv[1], 'r')

# Read the window value in "window.txt" file and convert the value to integer.
sliding_window_range = int(sliding_window_fd.read())

# We are done with "window.txt" file. It is closed here.
sliding_window_fd.close()

# Open the "actual.txt" located in "./input" folder as the third command line argument.
actual_fd = open(sys.argv[2], 'r')

# Create an empty dictionary to store values in the "actual.txt" file.
actual_dic = {}

# Open the "predicted.txt" located in "./input" folder as the fourth command line argument.
predicted_fd = open(sys.argv[3], 'r')

# Create an empty dictionary to store values in the "actual.txt" file.
predicted_dic = {}

# This variable stores the minimum time in the "actual.txt" file. It is initialized with an arbitrarily big number.
min_hour = 9999999

# This variable stores the maximum time in the "actual.txt" file. It is initialized with zero.
max_hour = 0

# Read "actual.txt" line by line and create a "actual_dic" dictionary using the
# first two column names (hour, ticker) as the key, and the price as the value.
for line in actual_fd:
    # Split each line using the pipe char as the delimiter.
    line_content = list(line.split('|'))

    # Assign the price of a stock using (hour, ticker) tuple as a key and its price as the value.
    actual_dic[(line_content[0], line_content[1])] = line_content[2]

    # Update the "min_hour" if necessary.
    min_hour = min(min_hour, int(line_content[0]))

    # Update the "max_hour" if necessary.
    max_hour = max(max_hour, int(line_content[0]))
# end of foor loop

# Close the "actual.txt" file.
actual_fd.close()

# Create an empty dictionary that stores the price differences
# of the matching stocks given in "actual.txt" and "predicted.txt".
# The key of this dictionary is the time (hour) that stock price is recorded.
# Its value is a list that stores the price differences of
# the matching stocks since collisions will occur for the matching stocks
# that fall in the same bucket.
hour_keyed_dic = {}

# Loop over the lines of the "predicted.txt" file.
for line in predicted_fd:
    # Split each line using the pipe char as the delimiter
    line_content = list(line.split('|'))

    # Create a key for the stocks in the "predicted.txt" file as a (hour, ticker) tuple.
    key = (line_content[0], line_content[1])

    # Get the hour value as the first value of each row.
    hour = int(line_content[0])

    # Get the price value as the last value of each row.
    predicted_price = float(line_content[2])

    # Calculate the absolute price difference of a stock using its actual and predicted price,
    # if the actual stock price has a corresponding entry in "predicted.txt" file.
    if key in actual_dic:

        # Get the absolute value of the difference
        abs_diff = abs(float(actual_dic[key]) - predicted_price)

        # If this key exists in the list append the difference at the end of its list.
        if hour in hour_keyed_dic:
            hour_keyed_dic[hour].append(abs_diff)

        # If the key does not exist create a list with the first absolute difference.
        else:
            differences = list()
            differences.append(abs_diff)
            hour_keyed_dic[hour] = differences
        # end of inner if
    # end of outer if
# end of for loop

# Close the "predicted.txt" file.
predicted_fd.close()

# Calculate the average price differences for each hour.
for key in hour_keyed_dic.keys():
    hour_keyed_dic[key] = sum(hour_keyed_dic[key]) / len(hour_keyed_dic[key])

# Create a list that stores all hours.
# Alternatively, this value can be extracted from the
# first row of the "actual.txt" file.
# I assume that time values are consecutive and do not have a tipe gap
# anywhere.
hours = range(min_hour, max_hour + 1)

# Create a "comparison.txt" located in "./output" folder to write the outputs of the code.
# Output file name is given as the last command line argument.
comparison_fd = open(sys.argv[4], 'w')

# Get sliding window generator by calling "create_sliding_windows" method.
window_generator = create_sliding_windows(hours, stride = sliding_window_range)

# Loop through the sliding windows
for current_window in window_generator:

    # Use a temporary total variable to store the total value of
    # the absolute stock price differences in a particular sliding window.
    temp_total = 0.0

    # Use an average variable to store the average value of
    # the absolute stock price differences in a particular sliding window.
    average = 0.0

    # Calculate the total price difference in a particular sliding window
    for i in range(0, len(current_window)):
        temp_total = temp_total + hour_keyed_dic[current_window[i]]
    # end for

    # Calculate the average of the sliding window and round it to two decimal points.
    average = round(temp_total / len(current_window), 2)

    # Get the sliding window start time to otput to "comparison.txt"
    sliding_window_start = int(current_window[0])

    # Get the sliding window end time to otput to "comparison.txt"
    sliding_window_end = int(current_window[sliding_window_range - 1])

    # Write the output with a pipe char delimited format to "comparison.txt"
    comparison_fd.write(str(sliding_window_start) + '|' + str(sliding_window_end) + '|' + str(average) + '\n')
# end for loop

# Close the "comparison.txt" file.
comparison_fd.close()
