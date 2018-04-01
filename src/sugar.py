class TestClass:         # 类的定义
    DESCRIPTION = "class introduction of sample"  # 类变量，可直接通过类名调用
    __test = "test"      # 属于私有，不可在类外部直接调用以“__”开头
    _single = "single"   # 属于私有,不可使用from module import *导入使用

    def __init__(self, name):
        '测试类'        # 注释文档
        self.name = name  # 通过self可以创建类的实例变量
        print(TestClass.__test)
        print(TestClass._single)

    def getName(self):  # 类的成员方法
        return self.name

    def __getName(self):  # 类的私有方法
        return TestClass._single

    @staticmethod
    def getsingle():   # 类的静态方法
        return TestClass.__test


print(TestClass.DESCRIPTION)

print(TestClass.getsingle())

test = TestClass("sample")
print(test.name)
print(test.getName)
print(TestClass.getName)
