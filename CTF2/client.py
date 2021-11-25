import os
import pickle
import base64
def fun(name,password):
    global x
    y=base64.b64decode(x).decode("utf-8")
    z=base64.b64encode(y.encode("utf-8"))
    s = {"username":name,"password":z}
    safecode = pickle.dumps(s)
    with open("users.json","wb") as f:
        f.write(safecode)
    return safecode

if __name__ == '__main__':
    u = input("Username : ")
    p = input("Password : ")
    x=base64.b64encode(p.encode("utf-8"))
    yo_fun = fun(u,p)
