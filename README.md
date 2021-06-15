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

- **SavaPath**: "savepath", "sp", "logsp", "logsavePath"<br/>
  This parameter is the **Log Directory** and is optional, and same as previus parametes You may use (parameter, -parameter, --parameter)=value
	
	> For example:
	>   - `XlsToCsv.py input=C:\XlsToCsv\test.xls logsp=C:\XlsToCsvLogs`
	>   - `XlsToCsv.py --xls=C:\XlsToCsv\test.xls --sp=C:\XlsToCsvLogs`

	***If the output value is empty or not provided, it will be saved in a subfolder where the program is running.***<br/><br/>

- **Verbosity**: "verbosity", "verb", "vl", "v", "lv"<br/>
  This parameter is the **Log Verbosity** and is optional, and same as previus parametes You may use (parameter, -parameter, --parameter)=value[1-3]
	
	> For example:
	>   - `XlsToCsv.py input=C:\XlsToCsv\test.xls verb=2`
	>   - `XlsToCsv.py --xls=C:\XlsToCsv\test.xls --v=2`

	***This parameter is*** **2** ***by default.***<br/><br/>
	
# Made by
    First than all sorry for the spanglish and soryy if my english is too bad, i'm trying to learn 🥰.
    Program maid by **Funkyo Alejandra** -2021

## Social Networks

    **Disclaimer**
    - I usualy speak spanish
    - I'm a 🏳‍⚧(Trans) Girl 🥰
    **end of the disclaimer**
    
    All my social networks: https://linktr.ee/FunkyoEnma
    
