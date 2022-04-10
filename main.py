from match import match_list

with open("inputs.csv", "r") as f:
    names = [(l.split('\t')[0], i) for i, l in enumerate(f.readlines())]

merged = match_list(names)

with open("outputs.csv", "w") as f:
    for n, keys in merged.items():
        f.write(n + '\t' + ', '.join([str(k) for k in keys]) + '\n')
