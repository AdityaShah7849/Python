# class Subject:
#     def c(self):
#         a="C "

#     def py(self):
#         d="pythone"

class Bank:
    def getROI(self):
        print("8%")

class HDFC(Bank):
    def homeLoan(self):
        print("Good bank for home loan")

    # Here we are doing method overriding
    def getROI(self):
        print("9.5%")

    # Like other languages (for example method overloading in C++) do, 
    # python does not supports method overloading. 
    # We may overload the methods but can only use the latest defined method.

    # https://www.geeksforgeeks.org/python-method-overloading/
    # https://www.quora.com/Why-isnt-method-overloading-supported-in-Python

    def sum(self, sum1, sum2):
      print("Method 1")
    
    # def sum(self, a, b,c) :
    #     print("Method 2")
        
class ICICI(Bank):
    
    def credi_card(self):

         print("Credit card facility...")

obj = HDFC()
# obj.getROI()

obj.sum(2,5)
# obj.sum(5,10,15)

