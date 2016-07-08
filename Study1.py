#-*-coding:uft-8-*-
import re

f = open('C:/Users/Bob.Yao/Python/CFR.log','r')
lines = f.readlines()
f.close()

#打印出所有的'CAPC(ID 8615)', 'SCNL(ID 8578)', 'SCNL(ID 8577)', 'SNL(ID 8732)', 'MCAPC(ID 8732)', 'MCAPC(ID 8577)', 'MCAPC(ID 4410)'
result = []
for line in lines:
    m = re.search("\w{3,5}\(ID\s\d{4}\)", line)
    if m:
        n = m.group(0)
        result.append(n)
        #print (n)
print (result)   

#打印出所有的'CAPC', 'SCNL', 'SCNL', 'SNL', 'MCAPC', 'MCAPC', 'MCAPC'
element_result = []
for element in result:
    element_pre = re.search("\w{3,5}", element)
    if element_pre:
        element_pre_value=element_pre.group(0)
        element_result.append(element_pre_value)
print (element_result)     

#去重复得到'CAPC', 'SCNL', 'MCAPC', 'SNL'
element_without_duplicate = list(set(element_result))
print (element_without_duplicate)

#统计次数 出现大于一次的才留下SCNL MCAPC
print ('\n')
final_result=[]
for index in element_without_duplicate:
    number = element_result.count(index)
    if number > 1:
        final_result.append(index)
        print (index)