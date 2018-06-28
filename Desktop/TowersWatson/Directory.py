import os
import heapq

# Make sure to change the directory
directory ="C:"

# Get all files.
list = os.listdir(directory)

# Loop and add files to list.
pairs = []
for file in list:

    # Use join to get full file path.
    location = os.path.join(directory, file)

    # Get size and add to list of tuples.
    size = os.path.getsize(location)
    size = "{0:5f}".format(size/1024/1024)
    pairs.append((size, file))

# Sort list of tuples by the first element, size.
pairs.sort(key=lambda s: s[0:], reverse = True)

pairs = heapq.nlargest(5,pairs)



# Display pairs.
for pair in pairs:
    print(pair)
"# Enterprise" 
