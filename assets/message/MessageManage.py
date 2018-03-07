import assets.message.errMessage as errMessage
import assets.message.sucMessage as sucMessage
import assets.message.msgMessage as msgMessage 

class Message:
    def msgMessage(number,txt=""):
        return msgMessage.message(number,txt)
    
    def errMessage(number,txt=""):
        return errMessage.error(number,txt)

    def sucMessage(number,txt=""):
        return sucMessage.success(number,txt)
