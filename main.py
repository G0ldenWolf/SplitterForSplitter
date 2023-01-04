import os

def split(name, *positions):
    output = []
    with open(name, 'r') as file:
        content = file.read().splitlines()
        start = 0
        for i in positions:
            for position in i:
                output.append(content[start:position])
                start = position
        output.append(content[start:])
    counter = 1
    for out in output:
        with open(f"{name.split('.')[0]}_part{counter}.tess", 'w') as file:
            for line in out:
                file.write(f"{line}\n")
        counter += 1
    return


files = os.listdir()
print(f"{len(files)} files in directory")
for file in files:
    if 'tess' in file:
        print(f"Checking {file}")
        with open(file, 'r') as f:
            prev, temp = map(float, f.readline().split())
            counter = 0
            doINeedToSplit = False
            whereDoINeedToSplit = []
            for line in f:
                time, temp = map(float, line.split())
                counter += 1
                if time - prev > 1:
                    doINeedToSplit = True
                    whereDoINeedToSplit.append(counter)
                prev = time
            if doINeedToSplit:
                split(file, whereDoINeedToSplit)

