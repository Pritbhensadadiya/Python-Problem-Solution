from flask import Flask,jsonify
app = Flask (__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0 
    order = len(str(n)) 
    copy_n = n
    while (n>0):
        digit = n%10
        sum += digit **order
        n=  n //10
    if (sum==copy_n):
        print(f"{copy_n} is an armstrong number")
        
        result = {
            "Number": copy_n,
            "Armstrong": "True",
            "IP": "122.33.422.333"
        }
        
    else:
        print (f"{copy_n}is not anarmstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": "False",
            "IP": "122.33.422.333"
        }

    
    return jsonify(result)
if __name__=="__main__":
    app.run(debug=True  )