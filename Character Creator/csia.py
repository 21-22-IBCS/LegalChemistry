from graphics import*
from Button import*

def main():
    win = GraphWin("Schedule",800,800)
    title = Text(Point(400,50), "What time you can arrive to school?")
    title.setSize(32)
    title2 = Text(Point(400,110), "Please answer the questions below ")
    title2.setSize(20)
    title.draw(win)
    title2.draw(win)
  
    funText = Text(Point(300,400), "How is the weather today?(good or bad)  =  ")
    funText.setSize(24)
    funText.draw(win)
    fun1 = Entry(Point(650,400),30)
    fun1.draw(win)
    
    funText = Text(Point(300,500), "How is the traffic today?(good or bad)  =  ")
    funText.setSize(24)
    funText.draw(win)
    fun2 = Entry(Point(650,500),30)
    fun2.draw(win)
 
    funText = Text(Point(280,600), "What time you went to bed last night?(number)  =  ")
    funText.setSize(24)
    funText.draw(win)
    fun3 = Entry(Point(650,600),30)
    fun3.draw(win)
 
   
    graph = Button(win, 'blue', "ENTER", Point(700,750),60)
    quitB = Button(win, 'red', "QUIT", Point(100,750), 50)
    ff = Text(Point(350,700), "")

 
    
 
    while True:
        m1 = win.getMouse()
        if graph.isClicked(m1):
            ff.undraw()
            f1 = fun1.getText()
            f2 = fun2.getText()
            f3 = fun3.getText()
            f3 = int(f3)
            if f1 == "good" and f2 == "good" and f3 <=12:
                ff = Text(Point(350,700), "you will arrive school at 9am")
                ff.setSize(24)
                ff.draw(win)
                 
            if f1 == "bad" and f2 == "good" and f3 >=13:
                ff = Text(Point(350,700), "you will be late for school")
                ff.setSize(24)
                ff.draw(win)
                
            if f1 == "bad" and f2 == "bad" and f3 >=13:
                ff = Text(Point(350,700), "you will be late for school")
                ff.setSize(24)
                ff.draw(win)

            if f1 == "good" and f2 == "bad" and f3 <=12:
                ff = Text(Point(350,700), "you will arrive school at 9am")
                ff.setSize(24)
                ff.draw(win)

            if f1 == "bad" and f2 == "good" and f3 >=13:
                ff = Text(Point(350,700), "you will be late for school")
                ff.setSize(24)
                ff.draw(win)

            if f1 == "bad" and f2 == "bad" and f3 <=12:
                ff = Text(Point(350,700), "you will be late for school")
                ff.setSize(24)
                ff.draw(win)
                
            if f1 == "good" and f2 == "good" and f3 >=13:
                ff = Text(Point(350,700), "you will be late for school")
                ff.setSize(24)
                ff.draw(win)

            if f1 == "good" and f2 == "bad" and f3 >=13:
                ff = Text(Point(350,700), "you will be late for school")
                ff.setSize(24)
                ff.draw(win)
            
                
            
 
        if quitB.isClicked(m1):
            win.close()
            break
         
                
    
 
if __name__ == "__main__":
    main()
