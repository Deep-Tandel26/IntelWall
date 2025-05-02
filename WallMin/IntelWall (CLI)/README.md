# IntelWall (CLI) - Intelligent Firewall Management Tool

IntelWall is a command-line interface (CLI) tool designed to manage firewall rules and policies intelligently. It provides a user-friendly interface for adding, modifying, deleting, and reviewing firewall rules while ensuring user-specific data persistence.

---

## Technologies Used

### Programming Language:
- **Python 3.9+**

### Libraries:
- **[simplepam](https://pypi.org/project/simplepam/):** For PAM-based user authentication.
- **[Rich](https://pypi.org/project/rich/):** For creating a visually appealing CLI interface.
- **[JSON](https://docs.python.org/3/library/json.html):** For storing user-specific chains and rules in a hierarchical structure.

### Tools:
- **nftables:** The Linux kernel's firewall subsystem for managing chains and rules.

---

## Step-by-Step Working of IntelWall

### 1. Authentication
- The user is prompted to log in using their username.
- If PAM is enabled, the user must also provide a password.

### 2. Table Selection
- The user selects a table (e.g., `filter`, `nat`, etc.) to work with.

### 3. Main Menu
- The user is presented with four main options:
  1. Add Chains and Rules
  2. Delete Chains and Rules
  3. Modify Chains and Rules
  4. Review and Analyse Policies and Rules

### 4. Adding Chains and Rules
- **Add Chain**:
  - The user provides necessary details (e.g., chain name, hook, priority, policy).
  - The chain is saved in the `nftables` format.
- **Add Rule**:
  - The user selects a chain and provides rule details (e.g., source, destination, action).
  - The rule is saved in the `nftables` format.

### 5. Deleting Chains and Rules
- **Delete Chain**:
  - The user selects a chain to delete.
- **Delete Rule**:
  - The user selects a chain and a specific rule to delete.

### 6. Modifying Chains and Rules
- **Modify Chain**:
  - The user selects a chain and modifies its attributes (e.g., hook, priority, policy).
- **Modify Rule**:
  - The user selects a chain and modifies a specific rule.

### 7. Reviewing and Analyzing
- **Review Chains and Rules**:
  - Displays all chains and rules in the `nftables` format.
- **Analyze Chains and Rules**:
  - Highlights potential issues or optimizations (e.g., overly permissive rules).

### 8. Exit
- The user can exit the tool at any point, and their data is saved in their JSON file.

---

## Example JSON Format for Chains and Rules

```json
{
    "username": "john_doe",
    "chains": {
        "input_chain": {
            "table": "filter",
            "hook": "input",
            "priority": "0",
            "policy": "accept",
            "rules": [
                {
                    "type": "ip",
                    "source": "192.168.1.1/24",
                    "destination": "192.168.1.2/24",
                    "action": "accept"
                },
                {
                    "type": "port",
                    "protocol": "tcp",
                    "dport": "22",
                    "action": "drop"
                }
            ]
        }
    }
}
```
