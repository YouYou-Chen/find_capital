# -*- coding: utf-8 -*- 
# 函数化，以备import 调用模块（module）

def get_National_GDP_name(fn='data\National_GDP.tsv'):
   import csv
   with open(fn, 'r', encoding='utf8') as csvfile:
       reader = csv.DictReader(csvfile, fieldnames=['c_code', 'c_name'], delimiter='\t')
       fieldnames = reader.fieldnames

       list_dict_National_GDP = []
       for row in reader:
          list_dict_National_GDP.append(dict(row))

       data = {d['c_code']:d['c_name'] for d in list_dict_National_GDP}
   return(data)

def country_name(c_code=''):
    d = get_National_GDP_name()
    c_name =  d.get(c_code, None)
    return (c_name)

#測試   
print (_name('CN'))
print (National_GDP_name('SG'))
print (National_GDP_name('ZZ'))
print (National_GDP_name('ABC'))
print (National_GDP_name(''))
