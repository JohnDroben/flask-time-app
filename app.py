import os
from flask  import Flask, render_template, request, redirect, url_for
from datetime import datetime
import logging
from flask_wtf.csrf import CSRFProtect





app = Flask(__name__)
app.secret_key = os.urandom(24)
csrf = CSRFProtect(app)




posts = [
]
# Настройка логирования в начале
logging.basicConfig(
    filename='portfolio.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())

@app.route('/')
def index():
    app.logger.info('Accessed main page')
    return render_template(
        'index.html',
        current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    global posts  # Временное решение для демонстрации
    if request.method == 'POST':
        new_post = {
            'title': request.form.get('title'),
            'body': request.form.get('body'),
            'created_at': datetime.now()
        }
        posts.append(new_post)
        return redirect(url_for('blog'))
    return render_template('blog.html', posts=posts)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning('Page not found: %s', request.path)
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)