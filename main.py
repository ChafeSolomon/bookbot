path_to_file = '/root/bookbot/books/frankenstein.txt'

def main():
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def count(args):
    args = args.split()
    print(len(args))

results = main()
count(results)

