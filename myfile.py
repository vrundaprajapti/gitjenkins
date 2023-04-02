Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> y='yes'
... while(y=='yes' or y=='y'): 
...     print("Enter Two Number")
...     a=int(input("Frist Number"))
...     b=int(input("Second Number"))
...     print("a.add of two number")
...     print("s.sub of two number")
...     print("m.multi of two number")
...     print("d.div of two number")
...     c=input("Enter Your Choice:")
...     if(c=='a'):
...         v=a+b
...         print(v)
...     elif(c=='s'):
...         c=a-b
...         print(c)   
...     elif(c=='m'):
...         k=a*b
...         print(k)
...     elif(c=='d'):
...         l=a/b
...         print(l)
...     else:
...         print("  wrong choise enter kindly reenetr your choice")
...     y=input("repeat program? yes or no : ") 
...    
...     
...     
