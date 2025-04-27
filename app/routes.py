from flask import Blueprint, render_template, request, current_app
from prometheus_flask_exporter import PrometheusMetrics

main_bp = Blueprint("main", __name__)

# कस्टम काउंटर
loan_calculations = PrometheusMetrics.for_app_factory().counter(
    'loan_calculations_total', 'Total loan calculations performed'
)

@main_bp.route("/")
def home():
    return render_template("home.html")

@main_bp.route("/loan-calculator", methods=["GET", "POST"])
def loan_calculator():
    if request.method == "POST":
        amount = float(request.form["amount"])
        interest = float(request.form["interest"])
        years = int(request.form["years"])
        monthly_rate = interest / 100 / 12
        months = years * 12
        monthly_payment = (amount * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
        # काउंटर बढ़ाएँ
        loan_calculations.inc()
        return render_template("loan_calculator.html", payment=round(monthly_payment, 2))
    return render_template("loan_calculator.html", payment=None)

@main_bp.route("/investment-tracker")
def investment_tracker():
    return render_template("investment_tracker.html")

@main_bp.route("/contact")
def contact():
    return render_template("contact.html")

@main_bp.route("/health")
def health():
    return "OK", 200

@main_bp.route('/debug_routes')
def debug_routes():
    return '<br>'.join([str(rule) for rule in current_app.url_map.iter_rules()])