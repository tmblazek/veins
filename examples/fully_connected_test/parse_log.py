import os
import numpy as np
from matplotlib import pyplot as plt


def main(input_file="test.txt"):
    results = {}
    begin_times = {}
    with open(input_file, 'r') as fp:

        line = fp.readline()
        while (line):
            print(line)
            parts = line.split(" ")
            timestamp = parts[1]
            mode = parts[-1].strip()
            node = parts[3].split(".")[1]
            print(mode)
            if mode == "sched":
                assert (node not in begin_times)
                begin_times[node] = float(timestamp)
            elif mode == "tx":
                assert (node in begin_times)
                print(node)
                if node in results:
                    results[node].append(float(timestamp) - begin_times[node])
                else:
                    results[node] = [float(timestamp) - begin_times[node]]
                del begin_times[node]
            else:
                raise ()
            line = fp.readline()
    times_array = np.array([np.mean(y) for x in results.values() for y in x])
    print(np.mean(times_array))
    plt.hist(times_array)
    plt.show()


if __name__ == '__main__':
    main()
