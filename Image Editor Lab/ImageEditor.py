from graphics import*
from Button import*

#getPixel(x,y) (returns list of colors)
#setPixel(x,y,color_rgb(r,g,b))

#Increases the rgb values of the pixel.  If the raised values are above 255 they are set equal to 255. 
def brighten(cats):
    for i in range(0,499):
        for j in range(0,450):
            r = cats.getPixel(i,j)[0]+20
            g = cats.getPixel(i,j)[1]+20
            b = cats.getPixel(i,j)[2]+20

            if r > 255:
                r = 255

            if g > 255:
                g = 255
            
            if b > 255:
                b = 255
            cats.setPixel(i,j, color_rgb(r,g,b))

#Lowers the rgb values of the pixel.  If the lowered ones are below 0 it sets them equal to 0             
def darken(cats):
    for i in range(0,499):
        for j in range(0,450):
            r = cats.getPixel(i,j)[0]-20
            g = cats.getPixel(i,j)[1]-20
            b = cats.getPixel(i,j)[2]-20

            if r < 0:
                r = 0

            if g < 0:
                g = 0
            
            if b < 0:
                b = 0
            cats.setPixel(i,j, color_rgb(r,g,b))
            
#This function finds the new value of a pixel by the average of the r,g, and b values of the pixel above, beside (left), beside (right), and below.  
#This is relativly simple - it just diffuses the colors until everything is the average of all values. 
def blurr(cats):
    for i in range(1,498):
        for j in range(1,449):
            r = int((cats.getPixel(i,j)[0]+cats.getPixel(i+1,j)[0]+cats.getPixel(i-1,j)[0]+cats.getPixel(i,j+1)[0]+cats.getPixel(i,j-1)[0])/5)
            g = int((cats.getPixel(i,j)[1]+cats.getPixel(i+1,j)[1]+cats.getPixel(i-1,j)[1]+cats.getPixel(i,j+1)[1]+cats.getPixel(i,j-1)[1])/5)
            b = int((cats.getPixel(i,j)[2]+cats.getPixel(i+1,j)[2]+cats.getPixel(i-1,j)[2]+cats.getPixel(i,j+1)[2]+cats.getPixel(i,j-1)[2])/5)

            cats.setPixel(i,j, color_rgb(r,g,b))

#Contrast works by increasing the bright pixels, and darkening the dark ones.  We had two options to chose from, one where you get the overall brightness
#by averaging the RGB values then increasing or decreasing them all together (depending on if they were greater than or less than 255/2).  The other option
#was where you take the value of each pixel and increase it or decrease it depending on if its greater than or less than 255/2.  This means that one component 
#of a pixel may get brighter while another gets darker.  This was the one we decided on, and it produces the desired effect.  The main positives to this meathod
#is that pixels will not all go black/white, they can create a scale of colors.  If you continue clicking this button you will get 8 different colors - 
#0,0,0 - 255,255,255 - 255,0,0 - 0,255,0 - 0,0,255 - 255,255,0 - 255,0,255 - 0,255,255
def contrast(cats):
    for i in range(0,499):
        for j in range(0,450):
            r = cats.getPixel(i,j)[0]
            g = cats.getPixel(i,j)[1]
            b = cats.getPixel(i,j)[2]
            
            if r > 127:
                r = r +20
            if g > 127:
                g = g +20
            if b > 127:
                b = b +20

            if r < 127:
                r = r -20
            if g < 127:
                g = g -20
            if b < 127:
                b = b -20




            if r < 0:
                r = 0

            if g < 0:
                g = 0
            
            if b < 0:
                b = 0

            if r > 255:
                r = 255

            if g > 255:
                g = 255
            
            if b > 255:
                b = 255

            cats.setPixel(i,j, color_rgb(r,g,b))
#Makes the image grayscale.  This works by setting the value of the rgb values for each pixel to the rgb value of the brightest component.  For example,
#if a pixel is 25, 49, 213 then the grayscale value would be 213,213,213.  This works because it makes everyone a color on a scale between white and black, and 
#rather than using 3 variables, it just scales it down to the one.  This is how grayscale is stored, just as a single value...between 0 and 1 (black -> white)
#to make the conversion just divide the value of anyone of the rgb values (because they are all equal), by 255.  This will scale from 0->1.  
def specialFilter(cats):
    for i in range(0,499):
        for j in range(0,450):
            r = cats.getPixel(i,j)[0]
            g = cats.getPixel(i,j)[1]
            b = cats.getPixel(i,j)[2]
            
            arr = [r,g,b]
            #List.max gets the greatest numerical value out of the list
            greatest = max(arr)



            r = greatest
            b = greatest
            g = greatest

            

            cats.setPixel(i,j, color_rgb(r,g,b))

#Okay, this will take a while.  This algoritm detects edges on the image.  This function has two sections, loop A and loop B

#Loop A
#This loop is how the computer finds the edges.  It contrasts the picture to all 255,255,255 and 0,0,0 based on the average of the RGB values of each pixel
#If the average is above 255/2, the it increases it to black, if its below, it decreases it to white.  The reason this finds most edges is that objects tend
#to have a different color from surrounding stuff, which is why they can be differentiated.  Many objects have dark/light contrast between things, which makes 
#it easy to tell where edges are.  This algorithm can use shadows to find edges as well, because they are significantly darker than the surrounding area, which
#makes them easy to detect.  Typically shadows start right next to an edge, so by detecting the shadow you detect the edge.  

