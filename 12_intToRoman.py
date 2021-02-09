class Solution:
    def intToRoman(self, num: int) -> str:
        
        int_roman_mapping = {
            1000 : 'M',
            900 : 'CM',
            500 : 'D',
            400 : 'CD',
            100 : 'C',
            90 : 'XC',
            50 : 'L',
            40 : 'XL',
            10 : 'X',
            9 : 'IX',
            5 : 'V',
            4 : 'IV',
            1 : 'I',
        }
        
        ret = ""
        
        for val, roman in int_roman_mapping.items():
            q = num // val
            r = num % val
            
            ret += q*roman
            num = r
            
        return ret 
        
