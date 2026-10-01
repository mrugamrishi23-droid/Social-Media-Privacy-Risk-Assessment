# Project Report — Social Media Privacy Risk Assessment Framework

## Abstract
This project presents a defensive, privacy-first framework for assessing self-reported social-media privacy exposure and account-security practices. It uses a 50-question questionnaire, feature extraction, ten category scores, configurable weighted scoring, findings, recommendations, an improvement simulator, a dashboard, and an assessment report. Synthetic data is provided for aggregate analytics.

## Introduction
Social-media privacy concerns arise when personal context, location, relationships, content, and account-security practices are more exposed than intended. The framework provides an educational way to identify common exposure categories without scraping or profiling real users.

## Problem Statement
Users often review privacy settings inconsistently and may not understand how public information, tagging, location sharing, old posts, third-party applications, and authentication controls interact.

## Objectives
- Assess privacy exposure using self-reported answers.
- Produce interpretable category scores.
- Identify privacy weaknesses.
- Provide prioritized defensive recommendations.
- Simulate improvements.
- Demonstrate privacy-by-design engineering.

## Privacy vs Security
Privacy controls how information is exposed, shared, and used. Security protects accounts and systems from unauthorized access or misuse. Strong account security does not automatically mean strong privacy.

## Proposed Framework
User → Questionnaire → Validation → Feature Extraction → Category Analysis → Risk Scoring → Findings → Recommendations → Dashboard/Report.

## Risk Scoring
The framework uses ten educational weights: Profile 10%, Personal Information 15%, Location 15%, Content 10%, Connections 10%, Tagging 5%, Account Security 15%, Third-Party Apps 5%, Social Engineering 10%, Digital Footprint 5%.

## Risk Levels
0–20 LOW, 21–40 MODERATE, 41–70 HIGH, 71–100 CRITICAL. Higher values mean higher assessed exposure/risk.

## Synthetic Dataset
`data/generate_dataset.py` creates 1,000 fictional records. No real social-media data is used.

## Testing
The project contains 35 automated unit tests covering questionnaire validation, category scoring, boundaries, findings, recommendations, simulation, and privacy-storage assumptions.

## Limitations
The weights and thresholds are educational assumptions. Platform-specific settings vary. Self-reported answers can be inaccurate. The score is not a probability of compromise and is not a professional security certification.

## Future Scope
Platform-specific checklists, privacy maturity scoring, enterprise awareness training, GRC reporting, anonymized trend analysis, localization, accessibility, longitudinal comparisons, and a local-only client mode.

## Conclusion
The framework demonstrates defensive cybersecurity, privacy engineering, data minimization, risk scoring, security awareness, and application development while avoiding invasive monitoring.
