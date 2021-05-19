"""
Corner Cases:
- timewrap? no
"""
BANK_LIST = []
class Bank():
    def __init__(self,start=0,end=0):
        self.start = start
        self.end = end
        BANK_LIST.append(self)

    @classmethod
    def are_banks_trading(cls,start:int,end:int):
        for b in BANK_LIST:
            if b.start <= start and start < b.end:
                start = b.end
                if end < b.end:
                    return True
        return False


    
rbs = Bank(9,16)
ms = Bank(11,17)
jpm = Bank(14,20)
nab = Bank(2,7)

print(Bank.are_banks_trading(10,17))
print(Bank.are_banks_trading(15,21))
print(Bank.are_banks_trading(4,10))

