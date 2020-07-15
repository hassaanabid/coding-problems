import argparse, re
parser = argparse.ArgumentParser()
parser.add_argument("s")
args = parser.parse_args()
s = args.s
s = re.sub('[^a-zA-Z0-9\s]', '', args.s)
rv = s.split()
for i, v in enumerate(rv):
    rv[i] = v.lower()
rv = '-'.join(rv)
print(args.s)

print(rv + '.py')