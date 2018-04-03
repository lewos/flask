from hello import square,hello

def main():
    print (square(10))
    hello()


if __name__ == "__main__":
    main()

#------------------

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

p = Point(3,5)
print(p.x)
print(p.y)