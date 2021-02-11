class Person :
    hair = "back"
    def __init__ (self, name = 'Charlie', age = 8):
        self.name = name;
        self.age = age;
    def say (self, content) :
        print(content)
    @classmethod
    def sayClass (cls) :
        print("我是类方法")
    def getSize (self) :
        print(self.width, self.height);
    def setSize (self, size) :
        self.width, self.height = size;
    def deleteSize (self) :
        self.width = 10;
        self.height = 120;
    size = property(getSize, setSize, deleteSize, "我是说明size");

p = Person();
print(p.name, p.age);
p.name = '李刚'
p.say("python很简单")
Person.sayClass()
print(p.name, p.age);

def A (fn):
    print("打印")
    fn()
    print("A结束")
    return "aaa"

@A
def B () :
    print("B");

print(B);
p.size = 10, 20;
print(p.size);
del p.size
print(p.width)
print(p.height)