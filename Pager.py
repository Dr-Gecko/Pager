class Pager:
    def Binary_To_Decimal(self, bits): # Converts a binary string to decimal representation 
        return int(bits, 2)

    def Hex_To_Bin(self, hex_str): # Convert hex string to binary
        return bin(int(hex_str, 16))[2:].zfill(24).upper()

    def Binary_To_Hex(self, bits): # Convert binary string to hex
        return hex(int(bits, 2))[2:].upper().zfill(6)
    
    def Invert(self,bits): # Invert the string
        return ''.join(str(1 - int(b)) for b in bits)

    def Reverse(self,bits): # Reverse the string
        return bits[::-1]
    
    def Decimal_To_Binary(self, num, length): # Decimal To bibnary
        Result=bin(num)[2:]
        return Result.zfill(length) 
    
    def Generate_Key_Data(self,hex_value):
        Formatted = ' '.join([hex_value[i:i+2] for i in range(0, len(hex_value), 2)]).strip()
        return f"Key: {Formatted}\n"

    def Calculate_Number_To_Hex(self,Station,Pager,Action): # Calculate the Station+Pager+Action and convert it to hex
        # Convert The station to to binary
        Station = self.Decimal_To_Binary(Station, 10);
        Pager = self.Decimal_To_Binary(Pager, 10);
        Hex_String=str(self.Binary_To_Hex(Station + Pager + Action)).zfill(16)
        Hex_String="Key: "+" ".join([Hex_String[i:i+2] for i in range(0, len(Hex_String), 2)])+'\n'
        self.Generate_Key_File(Station,Pager,Hex_String)

    def Generate_Key_File(self,Station,Pager,Key_Data):
        Header = 'Filetype: Flipper SubGhz Key File\nVersion: 1\nFrequency: 433920000\nPreset: FuriHalSubGhzPresetOok650Async\nProtocol: Princeton\nBit: 24\n'
        Footer = 'TE: 212\n'
        with open(f"{Station}-{Pager}.sub", 'w') as Key_File:
            Key_File.write(Header+Key_Data+Footer)
        Key_File.close()
        return f"Saved At: {Station}-{Pager}.sub"
      
 
 
 
    def Convert_Hex_To_Station_And_Pager(self,Hex_String):
        print('Converting Hex String to Base Station & Pager Number')
        # Convert the hex to binary
        print('\t1. Converting Hex String to Binary')
        Binary_String=self.Hex_To_Bin(Hex_String)
        print(f'\t Binary String: {Binary_String}')
        # First get the Base Station
        print('\t2. Get Base Station Number')
        Base_Binary_String=Binary_String[0:10]
        print(f'\t Base Station Binary: {Base_Binary_String}')
        Base_Station=self.Binary_To_Decimal(Base_Binary_String)
        print(f'\t Base Station Number: {Base_Station}')
        # Next Get The Pager Number
        print('\t3. Get Pager Number')
        Pager_Binary_String=Binary_String[10:20]
        print(f'\t Pager Binary String: {Pager_Binary_String}')
        Pager_Number=self.Binary_To_Decimal(Pager_Binary_String)
        print(f'\t Pager Number: {Pager_Number}')
        return Base_Station,Pager_Number