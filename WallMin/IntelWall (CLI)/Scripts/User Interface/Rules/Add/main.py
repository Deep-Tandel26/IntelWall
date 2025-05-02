from ui_components import display_panel, get_input

class Add:
    def __init__(self, chains):
        """
        Initialize the Add class with the user's chains.
        :param chains: Dictionary to store chains and their rules.
        """
        self.chains = chains

    def add_chain(self, table_name=None):
        """Add a new chain."""
        display_panel("Add Chain", "[cyan]Please provide the details for the new chain.[/cyan]", "cyan")
        chain_name = get_input("[yellow]Enter the name of the chain: [/yellow]")
        hook = get_input("[yellow]Enter the hook (e.g., 'input', 'output', 'forward'): [/yellow]")
        priority = get_input("[yellow]Enter the priority (e.g., '0', '-1'): [/yellow]")
        policy = get_input("[yellow]Enter the policy (e.g., 'accept', 'drop'): [/yellow]")

        if chain_name in self.chains:
            return f"[red]Chain '{chain_name}' already exists.[/red]"
        else:
            self.chains[chain_name] = {
                "table": table_name,
                "hook": hook,
                "priority": priority,
                "policy": policy,
                "rules": []
            }
            return f"[green]Chain '{chain_name}' added successfully.[/green]"

    def add_rule(self):
        """Add a new rule."""
        display_panel("Add Rule", "[cyan]Please provide the details for the new rule.[/cyan]", "cyan")
        chain_name = get_input("[yellow]Enter the chain name to add the rule to: [/yellow]")
        if chain_name not in self.chains:
            return f"[red]Chain '{chain_name}' does not exist. Please add the chain first.[/red]"

        display_panel(
            "Rule Types",
            "[cyan]Select the type of rule you want to add:[/cyan]\n"
            "[yellow]1. Basic Rules\n2. IP-Based Rules\n3. Port-Based Rules\n"
            "4. Logging and Monitoring Rules\n5. Stateful Rules\n6. Rate Limiting Rules\n7. Advanced Rules[/yellow]",
            "cyan"
        )
        rule_type = get_input("[yellow]Enter the number corresponding to the rule type: [/yellow]")

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
            return "[red]Invalid rule type selected. Please try again.[/red]"

    def add_basic_rule(self, chain_name):
        """Add a basic rule."""
        action = get_input("[yellow]Enter the action (e.g., 'accept', 'drop', 'reject'): [/yellow]")
        rule = {"type": "basic", "action": action}
        self.chains[chain_name]["rules"].append(rule)
        return f"[green]Basic rule added to chain '{chain_name}'.[/green]"

    def add_ip_based_rule(self, chain_name):
        """Add an IP-based rule."""
        source = get_input("[yellow]Enter the source IP address (e.g., '192.168.1.1/24', 'any'): [/yellow]")
        destination = get_input("[yellow]Enter the destination IP address (e.g., '192.168.1.2/24', 'any'): [/yellow]")
        action = get_input("[yellow]Enter the action (e.g., 'accept', 'drop', 'reject'): [/yellow]")
        rule = {"type": "ip", "source": source, "destination": destination, "action": action}
        self.chains[chain_name]["rules"].append(rule)
        return f"[green]IP-based rule added to chain '{chain_name}'.[/green]"

    def add_port_based_rule(self, chain_name):
        """Add a port-based rule."""
        protocol = get_input("[yellow]Enter the protocol (e.g., 'tcp', 'udp'): [/yellow]")
        sport = get_input("[yellow]Enter the source port (e.g., '80', 'any'): [/yellow]")
        dport = get_input("[yellow]Enter the destination port (e.g., '443', 'any'): [/yellow]")
        action = get_input("[yellow]Enter the action (e.g., 'accept', 'drop', 'reject'): [/yellow]")
        rule = {"type": "port", "protocol": protocol, "sport": sport, "dport": dport, "action": action}
        self.chains[chain_name]["rules"].append(rule)
        return f"[green]Port-based rule added to chain '{chain_name}'.[/green]"

    def add_logging_rule(self, chain_name):
        """Add a logging and monitoring rule."""
        log_prefix = get_input("[yellow]Enter the log prefix (e.g., 'LOGGING: '): [/yellow]")
        log_level = get_input("[yellow]Enter the log level (e.g., 'info', 'warning'): [/yellow]")
        rule = {"type": "logging", "log_prefix": log_prefix, "log_level": log_level}
        self.chains[chain_name]["rules"].append(rule)
        return f"[green]Logging rule added to chain '{chain_name}'.[/green]"

    def add_stateful_rule(self, chain_name):
        """Add a stateful rule."""
        state = get_input("[yellow]Enter the connection state (e.g., 'new', 'established'): [/yellow]")
        action = get_input("[yellow]Enter the action (e.g., 'accept', 'drop'): [/yellow]")
        rule = {"type": "stateful", "state": state, "action": action}
        self.chains[chain_name]["rules"].append(rule)
        return f"[green]Stateful rule added to chain '{chain_name}'.[/green]"

    def add_rate_limiting_rule(self, chain_name):
        """Add a rate-limiting rule."""
        limit = get_input("[yellow]Enter the rate limit (e.g., '10/sec', '5/min'): [/yellow]")
        burst = get_input("[yellow]Enter the burst limit (e.g., '20', '10'): [/yellow]")
        action = get_input("[yellow]Enter the action (e.g., 'accept', 'drop'): [/yellow]")
        rule = {"type": "rate_limit", "limit": limit, "burst": burst, "action": action}
        self.chains[chain_name]["rules"].append(rule)
        return f"[green]Rate-limiting rule added to chain '{chain_name}'.[/green]"

    def add_advanced_rule(self, chain_name):
        """Add an advanced rule."""
        raw_rule = get_input("[yellow]Enter the advanced rule details (e.g., 'meta l4proto tcp accept'): [/yellow]")
        rule = {"type": "advanced", "raw_rule": raw_rule}
        self.chains[chain_name]["rules"].append(rule)
        return f"[green]Advanced rule added to chain '{chain_name}'.[/green]"

    def display_chains_and_rules(self):
        """Display all chains and their rules."""
        if not self.chains:
            return "[red]No chains or rules found.[/red]"

        output = []
        for chain_name, chain_data in self.chains.items():
            output.append(f"\n[cyan]Chain: {chain_name}[/cyan]")
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
    chains = {}
    add = Add(chains)
    while True:
        display_panel(
            "Options",
            "[cyan]Select an option:[/cyan]\n"
            "[yellow]1. Add Chain\n2. Add Rule\n3. Display Chains and Rules\n4. Exit[/yellow]",
            "cyan"
        )
        choice = get_input("[yellow]Enter your choice (1/2/3/4): [/yellow]")

        if choice == "1":
            print(add.add_chain())
        elif choice == "2":
            print(add.add_rule())
        elif choice == "3":
            print(add.display_chains_and_rules())
        elif choice == "4":
            print("[green]Exiting...[/green]")
            break
        else:
            print("[red]Invalid choice. Please try again.[/red]")

