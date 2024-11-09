import Pager as API_Interface
API=API_Interface.Pager()

# Convert The Given Hex String to the Base Station & Pager Number
Station,Pager=API.Convert_Hex_To_Station_And_Pager("280022")
Action='0010'
API.Calculate_Number_To_Hex(Station,Pager,Action)

# DrGecko 2024 
