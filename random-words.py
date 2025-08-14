import random

# Path to your file
file_path = "linux.words.txt"

# Read all words from file, stripping newlines
with open(file_path, "r", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]

# Choose 4 random words
password_words = random.sample(words, 4)

# Join them with spaces
password = " ".join(password_words)

print(password)