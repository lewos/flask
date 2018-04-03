# flask

virtualenv venv
. venv/Scripts/activate
pip install Flask
touch app.py
export FLASK_APP=app.py
export FLASK_DEBUG=1 ---> para que corra en debug
flask run

pip install Flask-Session
