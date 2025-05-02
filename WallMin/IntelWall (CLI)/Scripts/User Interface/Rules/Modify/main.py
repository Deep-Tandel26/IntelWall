from ui_components import display_panel, get_input

class Modify:
    def __init__(self, chains):
        """
        Initialize the Modify class with existing chains.
        :param chains: Dictionary containing chains and their rules.
        """
        self.chains = chains

    def modify_chain(self):
        """Modify an existing chain."""
        display_panel("Modify Chain", "Enter the details of the chain to modify.", "cyan")
        chain_name = get_input("Enter the name of the chain to modify: ")
        if chain_name not in self.chains:
            return f"[bold red]Chain '{chain_name}' does not exist.[/bold red]"

        display_panel(
            "Modify Chain Options",
            "Select the attribute to modify:\n"
            "[bold yellow]1. Table\n2. Hook\n3. Priority\n4. Policy[/bold yellow]",
            "cyan"
        )
        attribute = get_input("Enter the number corresponding to the attribute to modify: ")
        if attribute == "1":
            new_table = get_input("Enter the new table name (e.g., 'filter', 'nat'): ")
            self.chains[chain_name]["table"] = new_table
            return f"[bold green]Table for chain '{chain_name}' updated to '{new_table}'.[/bold green]"
        elif attribute == "2":
            new_hook = get_input("Enter the new hook (e.g., 'input', 'output', 'forward'): ")
            self.chains[chain_name]["hook"] = new_hook
            return f"[bold green]Hook for chain '{chain_name}' updated to '{new_hook}'.[/bold green]"
        elif attribute == "3":
            new_priority = get_input("Enter the new priority (e.g., '0', '-1'): ")
            self.chains[chain_name]["priority"] = new_priority
            return f"[bold green]Priority for chain '{chain_name}' updated to '{new_priority}'.[/bold green]"
        elif attribute == "4":
            new_policy = get_input("Enter the new policy (e.g., 'accept', 'drop'): ")
            self.chains[chain_name]["policy"] = new_policy
            return f"[bold green]Policy for chain '{chain_name}' updated to '{new_policy}'.[/bold green]"
        else:
            return "[bold red]Invalid attribute selection. Please try again.[/bold red]"

    def modify_rule(self):
        """Modify a rule in an existing chain."""
        display_panel("Modify Rule", "Enter the details of the rule to modify.", "cyan")
        chain_name = get_input("Enter the chain name to modify the rule in: ")
        if chain_name not in self.chains:
            return f"[bold red]Chain '{chain_name}' does not exist.[/bold red]"

        if not self.chains[chain_name]["rules"]:
            return f"[bold red]No rules found in chain '{chain_name}'.[/bold red]"

        display_panel(
            "Rules in Chain",
            "Select the rule to modify:\n" +
            "\n".join(f"[bold yellow]{i + 1}. {rule}[/bold yellow]" for i, rule in enumerate(self.chains[chain_name]["rules"])),
            "cyan"
        )
        rule_index = get_input("Enter the number corresponding to the rule to modify: ")
        if rule_index.isdigit() and 1 <= int(rule_index) <= len(self.chains[chain_name]["rules"]):
            rule = self.chains[chain_name]["rules"][int(rule_index) - 1]
            display_panel(
                "Modify Rule Options",
                "Select the attribute to modify:\n"
                "[bold yellow]1. Source\n2. Destination\n3. Protocol\n4. Ports\n5. Action[/bold yellow]",
                "cyan"
            )
            attribute = get_input("Enter the number corresponding to the attribute to modify: ")
            if attribute == "1":
                new_source = get_input("Enter the new source IP address (e.g., '192.168.1.1/24', 'any'): ")
                rule["source"] = new_source
                return f"[bold green]Source for rule updated to '{new_source}'.[/bold green]"
            elif attribute == "2":
                new_destination = get_input("Enter the new destination IP address (e.g., '192.168.1.2/24', 'any'): ")
                rule["destination"] = new_destination
                return f"[bold green]Destination for rule updated to '{new_destination}'.[/bold green]"
            elif attribute == "3":
                new_protocol = get_input("Enter the new protocol (e.g., 'tcp', 'udp'): ")
                rule["protocol"] = new_protocol
                return f"[bold green]Protocol for rule updated to '{new_protocol}'.[/bold green]"
            elif attribute == "4":
                new_ports = get_input("Enter the new ports (e.g., '80', '443'): ")
                rule["ports"] = new_ports
                return f"[bold green]Ports for rule updated to '{new_ports}'.[/bold green]"
            elif attribute == "5":
                new_action = get_input("Enter the new action (e.g., 'accept', 'drop'): ")
                rule["action"] = new_action
                return f"[bold green]Action for rule updated to '{new_action}'.[/bold green]"
            else:
                return "[bold red]Invalid attribute selection. Please try again.[/bold red]"
        else:
            return "[bold red]Invalid rule selection. Please try again.[/bold red]"

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
                {"source": "192.168.1.1/24", "destination": "192.168.1.2/24", "protocol": "tcp", "ports": "80", "action": "accept"}
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

    modify = Modify(chains)
    while True:
        display_panel(
            "Options",
            "Select an option:\n"
            "[bold yellow]1. Modify Chain\n2. Modify Rule\n3. Display Chains and Rules\n4. Exit[/bold yellow]",
            "cyan"
        )
        choice = get_input("Enter your choice (1/2/3/4):")

        if choice == "1":
            output = modify.modify_chain()
            display_panel("Modify Chain Output", output, "green")
        elif choice == "2":
            output = modify.modify_rule()
            display_panel("Modify Rule Output", output, "green")
        elif choice == "3":
            output = modify.display_chains_and_rules()
            display_panel("Chains and Rules", output, "cyan")
        elif choice == "4":
            display_panel("Exit", "[bold magenta]Exiting...[/bold magenta]", "magenta")
            break
        else:
            display_panel("Error", "Invalid choice. Please try again.", "red")