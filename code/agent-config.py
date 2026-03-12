"""
AtithiAI - Azure AI Agent Client

This script connects to the Azure AI Foundry agent and enables
interactive conversations with the AtithiAI hotel assistant.

Author: Mannat Sardana
"""

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import ListSortOrder


# -------------------------------
# Azure Project Configuration
# -------------------------------

PROJECT_ENDPOINT = (
    "https://mannat-mjb3ghl3-eastus2.services.ai.azure.com/"
    "api/projects/mannat-mjb3ghl3-eastus2_project"
)

AGENT_ID = "asst_i0gxwds9xL2axMPFUlfi97My"


# -------------------------------
# Initialize Azure AI Client
# -------------------------------

def initialize_client():
    """
    Initialize Azure AI Project Client.

    Returns:
        AIProjectClient
    """
    return AIProjectClient(
        credential=DefaultAzureCredential(),
        endpoint=PROJECT_ENDPOINT
    )


# -------------------------------
# Start Conversation Thread
# -------------------------------

def create_thread(project):
    """
    Create a new conversation thread.

    Args:
        project: Azure AI Project client

    Returns:
        thread object
    """
    thread = project.agents.threads.create()
    print(f"\nStarted new conversation thread: {thread.id}\n")
    return thread


# -------------------------------
# Send Message to Agent
# -------------------------------

def send_message(project, thread_id, user_input):
    """
    Send user message to the AI agent.

    Args:
        project: Azure AI client
        thread_id: conversation thread id
        user_input: user query
    """

    project.agents.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_input
    )


# -------------------------------
# Run Agent
# -------------------------------

def run_agent(project, thread_id):
    """
    Run the AI agent and process the request.

    Args:
        project: Azure AI client
        thread_id: conversation thread id

    Returns:
        run result
    """

    return project.agents.runs.create_and_process(
        thread_id=thread_id,
        agent_id=AGENT_ID
    )


# -------------------------------
# Print Agent Responses
# -------------------------------

def print_responses(project, thread_id):
    """
    Retrieve and display agent responses.

    Args:
        project: Azure AI client
        thread_id: conversation thread id
    """

    messages = project.agents.messages.list(
        thread_id=thread_id,
        order=ListSortOrder.ASCENDING
    )

    for message in messages:
        if message.text_messages:
            response_text = message.text_messages[-1].text.value
            print(f"{message.role.capitalize()}: {response_text}")


# -------------------------------
# Main Application Loop
# -------------------------------

def main():
    """
    Run the AtithiAI assistant CLI.
    """

    print("🏨 Welcome to AtithiAI – Your Hotel Assistant")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    try:
        project = initialize_client()
        agent = project.agents.get_agent(AGENT_ID)

        thread = create_thread(project)

        while True:
            user_input = input("Guest: ").strip()

            if user_input.lower() in {"exit", "quit"}:
                print("\nAtithiAI: Thank you for visiting. Have a wonderful stay!")
                break

            send_message(project, thread.id, user_input)

            run = run_agent(project, thread.id)

            if run.status == "failed":
                print(f"Agent run failed: {run.last_error}")
                continue

            print_responses(project, thread.id)

    except Exception as error:
        print(f"Error occurred: {error}")


# -------------------------------
# Entry Point
# -------------------------------

if __name__ == "__main__":
    main()
