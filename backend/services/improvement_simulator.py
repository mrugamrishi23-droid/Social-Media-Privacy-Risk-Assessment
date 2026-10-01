from copy import deepcopy
from .assessment_engine import calculate_privacy_risk

def simulate_improvement(answers, changes):
    before = calculate_privacy_risk(answers)
    improved = deepcopy(answers)
    for qid, value in changes.items():
        if qid in improved:
            improved[qid] = value
    after = calculate_privacy_risk(improved)
    return {
        "before": before,
        "after": after,
        "risk_reduction": before["overall_score"] - after["overall_score"],
        "simulated_answers": improved,
        "disclaimer": "Simulation only; it does not guarantee real-world safety."
    }
