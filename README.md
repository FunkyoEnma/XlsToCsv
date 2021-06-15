XLS TO CSV CONVERTER

This program converts a file in Xls format to Csv Format

# How to use
## execution params

 - **Input**: "input" "in", "xls", "i", "entrada"<br/>
   This parameter needs the original file in Xls format, You may use     	(parameter, -parameter, --parameter)=value
	 > For example:
	 > - `XlsToCsv.py input=C:\XlsToCsv\test.xls`
	 > - `XlsToCsv.py --xls=C:\XlsToCsv\test.xls`
		 
	***This parameter is mandatory***<br/><br/>

- **Output**: "output", "out", "csv", "o", "salida"<br/>
  This parameter is the output **Directory** and is ***Optional***, same as Input You may use (parameter, -parameter, --parameter)=value

	> For example:
	>   - `XlsToCsv.py input=C:\XlsToCsv\test.xls output=C:\CsvFiles`
	>	 - `XlsToCsv.py --xls=C:\XlsToCsv\test.xls --csv=C:\CsvFiles`
	
	***If the output value is empty or not provided, it will be saved in a subfolder where the program is running.***<br/><br/>

- **Save**: "save", "saving", "s", "loggging", "log", "l"<br/>
	This parameter is used to know if you want to save the **log** file and is ***Optional***, and same as previus parametes You may use (parameter, -parameter, --parameter)=value[True or False]
	
	> For example:
	>   - `XlsToCsv.py input=C:\XlsToCsv\test.xls logging=True`
	>	 - `XlsToCsv.py --xls=C:\XlsToCsv\test.xls --log=True`
	
	***This parameter is*** **False** ***by default.***<br/><br/>
