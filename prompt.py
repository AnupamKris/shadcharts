"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    system_instruction="The user gives you the meta data about a csv file and you are required to give the exact python code to get that data. All the data are to be used to plot charts using the a special plotting library\n\nconvert the data for bar chart into the format [{ 'category1': '...', 'category2', '...', ..., name: '<the xaxis label>'}, {...}]\nconvert the data for pie chart into the format [{name: '<category name>' , value: ...}, ...]\n\nreturn format \n{\n \"existing_code\" : `\nimport pandas as pd\ndata = pd.read_csv('data.csv')\n`,\n\"generated_code\" : \"<fill this with your code to get the required data>\",\n\"output_var\" : \"<fill with the name of the variable where the output is stored after running generated code>\",\n}",
)

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "# dataframe info\n<class 'pandas.core.frame.DataFrame'>\nRangeIndex: 1000 entries, 0 to 999\nData columns (total 17 columns):\nColumn Non-Null Count Dtype\n0 Invoice ID 1000 non-null object\n1 Branch 1000 non-null object\n2 City 1000 non-null object\n3 Customer type 1000 non-null object\n4 Gender 1000 non-null object\n5 Product line 1000 non-null object\n6 Unit price 1000 non-null float64\n7 Quantity 1000 non-null int64\n8 Tax 5% 1000 non-null float64\n9 Total 1000 non-null float64\n10 Date 1000 non-null object\n11 Time 1000 non-null object\n12 Payment 1000 non-null object\n13 cogs 1000 non-null float64\n14 gross margin percentage 1000 non-null float64\n15 gross income 1000 non-null float64\n16 Rating 1000 non-null float64\ndtypes: float64(7), int64(1), object(9)\n\n# data.head()\nInvoice ID Branch City Customer type Gender Product line Unit price Quantity Tax 5% Total Date Time Payment cogs gross margin percentage gross income Rating\n0 750-67-8428 A Yangon Member Female Health and beauty 74.69 7 26.1415 548.9715 1/5/2019 13:08 Ewallet 522.83 4.761905 26.1415 9.1\n1 226-31-3081 C Naypyitaw Normal Female Electronic accessories 15.28 5 3.8200 80.2200 3/8/2019 10:29 Cash 76.40 4.761905 3.8200 9.6\n2 631-41-3108 A Yangon Normal Male Home and lifestyle 46.33 7 16.2155 340.5255 3/3/2019 13:23 Credit card 324.31 4.761905 16.2155 7.4\n3 123-19-1176 A Yangon Member Male Health and beauty 58.22 8 23.2880 489.0480 1/27/2019 20:33 Ewallet 465.76 4.761905 23.2880 8.4\n4 373-73-7910 A Yangon Normal Male Sports and travel 86.31 7 30.2085 634.3785 2/8/2019 10:37 Ewallet 604.17 4.761905 30.2085 5.3\n\n- required data\nunits sold per month in each category for a barchart",
            ],
        },
        {
            "role": "model",
            "parts": [
                "```python\n{\n \"existing_code\" : \"\\nimport pandas as pd\\ndata = pd.read_csv('data.csv')\\n\",\n \"generated_code\" : \"data['Date'] = pd.to_datetime(data['Date'])\\ndata['Month'] = data['Date'].dt.strftime('%Y-%m') \\nunits_sold_per_month = data.groupby(['Month', 'Product line'])['Quantity'].sum().reset_index()\\nbarchart_data = []\\nfor month in units_sold_per_month['Month'].unique():\\n    month_data = units_sold_per_month[units_sold_per_month['Month'] == month].set_index('Product line')['Quantity'].to_dict()\\n    month_data['name'] = month\\n    barchart_data.append(month_data)\\n\",\n \"output_var\" : \"barchart_data\"\n}\n```",
            ],
        },
        {
            "role": "user",
            "parts": [
                "- required data\ntotal sales by city for pie chart",
            ],
        },
        {
            "role": "model",
            "parts": [
                "```python\n{\n \"existing_code\" : \"\\nimport pandas as pd\\ndata = pd.read_csv('data.csv')\\n\",\n \"generated_code\" : \"city_sales = data.groupby('City')['Total'].sum().reset_index()\\npiechart_data = [{'name': row['City'], 'value': row['Total']} for _, row in city_sales.iterrows()]\\n\",\n \"output_var\" : \"piechart_data\"\n}\n```\n",
            ],
        },
        {
            "role": "user",
            "parts": [
                "- required data\ntotal sales per day for each city for a bar chart",
            ],
        },
        {
            "role": "model",
            "parts": [
                "```python\n{\n \"existing_code\" : \"\\nimport pandas as pd\\ndata = pd.read_csv('data.csv')\\n\",\n \"generated_code\" : \"data['Date'] = pd.to_datetime(data['Date'])\\nsales_per_day_city = data.groupby(['Date', 'City'])['Total'].sum().reset_index()\\nbarchart_data = []\\nfor day in sales_per_day_city['Date'].unique():\\n    day_data = sales_per_day_city[sales_per_day_city['Date'] == day].set_index('City')['Total'].to_dict()\\n    day_data['name'] = str(day.date())\\n    barchart_data.append(day_data)\\n\",\n \"output_var\" : \"barchart_data\"\n}\n```\n",
            ],
        },
    ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)
