from graphics import*
from Button import*
from math import*






def calcy(f, num):
    if "+" in f:
        l = f.split("+")
        result = 0
        for j in l:
            result = result + calcy(j,num)
        return result

    elif "-" in f:
        l = f.split("-")
        result = calcy(l[0],num)-calcy(l[1],num)
        return result
    
    elif "*" in f:
        l = f.split("*")
        result = 1
        for j in l:
            result = calcy(j,num)*result
        return result
    elif "/" in f:
        l = f.split("/")
        result = calcy(l[0],num)/calcy(l[1],num)
        return result
    elif "e^x" in f:
        return e**num
    elif "^" in f:
        l = f.split("^")
        result = 1
        for i in range(int(calcy(l[1],num))):
            result = result*calcy(l[0],num)
        return result
            
        
        
    
    if "sqrt(x)" in f:
        return sqrt(num)
    elif "x^2" in f:
        return num**2
    elif "sin(x)" in f:
        return sin(num)
    elif "cos(x)" in f:
        return cos(num)
    elif "log(x)" in f:
        return log(num)
    elif "x" in f:
        return num
    else:
        return float(f)






def main():

    win = GraphWin("calc",800,800)
    title = Text(Point(400,50), "Welcome to Frank's Desmos")
    title.setSize(32)
    title2 = Text(Point(400,110), "Enter a function")
    title2.setSize(20)
    title.draw(win)
    title2.draw(win)

    yAxis = Line(Point(400,150), Point(400,650))
    yAxis.draw(win)
    xAxis = Line(Point(150,400), Point(650,400))
    xAxis.draw(win)

    funText = Text(Point(200,700), "Y  =  ")
    funText.setSize(24)
    funText.draw(win)

    fun = Entry(Point(340,700),30)
    fun.draw(win)

    graph = Button(win, 'blue', "GRAPH", Point(700,750),60 )
    quitB = Button(win, 'red', "QUIT", Point(100,750), 50)

    scale = 100

    for ax in range(0,6 ):
        xn = Text(Point(400-ax*50,410),"-" + str(ax))
        xp = Text(Point(400+ax*50,410),ax)
        yn = Text(Point(390,400-ax*50),"-" + str(ax))
        yp = Text(Point(390,400+ax*50),ax)
        xn.draw(win)
        xp.draw(win)
        yn.draw(win)
        yp.draw(win)
        
        

    while True:
        m1 = win.getMouse()
        if graph.isClicked(m1):
            f = fun.getText()


            points = []
            l = f.split("+")
            if "sqrt(x)" in f:
                for i in range(0, 250):
                    x = i + 400
                    y = 400 - scale*calcy(f,i/scale)
                    points.append(Point(x,y))
                for p in points:
                    p.draw(win)

            elif "log(x)" in f:
                for i in range(1, 250):
                    x = i + 400
                    y = 400 - scale*calcy(f,i/scale)
                    points.append(Point(x,y))
                for p in points:
                    p.draw(win)
            else:
                for i in range(-250,250):
                    x = i + 400
                    
                    y = 400 - scale*calcy(f,i/scale)
                    points.append(Point(x,y))

                for p in points:
                    p.draw(win)

        if quitB.isClicked(m1):
            win.close()
            break
                
    

if __name__ == "__main__":
    main()
