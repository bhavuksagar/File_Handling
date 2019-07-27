class file: 
  def creation():                   #function for creating the file  
    f=open("abc.txt",'w')
    f.write("hello it is a text file")
  
  
  def reading():                    #function for reading the data from the file
    f=open("abc.txt",'r')
    print(f.read())
  
#creating object of class and calling the function
obj=file
obj.creation()
obj.reading()
