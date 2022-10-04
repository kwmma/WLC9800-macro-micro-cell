# Cisco WLC Catalyst 9800 macro/micro cell
Use a CSV file with AP names as input to get CLI syntax to setup APs for Macro Micro cell configuration. Python script.

Input file: ap-input.csv
Output file: ap-output-from-csv.txt

The file ap-input.csv should be placed in the same folder as the python script. 

After the script has run the file ap-output-from-csv.txt is created in the same folder.

The file ap-input.csv provided is from an export inside the WLC Gui (Monitoring -> Wireless -> AP Statistics). The scripts reads from the first column skiping the first row. You can build the file any way you want and not necessarily export it from the WLC.


Kristian Winckler

C9800 Catalyst XOR
