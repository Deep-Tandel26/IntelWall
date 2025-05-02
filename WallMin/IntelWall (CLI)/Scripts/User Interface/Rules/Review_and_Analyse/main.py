from ui_components import display_panel, get_input

class ReviewAndAnalyse:
    def __init__(self, chains):
        """
        Initialize the ReviewAndAnalyse class with existing chains.
        :param chains: Dictionary containing chains and their rules.
        """
        self.chains = chains

    def review_chains_and_rules(self):
        """Review all chains and their rules."""
        if not self.chains:
            return "No chains or rules found."

        output = []
        for chain_name, chain_data in self.chains.items():
            output.append(f"\nChain: {chain_name}")
            output.append(f"  Table: {chain_data['table']}")
            output.append(f"  Hook: {chain_data['hook']}")
            output.append(f"  Priority: {chain_data['priority']}")
            output.append(f"  Policy: {chain_data['policy']}")
            output.append("  Rules:")
            for rule in chain_data["rules"]:
                output.append(f"    - {rule}")
        return "\n".join(output)

    def analyse_chains_and_rules(self):
        """Analyze chains and rules for potential issues or optimizations."""
        if not self.chains:
            return "No chains or rules found to analyze."

        output = []
        for chain_name, chain_data in self.chains.items():
            output.append(f"\nAnalyzing Chain: {chain_name}")
            if chain_data["policy"] == "accept" and not chain_data["rules"]:
                output.append(f"  [bold red]Warning:[/bold red] Chain '{chain_name}' has an 'accept' policy but no rules.")
            for rule in chain_data["rules"]:
                if rule.get("type") == "ip" and rule.get("source") == "any" and rule.get("destination") == "any":
                    output.append(f"  [bold yellow]Optimization:[/bold yellow] Rule '{rule}' in chain '{chain_name}' allows all traffic. Consider restricting it.")
                if rule.get("type") == "port" and rule.get("protocol") == "tcp" and rule.get("dport") == "22":
                    output.append(f"  [bold yellow]Optimization:[/bold yellow] Rule '{rule}' in chain '{chain_name}' allows SSH traffic. Ensure it's secured.")
        return "\n".join(output)

# Example usage
if __name__ == "__main__":
    # Mock data for testing
    chains = {
        "chain1": {
            "table": "filter",
            "hook": "input",
            "priority": "0",
            "policy": "accept",
            "rules": [
                {"type": "ip", "source": "any", "destination": "any", "action": "accept"},
                {"type": "port", "protocol": "tcp", "dport": "22", "action": "accept"}
            ]
        },
        "chain2": {
            "table": "nat",
            "hook": "output",
            "priority": "-1",
            "policy": "drop",
            "rules": []
        }
    }

    review_and_analyse = ReviewAndAnalyse(chains)
    while True:
        display_panel(
            "Options",
            "Select an option:\n"
            "[bold yellow]1. Review Chains and Rules\n2. Analyze Chains and Rules\n3. Exit[/bold yellow]",
            "cyan"
        )
        choice = get_input("Enter your choice (1/2/3):")

        if choice == "1":
            output = review_and_analyse.review_chains_and_rules()
            display_panel("Review Chains and Rules", output, "cyan")
        elif choice == "2":
            output = review_and_analyse.analyse_chains_and_rules()
            display_panel("Analyze Chains and Rules", output, "cyan")
        elif choice == "3":
            display_panel("Exit", "[bold magenta]Exiting...[/bold magenta]", "magenta")
            break
        else:
            display_panel("Error", "Invalid choice. Please try again.", "red")