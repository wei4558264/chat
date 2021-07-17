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
		print(line)
	return lines

def count_data(lines):
	amy_count = 0
	roy_count = 0
	for line in lines:
		s = line.split('\t')
		if s[1] == '王亞薇':
			for m in s[2: ]:
				amy_count += len(m)
		elif s[1] == 'Roy.Wang':
			for m in s[2: ]:
				roy_count += len(m)
	print("王亞薇說了", amy_count, '個字')
	print("Roy.Wang說了", roy_count, '個字')




def write_in(filename,lines):
	with open(filename, 'w',encoding='utf-8-sig')as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_in('chat2.txt')
	#lines = re_do(lines)
	count_data(lines)
	

	#write_in('new_chat.txt', lines)


main()
