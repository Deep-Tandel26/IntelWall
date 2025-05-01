from ui_components import display_panel, get_input

class Add:
    def __init__(self):
        self.chains = {}  # Dictionary to store chains and their rules

    def add_chain(self):
        """Add a new chain."""
        display_panel("Add Chain", "Please provide the details for the new chain.", "cyan")
        chain_name = get_input("Enter the name of the chain:")
        table_name = get_input("Enter the table name (e.g., 'filter', 'nat'):")
        hook = get_input("Enter the hook (e.g., 'input', 'output', 'forward'):")
        priority = get_input("Enter the priority (e.g., '0', '-1'):")
        policy = get_input("Enter the policy (e.g., 'accept', 'drop'):")

        if chain_name in self.chains:
            return f"Chain '{chain_name}' already exists."
        else:
            self.chains[chain_name] = {
                "table": table_name,
                "hook": hook,
                "priority": priority,
                "policy": policy,
                "rules": []
            }
            return f"Chain '{chain_name}' added successfully."

    def add_rule(self):
        """Add a new rule."""
        display_panel("Add Rule", "Please provide the details for the new rule.", "cyan")
        chain_name = get_input("Enter the chain name to add the rule to:")
        if chain_name not in self.chains:
            return f"Chain '{chain_name}' does not exist. Please add the chain first."

        display_panel(
            "Rule Types",
            "Select the type of rule you want to add:\n"
            "[bold yellow]1. Basic Rules\n2. IP-Based Rules\n3. Port-Based Rules\n"
            "4. Logging and Monitoring Rules\n5. Stateful Rules\n6. Rate Limiting Rules\n7. Advanced Rules[/bold yellow]",
            "cyan"
        )
        rule_type = get_input("Enter the number corresponding to the rule type:")

        if rule_type == "1":
            return self.add_basic_rule(chain_name)
        elif rule_type == "2":
            return self.add_ip_based_rule(chain_name)
        elif rule_type == "3":
            return self.add_port_based_rule(chain_name)
        elif rule_type == "4":
            return self.add_logging_rule(chain_name)
        elif rule_type == "5":
            return self.add_stateful_rule(chain_name)
        elif rule_type == "6":
            return self.add_rate_limiting_rule(chain_name)
        elif rule_type == "7":
            return self.add_advanced_rule(chain_name)
        else:
            return "Invalid rule type selected."

    def add_basic_rule(self, chain_name):
        """Add a basic rule."""
        action = get_input("Enter the action (e.g., 'accept', 'drop', 'reject'):")
        rule = {"type": "basic", "action": action}
        self.chains[chain_name]["rules"].append(rule)
        return f"Basic rule added to chain '{chain_name}'."

    def add_ip_based_rule(self, chain_name):
        """Add an IP-based rule."""
        source = get_input("Enter the source IP address (e.g., '192.168.1.1/24', 'any'):")
        destination = get_input("Enter the destination IP address (e.g., '192.168.1.2/24', 'any'):")
        action = get_input("Enter the action (e.g., 'accept', 'drop', 'reject'):")
        rule = {"type": "ip", "source": source, "destination": destination, "action": action}
        self.chains[chain_name]["rules"].append(rule)
        return f"IP-based rule added to chain '{chain_name}'."

    def add_port_based_rule(self, chain_name):
        """Add a port-based rule."""
        protocol = get_input("Enter the protocol (e.g., 'tcp', 'udp'):")
        sport = get_input("Enter the source port (e.g., '80', 'any'):")
        dport = get_input("Enter the destination port (e.g., '443', 'any'):")
        action = get_input("Enter the action (e.g., 'accept', 'drop', 'reject'):")
        rule = {"type": "port", "protocol": protocol, "sport": sport, "dport": dport, "action": action}
        self.chains[chain_name]["rules"].append(rule)
        return f"Port-based rule added to chain '{chain_name}'."

    def add_logging_rule(self, chain_name):
        """Add a logging and monitoring rule."""
        log_prefix = get_input("Enter the log prefix (e.g., 'LOGGING: '):")
        log_level = get_input("Enter the log level (e.g., 'info', 'warning'):")
        rule = {"type": "logging", "log_prefix": log_prefix, "log_level": log_level}
        self.chains[chain_name]["rules"].append(rule)
        return f"Logging rule added to chain '{chain_name}'."

    def add_stateful_rule(self, chain_name):
        """Add a stateful rule."""
        state = get_input("Enter the connection state (e.g., 'new', 'established'):")
        action = get_input("Enter the action (e.g., 'accept', 'drop'):")
        rule = {"type": "stateful", "state": state, "action": action}
        self.chains[chain_name]["rules"].append(rule)
        return f"Stateful rule added to chain '{chain_name}'."

    def add_rate_limiting_rule(self, chain_name):
        """Add a rate-limiting rule."""
        limit = get_input("Enter the rate limit (e.g., '10/sec', '5/min'):")
        burst = get_input("Enter the burst limit (e.g., '20', '10'):")
        action = get_input("Enter the action (e.g., 'accept', 'drop'):")
        rule = {"type": "rate_limit", "limit": limit, "burst": burst, "action": action}
        self.chains[chain_name]["rules"].append(rule)
        return f"Rate-limiting rule added to chain '{chain_name}'."

    def add_advanced_rule(self, chain_name):
        """Add an advanced rule."""
        raw_rule = get_input("Enter the advanced rule details (e.g., 'meta l4proto tcp accept'):")
        rule = {"type": "advanced", "raw_rule": raw_rule}
        self.chains[chain_name]["rules"].append(rule)
        return f"Advanced rule added to chain '{chain_name}'."

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
    add = Add()
    while True:
        display_panel(
            "Options",
            "Select an option:\n"
            "[bold yellow]1. Add Chain\n2. Add Rule\n3. Display Chains and Rules\n4. Exit[/bold yellow]",
            "cyan"
        )
        choice = get_input("Enter your choice (1/2/3/4):")

        if choice == "1":
            print(add.add_chain())
        elif choice == "2":
            print(add.add_rule())
        elif choice == "3":
            print(add.display_chains_and_rules())
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

