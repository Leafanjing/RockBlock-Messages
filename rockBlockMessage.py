import rockBlock

from rockBlock import rockBlockProtocol

class MoExample (rockBlockProtocol):
    
    def main(self):

        userString = input('Enter the message RockBlock will send to the Irdidium Satellite Network\n')

        rb = rockBlock.rockBlock("/dev/ttyUSB0", self)
        
        rb.sendMessage(userString)

        rb.close()
        
    def rockBlockTxStarted(self):
        print("rockBlockTxStarted")
        
    def rockBlockTxFailed(self):
        print("rockBlockTxFailed")
        
    def rockBlockTxSuccess(self, momsn):
        print(f"rockBlockTxSuccess {momsn}")

if __name__ == '__main__':
    MoExample().main()