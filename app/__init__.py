from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    from config import Config
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.medicos import bp_medicos
    from app.pacientes import bp_pacientes
    from app.citas import bp_citas

    app.register_blueprint(bp_medicos, url_prefix="/medicos")
    app.register_blueprint(bp_pacientes, url_prefix="/pacientes")
    app.register_blueprint(bp_citas, url_prefix="/citas")

    from app.medicos.models import Medico
    from app.pacientes.models import Paciente
    from app.citas.models import Cita

    @app.route("/")
    def home():
        return redirect(url_for("bp_medicos.index"))

    with app.app_context():
        db.create_all()

    return app