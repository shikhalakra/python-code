
''' Read inputSTDIN. Print your output to STDOUT '''
    #Use input() to read inputSTDIN and use print to write your output to STDOUT

def main():
    n=int(raw_input())
    for i in xrange(0,n):
        for j in xrange(0,n-i-1):
            print " ",
        for k in xrange(0,(2*i)+1):
            if k!=(2*i):
                print (k+1),
            else:
                print (k+1)
        
        
            
            
        
 # Write code here 

main()