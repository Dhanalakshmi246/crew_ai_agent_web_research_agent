import os
from dotenv import load_dotenv
from exa_py import Exa

from crewai import Agent, Task, Crew, LLM

# Load environment variables from .env file
load_dotenv()

# Get API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
EXA_API_KEY = os.getenv("EXA_API_KEY")

# Initialize LLM using CrewAI's wrapper
llm = LLM(
    model="llama3-70b-8192",
    provider="groq",
    api_key=GROQ_API_KEY
)

# Initialize Exa client
exa = Exa(EXA_API_KEY)

# Ask user for a research topic
query = input("Enter your research query: ").strip()

# Validate query
if not query:
    print("❌ You must enter a non-empty query.")
    exit()

# Perform Exa web search
search_results = exa.search(query, use_autoprompt=True, num_results=5)

# Extract search result content
context = "\n\n".join(
    [f"- {r.title}\n{r.text}" for r in search_results.results]
)

# Define agents
researcher = Agent(
    role="Web Research Specialist",
    goal="Find and organize the most relevant, trustworthy information for a topic",
    backstory="You're great at finding accurate and concise information from the internet.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

summarizer = Agent(
    role="Technical Summarizer",
    goal="Summarize complex research into student-friendly content",
    backstory="You're an expert in simplifying tough technical content.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Define tasks
research_task = Task(
    description=f"Research the topic: '{query}' using the information below:\n\n{context}",
    expected_output="A list of well-organized, factual key findings.",
    agent=researcher
)

summary_task = Task(
    description="Summarize the research findings into simple, clear language suitable for students.",
    expected_output="A concise and easy-to-understand summary of the topic.",
    agent=summarizer
)

# Create crew and run it
crew = Crew(
    agents=[researcher, summarizer],
    tasks=[research_task, summary_task],
    verbose=True
)

# Run the CrewAI workflow
result = crew.kickoff()

# Print the final result
print("\n📄 Final Summary:\n")
print(result)
