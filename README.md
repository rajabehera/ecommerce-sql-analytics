# E-commerce SQL Analytics

Practice SQL analytics on a deliberately messy e-commerce dataset,
using PostgreSQL in Docker.

## Run it
1. pip install faker
2. python data/generate.py
3. docker compose up -d
4. Load schema and data (see commands below)

## Dataset
- 5,000 customers (about 5% missing emails)
- about 51,000 orders (about 1,000 duplicates, inconsistent status values)

## Plan
Week 1: aggregations, joins, cleaning. Week 2: CTEs, window
functions, indexes, star schema.