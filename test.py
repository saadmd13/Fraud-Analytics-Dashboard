from dashboard.api import get_random_fraud

x = get_random_fraud()

print(x["actual_class"])