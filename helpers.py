
# Convert processing code to function
def process_results(data):

    nested_values = ["video", "author", "music", "stats", "authorStats", 
                "challenges", "duetInfo", "textExtra", "stickersOnItem"]
    skip_values = ["challenges", "duetInfo", "textExtra", "stickersOnItem"]

    # Store data which is already flattened
    flattened_data = {}

    # Iterate through all to get nested into more flattened
    for idx, value in enumerate(data):
        
        # Intialized dictionary for each ID (numbered json item)
        flattened_data[idx] = {}
        
        for prop_idx, prop_value  in value.items():
            
            # If in nested value, we need to expand
            if prop_idx in nested_values:
                
                # Check if we need to skip it
                if prop_idx in skip_values:
                    pass
                else:
                    # Loop to each nested propeerty in value
                    for nested_idx, nested_value in prop_value.items():
                        flattened_data[idx][prop_idx +"_"+nested_idx] = nested_value
            
            # It not nested value, simply add to already flattened data
            else:
                flattened_data[idx][prop_idx] = prop_value

    return flattened_data