class mustangBroncoTest():
    def __init__(self):
        print("check")
        if self.Test1() and self.Test2() and self.Test3() and self.Test4() and self.Test5() and self.Test6() and self.Test7() and self.Test8() and self.Test9() and self.TestA() and self.TestB() and self.TestC():
            print("Internal test cases passed")
    def Test1(self):
        return mustangBroncoLogic("0") == "MustangBronco"
    def Test2(self):
        return mustangBroncoLogic("7") == 7
    def Test3(self):
        return mustangBroncoLogic("-7") == -7
    def Test4(self):
        return mustangBroncoLogic("3") == "Mustang"
    def Test5(self):
        return mustangBroncoLogic("-3") == "Mustang"
    def Test6(self):
        return mustangBroncoLogic("5") == "Bronco"
    def Test7(self):
        return mustangBroncoLogic("-5") == "Bronco"
    def Test8(self):
        return mustangBroncoLogic("10") == "Bronco"
    def Test9(self):
        return mustangBroncoLogic("-10") == "Bronco"
    def TestA(self):
        return mustangBroncoLogic("15") == "MustangBronco" 
    def TestB(self):
        return mustangBroncoLogic("-15") == "MustangBronco"
    def TestC(self):
        return mustangBroncoLogic("17.0") == "ERROR: Invalid input (potentially non-integer), please try again"
        
        
        
def mustangBroncoLogic(user_input):
        try:
            user_input = int(user_input)
        except ValueError:
            output = "ERROR: Invalid input (potentially non-integer), please try again"
            return output
        if (user_input % 3 == 0) and (user_input % 5 == 0):
            output = "MustangBronco"
        elif user_input % 3 == 0:
            output = "Mustang"
        elif user_input % 5 == 0:
            output = "Bronco"
        else:
            output = user_input
        return output
        
        
mustangBroncoTest()

