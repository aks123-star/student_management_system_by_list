import sys
li=[["ROLL_NO",1,2,3,4],["name","a","b","c","d"],["phone",123,234,345,456],["marks",10,20,30,40]]
s=5
for i in range(0,s):
    print(str(li[0][i])+"\t\t"+str(li[1][i])+"\t\t"+str(li[2][i])+"\t\t"+str(li[3][i]))
    
        
        

print("""
          for insertion press---------- 1
          for display press----------2
          for edit a particular student record press---------- 3
          for display record by roll number pres---------- 4
          for delete any particular student record press---------- 5
          for exit press---------- 6
                                     """)


while(1):
     choice=int(input("enter your choice: "))
     if choice==1:
         r=int(input("enter roll number: "))
         if r in li[0]:
             print("record already exist")
        
         else:
             s+=1
             li[0].append(r)
             n=input("enter name: ")
             li[1].append(n)
             p= input("enter phone no: ")
             li[2].append(p)
             m=input("enter marks: ")
             li[3].append(m)
     
         for i in range(0,s):
             print(str(li[0][i])+"\t\t"+str(li[1][i])+"\t\t"+str(li[2][i])+"\t\t"+str(li[3][i]))
            

     if choice==2:
         for i in range(0,s):
             print(str(li[0][i])+"\t\t"+str(li[1][i])+"\t\t"+str(li[2][i])+"\t\t"+str(li[3][i]))

     if choice==3:
         r=int(input("enter the roll no: "))
         if r not in li[0]:
             print("record not found")

         else:
             x=li[0].index(r)
             n=input("enter name: ")
             li[1][x]=n
             p=input("enter hone number")
             li[2][x]=p
             m=input("enter marks: ")
             li[3][x]=m
             #li[1].pop(x+1)
             
         for i in range(0,s):
             print(str(li[0][i])+"\t\t"+str(li[1][i])+"\t\t"+str(li[2][i])+"\t\t"+str(li[3][i]))

     if choice==4:
         r=int(input("enter roll number: "))
         if r not in li[0]:
             print("record not found")

         else:
             x=li[0].index(r)
             for i in range(0,4):
                 print(str(li[i][0]),str(li[i][x]))

     if choice==5:
         r=int(input("enter roll number for delete: "))
         if r not in li[0]:
             print("record not find")
         else:
             s=s-1
             x=li[0].index(r)
             li[0].pop(x)
             li[1].pop(x)
             li[2].pop(x)
             li[3].pop(x)
         for i in range(0,s):
             print(str(li[0][i])+"\t\t"+str(li[1][i])+"\t\t"+str(li[2][i])+"\t\t"+str(li[3][i]))
            

     if choice==6:
         print("exit")
         sys.exit()

     if choice>=7:
         print("invalid choice")












            

    
         
     




             
            

         
        
    
    
        
    

    
    
