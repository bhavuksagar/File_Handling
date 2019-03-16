class file:
    x=0
    def creation():                   #function for creating the file
      print("Enter the file name with extention:")
      global x
      x=input()
      f=open( x,'w')
      print("Enter the data which you want to add in a file:")
      data=input()
      f.write(data)
  
  
    def reading():                    #function for reading the data from the file
        global x
        f=open(x,'r')
        print(f.read())
    
obj=file
obj.creation()
obj.reading()
