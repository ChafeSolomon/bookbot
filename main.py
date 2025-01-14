path_to_file = '/root/bookbot/books/frankenstein.txt'

def main():
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def count(args):
    args = args.split()
    return len(args)

def characters(args, args2):
    alphabet = {}
    for char in args:
        char = char.lower()
        if char in alphabet:
            alphabet[char] += 1
        elif char not in alphabet:
            alphabet[char] = 1
        else:
            raise Exception("something went wrong")
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{args2} words found in the document\n")
    for char in alphabet:
        print(f"The '{char}' character was found {alphabet[char]} times")

results = main()
word_count = count(results)
character_count = characters(results, word_count)
