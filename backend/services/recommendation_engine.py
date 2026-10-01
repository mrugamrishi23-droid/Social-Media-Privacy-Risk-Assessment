RECOMMENDATIONS = {
    "Public phone number": ("Limit phone-number visibility where possible.", "IMMEDIATE"),
    "Public personal email": ("Limit personal email visibility and use platform privacy controls.", "IMPORTANT"),
    "Public full birthday": ("Hide the full birth date or limit its visibility.", "IMPORTANT"),
    "Real-time location sharing": ("Avoid publicly broadcasting real-time location unless intentionally needed.", "IMMEDIATE"),
    "Travel plans exposed": ("Consider sharing travel details after leaving the location rather than broadcasting plans in real time.", "IMMEDIATE"),
    "Unknown connections accepted": ("Verify unfamiliar profiles before accepting connections.", "IMMEDIATE"),
    "Tag review disabled": ("Enable tag review where the platform supports it.", "IMPORTANT"),
    "MFA disabled": ("Enable multi-factor authentication using the strongest supported method available.", "IMMEDIATE"),
    "Login alerts disabled": ("Enable login/security alerts where available.", "IMPORTANT"),
    "Password reuse reported": ("Use a unique password and a password manager where appropriate.", "IMMEDIATE"),
    "Third-party apps not reviewed": ("Review connected applications and revoke unused or unnecessary access.", "IMPORTANT"),
    "Unexpected links may be clicked": ("Treat unexpected links as untrusted and verify through a separate trusted channel.", "IMMEDIATE"),
    "Verification-code sharing risk": ("Never share authentication or verification codes with another person.", "IMMEDIATE"),
    "Old public posts not reviewed": ("Review and limit old public posts that are no longer necessary.", "IMPORTANT"),
    "Privacy settings not reviewed regularly": ("Schedule periodic privacy-setting reviews.", "GOOD PRACTICE"),
}

def generate_recommendations(findings):
    out = []
    for f in findings:
        title = f["finding_type"]
        if title in RECOMMENDATIONS:
            rec, priority = RECOMMENDATIONS[title]
            out.append({"finding_type": title, "recommendation": rec, "priority": priority})
    priority_order = {"IMMEDIATE":0,"IMPORTANT":1,"GOOD PRACTICE":2}
    return sorted(out, key=lambda x: priority_order[x["priority"]])
