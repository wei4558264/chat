import os
def read_in(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def re_do(lines):
	newdata = []
	person = None
	for line in lines:
		if line =='Tom':
			person = 'Tom'
			continue
		elif line == 'Allen':
			person = 'Allen'
			continue
		if person:
			newdata.append(person+ ': '+line )
	return newdata


def write_in(filename,lines):
	with open(filename, 'w',encoding='utf-8-sig')as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_in('input.txt')
	print(lines)
	lines = re_do(lines)
	print(lines)
	write_in('new_chat.txt', lines)


main()
