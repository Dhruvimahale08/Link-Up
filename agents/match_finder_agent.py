from agno.agent import Agent
import pandas as pd

class MatchFinderAgent(Agent):
    def run(self, query: str) -> str:
        df = pd.read_csv("knowledge_base/student_profiles.csv")
        matches = []
        for _, row in df.iterrows():
            if query.lower() in row["interests"].lower() or query.lower() in row["struggles"].lower():
                matches.append(f"{row['name']} ({row['year']} Year - {row['branch']})")
        if not matches:
            return "No matches found."
        return "Students with similar interests or struggles:\n" + "\n".join(matches)
