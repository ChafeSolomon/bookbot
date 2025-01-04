path_to_file = '/root/bookbot/books/frankenstein.txt'

def main():
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def count(args):
    count = 0
    args = args.split(' ')
    for word in args:
        count += 1
        print(count, word)

results = main()
count(results) 
