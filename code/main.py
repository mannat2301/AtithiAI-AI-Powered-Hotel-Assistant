"""
AtithiAI - Hotel Management Assistant

This module runs the command-line interface for AtithiAI,
a hotel concierge assistant designed to answer common
guest questions about hotel policies and services.

Author: AtithiAI Project
"""

from typing import Dict

EXIT_COMMANDS = {"exit", "quit", "bye"}


def load_knowledge_base() -> Dict[str, str]:
    """
    Load predefined hotel FAQ responses.

    Returns:
        Dict[str, str]: Mapping of keywords to responses.
    """

    return {
        "check-in": "Check-in starts at 3:00 PM. [Source: hotel_policies.txt]",
        "check-out": "Check-out is by 12:00 PM. [Source: hotel_policies.txt]",
        "pet": "Pet policies vary by property. Please contact the front desk for specific details. [Source: hotel_policies.txt]",
        "shuttle": "Shuttle services may be available upon request. Please contact the front desk for availability. [Source: hotel_policies.txt]",
        "wifi": "Complimentary Wi-Fi is available for all registered guests. [Source: hotel_policies.txt]",
        "housekeeping": "Housekeeping services are available daily between 9:00 AM and 5:00 PM. [Source: hotel_policies.txt]",
    }


def generate_response(query: str, knowledge_base: Dict[str, str]) -> str:
    """
    Generate a response based on a guest query.

    Args:
        query (str): Guest question
        knowledge_base (Dict[str, str]): FAQ knowledge base

    Returns:
        str: Assistant response
    """

    query = query.lower()

    for keyword, response in knowledge_base.items():
        if keyword in query:
            return response

    return (
        "I need to check with a staff member. "
        "Please contact the hotel reception for further assistance."
    )


def run_assistant() -> None:
    """
    Start the interactive AtithiAI command-line assistant.
    """

    knowledge_base = load_knowledge_base()

    print("🏨 Welcome to AtithiAI – Your Hotel Assistant")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        user_input = input("Guest: ").strip()

        if user_input.lower() in EXIT_COMMANDS:
            print("\nAtithiAI: Thank you for choosing our hotel. Have a wonderful stay!")
            break

        response = generate_response(user_input, knowledge_base)
        print(f"AtithiAI: {response}")


if __name__ == "__main__":
    run_assistant()
