data = [120, 56, 309, 220, 156, 23, 98]
t = turtle.Turtle()
t.color("blue")
t.fillcolor("red")
t.pensize(3)
for d in data:
    drawBar(d)
turtle.mainloop()
turtle.bye()