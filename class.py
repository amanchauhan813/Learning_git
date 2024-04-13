class Cars:
    def __init__(self,model,colour):
        self.model=model
        self.colour=colour
    def myfunction(self,):
        print('The model of the car is '+self.model)
        print('And Colour of my car is '+self.colour)
a= Cars('BMW 3 Series','White')
a.myfunction()