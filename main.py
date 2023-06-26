from flask import Flask 

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello , world"

if __name__ == '__main__' :
  app.run(host = '0.0.0.0' , debug=True)















#<---------------------------------------------------------------------------------->#

# Learning python using Cheatsheet

# Indentation is very important in Python 

# 1.) Defining the variables

# a = 10
# b= 12.1
# c= True 

# if (c):
#   print("the value of a is :" , a , "the value of b is : " , b)

#Taking the input
# i = int(input("Enter your age : "))
# print(i)

# #using the Strings
# s = "My name is nishant kumar"

# # these all are for temporary,  they don't change the strings
# print(s[0:5])
# print(s.upper())  
# print(s.title())
# print(s.replace('n' , 'h'))
