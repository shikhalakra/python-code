
''' Read inputSTDIN. Print your output to STDOUT '''
    #Use input() to read inputSTDIN and use print to write your output to STDOUT

def main():
    n=int(raw_input())
    for i in xrange(0,n):
        for j in xrange(0,n-i-1):
            print " ",
        for k in xrange((2*i)+1,0,-1):
            if k!=1:
                print (chr(k+64)),
            else:
                print (chr(k+64))
        
        
            
            
        
 # Write code here 

main()