# TITANCORP: PERIMETER ASSESSMENT REPORT
**Operator:** **Target Subnet:** 172.88.0.0/24

## PHASE 1: ACTIVE ENUMERATION (NMAP)
*(List the live IPs discovered and their running services/versions)*
- Host 1 (172.88.0.10): nginx 1.14.2
- Host 2 (172.88.0.15): [Unknown/Filtered]
- Host 3 (172.88.0.20): Apache httpd 2.4.66

## PHASE 2: VULNERABILITY AUDIT (NIKTO)
*(Run Nikto against the TWO web servers discovered above. List one major finding for each.)*
- Web Server 1 Finding: 172.88.0.10 lacks the anti-clickjacking X-Frame-Options header, which could allow an attacker to overlay malicious frames over the site.
- Web Server 2 Finding: 172.88.0.20 is running an outdated Apache httpd 2.4.66 server, which may be susceptible to known vulnerabilities and service-specific exploits.

## PHASE 3: RISK TRIAGE
*(Review your findings. Identify the SINGLE highest-risk vulnerability across the entire DMZ. Justify why it is the top priority using the Likelihood x Impact formula.)
- Top Priority Finding: Outdated nginx 1.14.2 on 172.88.0.10.
- Justification: This represents the highest risk because the likelihood of exploitation is high due to the presence of known public vulnerabilities for this version, and the impact is critical as it could result in full host compromise through Remote Code Execution.
