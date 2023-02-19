import os
l = [1, 2, 3, 4, 5]
with open("test.txt", "w+") as f:
    for i in l:
        f.write(f"{str(i)} \n", )

for i in range(97, 123):
    f = open(f"/Users/tolebi/code/pp2-22B030420/tsis6/test/{chr(i)}.txt", "w")
    f.close()


with open("test.txt") as f:
    with open('copy.txt', "w") as cop:
        for line in f:
            cop.write(line)

path = r"/Users/tolebi/code/pp2-22B030420/tsis6/copy.txt"
if not os.path.exists(path=path):
    print("Doesnt exist")
else:
    print("PATH exists")
os.remove(path)
print("Deleted")