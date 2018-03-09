import assets.message.MessageManage as Msg 

class Appropriate:
    def __init__(self,item,locate):
        self.item = item
        self.locate = locate

    def checkType(self):
        return self.emptyReport() if self.item == "" or self.item == self.locate else self.checkTrue()
    
    def checkTrue(self):
        return self.resultReport() # 需要增加判斷

    def emptyReport(self):
        return self.locate

    def resultReport(self):
        return self.item