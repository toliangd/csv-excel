def filelist(path):
	import os
	files = os.listdir(path)
	return files

def add_path(string, path):
	result = path + '\\' + string
	return result

def split(line, number_str):
	if number_str > 0:
		l = line.split(',"')
	else:
		l = line.split(',')
	return l

def excel(dict_out):
	import pandas as pd
	z = pd.DataFrame(dict_out)
	s = input ("путь к файлу excel: ")
	z.to_excel(s)
	return "excel"

def parse(path):
	files = filelist(path)
	d = dict() # словарь ключ-название столбца, значение-остальные колонки
	number_file = 0
	for i in files: # файлы поочереди
		number_file += 1
		if number_file == 1: # если файл первый, то берем его первую строку как шапку таблицы
			j = add_path(i, path)
			f = open(j,'r')
			number_str = 0 # номер строки в очеред
			for line in f: # смотри каждую строку файла
				if number_str == 0: # если строка первая, то используем ее значения как ключи словаря
					l = split(line, number_str)
					number_str += 1
					first_str = l # для поиска ключа в словаре по имени
					for k in l:
						d[k] = list() # словарь из наименований столбцов, значения-список
				else: # если не первая, используем как значения словаря
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

		else: # если файл не первый, то отбрасываем его первую строку
			j = add_path(i, path)
			f = open(j,'r')
			number_str = 0
			for line in f:
				l = split(line, number_str)
				number_str += 1
				if number_str == 1:
					continue
				else:
					number_column = 0
					for k in l:
						try:
							print (first_str[number_column])
							d[first_str[number_column]].append(k)
							number_column += 1
						except IndexError:
							print (number_column)
							break
	excel(d)

a = input("путь к файлам: ")
parse(a)
