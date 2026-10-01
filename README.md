# Social Media Privacy Risk Assessment Framework

## Overview
A privacy-focused cybersecurity framework for assessing social-media exposure, account-security practices, social-engineering awareness, and digital-footprint risk using synthetic/self-reported data.

## Problem Statement
Users may unintentionally expose personal context through profile visibility, contact information, location sharing, posts, tags, connections, third-party apps, and historical content. This project provides a structured educational assessment without accessing social-media accounts.

## Objectives
- Assess 50 privacy and security behaviors.
- Calculate 10 category risk scores and one overall 0–100 score.
- Generate findings and personalized defensive recommendations.
- Simulate privacy improvements.
- Provide a dashboard and printable HTML report.
- Demonstrate privacy-by-design principles.

## Cybersecurity Relevance
Relevant to cybersecurity analysis, privacy engineering, GRC, security awareness, application security, identity protection, and consulting.

## Privacy vs Security
Privacy controls exposure and use of personal information. Security protects systems/accounts from unauthorized access. Strong account security does not automatically mean strong privacy.

## Features
- 50-question questionnaire
- Server-side validation
- Privacy feature extraction
- 10 category scores
- Configurable weighted risk engine
- LOW / MODERATE / HIGH / CRITICAL classification
- Findings engine
- Recommendation engine
- Improvement simulator
- Synthetic 1,000-record dataset
- Aggregate dashboard
- Printable HTML report
- SQLite database
- 35 automated tests
- Privacy-by-design documentation

## Risk Categories
Profile Exposure, Personal Information, Location Exposure, Content Exposure, Connection Risk, Tagging Risk, Account Security, Third-Party App Risk, Social Engineering, Digital Footprint.

## Risk Scoring
Weights:
- Profile 10%
- Personal Information 15%
- Location 15%
- Content 10%
- Connections 10%
- Tagging 5%
- Account Security 15%
- Third-Party Apps 5%
- Social Engineering 10%
- Digital Footprint 5%

Thresholds:
- 0–20: LOW
- 21–40: MODERATE
- 41–70: HIGH
- 71–100: CRITICAL

Higher score = higher assessed exposure/risk.

These weights and thresholds are educational assumptions and should be validated before any professional risk decision.

## Architecture
User → Questionnaire → Validation → Feature Extraction → Category Analysis → Risk Scoring → Findings → Recommendations → Dashboard → Report.

See `docs/ARCHITECTURE.md`.

## Technology Stack
- Python 3.11+
- Flask
- SQLite
- HTML/CSS/JavaScript
- Chart.js for the aggregate dashboard

## Installation — Windows PowerShell

```powershell
git clone <repository-url>
cd Social-Media-Privacy-Risk-Assessment
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python data\generate_dataset.py
python -m backend.app
```

If `py` is unavailable, use:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python data\generate_dataset.py
python -m backend.app
```

Open:
- Assessment: `http://127.0.0.1:5000/assessment`
- Dashboard: `http://127.0.0.1:5000/dashboard`

## Safe Demo
Run:

```powershell
python data\demo_runner.py
```

The demo is fictional and demonstrates public profile/contact/location exposure, weak authentication controls, unknown connections, tagging, third-party app review, and historical-post review.

Then it simulates improvements such as private phone/birthday/location, rejecting unknown requests, enabling tag review/MFA/login alerts, reviewing apps, and reviewing old posts.

## API
### POST `/api/assessment`
Request:
```json
{"answers":{"q01":"PUBLIC","q02":true}}
```
A complete answer set is required.

### GET `/api/assessment/{id}`
Returns stored assessment results without questionnaire PII.

### GET `/api/assessment/{id}/recommendations`
Returns recommendations.

### POST `/api/assessment/simulate-improvement`
Simulates changes without modifying the stored assessment.

### GET `/api/dashboard/stats`
Returns aggregate score/risk-level statistics.

### GET `/api/privacy-checklist`
Returns the defensive checklist.

### GET `/api/report/{id}`
Returns printable HTML report.

## Database
Only assessment ID, category scores, overall score, risk level, finding types, and timestamps are persisted by the default application.

The framework avoids storing:
- phone numbers
- email addresses
- home addresses
- birth dates
- passwords
- exact locations
- private messages

## Testing
Run:

```powershell
python -m unittest discover -s tests -v
```

The suite includes 35 tests covering:
1. Fully private profile
2. Public profile
3. Public phone
4. Public email
5. Public birthday
6. Public location
7. Real-time check-ins
8. Travel plans
9. Workplace exposure
10. Education exposure
11. Public posts
12. Unknown connections
13. Tag review disabled
14. MFA disabled
15. Login alerts disabled
16. Password reuse
17. Unreviewed apps
18. Suspicious-link behavior
19. Old posts
20. Privacy settings review
21. Category calculation
22. Score range
23. Boundary 20
24. Boundary 40
25. Boundary 70/71
26. Findings
27. Recommendations
28. Improvement simulation
29. Validation
30. Invalid choices
31. Invalid boolean
32. Weight total
33. Sensitive-field check
34. Recommendation priority
35. Additional scoring consistency

## Security & Privacy Testing
Verify input validation, safe HTML rendering, environment-variable use for future secrets, report safety, local data handling, and deletion/retention controls before production use.

A production deployment should additionally add authentication, authorization, CSRF protection, strict Content Security Policy, rate limiting, secure cookies, HTTPS, audit logging, dependency scanning, and a formal threat model.

## Threat Model
See `docs/THREAT_MODEL.md`.

## Privacy by Design
See `docs/PRIVACY_BY_DESIGN.md`.

## Photo Metadata Awareness
See `docs/PHOTO_METADATA.md`.

## Ethical Disclaimer
This project is designed for defensive cybersecurity and privacy education. It uses synthetic or voluntarily provided assessment responses and does not scrape, track, enumerate, or profile real social-media users.

A high score indicates higher assessed exposure/risk; it is not a guarantee that an account will or will not be compromised.

## GitHub
Repository name:
`Social-Media-Privacy-Risk-Assessment`

Description:
`Privacy-focused cybersecurity framework for assessing social-media exposure, account-security practices, social-engineering risk, digital-footprint risk, and personalized privacy improvements using synthetic/self-reported data.`

Suggested topics:
`cybersecurity privacy social-media-privacy privacy-risk security-awareness python flask digital-footprint risk-assessment grc privacy-by-design defensive-security`

## Learning Outcomes
Python application development, REST APIs, risk modeling, feature engineering, privacy-by-design, data minimization, SQLite, testing, security awareness, dashboard development, and Git/GitHub workflows.
