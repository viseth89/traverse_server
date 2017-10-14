# traverse_server

1. Initial Setup

sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get install python3-setuptools -y && sudo apt-get install nginx -y && sudo apt-get install python3-pip -y && pip3 install virtualenv && virtualenv venv && source venv/bin/activate && pip install flask gunicorn

2. Changing of ownerships + Init File (copy and paste from part 2)

sudo chown -R $USER /var/www && cd /var/www && mkdir FlaskApp && cd FlaskApp && mkdir FlaskApp && cd FlaskApp && mkdir static templates && nano __init__.py

3. using nginx and gunicorn (copy and paste from part 3)

sudo rm /etc/nginx/sites-enabled/default && sudo nano /etc/nginx/sites-available/example.com && sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/example.com && sudo service nginx restart && gunicorn __init__:app


part 2


from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
        return 'Hello This server was setup in less than 10 mintues :)'

if __name__ == "__main__":
        app.run()

part 3

server {
	listen 80;

	location / {
		proxy_pass http://127.0.0.1:8000/;
	}
}
