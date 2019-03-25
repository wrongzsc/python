# ***
# @Encoding: utf-8
# @Author: wrong.zsc
# @Date: 2018-04-11 17:52:19
# @Last Modified time: 2018-04-11 17:52:19
# ***

# read file from txt sep by tab
import pandas as pd
import os

print(os.getcwd())
print(os.listdir())
os.chdir('C:/Users/zheng/OneDrive/Python/code/ToniBatch/')
print(os.getcwd())

Rawdata = pd.read_table("180410liuyang.txt", sep="\t")
m = 0
