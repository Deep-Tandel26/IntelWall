from ui_components import display_panel, get_input

class Delete:
    def __init__(self, chains):
        """
        Initialize the Delete class with existing chains.
        :param chains: Dictionary containing chains and their rules.
        """
        self.chains = chains

    def delete_chain(self):
        """Delete an existing chain."""
        display_panel("Delete Chain", "Please provide the details for the chain to delete.", "cyan")
        chain_name = get_input("Enter the name of the chain to delete:")
        if chain_name in self.chains:
            del self.chains[chain_name]
            return f"Chain '{chain_name}' deleted successfully."
        else:
            return f"Chain '{chain_name}' does not exist."

    def delete_rule(self):
        """Delete a rule from an existing chain."""
        display_panel("Delete Rule", "Please provide the details for the rule to delete.", "cyan")
        chain_name = get_input("Enter the chain name to delete the rule from:")
        if chain_name not in self.chains:
            return f"Chain '{chain_name}' does not exist."

        if not self.chains[chain_name]["rules"]:
            return f"No rules found in chain '{chain_name}'."

        display_panel(
            "Rules in Chain",
            "Select the rule to delete:\n" +
            "\n".join(f"[bold yellow]{i + 1}. {rule}[/bold yellow]" for i, rule in enumerate(self.chains[chain_name]["rules"])),
            "cyan"
        )
        rule_index = get_input("Enter the number corresponding to the rule to delete:")
        if rule_index.isdigit() and 1 <= int(rule_index) <= len(self.chains[chain_name]["rules"]):
            rule = self.chains[chain_name]["rules"].pop(int(rule_index) - 1)
            return f"Rule '{rule}' deleted successfully from chain '{chain_name}'."
        else:
            return "Invalid rule selection. Please try again."

    def display_chains_and_rules(self):
        """Display all chains and their rules."""
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
                {"type": "basic", "action": "accept"},
                {"type": "ip", "source": "192.168.1.1/24", "destination": "192.168.1.2/24", "action": "drop"}
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

    delete = Delete(chains)
    while True:
        display_panel(
            "Options",
            "Select an option:\n"
            "[bold yellow]1. Delete Chain\n2. Delete Rule\n3. Display Chains and Rules\n4. Exit[/bold yellow]",
            "cyan"
        )
        choice = get_input("Enter your choice (1/2/3/4):")

        if choice == "1":
            output = delete.delete_chain()
            display_panel("Delete Chain Output", output, "green")
        elif choice == "2":
            output = delete.delete_rule()
            display_panel("Delete Rule Output", output, "green")
        elif choice == "3":
            output = delete.display_chains_and_rules()
            display_panel("Chains and Rules", output, "cyan")
        elif choice == "4":
            display_panel("Exit", "[bold magenta]Exiting...[/bold magenta]", "magenta")
            break
        else:
            display_panel("Error", "Invalid choice. Please try again.", "red")