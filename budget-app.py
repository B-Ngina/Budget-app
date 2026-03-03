** start of main.py **

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    def get_balance(self):
        total_balance = 0
        for item in self.ledger:
            total_balance += item["amount"]
        return total_balance
    def transfer(self, amount, category_instance):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category_instance.name}")
            category_instance.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
    def __str__(self):
        title = f"{self.name.center(30, '*')}\n"
        items = ""
        for item in self.ledger:
           
            desc = item["description"][:23] 
            amount = f"{item['amount']:>7.2f}"
            
            items += f"{desc:<23}{amount[:7]}\n"
        
        total = f"Total: {self.get_balance()}"
        
        return title + items + total
def create_spend_chart(categories):
    spent = []
    for cat in categories:
        total = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])
        spent.append(total)

    total_spent = sum(spent)
    res = "Percentage spent by category\n"
    percentages = []
    for s in spent:
        percentages.append((s / total_spent * 100) // 10 * 10)
    for i in range(100, -1, -10):
        res += f"{str(i).rjust(3)}| "
        for p in percentages:
            if p >= i:
                res += "o  "
            else:
                res += "   "
        res += "\n"
        
    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)
    
    for i in range(max_len):
        res += "     "
        for name in names:
            if i < len(name):
                res += name[i] + "  "
            else:
                res += "   "
        if i < max_len - 1:
            res += "\n"
            
    return res

** end of main.py **

