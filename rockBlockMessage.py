import rockBlock

from rockBlock import rockBlockProtocol

class MoExample (rockBlockProtocol):
    
    def main(self):

        userInput = input('Enter the message RockBlock will send to the Irdidium Satellite Network')
        
        rb = rockBlock.rockBlock("/dev/ttyUSB0", self)
        
        rb.sendMessage(userInput)      
        
	    rb.close()
        
    def rockBlockTxStarted(self):
        print "rockBlockTxStarted"
        
    def rockBlockTxFailed(self):
        print "rockBlockTxFailed"
        
    def rockBlockTxSuccess(self,momsn):
        print "rockBlockTxSuccess " + str(momsn)
        
if __name__ == '__main__':
    MoExample().main()