# Agentic_AI----Multi_Agent_ERP_System

-- Agentic ERP: Tyre Inventory Manager --

A lightweight, multi-agent system built with CrewAI to automate the supply chain from order validation to procurement triggers.

===========================================================================================================================================

-- Overview --

This project demonstrates how two specialized AI agents collaborate to manage a tyre warehouse:

Stock Controller "inventory_agent": Validates incoming orders against a mock database and calculates remaining inventory.

Purchaser "procurement_agent": Monitoring the output of the Controller, this agent automatically drafts a Purchase Order (PO) only if stock levels drop below a critical threshold (5 units).

=====================================================================================================================================================

-- Quick Start --

1. Prerequisites
Ensure you have Python 3.10+ installed.

2. Installation
Install the core dependencies:
Bash
pip install crewai langchain-openai python-dotenv

3. Environment Setup
Add your OpenAI API key to a .env file in the root directory
.env file
OPENAI_API_KEY=add_key_here

4. Run the System
Bash
python agent.py

