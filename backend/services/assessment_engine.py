from .questionnaire import QUESTIONS, CATEGORIES, WEIGHTS

YES_RISK = {
    "q02": 70, "q03": 55, "q04": 55, "q05": 100, "q06": 75, "q07": 80,
    "q08": 90, "q09": 45, "q10": 40, "q11": 55, "q12": 100, "q13": 70,
    "q14": 80, "q15": 55, "q16": 75, "q17": 75, "q18": 70, "q20": 60,
    "q21": 70, "q22": 60, "q24": 55, "q25": 45, "q26": 65, "q27": 80,
    "q28": 50, "q29": 40, "q30": 0, "q31": 0, "q32": 0, "q33": 0,
    "q34": 0, "q35": 0, "q36": 85, "q37": 0, "q38": 0, "q39": 0, "q40": 0,
    "q43": 100, "q44": 0, "q46": 75, "q47": 55, "q48": 55, "q49": 0,
}
NO_RISK = {qid: 0 for qid in YES_RISK}

FREQUENCY_RISK = {
    "q19": {"REGULARLY":0, "SOMETIMES":40, "NEVER":80, "NOT SURE":70},
    "q23": {"OFTEN":100, "SOMETIMES":65, "RARELY":25, "NEVER":0},
    "q41": {"OFTEN":100, "SOMETIMES":65, "RARELY":25, "NEVER":0},
    "q42": {"OFTEN":100, "SOMETIMES":65, "RARELY":25, "NEVER":0},
    "q45": {"OFTEN":90, "SOMETIMES":60, "RARELY":25, "NEVER":0},
    "q50": {"REGULARLY":0, "SOMETIMES":35, "NEVER":80, "NOT SURE":65},
}

def validate_answers(answers):
    allowed = {q["id"]: q for q in QUESTIONS}
    errors = []
    if not isinstance(answers, dict):
        return ["answers must be an object"]
    missing = [qid for qid in allowed if qid not in answers]
    if missing:
        errors.append(f"Missing answers: {', '.join(missing)}")
    for qid, value in answers.items():
        if qid not in allowed:
            errors.append(f"Unknown question id: {qid}")
            continue
        q = allowed[qid]
        if q["type"] == "choice" and value not in q["options"]:
            errors.append(f"{qid}: invalid choice")
        elif q["type"] == "frequency" and value not in q["options"]:
            errors.append(f"{qid}: invalid frequency")
        elif q["type"] == "yesno" and not isinstance(value, bool):
            errors.append(f"{qid}: expected true/false")
    return errors

def extract_privacy_features(answers):
    features = {}
    for q in QUESTIONS:
        qid, value = q["id"], answers.get(q["id"])
        if qid == "q01":
            features[qid] = {"PUBLIC":100, "FRIENDS":35, "PRIVATE":0}.get(value, 0)
        elif qid in FREQUENCY_RISK:
            features[qid] = FREQUENCY_RISK[qid].get(value, 0)
        elif q["type"] == "yesno":
            risk = YES_RISK.get(qid, 0)
            # For protective controls, YES is safer and NO is riskier.
            protective = {"q21","q25","q27","q29","q30","q31","q32","q33","q34","q35","q37","q38","q39","q40","q44","q49"}
            if qid in protective:
                features[qid] = 0 if value else (risk if risk else 70)
            else:
                features[qid] = risk if value else 0
    return features

def category_scores(answers):
    features = extract_privacy_features(answers)
    scores = {}
    for key in CATEGORIES:
        qids = [q["id"] for q in QUESTIONS if q["category"] == key]
        vals = [features[qid] for qid in qids]
        scores[key] = round(sum(vals) / len(vals)) if vals else 0
    return scores

def risk_level(score):
    if score <= 20: return "LOW"
    if score <= 40: return "MODERATE"
    if score <= 70: return "HIGH"
    return "CRITICAL"

def calculate_privacy_risk(answers, weights=None):
    scores = category_scores(answers)
    weights = weights or WEIGHTS
    if abs(sum(weights.values()) - 1.0) > 1e-6:
        raise ValueError("Risk weights must total 1.0")
    overall = round(sum(scores[k] * weights[k] for k in scores))
    return {"overall_score": overall, "risk_level": risk_level(overall), "category_scores": scores}
