import csv, random
from faker import Faker
fake = Faker("en_IN"); Faker.seed(42); random.seed(42)

with open("data/customers.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["customer_id", "name", "email", "city", "signup_date"])
    for i in range(1, 5001):
        email = fake.email() if random.random() > 0.05 else ""
        w.writerow([i, fake.name(), email, fake.city(),
                    fake.date_between("-2y", "today")])

rows = []
for oid in range(1, 50001):
    status = random.choice(["completed", "Completed ", "CANCELLED", "returned"])
    rows.append([oid, random.randint(1, 5000),
                 fake.date_between("-1y", "today"),
                 round(random.uniform(5, 500), 2), status])
rows += random.sample(rows, 1000)

with open("data/orders.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["order_id", "customer_id", "order_date", "amount", "status"])
    w.writerows(rows)