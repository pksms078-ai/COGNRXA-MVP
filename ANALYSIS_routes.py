Python
from flask import Blueprint

analysis_bp = Blueprint(
    "analysis",
    __name__
)

@analysis_bp.route("/analyze")
def analyze():

    return {
        "message":"Analysis endpoint"
    }
routes/insight_routes.py
Python
from flask import Blueprint

insight_bp = Blueprint(
    "insight",
    __name__
)

@insight_bp.route("/insights")
def insights():

    return {
        "message":"Insights endpoint"
    }
routes/decision_routes.py
Python
from flask import Blueprint

decision_bp = Blueprint(
    "decision",
    __name__
)

@decision_bp.route("/decisions")
def decisions():

    return {
        "message":"Decision endpoint"
    }
