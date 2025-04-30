# Table to create a sample table with txn_id and accm_txn_complete_time

import pandas as pd
from datetime import datetime, timedelta
import random

def generate_txn_table(n):
    base_time = datetime(2025, 4, 30, 8, 0, 0)  
    txn = []
    
    for i in range(n):
        random_minutes = random.randint(1, 60 * 48)  
        txn_time = base_time + timedelta(minutes=random_minutes)
        txn.append({
            'txn_id': i,
            'accm_txn_complete_time': txn_time.strftime('%Y-%m-%d %H:%M:%S')
        })

    return txn

txn_data = generate_txn_table(1370)

# Save to CSV
df = pd.DataFrame(txn_data)
df.to_csv("CSVs/txn.csv", index=False)
