import sys
import logging
import logging.handlers

from flask import Flask
print(sys.path)
from tools.Tools import ToolManager, tools_page
from users.UserServices import users_page
from bets.BetsServices import bets_page
from games.GameServices import games_page
from stats.StatsServices import stats_page

app = Flask(__name__)

app.secret_key = u'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT#BB'

app.register_blueprint(tools_page, url_prefix="/tools", template_folder='templates')
app.register_blueprint(users_page, url_prefix="/users", template_folder='templates')
app.register_blueprint(bets_page, url_prefix="/bets", template_folder='templates')
app.register_blueprint(games_page, url_prefix="/games", template_folder='templates')
app.register_blueprint(stats_page, url_prefix="/stats", template_folder='templates')

print(sys.path)
app.logger.warning('Started')
#ch = logging.StreamHandler(sys.stdout)
#ch.setLevel(logging.DEBUG)
logging.basicConfig(filename='bet.log',level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

logger = logging.getLogger(__name__)
#logger.addHandler(ch)


logger.info('Started')


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0, no-cache, no-store, must-revalidate'
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    #logger.info(u'response.headers={}'.format(response.headers))
    return response

@app.route("/")
def hello_world():
    return app.send_static_file('index.html')

@app.route('/yeah')
def yo():
    return 'yooooooooooooooooooooooooo'

@app.route('/hello')
def yeah():
    return 'Hello, World'


@app.errorhandler(404)
def ma_page_404(error):
	return u"Page not found !<br/> <h1>404 error code !</h1> Where do you really want to go ?", 404

if __name__ == '__main__':
    app.run()
