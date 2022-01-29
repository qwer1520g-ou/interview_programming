#!/usr/bin/env python3
class stack:
 
  def __init__(self):
 
    self.array = []
    self.max = 100 
 
  def isEmpty(self):
 
    if self.array == []:
        return True
    else:
        return False 
 
  def isFull(self): 
     
    if len(self.array) == self.max:
        return True
    else:
        return False  
 
  def push(self, data):
 
    if self.isFull():
        print('Stack OverFlow')
        return
    else:
        self.array.append(data)    
        

  def pop(self):
 
    if self.isEmpty():
        print('Stack UnderFlow')
        return
    else:
        tempt=self.array.pop()
        
        return tempt
 
    
class MinStack(stack):
 
  def __init__(self):
    super().__init__()
    self.Min = stack() 
 

  def push(self, x):
    
    if self.isEmpty():
        super().push(x)
        self.Min.push(x)
    else:
        super().push(x)
        y = self.Min.pop()
        self.Min.push(y)

        if x <= y:
            self.Min.push(x)
        

  def pop(self):

    x = super().pop()

    return x 

  def getmin(self):
    
    x = self.Min.pop()
    self.Min.push(x)
    return x
 
# Driver code
if __name__ == '__main__':
   
    m = MinStack()
    
    m.push(10)

    m.push(20)

    m.push(30)

    print("Stack:",m.array)
    m.pop()
    print("Stack:",m.array)
    print(m.getmin())
    m.push(5)
    print("Stack:",m.array)
    print(m.getmin())
