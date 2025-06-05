from agno.agent import Agent
import pandas as pd

class MentorSuggesterAgent(Agent):
    def run(self, query: str) -> str:
        df = pd.read_csv("knowledge_base/student_profiles.csv")
        suggestions = []
        for _, row in df.iterrows():
            if int(row["year"]) > 1 and query.lower() in row["goals"].lower():
                suggestions.append(f"{row['name']} ({row['year']} Year - {row['branch']})")
        return "Recommended mentors:\n" + "\n".join(suggestions) if suggestions else "No suitable mentors found."
