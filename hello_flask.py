from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello, World!"
# def main():
#     print('hello world')




# if __name__ == "__main__":
#     main()