# Importing libraries
from TikTokApi import TikTokApi as tiktok
import json
import pandas as pd
import numpy as np

# Import data processing helper
from helpers import process_results

# Get cookie data to setup instance
verifyFp = "verify_kzalnn0z_L1R14y9X_NHri_4HW2_8qF7_3cqeUuiEJnRb"
# Setup instance
print("testing code")
api = tiktok.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

# Get data by hashtag
trending = api.by_hashtag("crypto")

# Process data
flattened_data = process_results(trending)

print(pd.DataFrame.from_dict(flattened_data, orient="index"))


# Export to json
# with open("/mnt/c/Users/JOSE/Documents/PROJECT/streamlit_tiktok/python_dump.json", "w") as f:
#     json.dump(trending, f)