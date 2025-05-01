class Add:
    def __init__(self):
        self.chains = {}  # Dictionary to store chains and their rules

    def add_chain(self):
        """Add a new chain."""
        chain_name = input("Enter the name of the chain: ").strip()
        table_name = input("Enter the table name (e.g., 'filter', 'nat'): ").strip()
        hook = input("Enter the hook (e.g., 'input', 'output', 'forward'): ").strip()
        priority = input("Enter the priority (e.g., '0', '-1'): ").strip()
        policy = input("Enter the policy (e.g., 'accept', 'drop'): ").strip()

        if chain_name in self.chains:
            print(f"Chain '{chain_name}' already exists.")
        else:
            self.chains[chain_name] = {
                "table": table_name,
                "hook": hook,
                "priority": priority,
                "policy": policy,
                "rules": []
            }
            print(f"Chain '{chain_name}' added successfully.")

        # Ask if the user wants to add rules inside the chain
        add_rule = input(f"Do you want to add rules to the chain '{chain_name}'? (yes/no): ").strip().lower()
        if add_rule == "yes":
            self.add_rule(chain_name)

    def add_rule(self, chain_name=None):
        """Add a new rule."""
        if not chain_name:
            chain_name = input("Enter the chain name to add the rule to: ").strip()
            if chain_name not in self.chains:
                print(f"Chain '{chain_name}' does not exist. Please add the chain first.")
                return

        print("\nRule Types:")
        print("1. Basic Rules")
        print("2. IP-Based Rules")
        print("3. Port-Based Rules")
        print("4. Logging and Monitoring Rules")
        print("5. Stateful Rules")
        print("6. Rate Limiting Rules")
        print("7. Advanced Rules")
        rule_type = input("Select the type of rule you want to add (1-7): ").strip()

        if rule_type == "1":
            self.add_basic_rule(chain_name)
        elif rule_type == "2":
            self.add_ip_based_rule(chain_name)
        elif rule_type == "3":
            self.add_port_based_rule(chain_name)
        elif rule_type == "4":
            self.add_logging_rule(chain_name)
        elif rule_type == "5":
            self.add_stateful_rule(chain_name)
        elif rule_type == "6":
            self.add_rate_limiting_rule(chain_name)
        elif rule_type == "7":
            self.add_advanced_rule(chain_name)
        else:
            print("Invalid choice. Please try again.")

    def add_basic_rule(self, chain_name):
        """Add a basic rule."""
        action = input("Enter the action (e.g., 'accept', 'drop', 'reject'): ").strip()
        rule = {"type": "basic", "action": action}
        self.chains[chain_name]["rules"].append(rule)
        print(f"Basic rule added to chain '{chain_name}'.")

    def add_ip_based_rule(self, chain_name):
        """Add an IP-based rule."""
        source = input("Enter the source IP address (e.g., '192.168.1.1/24', 'any'): ").strip()
        destination = input("Enter the destination IP address (e.g., '192.168.1.2/24', 'any'): ").strip()
        action = input("Enter the action (e.g., 'accept', 'drop', 'reject'): ").strip()
        rule = {"type": "ip", "source": source, "destination": destination, "action": action}
        self.chains[chain_name]["rules"].append(rule)
        print(f"IP-based rule added to chain '{chain_name}'.")

    def add_port_based_rule(self, chain_name):
        """Add a port-based rule."""
        protocol = input("Enter the protocol (e.g., 'tcp', 'udp'): ").strip()
        sport = input("Enter the source port (e.g., '80', 'any'): ").strip()
        dport = input("Enter the destination port (e.g., '443', 'any'): ").strip()
        action = input("Enter the action (e.g., 'accept', 'drop', 'reject'): ").strip()
        rule = {"type": "port", "protocol": protocol, "sport": sport, "dport": dport, "action": action}
        self.chains[chain_name]["rules"].append(rule)
        print(f"Port-based rule added to chain '{chain_name}'.")

    def add_logging_rule(self, chain_name):
        """Add a logging and monitoring rule."""
        log_prefix = input("Enter the log prefix (e.g., 'LOGGING: '): ").strip()
        log_level = input("Enter the log level (e.g., 'info', 'warning'): ").strip()
        rule = {"type": "logging", "log_prefix": log_prefix, "log_level": log_level}
        self.chains[chain_name]["rules"].append(rule)
        print(f"Logging rule added to chain '{chain_name}'.")

    def add_stateful_rule(self, chain_name):
        """Add a stateful rule."""
        state = input("Enter the connection state (e.g., 'new', 'established'): ").strip()
        action = input("Enter the action (e.g., 'accept', 'drop'): ").strip()
        rule = {"type": "stateful", "state": state, "action": action}
        self.chains[chain_name]["rules"].append(rule)
        print(f"Stateful rule added to chain '{chain_name}'.")

    def add_rate_limiting_rule(self, chain_name):
        """Add a rate-limiting rule."""
        limit = input("Enter the rate limit (e.g., '10/sec', '5/min'): ").strip()
        burst = input("Enter the burst limit (e.g., '20', '10'): ").strip()
        action = input("Enter the action (e.g., 'accept', 'drop'): ").strip()
        rule = {"type": "rate_limit", "limit": limit, "burst": burst, "action": action}
        self.chains[chain_name]["rules"].append(rule)
        print(f"Rate-limiting rule added to chain '{chain_name}'.")

    def add_advanced_rule(self, chain_name):
        """Add an advanced rule."""
        raw_rule = input("Enter the advanced rule details (e.g., 'meta l4proto tcp accept'): ").strip()
        rule = {"type": "advanced", "raw_rule": raw_rule}
        self.chains[chain_name]["rules"].append(rule)
        print(f"Advanced rule added to chain '{chain_name}'.")

    def display_chains_and_rules(self):
        """Display all chains and their rules."""
        if not self.chains:
            print("No chains or rules found.")
            return

        for chain_name, chain_data in self.chains.items():
            print(f"\nChain: {chain_name}")
            print(f"  Table: {chain_data['table']}")
            print(f"  Hook: {chain_data['hook']}")
            print(f"  Priority: {chain_data['priority']}")
            print(f"  Policy: {chain_data['policy']}")
            print("  Rules:")
            for rule in chain_data["rules"]:
                print(f"    - {rule}")

# Example usage
if __name__ == "__main__":
    add = Add()
    while True:
        print("\nOptions:")
        print("1. Add Chain")
        print("2. Add Rule")
        print("3. Display Chains and Rules")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            add.add_chain()
        elif choice == "2":
            add.add_rule()
        elif choice == "3":
            add.display_chains_and_rules()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

