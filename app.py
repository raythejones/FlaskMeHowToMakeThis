from flask import Flask

my_site = Flask(__name__)

@my_site.route("/")
def fool():
    return "<h1><font color='orange'>Fool!</font></h1>"

@my_site.route("/pool")
def pool():
    return "<h2><font color='blue'>Pool!</font></h2>"

@my_site.route("/cool")
def cool():
    return "<h3> <font color='green'>Cool!</font></h3>"

if __name__ == "__main__":
   #my_site.debug = true
    my_site.run()