import typer
from agents.match_finder_agent import MatchFinderAgent
from agents.mentor_suggester_agent import MentorSuggesterAgent


app = typer.Typer()

@app.command()
def match(query: str):
    agent = MatchFinderAgent(name="Match Finder")
    print(agent.run(query))

@app.command()
def mentor(goal: str):
    agent = MentorSuggesterAgent(name="Mentor Suggester")
    print(agent.run(goal))


if __name__ == "__main__":
    app()
