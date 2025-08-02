# crew_ai_agent_web_research_agent
This project is an intelligent research assistant built using CrewAI, Groq’s LLaMA 3-70B, and Exa real-time web search API. It simulates a multi-agent system where one AI agent performs focused web research while another agent summarizes the results in a student-friendly format.
Key Features
Multi-Agent Workflow: Uses CrewAI to simulate a collaborative task between two specialized AI agents — a Web Researcher and a Technical Summarizer.

Groq + LLaMA 3: High-speed, low-latency large language model generation using Groq’s blazing-fast inference of Meta’s LLaMA 3 (70B).

Real-Time Web Search: Powered by Exa, the assistant fetches current information live from the internet.

User Input Driven: Accepts any custom research query from the user and delivers structured, useful results.

Tech Stack
Python

CrewAI – Multi-agent orchestration

langchain_groq – Groq LLM integration

exa_py – Real-time web search API

python-dotenv – For environment variable management

How It Works
User enters a research topic.

The Research Agent uses Exa to search the web and collect factual, relevant info.

The Summarizer Agent converts the raw findings into a clean, simple summary.

Results are printed for the user to read or copy.

Example Use Cases
Preparing notes for technical topics

Gathering up-to-date insights on fast-moving fields (e.g., AI, crypto, medicine)

Academic research assistance
