QUESTIONS = [
    # A Profile Visibility
    {"id":"q01","category":"profile","text":"Is your profile publicly visible?","type":"choice","options":["PUBLIC","FRIENDS","PRIVATE"]},
    {"id":"q02","category":"profile","text":"Can search engines index your profile?","type":"yesno"},
    {"id":"q03","category":"profile","text":"Is your followers/friends list visible to people you do not know?","type":"yesno"},
    {"id":"q04","category":"profile","text":"Can unknown people discover your profile through public activity?","type":"yesno"},
    # B Personal Information
    {"id":"q05","category":"personal_info","text":"Is your phone number publicly visible?","type":"yesno"},
    {"id":"q06","category":"personal_info","text":"Is your personal email publicly visible?","type":"yesno"},
    {"id":"q07","category":"personal_info","text":"Is your full birth date publicly visible?","type":"yesno"},
    {"id":"q08","category":"personal_info","text":"Is home-related information publicly visible?","type":"yesno"},
    {"id":"q09","category":"personal_info","text":"Is your workplace publicly visible?","type":"yesno"},
    {"id":"q10","category":"personal_info","text":"Is your education information publicly visible?","type":"yesno"},
    {"id":"q11","category":"personal_info","text":"Are family or relationship details publicly visible?","type":"yesno"},
    # C Location
    {"id":"q12","category":"location","text":"Do you publicly share your current or real-time location?","type":"yesno"},
    {"id":"q13","category":"location","text":"Do you use public geotags or check-ins?","type":"yesno"},
    {"id":"q14","category":"location","text":"Can posts reveal your home location or routine?","type":"yesno"},
    {"id":"q15","category":"location","text":"Can posts reveal your work or college location?","type":"yesno"},
    {"id":"q16","category":"location","text":"Do you post travel plans before or during a trip?","type":"yesno"},
    {"id":"q17","category":"location","text":"Do you publicly share vacation or event locations in real time?","type":"yesno"},
    # D Posts & Content
    {"id":"q18","category":"content","text":"Are most of your posts publicly visible?","type":"yesno"},
    {"id":"q19","category":"content","text":"Do you regularly review old public posts?","type":"frequency","options":["REGULARLY","SOMETIMES","NEVER","NOT SURE"]},
    {"id":"q20","category":"content","text":"Do photos sometimes reveal documents, badges, screens, vehicles, or family details?","type":"yesno"},
    {"id":"q21","category":"content","text":"Do you check photo metadata/privacy implications before sharing?","type":"yesno"},
    {"id":"q22","category":"content","text":"Can tagged posts appear automatically on your profile?","type":"yesno"},
    # E Friends / Followers
    {"id":"q23","category":"connections","text":"Do you accept connection requests from people you do not know?","type":"frequency","options":["OFTEN","SOMETIMES","RARELY","NEVER"]},
    {"id":"q24","category":"connections","text":"Is your followers/friends list broadly visible?","type":"yesno"},
    {"id":"q25","category":"connections","text":"Do you periodically review unfamiliar followers/connections?","type":"yesno"},
    # F Tagging & Mentions
    {"id":"q26","category":"tagging","text":"Can anyone tag you without approval?","type":"yesno"},
    {"id":"q27","category":"tagging","text":"Is tag review enabled?","type":"yesno"},
    {"id":"q28","category":"tagging","text":"Can unknown users mention your account?","type":"yesno"},
    {"id":"q29","category":"tagging","text":"Do you review tagged content periodically?","type":"yesno"},
    # G Account Security
    {"id":"q30","category":"account_security","text":"Do you use multi-factor authentication (MFA)?","type":"yesno"},
    {"id":"q31","category":"account_security","text":"Do you use a unique password for this account?","type":"yesno"},
    {"id":"q32","category":"account_security","text":"Do you use a password manager where appropriate?","type":"yesno"},
    {"id":"q33","category":"account_security","text":"Are login alerts enabled?","type":"yesno"},
    {"id":"q34","category":"account_security","text":"Do you review recovery information periodically?","type":"yesno"},
    {"id":"q35","category":"account_security","text":"Do you review active sessions and unknown devices?","type":"yesno"},
    {"id":"q36","category":"account_security","text":"Have you reported password reuse for this account?","type":"yesno"},
    # H Third-party apps
    {"id":"q37","category":"third_party_apps","text":"Do you regularly review connected third-party applications?","type":"yesno"},
    {"id":"q38","category":"third_party_apps","text":"Do you remove unused integrations?","type":"yesno"},
    {"id":"q39","category":"third_party_apps","text":"Do you review permissions granted to connected apps?","type":"yesno"},
    {"id":"q40","category":"third_party_apps","text":"Do you review old 'Sign in with social account' connections?","type":"yesno"},
    # I Messaging / Social Engineering
    {"id":"q41","category":"social_engineering","text":"Do you respond to suspicious or unexpected direct messages?","type":"frequency","options":["OFTEN","SOMETIMES","RARELY","NEVER"]},
    {"id":"q42","category":"social_engineering","text":"Do you click unexpected links received through social platforms?","type":"frequency","options":["OFTEN","SOMETIMES","RARELY","NEVER"]},
    {"id":"q43","category":"social_engineering","text":"Would you share a verification code if someone claiming to be support requested it?","type":"yesno"},
    {"id":"q44","category":"social_engineering","text":"Do you verify unfamiliar or impersonated accounts before trusting them?","type":"yesno"},
    {"id":"q45","category":"social_engineering","text":"Do you participate in suspicious giveaways or offers?","type":"frequency","options":["OFTEN","SOMETIMES","RARELY","NEVER"]},
    # J Digital Footprint
    {"id":"q46","category":"digital_footprint","text":"Do you have old public posts that you have never reviewed?","type":"yesno"},
    {"id":"q47","category":"digital_footprint","text":"Do you have old social accounts that you no longer use?","type":"yesno"},
    {"id":"q48","category":"digital_footprint","text":"Are older public comments still visible?","type":"yesno"},
    {"id":"q49","category":"digital_footprint","text":"Have you reviewed your public profile history recently?","type":"yesno"},
    {"id":"q50","category":"digital_footprint","text":"Do you periodically review your privacy settings?","type":"frequency","options":["REGULARLY","SOMETIMES","NEVER","NOT SURE"]},
]

CATEGORIES = {
    "profile":"Profile Exposure",
    "personal_info":"Personal Information",
    "location":"Location Exposure",
    "content":"Content Exposure",
    "connections":"Connection Risk",
    "tagging":"Tagging Risk",
    "account_security":"Account Security",
    "third_party_apps":"Third-Party App Risk",
    "social_engineering":"Social Engineering",
    "digital_footprint":"Digital Footprint",
}

WEIGHTS = {
    "profile":0.10, "personal_info":0.15, "location":0.15, "content":0.10,
    "connections":0.10, "tagging":0.05, "account_security":0.15,
    "third_party_apps":0.05, "social_engineering":0.10, "digital_footprint":0.05
}
