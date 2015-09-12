"""
Takes raw points and calculates positional draft order as:
    points - sum_top / n + drop
or more specifically:
    VOR + drop
"""

POS = ['K', 'DST', 'QB', 'RB', 'WR', 'TE']

def read_stats(pos):
    res = {'Name': [], 'Risky': [], 'Points': [], 'Drop': []}
    print(pos)

    with open('../data/%s.csv' % (pos), 'r') as f_in:
        for line in f_in:
            line = line.strip()
            if line == '':
                continue

            print(line)

            parts = line.split(',')

            res['Name'].append(parts[0])
            res['Risky'].append(parts[1])
            res['Points'].append(float(parts[2]))
            res['Drop'].append(float(parts[3]))

    print('')
    return res

def calc_value(stats):
    res = {'Name': [], 'Risky': [], 'Score': []}

    avg = sum(stats['Points']) / len(stats['Points'])

    for i in range(len(stats['Name'])):
        res['Name'].append(stats['Name'][i])
        res['Risky'].append(stats['Risky'][i])
        res['Score'].append(stats['Points'][i] - avg + stats['Drop'][i])
    
    return res

def write_value(pos, stats):
    with open('../data/clean_%s.csv' % (pos), 'w') as f_out:
        for i in range(len(stats['Name'])):
            f_out.write('%s,%s,%f\n' % (stats['Name'][i], stats['Risky'][i], stats['Score'][i]))

def main():
    stats = {}
    value = {}
    for pos in POS:
        stats[pos] = read_stats(pos)
        value[pos] = calc_value(stats[pos])
        write_value(pos, value[pos])

if __name__ == '__main__':
    main()

