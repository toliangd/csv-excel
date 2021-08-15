# split строк большого количества одинаковых по структуре файлов, представление в виде словаря и запись в таблицу
def filelist(path):
	import os
	files = os.listdir(path)
	return files

def add_path(string, path):
	result = path + '\\' + string #работает под windows, в Linux меняем разделители
	return result

def split(line, number_str):
	if number_str > 0:
		l = line.split(',"')
	else:
		l = line.split(',')
	return l

def excel(dict_out, name):
	import pandas as pd
	z = pd.DataFrame(dict_out)
	name = name.split(".")
	s = "path" + "\\" + name[0] + ".xlsx"
	z.to_excel(s)
	return "excel"

def parse(path):
	files = filelist(path)
	for i in files: # файлы поочереди	
		d = dict() # словарь ключ-название столбца, значение-остальные колонки
		j = add_path(i, path)
		f = open(j,'r')
		number_str = 0
		for line in f: # смотри каждую строку файла
			if number_str == 0: # если строка первая, то используем ее значения как ключи словаря
				l = split(line, number_str)
				number_str += 1
				first_str = l # для поиска ключа в словаре по имени
				for k in l:
					d[k] = list() # словарь из наименований столбцов, значения-список
			else: # если не первая, исползуем как значения словаря
				l = split(line, number_str)
				number_str += 1
				number_column = 0
				for k in l:
					try:
						d[first_str[number_column]].append(k)
						number_column += 1
					except IndexError:
						print('errrrroooooooooooooooooooooooooooooooooooorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr', '\n')
						continue 
		excel(d, i)

a = "path"
number_file = 0
parse(a)