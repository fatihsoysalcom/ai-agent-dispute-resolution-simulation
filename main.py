import datetime

class AIAgent:
    """Represents an autonomous AI agent capable of making decisions/actions."""
    def __init__(self, agent_id: str, initial_funds: float = 1000.0):
        self.agent_id = agent_id
        self.funds = initial_funds
        print(f"AI Agent '{self.agent_id}' initialized with {self.funds:.2f} funds.")

    def propose_transaction(self, amount: float) -> dict:
        """Simulates an AI agent proposing a financial transaction."""
        action_time = datetime.datetime.now().isoformat()
        print(f"  Agent '{self.agent_id}' proposes transaction of {amount:.2f} at {action_time}.")
        return {
            "agent_id": self.agent_id,
            "action_type": "financial_transaction",
            "amount": amount,
            "timestamp": action_time
        }

class DigitalContract:
    """Represents a simplified digital contract with terms for transactions."""
    def __init__(self, contract_id: str, min_amount: float, max_amount: float, max_daily_transactions: int = 5):
        self.contract_id = contract_id
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.max_daily_transactions = max_daily_transactions
        self.daily_transactions = {} # {agent_id: {"date": "YYYY-MM-DD", "count": N}}
        print(f"Digital Contract '{self.contract_id}' established: Min={min_amount:.2f}, Max={max_amount:.2f}, Max Daily Txn={max_daily_transactions}.")

    def check_transaction_compliance(self, agent_id: str, amount: float) -> bool:
        """Checks if a proposed transaction complies with contract terms."""
        # Check amount limits
        if not (self.min_amount <= amount <= self.max_amount):
            print(f"    Contract violation: Amount {amount:.2f} is outside [{self.min_amount:.2f}, {self.max_amount:.2f}].")
            return False

        # Check daily transaction limits (simplified for demonstration)
        today = datetime.date.today().isoformat()
        
        if agent_id not in self.daily_transactions or self.daily_transactions[agent_id]["date"] != today:
            self.daily_transactions[agent_id] = {"date": today, "count": 0}

        if self.daily_transactions[agent_id]["count"] >= self.max_daily_transactions:
            print(f"    Contract violation: Agent '{agent_id}' exceeded daily transaction limit ({self.max_daily_transactions}).")
            return False
        
        # If all checks pass, increment count and return True
        self.daily_transactions[agent_id]["count"] += 1
        return True

class InternetCourt:
    """Simulates the Internet Court for AI agents, resolving disputes based on rules."""
    def __init__(self, court_name: str = "Digital Justice Tribunal"):
        self.court_name = court_name
        print(f"\n--- {self.court_name} is now in session ---")

    def adjudicate_dispute(self, agent: AIAgent, contract: DigitalContract, proposed_action: dict) -> str:
        """
        Adjudicates a proposed action by an AI agent against a digital contract.
        This function represents the core concept of the article: resolving AI agent disputes.
        """
        print(f"\n{self.court_name} reviewing action by Agent '{agent.agent_id}':")
        print(f"  Proposed action: {proposed_action['action_type']} of {proposed_action['amount']:.2f}")
        print(f"  Against Contract '{contract.contract_id}' terms.")

        # --- This is where the 'court' logic for AI agent disputes happens ---
        # The court checks if the agent's proposed action complies with the contract.
        if contract.check_transaction_compliance(proposed_action["agent_id"], proposed_action["amount"]):
            # If compliant, the action is approved.
            agent.funds -= proposed_action["amount"] # Execute the transaction
            print(f"  Verdict: APPROVED. Action is compliant with contract '{contract.contract_id}'.")
            print(f"  Agent '{agent.agent_id}' funds remaining: {agent.funds:.2f}.")
            return "APPROVED"
        else:
            # If not compliant, the action is rejected, and a 'breach' is noted.
            print(f"  Verdict: REJECTED. Action violates contract '{contract.contract_id}'.")
            print(f"  Potential contract breach by Agent '{agent.agent_id}'.")
            return "REJECTED - CONTRACT BREACH"

# --- Main execution simulation ---
if __name__ == "__main__":
    # 1. Initialize an AI Agent
    ai_agent_alpha = AIAgent("AlphaBot", initial_funds=5000.0)

    # 2. Define a Digital Contract
    investment_contract = DigitalContract("InvestCo-001", min_amount=100.0, max_amount=1000.0, max_daily_transactions=2)

    # 3. Initialize the Internet Court
    internet_court = InternetCourt()

    # --- Scenario 1: Compliant transaction ---
    print("\n--- Scenario 1: Agent proposes a compliant transaction ---")
    action1 = ai_agent_alpha.propose_transaction(500.0)
    court_decision1 = internet_court.adjudicate_dispute(ai_agent_alpha, investment_contract, action1)
    print(f"Final Court Decision for Action 1: {court_decision1}")

    # --- Scenario 2: Transaction violating amount limits ---
    print("\n--- Scenario 2: Agent proposes a transaction violating amount limits ---")
    action2 = ai_agent_alpha.propose_transaction(1500.0) # Too high
    court_decision2 = internet_court.adjudicate_dispute(ai_agent_alpha, investment_contract, action2)
    print(f"Final Court Decision for Action 2: {court_decision2}")

    # --- Scenario 3: Transaction violating daily transaction limits ---
    print("\n--- Scenario 3: Agent proposes a transaction violating daily limits ---")
    # First, make another compliant transaction to reach the limit
    action3_part1 = ai_agent_alpha.propose_transaction(200.0)
    internet_court.adjudicate_dispute(ai_agent_alpha, investment_contract, action3_part1)
    
    # Now, the next transaction should exceed the daily limit (2 transactions allowed)
    action3_part2 = ai_agent_alpha.propose_transaction(300.0)
    court_decision3 = internet_court.adjudicate_dispute(ai_agent_alpha, investment_contract, action3_part2)
    print(f"Final Court Decision for Action 3: {court_decision3}")

    print("\n--- Simulation End ---")
