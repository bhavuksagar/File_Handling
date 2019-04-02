class file:
    x=0
    def creation():                   #function for creating the file
        try:  
            print("Enter the file name with extention:")
            global x
            x=input()
            f=open( x,'w')
            print("Enter the data which you want to add in a file:")
            data=input()
            f.write(data)
            f.close()
        except Exception:
            print "Error"
  
    def reading():                    #function for reading the data from the file
        try:
            global x
            f=open(x,'r')
            print(f.read())
            f.close()
        except Exception:
            print "ERROR"
    def app():                        #Function for append the new data in existing file 
        try:
            global x
            f=open(x,'a')
            print "Enter the new data:"
            new_data=input()
            f.write(new_data)
            f.close()
        except Exception:
            print "Error"
            

obj=file
obj.creation()
obj.reading()
obj.app()
