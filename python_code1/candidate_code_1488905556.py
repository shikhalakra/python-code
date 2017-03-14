
''' Read inputSTDIN. Print your output to STDOUT '''
    #Use input() to read inputSTDIN and use print to write your output to STDOUT

def main():
    n=int(raw_input())
    for i in xrange(0,n):
        for j in xrange(0,n-i-1):
            print " ",
        for k in xrange(i,-1,-1):
            if (i!=0):
                print (chr(k+65)),
            else:
                print (chr(k+65))
        for l in xrange(0,i):
            if (l!=i-1):
                print (chr(l+66)),
            else:
                print (chr(l+66))

 # Write code here 

main()