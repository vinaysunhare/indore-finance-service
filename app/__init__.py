from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Prometheus मैट्रिक्स इनिशियलाइज़ करें
    metrics = PrometheusMetrics(app, path='/metrics', defaults_prefix='flask')

    # वैकल्पिक: ऐप जानकारी मैट्रिक
    metrics.info('app_info', 'Application info', version='1.0.0')

    # ब्लूप्रिंट रजिस्टर करें
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app