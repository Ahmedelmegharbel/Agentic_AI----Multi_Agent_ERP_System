import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

load_dotenv()

# Config & LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
mock_stock = {"Michelin": 10, "Bridgestone": 2}

# Agents defined


def get_crew(order):
    inventory_agent = Agent(
        role="Stock Controller",
        goal=f"Check if we have enough stock for: {order}. Current levels: {mock_stock}",
        backstory="You are a precise inventory logic gate.",
        llm=llm
    )

    procurement_agent = Agent(
        role="Purchaser",
        goal="If stock is < 5 after the order, write a short PO. Otherwise, say 'STABLE'.",
        backstory="You only act when replenishment is critical.",
        llm=llm
    )

    # Tasks defined
    check_stock = Task(
        description=f"Analyze order: {order}. Calculate remaining stock.",
        expected_output="A summary of stock after fulfillment.",
        agent=inventory_agent
    )

    refill_stock = Task(
        description="Review stock summary. Draft PO only if stock dropped below 5.",
        expected_output="A PO or the word 'STABLE'.",
        agent=procurement_agent
    )

    return Crew(agents=[inventory_agent, procurement_agent], tasks=[check_stock, refill_stock])


# Execute
if __name__ == "__main__":
    order_input = "4x Michelin tyres"
    erp_crew = get_crew(order_input)

    print(f"\n--- Processing Order: {order_input} ---\n")
    print(erp_crew.kickoff())
