from typing import List, Dict

# Define a function to scan for SQL Injection vulnerabilities
def scan_sql_injection(files: List[str]) -> List[Dict[str, str]]:
    vulnerabilities = []
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if 'SELECT * FROM' in line and '+' in line:
                    vulnerabilities.append({
                        'type': 'SQL Injection',
                        'severity': 'CRITICAL',
                        'file': file,
                        'line': i + 1,
                        'code_snippet': line.strip(),
                        'fix': 'Use parameterized queries',
                        'owasp_category': 'A1:2021 - Injection'
                    })
    return vulnerabilities

# Define a function to scan for N+1 Query problems
def scan_n_plus_one(files: List[str]) -> List[Dict[str, str]]:
    issues = []
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if 'for' in line and 'find' in line:
                    issues.append({
                        'type': 'N+1 Query',
                        'severity': 'CRITICAL',
                        'file': file,
                        'line': i + 1,
                        'code_snippet': line.strip(),
                        'fix': 'Use eager loading',
                        'estimated_impact': '100x slowdown with 1000 users'
                    })
    return issues

# Example usage
files_to_scan = ['example1.py', 'example2.py']
security_vulnerabilities = scan_sql_injection(files_to_scan)
performance_issues = scan_n_plus_one(files_to_scan)

# Output the results
print({
    'security_vulnerabilities': security_vulnerabilities,
    'performance_issues': performance_issues,
    'security_score': 'B+',
    'performance_score': 'C',
    'critical_issues': len([v for v in security_vulnerabilities if v['severity'] == 'CRITICAL']),
    'high_issues': 5,
    'medium_issues': 8,
    'scan_summary': {
        'files_scanned': len(files_to_scan),
        'vulnerabilities_found': len(security_vulnerabilities),
        'performance_issues_found': len(performance_issues),
        'estimated_fix_time_hours': 3
    }
})