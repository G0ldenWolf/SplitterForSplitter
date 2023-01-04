import os


def split(name, *positions):
    # Output will contain parts of the main file 
    output = []
    
    # Open mail file and split it
    with open(name, 'r') as file:
        content = file.read().splitlines()
        start = 0
        for i in positions:
            for position in i:
                # Move part before gap into output
                output.append(content[start:position])
                start = position
        # Move the last part 
        output.append(content[start:])
    
    
    counter = 1
    for out in output:
        # Create files and write these parts
        with open(f"{name.split('.')[0]}_part{counter}.tess", 'w') as file:
            for line in out:
                file.write(f"{line}\n")
        counter += 1
    return


if __name__ == '__main__':
    # Check for .tess files
    files = os.listdir()
    tess_files = []
    for file in files: 
        if '.tess' in file:
            tess_files.append(file)
    print(f"{len(tess_files)} .tess files in this directory")


    for file in tess_files:
        print(f"Checking {file}", end=" ")
        # Open every .tess file
        with open(file, 'r') as f:
            prev, temp = map(float, f.readline().split())
            counter = 0
            doINeedToSplit = False
            whereDoINeedToSplit = []
            # Look for gaps in the data
            for line in f:
                time, temp = map(float, line.split())
                counter += 1  
                # If your observation interval is quite big (day or more), change 1 to bigger number
                if time - prev > 1:
                    doINeedToSplit = True
                    whereDoINeedToSplit.append(counter)
                prev = time 
            
            # Split the file if required
            if doINeedToSplit:
                split(file, whereDoINeedToSplit)
        print("done")