#The reason that there is a call to the blurr function in Loop A is because often edges will be extreamly sharp this way, and patterns such as spots on a cat
#get picked up on, which we don't want.  All this does is blurr the image each time before contrasting it, so that edges smooth out and there is less noise.  

#Loop B
#This loop is how the black and white image is interpreted to lines which the user can recognise as edges.  If a pixel has exactly 3 pixels next to it that are a 
#a different color from the other 2, then that means its on a border.  If this is the case it draws all the pixels white except for the subject pixel.  This makes
#lines where the edges are.  You might ask why is it 3 pixels not 2, or 4 - or why not a range of 2 to 3.  Idk I tried values and for some reason the other ones
#make weird lines though the image and didn't properly find the edges, so 3 worked and thats okay :D
def CustomB(cats):
    for i in range(2):
        blurr(cats)
        for i in range(0,499):
            for j in range(0,450):
                r = cats.getPixel(i,j)[0]
                g = cats.getPixel(i,j)[1]
                b = cats.getPixel(i,j)[2]
                
                ave = (r+g+b)/3
                if(ave>127):
                    r = 255
                    g = 255
                    b = 255
                else:
                    r = 0
                    g = 0
                    b = 0
                cats.setPixel(i,j, color_rgb(r,g,b))
    for i in range(1,498):
        for j in range(1,449):
            pix = 0
            if(cats.getPixel(i,j)[0]==255):
                pix = pix+1
            if(cats.getPixel(i+1,j)[0]==255):
                pix = pix+1
            if(cats.getPixel(i-1,j)[0]==255):
                pix = pix+1
            if(cats.getPixel(i,j+1)[0]==255):
                pix = pix+1
            if(cats.getPixel(i,j-1)[0]==255):
                pix = pix+1
            if pix ==3:
                cats.setPixel(i,j, color_rgb(0,0,0))
            else:
                cats.setPixel(i,j, color_rgb(255,255,255))
def RedFilter(cats):
    for i in range(0,499):
        for j in range(0,450):
            r = cats.getPixel(i,j)[0]+20
            g = cats.getPixel(i,j)[1]
            b = cats.getPixel(i,j)[2]
            if r > 255:
                r = 255

            cats.setPixel(i,j, color_rgb(r,g,b))

def GreenFilter(cats):
    for i in range(0,499):
        for j in range(0,450):
            r = cats.getPixel(i,j)[0]
            g = cats.getPixel(i,j)[1]+20
            b = cats.getPixel(i,j)[2]
            if g > 255:
                g = 255

def BlueFilter(cats):
    for i in range(0,499):
        for j in range(0,450):
            r = cats.getPixel(i,j)[0]
            g = cats.getPixel(i,j)[1]
            b = cats.getPixel(i,j)[2]+20
            if b > 255:
                b = 255

            cats.setPixel(i,j, color_rgb(r,g,b))
    
def main():
    win = GraphWin("Image Editor", 800, 600)
    sh = Button(win, "white", "Show", Point(150, 40), 45)
    hi = Button(win, "white", "Hide", Point(300, 40), 45)
    close = Button(win, "grey", "Quit", Point(150, 560), 45)
    bright = Button(win, "white", "Brighten", Point(720, 50), 45)
    dark = Button(win, "white", "Darken", Point(720, 150), 45)
    blur = Button(win, "white", "Blur", Point(720, 250), 45)
    cont = Button(win, "white", "Contrast", Point(720, 350), 45)
    filt = Button(win, "white", "Filter", Point(720, 450), 45)
    reset = Button(win,"white","Reset",Point(450, 40), 45)
    customB = Button(win, "white","Filter B", Point(720, 550), 45)
    Redfilter = Button(win,"white","RedFilter",Point(550,560),45)
    Greenfilter = Button(win,"white","GreenFilter",Point(425,560),45)
    Bluefilter  = Button(win,"white","BlueFilter",Point(300,560),45)


    cats = Image(Point(400,300), "Cats.png")

    m = win.getMouse()
    while True:
        if close.isClicked(m):
            break
        if sh.isClicked(m):
            cats.undraw()
            cats.draw(win)
        if hi.isClicked(m):
            cats.undraw()
        if dark.isClicked(m):
            darken(cats)
        if bright.isClicked(m):
            brighten(cats)
        if blur.isClicked(m):
            blurr(cats)
        if cont.isClicked(m):
            contrast(cats)
        if filt.isClicked(m):
            specialFilter(cats)
        if reset.isClicked(m):
            cats = Image(Point(400,300), "Cats.png")
            cats.undraw()
            cats.draw(win)
        if customB.isClicked(m):
            CustomB(cats)
        if Redfilter.isClicked(m):
            RedFilter(cats)
        if Greenfilter.isClicked(m):
            GreenFilter(cats)
        if Bluefilter.isClicked(m):
            BlueFilter(cats)
            
        m = win.getMouse()
        

        

    win.close()
    
if __name__ == "__main__":
    main()
