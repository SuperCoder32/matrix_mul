def transpose(M):
	return [list(col) for col in zip(*M)]


def _str_add_vecs(*vecs):
	return ['+'.join(dim) for dim in transpose(vecs)]

def _int_add_vecs(*vecs):
	return [sum(dim) for dim in transpose(vecs)]

def add_vecs(*vecs):
	if isinstance(vecs[0][0], str):
		return _str_add_vecs(*vecs)
	elif isinstance(vecs[0][0], int):
		return _int_add_vecs(*vecs)


def _str_scale_vec(s, vec):
	return [''.join(sorted([s, n])) for n in vec]

def _int_scale_vec(s, vec):
	return [s * n for n in vec]

def scale_vec(s, vec):
	if isinstance(s, str):
		return _str_scale_vec(s, vec)
	elif isinstance(s, int):
		return _int_scale_vec(s, vec)


def linear_trans(M, vec):
	return add_vecs(*(scale_vec(coord, basis) for basis, coord in zip(M, vec)))


def mul_matrices(M1, M2):
	d1 = len(M1)
	d2 = len(M2)

	if d1 != d2:
		raise ValueError("Matrices have different dimensions")

	return [linear_trans(M1, vec) for vec in M2]


def get_matrix(d, numerical=False):
	tipe = int if numerical else str

	M = []
	for i in range(d):
		M.append([tipe(val) for val in input().split()])

	return M

d = int(input("Number of dimensions: "))
n = input("Numerical? :") == "y"

M1 = transpose(get_matrix(d, n))
M2 = transpose(get_matrix(d, n))

ret = mul_matrices(M1, M2)
ret = transpose(ret)

for line in ret:
	print(' '.join(str(x) for x in line))

#print(ret)