# -*- coding: utf-8 -*- 
# 类化，以备模块

"""创建一个类"""
class national_list_name (object):

    def __init__(self, fn='data/national.tsv'):
       import csv
       with open(fn, 'r', encoding='utf8') as csvfile:
           reader = csv.DictReader(csvfile, fieldnames=['c_code', 'c_name'], delimiter='\t')
           fieldnames = reader.fieldnames

           list_dict_national = []
           for row in reader:
                  list_dict_national.append(dict(row))

           self.data = {d['c_code']:d['c_name'] for d in list_dict_national}

    def national_name(self, c_code=''):
        c_name =  self.data.get(c_code, None)
        return (c_name)

