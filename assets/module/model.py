import assets.message.MessageManage as Msg
import assets.feature.feature as feature
import assets.module.judge as judge

class ModuleModel:
    def __init__(self):
        self.locate = feature.Switch().userLocate()
        self.doPath = None 
        self.check = False
        self.type = "ALL" 
        self.size = (100,100)

    def modelLoop(self):
        # try:
            Msg.Message.sucMessage(1)
            
            while 1:
                self.doPath = input("> Enter Address : ({:8}) ".format(self.locate)) # 做例外處理
                self.doPath = judge.Appropriate(self.doPath,self.locate).checkType()
                self.type = input("> Enter Type : (ALL) ") 
                self.type = judge.Appropriate(self.type,"ALL").checkType()
                self.size = input("> Enter Size : (100x100) ")
                self.size = judge.Appropriate(self.size,(100,100))

                # do image deal with 
                feature.Switch().tryTest(self.doPath)
                Msg.Message.msgMessage(3,"path: {:10} , type: {:10} , size: {:10}".format(self.doPath,self.type,str(self.size)))

        # except:
        #     print("\nfinally")
            