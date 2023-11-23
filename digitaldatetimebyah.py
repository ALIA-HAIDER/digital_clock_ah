import turtle
import datetime
#creating screen 
sc=turtle.Screen()
sc.bgcolor("light green")
#creating box for clock
t1=turtle.Turtle()
t1.begin_fill()
t1.fillcolor("light grey")
t1.fd(350)
t1.left(90)
t1.fd(50)
t1.left(90)
t1.fd(350)
t1.left(90)
t1.fd(50)
t1.end_fill()
# obtaining current min,hour and sec
hr=datetime.datetime.now().hour
mn=datetime.datetime.now().minute
sc=datetime.datetime.now().second
#writting time in clock
t2=turtle.Turtle()
t2.pensize(3)
t2.write("  Hr:"+str(hr)+"  min:"+str(mn)+"  sec:"+str(sc),font=("Arial",24,"normal"))

t1.hideturtle()
t2.hideturtle()
#writting digi clock
t3=turtle.Turtle()
t3.up()
t3.goto(-200,200)
t3.down()
t3.write("DIGI CLOCK <A/H>",font=("Arial",35,"bold"))
t3.hideturtle()
turtle.exitonclick()