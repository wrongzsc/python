# ***
# @Encoding: utf-8
# @Author: wrong.zsc
# @Date: 2018-04-11 01:06:33
# @Last Modified time: 2018-04-11 01:06:33
# ***


class Person:
    def __init__(self, name):
        self.name = name

    def sayhi(self):
        print("helloA,my name is", self.name)


p = Person('wrongzsc')
p.sayhi()
