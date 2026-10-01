# Interview Preparation — 10 Questions and Strong Student Answers

## 1. Explain your project.
I built a defensive Social Media Privacy Risk Assessment Framework. Instead of accessing social-media accounts, it asks 50 self-assessment questions about visibility, personal-information exposure, location sharing, posts, connections, tagging, authentication, third-party apps, social engineering, and digital footprint. I convert the responses into ten category scores, calculate an overall 0–100 risk score, generate findings and recommendations, and provide an improvement simulator and report.

## 2. What is the difference between privacy and security?
Privacy is about how personal information is exposed, shared, and used. Security is about protecting accounts, systems, and information from unauthorized access or misuse. In my project I treat them as related but different areas.

## 3. What is a digital footprint?
It is the information associated with a person's online activity. I distinguish active footprint, which is deliberately shared information, from passive footprint, which can be generated or collected through online activity depending on the service context. My project evaluates only self-reported practices.

## 4. How does social engineering relate to this project?
Public context can sometimes make unwanted messages more believable. Therefore I assess behaviors such as accepting unknown connections, clicking unexpected links, sharing verification codes, and trusting impersonated accounts. I keep this defensive and do not generate attack scripts.

## 5. How did you design the risk score?
I created ten category scores from 0 to 100 and combine them using configurable weights that total 100%. Profile is 10%, personal information 15%, location 15%, content 10%, connections 10%, tagging 5%, account security 15%, third-party apps 5%, social engineering 10%, and digital footprint 5%.

## 6. Why is MFA included?
MFA adds another authentication factor beyond a password, so it can reduce account-takeover risk when a password is compromised. In my framework, disabled MFA increases the account-security risk score.

## 7. Why is data minimization important?
The framework does not need the actual phone number, email address, password, address, exact location, or private messages. It only needs to know whether those categories are exposed. That reduces unnecessary collection and follows privacy-by-design principles.

## 8. How did you handle third-party applications?
I ask whether connected applications and their permissions are reviewed and whether unused integrations are removed. The recommendation is to review and revoke unnecessary access according to least-privilege principles.

## 9. How did you test the application?
I created 35 automated unit tests covering private/public profiles, each major exposure category, scoring boundaries, validation, findings, recommendations, simulation, weight validation, and checks that sensitive fields are not part of the assessment data model.

## 10. What are the project's limitations?
The weights and thresholds are educational assumptions, not a professional risk standard. Platform privacy controls differ, self-reported answers may be inaccurate, and the score is not a probability of compromise. Before production use, the model would need validation, stronger security controls, and platform-specific policy mapping.
