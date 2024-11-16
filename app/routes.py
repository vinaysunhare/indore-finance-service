from flask import Blueprint, render_template, request

main_bp = Blueprint("main", __name__)

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
        return render_template("loan_calculator.html", payment=round(monthly_payment, 2))
    return render_template("loan_calculator.html", payment=None)

@main_bp.route("/investment-tracker")
def investment_tracker():
    return render_template("investment_tracker.html")

@main_bp.route("/contact")
def contact():
    return render_template("contact.html")
