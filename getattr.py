class A:

    def _a(self):
        print("a") 

    def _b(self):
        print("b") 

    def call(self, type="a"):
        f = getattr(self, "_"+type)
        f() 



obj = A() 
obj.call("a")
obj.call("b")
obj.call()
