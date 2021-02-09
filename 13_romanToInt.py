class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_mapping = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        ret = 0
        cur, pre = float('inf'), float('inf')
        
        for c in s:
            cur = roman_int_mapping[c]
            if cur > pre:
                ret += cur - 2 * pre
            else:
                ret += cur
            pre = cur
        
        return ret
            
