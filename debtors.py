#!/usr/bin/env python

__author__ = 'avs'

fileName = input('Введите путь до файла:')
fin = open(fileName, 'r')

lines = fin.readlines()
table_exp = '''<table id="debtors">
<thead>
<tr>
<th>№ уч.</th>
<th>Долг за предыд. периоды</th>
<th>Взносы за 2015</th>
<th>Итого</th>
</tr>
</thead>
<tbody>'''

for line in lines:
    tds = line.split('#')
    table_exp += '''<tr>
    <td>''' + tds[0] + '''</td>
    <td>''' + tds[1] + '''</td>
    <td>''' + tds[2] + '''</td>
    <td>''' + tds[3] + '''</td>
    </tr>'''

table_exp += '</tbody></table>'

fout = open( 'exp_debtors.txt', 'w' )
fout.write( table_exp )
