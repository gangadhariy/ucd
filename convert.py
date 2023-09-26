import json

# Update the file path to point to /opt/trivy_scan_pretty.json
file_path = '/opt/trivy_scan_pretty.json'

# Load JSON data from the specified file path
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)

# Define an HTML template with custom CSS styles
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Trivy Scan Report</title>
    <style>
        /* Add your custom CSS styles here */
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }}
        h1 {{
            color: #007bff;
            background-color: #f4f4f4;
            padding: 20px;
            text-align: center;
        }}
        table {{
            width: 100%;
            max-width: 80%;
            margin: 20px auto;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            border-collapse: collapse;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #007bff;
            color: white;
        }}
        /* Custom styles for even columns and odd rows */
        tr:nth-child(odd) {{
            background-color: #f2f2f2;
        }}
        td:nth-child(even) {{
            background-color: #ffcccb; /* Light Red */
            color: #000; /* Black text on the light red background */
            font-weight: bold;
        }}
        /* Add a horizontal scrollbar */
        .table-container {{
            overflow-x: auto;
        }}
        /* Add more custom styles as needed */
    </style>
</head>
<body>
    <h1>Trivy Scan Report</h1>
    <div class="table-container">
        <table>
            <tr>
                <th>Header 1</th>
                <th>Header 2</th>
                <!-- Add more headers as needed -->
            </tr>
            {{" ".join([f"<tr><td>{key}</td><td>{value}</td></tr>" for key, value in json_data.items()])}}
        </table>
    </div>
</body>
</html>
"""

# Save the complete HTML report to a file
with open('/tmp/trivy_scan.html', 'w') as html_file:
    html_file.write(html_template)

print("Conversion complete. The HTML report is saved as '/tmp/trivy_scan.html'.")
