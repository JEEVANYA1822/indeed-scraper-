from apify_client import ApifyClient
import pandas as pd

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_h1qDprWBeWlgkWTRauMLqaEZGWbRU43C76rh")

# Prepare the Actor input
run_input = {
    "position": "python developer",
    "country": "IN",
    "location": "chennai",
    "maxItems": 5,
    "parseCompanyDetails": True,
    "saveOnlyUniqueItems": True,
    "followApplyRedirects": True,
}

try:
    # Run the Actor and wait for it to finish
    run = client.actor("hMvNSpz3JnHgl5jkh").call(run_input=run_input)

    # Fetch results from the run's dataset
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    # Check if there are any items
    if items:
        # Create a DataFrame
        df = pd.DataFrame(items)
        
        # Save to Excel
        df.to_excel("job_results.xlsx", index=False)
        print("Results saved to job_results.xlsx")
    else:
        print("No items found.")

except Exception as e:
    print(f"An error occurred: {e}")