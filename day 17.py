 import re
print(dir(re))
#re.match


result=re.match(r'raju','raju is good boy')
print(result)
print(result.group(0))
print(result.start())
print(result.end())
result=re.match(r'ravi','raj is good boy')
print(result)
result=re.match(r'rani','raju is good boy')
print(result)
#re.search
result1=re.search(r'raju','raju is good boy')
print(result1)
result1=re.search(r'raju','raju is good,raju is bad')
print(result1)
#re.findall
result2=re.findall(r'raju','raju is  good,raju is bad')
print(result2)

result2=re.findall(r'ravi','raju is  good,raju is bad')
print(result2)
#re.spilt
s='python programming'
result3=re.split(r'a',s)
print(result3)
#re.sub
s1='python programming language'
result4=re.sub(r'p',r'l',s1)
print(result4)
s1='python programming language'
result4=re.sub(r'python',r'java',s1)
print(result4)
#re.compile
pattern=re.compile('python')
result5=pattern.findall('hello python,python program')
print(result5)
pattern=re.compile('hello')
result5=pattern.findall('hello python,python program')
print(result5)
pattern=re.compile('p')
result5=pattern.findall('hello python,python program')
print(result5)
#charecter clases
result6=re.findall('\s','hello python,python program')
print(result6)
result6=re.findall('\S','hello python,python program')
print(result6)
result6=re.findall('\d','hello python,python program')
print(result6)
result6=re.findall('\d','hello python2,python program4')
print(result6)
result6=re.findall('\D','hello python2,python program4')
print(result6)
result6=re.findall('\D','hello python2,python4 program')
print(result6)
result6=re.findall('\w','hello python2,python4 program')
print(result6)
result6=re.findall('\w','hello python,python program')
print(result6)
result6=re.findall('\W','hello python2,python4 program')
print(result6)
result6=re.findall('[^a-m]','hello python2,python4 program')
print(result6)
result6=re.findall('[a-m]','hello python,python program')
print(result6)









