from typing import Any, Dict, List

TeamData = Dict[str, List[Dict[str, Any]]]

def get_unique_skills(teams: TeamData) -> List[str]:
    return sorted({skill for members in teams.values() for member in members for skill in member["skills"]})

def get_member_team_mapping(teams: TeamData) -> Dict[str, str]:
    return {member["name"]: team for team, members in teams.items() for member in members}

def get_large_team_counts(teams: TeamData) -> Dict[str, int]:
    return {team: len(members) for team, members in teams.items() if len(members) > 1}

if __name__ == "__main__":
    teams_data = {
        "backend": [{"name": "asha", "skills": ["python", "sql"]},
                    {"name": "ravi", "skills": ["python", "redis"]}],
        "frontend": [{"name": "meera", "skills": ["react", "css"]}],
    }

print("Unique Skills:", get_unique_skills(teams_data))
print("Member Mapping:", get_member_team_mapping(teams_data))
print("Large Teams:", get_large_team_counts(teams_data))