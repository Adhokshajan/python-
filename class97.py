
introstring=input("enter your intro ")
charatercount=0
wordcount=1

for i in introstring:
        charatercount= charatercount+1
        if( i == ' '):
                wordcount=wordcount+1

                
print(wordcount)
print(charatercount)


        