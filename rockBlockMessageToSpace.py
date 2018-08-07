import rockBlock
 
from rockBlock import rockBlockProtocol
 
class mtExample (rockBlockProtocol):
    
    def main(self):
        
        rb = rockBlock.rockBlock("/dev/ttyUSB0", self)
             
        rb.requestMessageCheck()
                                                                  
        rb.close()
           
    def rockBlockRxStarted(self):
        print("rockBlockRxStarted")
        
    def rockBlockRxFailed(self):
        print("rockBlockRxFailed")
        
    def rockBlockRxReceived(self,mtmsn,data):
        print(f"rockBlockRxReceived {mtmsn} {data}")
        
    def rockBlockRxMessageQueue(self,count):
        print(f"rockBlockRxMessageQueue {count}")
             
        
if __name__ == '__main__':
    mtExample().main()