from repolens.models.issue import Issue

def calculate_score(issues: list[Issue]) -> int:
    return max(0, 100 - sum(issue.penalty for issue in issues))
