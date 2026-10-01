from flask import Flask, request, jsonify, send_from_directory, render_template
from pathlib import Path
import uuid
from .database import init_db, save_assessment, get_assessment, dashboard_stats
from .services.questionnaire import QUESTIONS
from .services.assessment_engine import validate_answers, calculate_privacy_risk
from .services.findings_engine import generate_privacy_findings
from .services.recommendation_engine import generate_recommendations
from .services.improvement_simulator import simulate_improvement

BASE = Path(__file__).resolve().parent.parent
app = Flask(__name__, static_folder=str(BASE/"frontend"), template_folder=str(BASE/"frontend"))
init_db()

@app.get("/")
def index():
    return send_from_directory(BASE/"frontend", "index.html")

@app.get("/assessment")
def assessment_page():
    return send_from_directory(BASE/"frontend", "assessment.html")

@app.get("/dashboard")
def dashboard_page():
    return send_from_directory(BASE/"frontend", "dashboard.html")

@app.get("/api/questions")
def questions():
    return jsonify({"questions": QUESTIONS})

@app.post("/api/assessment")
def create_assessment():
    payload = request.get_json(silent=True) or {}
    answers = payload.get("answers")
    errors = validate_answers(answers)
    if errors:
        return jsonify({"errors": errors}), 400
    result = calculate_privacy_risk(answers)
    findings = generate_privacy_findings(answers, result["category_scores"])
    recommendations = generate_recommendations(findings)
    assessment_id = uuid.uuid4().hex[:12]
    created_at = save_assessment(assessment_id, result, findings)
    return jsonify({
        "assessment_id": assessment_id,
        "created_at": created_at,
        **result,
        "findings": findings,
        "recommendations": recommendations,
        "disclaimer": "Educational framework only; not a guarantee that an account will or will not be compromised."
    }), 201

@app.get("/api/assessment/<assessment_id>")
def assessment(assessment_id):
    data = get_assessment(assessment_id)
    if not data:
        return jsonify({"error":"Assessment not found"}), 404
    return jsonify(data)

@app.get("/api/assessment/<assessment_id>/recommendations")
def assessment_recommendations(assessment_id):
    data = get_assessment(assessment_id)
    if not data:
        return jsonify({"error":"Assessment not found"}), 404
    return jsonify({"recommendations": generate_recommendations(data["findings"])})

@app.post("/api/assessment/simulate-improvement")
def improvement():
    payload = request.get_json(silent=True) or {}
    answers, changes = payload.get("answers"), payload.get("changes")
    errors = validate_answers(answers)
    if errors:
        return jsonify({"errors": errors}), 400
    if not isinstance(changes, dict):
        return jsonify({"error":"changes must be an object"}), 400
    return jsonify(simulate_improvement(answers, changes))

@app.get("/api/dashboard/stats")
def stats():
    return jsonify(dashboard_stats())

@app.get("/api/privacy-checklist")
def checklist():
    return jsonify({"checklist": [
        "Review profile visibility", "Hide unnecessary contact information",
        "Review birth-date visibility", "Review location sharing",
        "Avoid unnecessary real-time location posts", "Review tagging permissions",
        "Review followers/friends", "Verify unfamiliar requests", "Enable MFA",
        "Enable login alerts where available", "Review active sessions",
        "Review connected apps", "Remove unused integrations", "Review old public posts",
        "Review photo privacy", "Be cautious with unexpected links",
        "Never share verification codes", "Review privacy settings periodically"
    ]})

@app.get("/api/report/<assessment_id>")
def report(assessment_id):
    data = get_assessment(assessment_id)
    if not data:
        return jsonify({"error":"Assessment not found"}), 404
    return render_template("report.html", data=data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
