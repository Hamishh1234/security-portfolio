import hashlib

def get_file_hash(filename):
    with open(filename, "rb") as file:
        data = file.read()
        return hashlib.sha256(data).hexdigest()

original_hash = get_file_hash("important_file.txt")

print("Original hash:")
print(original_hash)

input("Now change important_file.txt, then press Enter to check it again...")

new_hash = get_file_hash("important_file.txt")

print("New hash:")
print(new_hash)

if original_hash == new_hash:
    print("No change detected.")
else:
    print("ALERT: The file has been changed.")