# to write to a current directory
with open("test.txt", "w") as file:
    file.write("This is a line.")

import csv
with open("test.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["col1", "col2", "col3"])
    writer.writerow(["data1", "data2","data3"])

# to write to a sub folder residing in the current directory
with open(r".\pfb_ind_assign2\test.txt", "w") as file:
    file.write("This is a line.")

with open(r".\pfb_ind_assign2\test.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["col1", "col2", "col3"])
    writer.writerow(["data1", "data2","data3"])