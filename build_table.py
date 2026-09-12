import os
import pandas as pd

excel_file = "data.xlsx"

# Check if spreadsheet exists
if not os.path.exists(excel_file):
    print(f"❌ Error: Cannot find '{excel_file}' in this folder. Make sure your spreadsheet is named data.xlsx")
    exit()

try:
    # Read the first worksheet tab
    df = pd.read_excel(excel_file)
except Exception as e:
    print(f"❌ Error reading Excel file: {e}")
    exit()

headers = df.columns.tolist()
rows = df.values.tolist()

# Generate HTML with native CSS styling, including the unblockable local script visitor counter
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>League Standings</title>
    <!-- Importing modern Inter font -->
    <link rel="preconnect" href="https://googleapis.com">
    <link rel="preconnect" href="https://gstatic.com" crossorigin>
    <link href="https://googleapis.com/css2?family=Inter:wght@400;500;600;700;900&display=swap" rel="stylesheet">
    
    <style>
        /* Base page layout */
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #f8fafc;
            color: #334155;
            margin: 0;
            padding: 40px 20px;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }}

        /* Centered page wrap container */
        .page-container {{
            width: 100%;
            max-width: 800px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        /* Clean header style */
        header {{
            width: 100%;
            text-align: center;
            background-color: #ffffff;
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
            border: 1px solid #e2e8f0;
            margin-bottom: 24px;
            box-sizing: border-box;
        }}

        header h1 {{
            margin: 0;
            font-size: 28px;
            font-weight: 900;
            color: #0f172a;
            letter-spacing: -0.5px;
        }}

        /* Table structural wrap box */
        .table-wrapper {{
            width: 100%;
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
            border: 2px solid #cbd5e1;
            overflow: hidden;
            margin-bottom: 24px;
        }}

        .scroll-box {{
            overflow-x: auto;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 14px;
        }}

        /* Table header titles cell style */
        th {{
            background-color: #f1f5f9;
            color: #475569;
            font-weight: 800;
            text-transform: uppercase;
            font-size: 12px;
            letter-spacing: 0.5px;
            padding: 16px;
            border-right: 1px solid #cbd5e1;
            border-bottom: 2px solid #cbd5e1;
            text-align: center;
        }}

        /* Table team body data cell grids */
        td {{
            padding: 14px 16px;
            color: #475569;
            font-weight: 500;
            border-right: 1px solid #e2e8f0;
            border-bottom: 1px solid #e2e8f0;
            white-space: nowrap;
        }}

        /* Remove the final floating right border line on the last columns */
        th:last-child, td:last-child {{
            border-right: none;
        }}

        /* Bold the team name text column exclusively */
        .team-cell {{
            font-weight: 700;
            color: #0f172a;
            background-color: #f8fafc;
        }}
        
        .center-cell {{
            text-align: center;
        }}

        /* Add a nice hover trace row effect for regular rows */
        tr:hover {{
            background-color: #f1f5f9;
        }}

        /* Distinct styling variables for the #1 League Leader row */
        .leader-row {{
            background-color: #fef08a !important;
        }}

        .leader-team {{
            font-weight: 900 !important;
            color: #713f12 !important;
            background-color: #fef9c3 !important;
        }}

        .leader-stats {{
            font-weight: 700 !important;
            color: #713f12 !important;
        }}

        /* Style for the local unblockable visual counter pill */
        .counter-badge {{
            display: inline-flex;
            align-items: center;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            border-radius: 4px;
            overflow: hidden;
            border: 1px solid #475569;
        }}
        .counter-label {{
            background-color: #1e293b;
            color: #ffffff;
            padding: 4px 8px;
        }}
        .counter-value {{
            background-color: #22c55e;
            color: #ffffff;
            padding: 4px 8px;
        }}
    </style>
</head>
<body>

    <div class="page-container">
        <header>
            <h1>🏆 LEAGUE TABLE</h1>
        </header>

        <div class="table-wrapper">
            <div class="scroll-box">
                <table>
                    <thead>
                        <tr>
"""

# Append headers
for header in headers:
    html_content += f'                            <th>{header}</th>\n'

html_content += """                        </tr>
                    </thead>
                    <tbody>
"""

# Append team rows with conditional leader check
for idx, row in enumerate(rows):
    if idx == 0:
        html_content += '                        <tr class="leader-row">\n'
        for cell_idx, cell in enumerate(row):
            val = str(cell) if pd.notna(cell) else ""
            if cell_idx == 0:
                html_content += f'                            <td class="team-cell leader-team">⭐ {val}</td>\n'
            else:
                html_content += f'                            <td class="center-cell leader-stats">{val}</td>\n'
        html_content += '                        </tr>\n'
    else:
        html_content += '                        <tr>\n'
        for cell_idx, cell in enumerate(row):
            val = str(cell) if pd.notna(cell) else ""
            if cell_idx == 0:
                html_content += f'                            <td class="team-cell">{val}</td>\n'
            else:
                html_content += f'                            <td class="center-cell">{val}</td>\n'
        html_content += '                        </tr>\n'

html_content += """                    </tbody>
                </table>
            </div>
        </div>

        <!-- VISITOR COUNTER FOOTER -->
        <footer style="margin-top: 20px;">
            <div class="counter-badge">
                <span class="counter-label">Visits</span>
                <span class="counter-value" id="visit_count">1</span>
            </div>
        </footer>

    </div>

    <!-- NATIVE TRACKING CODE: Increments views automatically locally without using the internet -->
    <script>
        window.addEventListener('DOMContentLoaded', () => {{
            let currentCount = localStorage.getItem('league_table_views');
            if (currentCount === null) {{
                currentCount = 1;
            }} else {{
                currentCount = parseInt(currentCount) + 1;
            }}
            localStorage.setItem('league_table_views', currentCount);
            document.getElementById('visit_count').textContent = currentCount;
        }});
    </script>

</body>
</html>
"""

# Save out the finished file right inside the folder
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("🏆 Success! Generated with a native, completely unblockable counter badge.")
