import csv, random
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backend.services.assessment_engine import calculate_privacy_risk

random.seed(42)
OUT = Path(__file__).resolve().parent / "social_media_privacy_assessments.csv"

def synthetic_answers():
    a = {}
    # Mixed synthetic population, intentionally not based on real users.
    a["q01"] = random.choices(["PUBLIC","FRIENDS","PRIVATE"], [45,40,15])[0]
    for q in ["q02","q03","q04","q05","q06","q07","q08","q09","q10","q11","q12","q13","q14","q15","q16","q17","q18","q20","q21","q22","q24","q25","q26","q27","q28","q29","q30","q31","q32","q33","q34","q35","q36","q37","q38","q39","q40","q43","q44","q46","q47","q48","q49"]:
        a[q] = random.random() < (0.35 if q in {"q30","q31","q33","q37","q38","q39","q40","q44","q49"} else 0.25)
    a["q19"] = random.choices(["REGULARLY","SOMETIMES","NEVER","NOT SURE"], [35,40,15,10])[0]
    a["q23"] = random.choices(["OFTEN","SOMETIMES","RARELY","NEVER"], [10,25,35,30])[0]
    a["q41"] = random.choices(["OFTEN","SOMETIMES","RARELY","NEVER"], [5,20,40,35])[0]
    a["q42"] = random.choices(["OFTEN","SOMETIMES","RARELY","NEVER"], [3,15,40,42])[0]
    a["q45"] = random.choices(["OFTEN","SOMETIMES","RARELY","NEVER"], [4,16,40,40])[0]
    a["q50"] = random.choices(["REGULARLY","SOMETIMES","NEVER","NOT SURE"], [35,40,15,10])[0]
    return a

def main():
    fields = ["profile_id","profile_visibility","phone_public","email_public","birthday_public","location_public","workplace_public","education_public","relationship_public","posts_public","location_tagging","travel_posts","unknown_connections","tag_review_enabled","third_party_apps_reviewed","mfa_enabled","login_alerts_enabled","password_reuse_reported","suspicious_link_awareness","old_posts_reviewed","privacy_settings_reviewed","risk_score","risk_level"]
    rows=[]
    for i in range(1,1001):
        a=synthetic_answers()
        r=calculate_privacy_risk(a)
        rows.append({
            "profile_id":f"SYN-{i:04d}","profile_visibility":a["q01"],
            "phone_public":a["q05"],"email_public":a["q06"],"birthday_public":a["q07"],
            "location_public":a["q12"],"workplace_public":a["q09"],"education_public":a["q10"],
            "relationship_public":a["q11"],"posts_public":a["q18"],"location_tagging":a["q13"],
            "travel_posts":a["q16"],"unknown_connections":a["q23"],
            "tag_review_enabled":a["q27"],"third_party_apps_reviewed":a["q37"],
            "mfa_enabled":a["q30"],"login_alerts_enabled":a["q33"],
            "password_reuse_reported":a["q36"],"suspicious_link_awareness":a["q42"],
            "old_posts_reviewed":a["q19"],"privacy_settings_reviewed":a["q50"],
            "risk_score":r["overall_score"],"risk_level":r["risk_level"]
        })
    with OUT.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
    print(f"Generated {len(rows)} synthetic records: {OUT}")

if __name__=="__main__":
    main()
