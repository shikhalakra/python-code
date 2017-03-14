
''' Read inputSTDIN. Print your output to STDOUT '''
    #Use input() to read inputSTDIN and use print to write your output to STDOUT

def main():
    n=int(raw_input())
    for i in xrange(0,n):
        for j in xrange(0,n-i-1):
            print " ",
        for k in xrange(0,i+1):
            print (k+1),
        for l in xrange(0,i-1):
            print (l+1),
        print ""
        
        
            
            
        
 # Write code here 

main()