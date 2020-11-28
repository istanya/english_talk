from app import create_app
from app.commands import InitDbCommand
from app.talk.models import TalksType
from app.summary.models import Retelling
from app.chat.models import StartPhrases

from flask_script import Manager
from flask_migrate import MigrateCommand

app = create_app()

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('init_db', InitDbCommand)

if __name__ == '__main__':
    manager.run()
