def strat1(x, mod):
	seq = [1,2]
	while seq[len(seq)-1]+seq[len(seq)-2] <= x:
		seq.append(seq[len(seq)-1]+seq[len(seq)-2])
	return sum([i for i in seq if i % mod == 0])

print strat1(4000000, 2)


