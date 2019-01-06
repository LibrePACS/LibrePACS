# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""

import redis

from MediaKraken import public, user, admins
from MediaKraken.assets import assets
from MediaKraken.extensions import (
    bcrypt,
    db,
    login_manager,
    fpika,
)
from MediaKraken.settings import ProdConfig
from flask import Flask, render_template
from flask_kvsession import KVSessionExtension
from flask_uwsgi_websocket import GeventWebSocket
from simplekv.memory.redisstore import RedisStore


def create_app(config_object=ProdConfig):
    app = Flask(__name__)
    KVSessionExtension(RedisStore(redis.StrictRedis(host='lbredis')), app)
    app.config.from_object(config_object)
    app.config['UPLOAD_FOLDER'] = '/librepacs/uploads'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    websocket = GeventWebSocket(app)
    return app


def register_extensions(app):
    assets.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    fpika.init_app(app)
    return None


def register_blueprints(app):
    # load up public bps
    app.register_blueprint(public.views.blueprint)
    # load up user bps
    app.register_blueprint(user.views.blueprint)
    app.register_blueprint(user.views_images.blueprint)
    app.register_blueprint(user.views_internet.blueprint)
    app.register_blueprint(user.views_queue.blueprint)
    app.register_blueprint(user.views_search.blueprint)
    # load up admin bps
    app.register_blueprint(admins.views.blueprint)
    app.register_blueprint(admins.views_backup.blueprint)
    app.register_blueprint(admins.views_cron.blueprint)
    app.register_blueprint(admins.views_docker.blueprint)
    app.register_blueprint(admins.views_messages.blueprint)
    app.register_blueprint(admins.views_reports.blueprint)
    app.register_blueprint(admins.views_users.blueprint)
    return None


def register_errorhandlers(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template("{0}.html".format(error_code)), error_code

    for errcode in [401, 403, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
