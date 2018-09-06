import sys

def window(iterable, size=4):
    i = iter(iterable)
    win = []
    for e in range(0, size):
        win.append(next(i))
    yield win
    for e in i:
        win = win[1:] + [e]
        yield win

sliding_window_fd = open(sys.argv[1], 'r')
sliding_window_range = int(sliding_window_fd.read())
sliding_window_fd.close()

actual_fd = open(sys.argv[2], 'r')
actual_dic = {}

predicted_fd = open(sys.argv[3], 'r')
predicted_dic = {}

min_hour = 10000000
max_hour = 0

# Read "actual.txt" line by line and create a "actual_dic" dictionary using
# first two column names (hour, ticker) as the key and the price as the value
for line in actual_fd:
    line_content = list(line.split('|'))

    actual_dic[(line_content[0], line_content[1])] = line_content[2]

    min_hour = min(min_hour, int(line_content[0]))
    max_hour = max(max_hour, int(line_content[0]))

actual_fd.close()


hour_keyed_dic = {}

for line in predicted_fd:
    line_content = list(line.split('|'))
    key = (line_content[0], line_content[1])
    hour = int(line_content[0])
    predicted_price = float(line_content[2])

    if key in actual_dic:
        abs_diff = abs(float(actual_dic[key]) - predicted_price)

        # If this key exists in the list append the difference at the end of its list.
        if hour in hour_keyed_dic:
            hour_keyed_dic[hour].append(abs_diff)
        # If the key does not exist create a list with the first absolute difference.
        else:
            differences = list()
            differences.append(abs_diff)
            hour_keyed_dic[hour] = differences

predicted_fd.close()

for key in hour_keyed_dic.keys():
    hour_keyed_dic[key] = sum(hour_keyed_dic[key]) / len(hour_keyed_dic[key])

hours = range(min_hour, max_hour + 1)

comparison_fd = open(sys.argv[4], 'w')

window_generator = window(hours, size = sliding_window_range)

for current_window in window_generator:

    temp_total = 0.0

    # Calculate the total difference of the sliding window
    for i in range(0, len(current_window)):
        temp_total = temp_total + hour_keyed_dic[current_window[i]]

    average = round(temp_total / len(current_window), 2)
    sliding_window_start = int(current_window[0])
    sliding_window_end = int(current_window[sliding_window_range - 1])

    comparison_fd.write(str(sliding_window_start) + '|' + str(sliding_window_end) + '|' + str(average) + '\n')


comparison_fd.close()
