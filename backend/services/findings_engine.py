from .assessment_engine import extract_privacy_features
from .questionnaire import QUESTIONS, CATEGORIES

FINDING_RULES = {
    "q05": ("personal_info","Public phone number","HIGH","Phone number reported as publicly visible."),
    "q06": ("personal_info","Public personal email","MEDIUM","Personal email reported as publicly visible."),
    "q07": ("personal_info","Public full birthday","HIGH","Full birth date reported as publicly visible."),
    "q12": ("location","Real-time location sharing","CRITICAL","Current or real-time location sharing is reported."),
    "q16": ("location","Travel plans exposed","HIGH","Travel plans are reported as public before or during trips."),
    "q23": ("connections","Unknown connections accepted","HIGH","Unknown connection requests are accepted frequently."),
    "q27": ("tagging","Tag review disabled","HIGH","Tag review is disabled, so tagged content may appear without approval."),
    "q30": ("account_security","MFA disabled","CRITICAL","Multi-factor authentication is reported as disabled."),
    "q33": ("account_security","Login alerts disabled","MEDIUM","Login alerts are reported as disabled."),
    "q36": ("account_security","Password reuse reported","CRITICAL","Password reuse is reported for the account."),
    "q37": ("third_party_apps","Third-party apps not reviewed","HIGH","Connected applications are not regularly reviewed."),
    "q42": ("social_engineering","Unexpected links may be clicked","HIGH","Unexpected social-platform links may be clicked."),
    "q43": ("social_engineering","Verification-code sharing risk","CRITICAL","The response indicates verification codes could be shared."),
    "q46": ("digital_footprint","Old public posts not reviewed","HIGH","Old public posts are not regularly reviewed."),
    "q50": ("digital_footprint","Privacy settings not reviewed regularly","HIGH","Privacy settings are not reviewed regularly."),
}

def generate_privacy_findings(answers, category_scores):
    findings = []
    for qid, (category, title, severity, description) in FINDING_RULES.items():
        q = next(q for q in QUESTIONS if q["id"] == qid)
        value = answers.get(qid)
        # Reuse feature extraction semantics to decide whether the condition is risky.
        feature = extract_privacy_features(answers).get(qid, 0)
        if feature >= 50:
            findings.append({
                "category": CATEGORIES[category],
                "finding_type": title,
                "severity": severity,
                "description": description,
                "score": feature
            })
    findings.sort(key=lambda x: ({"CRITICAL":0,"HIGH":1,"MEDIUM":2,"LOW":3}.get(x["severity"],9), -x["score"]))
    return findings[:10]
