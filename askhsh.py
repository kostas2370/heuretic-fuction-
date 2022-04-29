import numpy as np

def h(x,y):
        
        return (x**2)+(y**2)-(3*x*y)+(5*x)+(7*y)-2
        #return x**2+y**2
def geitonia(state):
        x,y=state
        p=0.001
        geitonia={(x, y - p):h(x, y - p),
                  (x, y + p):h(x, y + p),
                  (x - p, y):h(x - p, y),
                  (x + p, y):h(x + p, y),
                  (x - p, y -p):h(x - p, y -p),
                  (x - p, y + p):h(x - p, y + p),
                  (x + p, y- p): h(x + p, y- p),
                  (x + p, y + p):h(x + p, y + p)
                  }
        return geitonia

def hc(start_state,problem):
        current_state=start_state
        minimum=start_state
        j=0
        dx=0
        close=False
        while True:
                
                y=geitonia(current_state)
                for x in y:
                        t,s=x
                        m,n=minimum
                        
                        if(h(t,s)<h(m,n)):
                                
                                dx=dx+1
                                minimum=(t,s)
                                current_state=minimum
                                print(f"{dx} : {t,s}:{h(t,s)}")
                                close=False
                                break
                        else:
                                close=True
                if close or dx >=10000:
                    return minimum   
               
               
def problem():
        pro={}
        for i in np.arange(0,0.1,0.001):
                for j in np.arange(1,0.1,0.001):
                       pro[(i,j)]=h(i,j)
        return pro




if __name__ == '__main__':
        provlhma=problem()
        x0,y0=0,0
        t=(hc((x0,y0),problem()))
        n,r=t
        try:
                print(f"{n,r}  :  {h(n,r)}")
        except:
                print("error")
