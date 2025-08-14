import random
import argparse
import os

# Setup argument parser
parser = argparse.ArgumentParser(description="Generate random password from words file.")
parser.add_argument(
    "-l", "--length",
    type=int,
    default=4,
    help="optional number of words in password (must be >1, default: 4)"
)
parser.add_argument(
    "-f", "--file",
    type=str,
    default="linux.words.txt",
    help="optional path to the words file (default: linux.words.txt in current directory)"
)
args = parser.parse_args()

# Validate length
if args.length <= 1:
    parser.error("Length must be an integer greater than 1.")

# Ensure file exists
if not os.path.isfile(args.file):
    parser.error(f"File not found: {args.file}")

# Read words from file
with open(args.file, "r", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]

if len(words) < args.length:
    parser.error(f"File contains only {len(words)} words, but {args.length} requested.")

# Pick random words
password_words = random.sample(words, args.length)

# Output
print(" ".join(password_words))
