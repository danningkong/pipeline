from email import message
import os

class ScambleText:
    # def __init__(self,msg,charlen) -> None:
    #     self.msg=msg
    #     self.charlen=charlen
    #     # msg=input("Enter setence(s): ")
    #     # msg="This is a test"
        
        

    def scambletext(message,length)->str:
        # msg=self.msg
        msg=message.split(" ")
        newmsg=""
        for i in range(len(msg)):
            char=msg[i]
            charlen=len(char)
            if charlen>length:
                char=char[charlen-1]+char[1:charlen-1]+char[0]
                
            newmsg=newmsg+" "+char
        return newmsg
    
message=input("Enter setence(s): ")
print(ScambleText.scambletext(message,3))

# scamble=ScambleText(msg=message,charlen=3)
# finaltext=scamble.scambletext()
# print(finaltext)
