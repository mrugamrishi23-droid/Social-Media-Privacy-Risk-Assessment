import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backend.services.assessment_engine import calculate_privacy_risk, category_scores, risk_level, validate_answers
from backend.services.findings_engine import generate_privacy_findings
from backend.services.recommendation_engine import generate_recommendations
from backend.services.improvement_simulator import simulate_improvement

def base():
    a={"q01":"PRIVATE"}
    yes_ids=["q02","q03","q04","q05","q06","q07","q08","q09","q10","q11","q12","q13","q14","q15","q16","q17","q18","q20","q21","q22","q24","q25","q26","q27","q28","q29","q30","q31","q32","q33","q34","q35","q36","q37","q38","q39","q40","q43","q44","q46","q47","q48","q49"]
    for q in yes_ids:a[q]=False
    a.update({"q19":"REGULARLY","q23":"NEVER","q41":"NEVER","q42":"NEVER","q45":"NEVER","q50":"REGULARLY"})
    return a

class TestPrivacyFramework(unittest.TestCase):
    def test_01_fully_private(self): self.assertLessEqual(calculate_privacy_risk(base())["overall_score"],20)
    def test_02_public_profile(self): a=base();a["q01"]="PUBLIC";self.assertGreater(calculate_privacy_risk(a)["overall_score"],0)
    def test_03_public_phone(self): a=base();a["q05"]=True;self.assertGreater(category_scores(a)["personal_info"],0)
    def test_04_public_email(self): a=base();a["q06"]=True;self.assertGreater(category_scores(a)["personal_info"],0)
    def test_05_public_birthday(self): a=base();a["q07"]=True;self.assertGreater(category_scores(a)["personal_info"],0)
    def test_06_public_location(self): a=base();a["q12"]=True;self.assertGreater(category_scores(a)["location"],0)
    def test_07_realtime_checkins(self): a=base();a["q12"]=True;a["q13"]=True;self.assertGreater(category_scores(a)["location"],0)
    def test_08_travel_plans(self): a=base();a["q16"]=True;self.assertGreater(category_scores(a)["location"],0)
    def test_09_workplace(self): a=base();a["q09"]=True;self.assertGreater(category_scores(a)["personal_info"],0)
    def test_10_education(self): a=base();a["q10"]=True;self.assertGreater(category_scores(a)["personal_info"],0)
    def test_11_public_posts(self): a=base();a["q18"]=True;self.assertGreater(category_scores(a)["content"],0)
    def test_12_unknown_connections(self): a=base();a["q23"]="OFTEN";self.assertGreater(category_scores(a)["connections"],0)
    def test_13_tag_review_disabled(self): a=base();a["q27"]=False;self.assertGreater(category_scores(a)["tagging"],0)
    def test_14_mfa_disabled(self): a=base();a["q30"]=False;self.assertGreater(category_scores(a)["account_security"],0)
    def test_15_login_alerts_disabled(self): a=base();a["q33"]=False;self.assertGreater(category_scores(a)["account_security"],0)
    def test_16_password_reuse(self): a=base();a["q36"]=True;self.assertGreater(category_scores(a)["account_security"],0)
    def test_17_apps_unreviewed(self): a=base();a["q37"]=False;self.assertGreater(category_scores(a)["third_party_apps"],0)
    def test_18_link_awareness(self): a=base();a["q42"]="OFTEN";self.assertGreater(category_scores(a)["social_engineering"],0)
    def test_19_old_posts(self): a=base();a["q46"]=True;self.assertGreater(category_scores(a)["digital_footprint"],0)
    def test_20_settings_never_reviewed(self): a=base();a["q50"]="NEVER";self.assertGreater(category_scores(a)["digital_footprint"],0)
    def test_21_category_count(self): self.assertEqual(len(category_scores(base())),10)
    def test_22_score_range(self): r=calculate_privacy_risk(base());self.assertTrue(0<=r["overall_score"]<=100)
    def test_23_boundary_20(self): self.assertEqual(risk_level(20),"LOW")
    def test_24_boundary_40(self): self.assertEqual(risk_level(40),"MODERATE")
    def test_25_boundary_70(self): self.assertEqual(risk_level(70),"HIGH")
    def test_26_boundary_71(self): self.assertEqual(risk_level(71),"CRITICAL")
    def test_27_findings(self): a=base();a["q05"]=True;fs=generate_privacy_findings(a,category_scores(a));self.assertTrue(len(fs)>0)
    def test_28_recommendations(self): a=base();a["q30"]=False;fs=generate_privacy_findings(a,category_scores(a));self.assertTrue(len(generate_recommendations(fs))>0)
    def test_29_simulation_reduces_risk(self):
        a=base();a["q05"]=True;a["q12"]=True;a["q30"]=False
        sim=simulate_improvement(a,{"q05":False,"q12":False,"q30":True})
        self.assertGreaterEqual(sim["risk_reduction"],0)
    def test_30_validation_missing(self): self.assertTrue(validate_answers({}))
    def test_31_validation_bad_choice(self): a=base();a["q01"]="BAD";self.assertTrue(validate_answers(a))
    def test_32_validation_bad_bool(self): a=base();a["q05"]="yes";self.assertTrue(validate_answers(a))
    def test_33_weights_total(self):
        from backend.services.questionnaire import WEIGHTS
        self.assertAlmostEqual(sum(WEIGHTS.values()),1.0)
    def test_34_no_sensitive_fields_in_base(self):
        forbidden={"phone_number","email","address","password","exact_location","private_message"}
        self.assertTrue(forbidden.isdisjoint(base().keys()))
    def test_35_recommendation_priority(self):
        a=base();a["q30"]=False;a["q06"]=True
        fs=generate_privacy_findings(a,category_scores(a));rs=generate_recommendations(fs)
        self.assertEqual(rs[0]["priority"],"IMMEDIATE")
if __name__=="__main__": unittest.main()
