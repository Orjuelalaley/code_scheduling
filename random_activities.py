import sys
import random

if len(sys.argv) < 2:
    print("Usage: python3", sys.argv[0], "1 100")
    sys.exit(1)

nAct = int(sys.argv[1])
nSlots = int(sys.argv[2])

for i in range(100):
    with open(f'file_{i}.txt', 'w') as f:
        s = 0
        while s <= nAct:
            start = random.randint(0, nSlots - 1)
            end = random.randint(start + 1, nSlots)
            if start < end:
                f.write(f"act_{s} {start} {end}\n")
                s = s + 1
