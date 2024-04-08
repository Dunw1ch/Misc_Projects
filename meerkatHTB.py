import json

def parse_json_to_txt(file_path):
    try:
        # Opening JSON file
        with open(file_path) as f:
            # returns JSON object as a dictionary or list
            data = json.load(f)

        # Create a new text file to write the parsed JSON data
        with open('parsed_data.txt', 'w') as outfile:
            # Handling the case where data is a list
            if isinstance(data, list):
                for entry in data:
                    write_entry_to_file(entry, outfile)
            # Handling the case where data is a dictionary
            elif isinstance(data, dict):
                write_entry_to_file(data, outfile)

        print("Parsed JSON data successfully written to parsed_data.txt")
    except FileNotFoundError:
        print("File not found:", file_path)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)

def write_entry_to_file(entry, outfile):
    # Writing parsed JSON data to the text file
    outfile.write("Timestamp: " + entry.get('ts', 'N/A') + '\n')
    outfile.write("Event type: " + entry.get('event_type', 'N/A') + '\n')
    outfile.write("Source IP: " + entry.get('src_ip', 'N/A') + '\n')
    outfile.write("Source port: " + str(entry.get('src_port', 'N/A')) + '\n')
    outfile.write("Destination IP: " + entry.get('dest_ip', 'N/A') + '\n')
    outfile.write("Destination port: " + str(entry.get('dest_port', 'N/A')) + '\n')
    outfile.write("Protocol: " + entry.get('proto', 'N/A') + '\n')
    
    # Check if 'alert' key exists in entry and contains required fields
    if 'alert' in entry and isinstance(entry['alert'], dict):
        alert = entry['alert']
        outfile.write("Severity: " + str(alert.get('severity', 'N/A')) + '\n')
        outfile.write("Signature: " + alert.get('signature', 'N/A') + '\n')
        outfile.write("Category: " + alert.get('category', 'N/A') + '\n')
        outfile.write("Action: " + alert.get('action', 'N/A') + '\n')
        outfile.write("Signature ID: " + str(alert.get('signature_id', 'N/A')) + '\n')
        outfile.write("GID: " + str(alert.get('gid', 'N/A')) + '\n')
        outfile.write("Revision: " + str(alert.get('rev', 'N/A')) + '\n')
        
        # Check if 'metadata' key exists in 'alert' and contains 'tag' field
        if 'metadata' in alert and isinstance(alert['metadata'], dict):
            # Ensure 'tag' is iterable before joining
            tag_value = alert['metadata'].get('tag')
            if tag_value is not None:
                if isinstance(tag_value, (list, tuple)):
                    outfile.write("Tag: " + ', '.join(tag_value) + '\n')
                else:
                    outfile.write("Tag: " + str(tag_value) + '\n')
            else:
                outfile.write("Tag: N/A\n")
        else:
            outfile.write("Tag: N/A\n")
    else:
        outfile.write("Severity: N/A\n")
        outfile.write("Signature: N/A\n")
        outfile.write("Category: N/A\n")
        outfile.write("Action: N/A\n")
        outfile.write("Signature ID: N/A\n")
        outfile.write("GID: N/A\n")
        outfile.write("Revision: N/A\n")
        outfile.write("Tag: N/A\n")

# Absolute path to the JSON file
file_path = 'C:/Users/Admin/Desktop/meerkat-alerts.json'

# Call the function to parse JSON and write to text file
parse_json_to_txt(file_path)