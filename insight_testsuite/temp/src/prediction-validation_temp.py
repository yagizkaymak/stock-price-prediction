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
    print('a')

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


#print(hour_keyed_dic)
