import assets.message.MessageManage as Msg

class ModuleModel:
    def __init__(self):
        self.locate = None 
        self.check = False
        self.type = "ALL" 

    def modelLoop(self):
        # try:
            Msg.Message.sucMessage(1)
            while 1:
                self.locate = input("> Enter Address : (/) ")
                self.type = input("> Enter Type : (ALL) ")
                Msg.Message.msgMessage(1)

        # except:
        #     print("\nfinally")
            