from flask import Flask, jsonify


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SQLALCHEMY_DATABASE_URI="sqlite:///expenses.sqlite3")

    @app.route("/")
    def home():
        """
        Вітає користувача на головній сторінці
        ---
        tags:
            - домашня сторінка
        produces:
            - application/json
        responses:
            200:
                description: Привітання
                schema:
                    $ref: '#/definitions/Hello'
        """
        return jsonify(message="Привіт, я твій додаток для контролю витрат!")

    from app.swagger_utils import build_swagger
    from app.swagger_bp import swagger_ui_blueprint, SWAGGER_API_URL

    @app.route(SWAGGER_API_URL)
    def spec():
        return jsonify(build_swagger(app))

    from app.db import db

    db.init_app(app)
    with app.app_context():
        db.create_all()

    from app import expense

    app.register_blueprint(expense.bp)
    app.register_blueprint(swagger_ui_blueprint)

    @app.errorhandler(404)
    def handle_404(e):
        return jsonify(error="Ми не змогли знайти це :("), 404

    return app
