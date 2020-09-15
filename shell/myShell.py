
import os, sys, re

a = os.environ.get('$PS1') #value of PS1
pID = os.getpid()
rc = os.fork()

while(1):
    
    if (a == None):
        temp = input("$ ")
        print("here 1")
    
    if (rc < 0):
        print("here 2")
        os.write(2, ("Fork failed, returning %d\n" %rc).encode())
        sys.exit(1)

    if (rc == 0):
        print("here 3")
        os.write(1, ("Child: My pid==%d. Parent's pid=%\n"%
                     (os.getpid(), pID)).encode())
        print("hi")
        args = [temp, "myShell.py"]

        for dir in re.split(":", os.eniron['PATH']):
            print("here 4")
            program = "%s%s" % (dir, args[0])

            os.write(1, ("Child: ...trying to exec %s\n" % program).encode())

            try:
                os.execve(program, args, os.environ)

            except FileNotFoundError:
                pass


        os.write(2, ("Child:  Could not exec %s\n"%args[0].encode()))
        sys.exit(1)

                
