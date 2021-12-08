import pandas as pd
import numpy as np

df = pd.read_csv("input_files/day01.txt", header=None)

# part 1, count numbef of times it changes.
print(np.sum(df.diff() > 0))


# part 2, use a 3-number sample.  You can do this in one line, but it's
# very dense.
windows = df.rolling(3).sum()
print(np.sum(windows.diff()> 0))
