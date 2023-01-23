a = "Hello world"
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print("String is " + a)
print(b)
print(a[1])
for i in a:
    print(i)
print(len(b))
print("bye" in a)
if "bye" not in a:
    print("There is no bye in " + a)

