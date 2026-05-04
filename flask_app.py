import os
import logging
from flask import Flask, send_from_directory
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

from tools.Tools import ToolManager, tools_page
from users.UserServices import users_page
from bets.BetsServices import bets_page
from games.GameServices import games_page
from stats.StatsServices import stats_page

# Configuration de l'application
app = Flask(__name__, static_folder='static', static_url_path='/')
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
app.config['ENV'] = os.environ.get('FLASK_ENV', 'production')

# Enregistrement des blueprints
app.register_blueprint(tools_page, url_prefix="/tools", template_folder='templates')
app.register_blueprint(users_page, url_prefix="/users", template_folder='templates')
app.register_blueprint(bets_page, url_prefix="/bets", template_folder='templates')
app.register_blueprint(games_page, url_prefix="/games", template_folder='templates')
app.register_blueprint(stats_page, url_prefix="/stats", template_folder='templates')

# Configuration du logging
logging.basicConfig(
    filename='bet.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
logger = logging.getLogger(__name__)
logger.info('Application started')


@app.after_request
def add_header(response):
    """
    Add security and caching headers to response.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0, no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route("/")
def hello_world():
    """Serve the main index page."""
    return send_from_directory(app.static_folder, 'index.html')


@app.errorhandler(404)
def ma_page_404(error):
    """Handle 404 errors."""
    return "Page not found !<br/><h1>404 error code !</h1>Where do you really want to go ?", 404


if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', False)
    app.run(debug=debug_mode)
