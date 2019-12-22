import turtle

t = turtle.Turtle()
colors = [0, 0, 'green', 'darkgreen', 'red', 'yellow', 'blue', 'white', 'orange', 'skyblue', 'pink', 'purple', 'ivory', 'darkred', 'darkblue', 'lightblue', 'lightyellow', 'lightgreen', 'brown', 'brown', 'green', 'blue', 'red', 'red', 'hotpink', 'yellow']

def polygons(sides):
  if sides <= 2: # Base Case
      return
  t.fillcolor(colors[sides-1])
  t.begin_fill()
  for i in range(sides): # Middle polygon
    for j in range(sides-1): # Surrounding polygons
      t.right(360/(sides-1))
      t.back(20)
    t.forward(20)
    t.right(360/sides)
  t.end_fill()
  polygons(sides-1) #Recursive Call
polygons(15) # Valid range: 3-26




