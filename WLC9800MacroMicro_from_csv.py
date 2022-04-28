#!/usr/bin/env python3
# CLI syntax to set APs in Dual Band Clientserving mode
# CSV from WLC used as input
#
# Kristian Winckler - 20220427 - Version 1.0
# kristian.winckler@atea.se
#
# IOS-XE (WLC9800)
# ap name <CSV-COL1> dot11 dual-band shutdown
# ap name <CSV-COL1> dot11 dual-band role manual client-serving
# ap name <CSV-COL1> dot11 dual-band slot 0 band 5
# ap name <CSV-COL1> no dot11 dual-band shutdown

import csv
file_input = 'ap-input.csv'
file_output = 'ap-output-from-csv.txt'

output = open(file_output, 'a+')

with open(file_input) as aplist:
    csv_reader = csv.reader(aplist, delimiter=';')
    aplist.readline()
    line_count = 0
    for line in csv_reader:
#       output.write('! ' + line[0] + '\n')
        output.write('ap name ' + line[0] + ' dot11 dual-band shutdown' + '\n')
        output.write('ap name ' + line[0] + ' dot11 dual-band role manual client-serving' + '\n')
        output.write('ap name ' + line[0] + ' dot11 dual-band slot 0 band 5' + '\n')
        output.write('ap name ' + line[0] + ' no dot11 dual-band shutdown' + '\n')
        line_count += 1
output.close()
print(f'{line_count} APs created.')