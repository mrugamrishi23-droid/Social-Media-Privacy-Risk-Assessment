import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backend.services.assessment_engine import calculate_privacy_risk
from backend.services.findings_engine import generate_privacy_findings
from backend.services.recommendation_engine import generate_recommendations
from backend.services.improvement_simulator import simulate_improvement

def demo_answers():
    a={}
    a["q01"]="PUBLIC"
    yes=["q02","q03","q04","q05","q07","q08","q12","q13","q14","q15","q16","q17","q18","q20","q22","q24","q26","q28","q36","q43","q46","q47","q48"]
    for q in yes:a[q]=True
    no=["q06","q09","q10","q11","q21","q25","q27","q29","q30","q31","q32","q33","q34","q35","q37","q38","q39","q40","q44","q49"]
    for q in no:a[q]=False
    a.update({"q19":"NEVER","q23":"OFTEN","q41":"SOMETIMES","q42":"SOMETIMES","q45":"SOMETIMES","q50":"NEVER"})
    return a

if __name__=="__main__":
    a=demo_answers()
    before=calculate_privacy_risk(a)
    findings=generate_privacy_findings(a,before["category_scores"])
    print("CURRENT:", before)
    print("FINDINGS:")
    for f in findings: print("-",f["severity"],f["finding_type"])
    changes={"q05":False,"q07":False,"q12":False,"q16":"NEVER","q23":"NEVER","q27":True,"q30":True,"q33":True,"q37":True,"q19":"REGULARLY","q50":"REGULARLY"}
    sim=simulate_improvement(a,changes)
    print("IMPROVED:",sim["after"])
    print("RISK REDUCTION:",sim["risk_reduction"],"points")
