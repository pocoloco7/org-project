from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd

app = Flask(__name__)

# Function to read data from Excel
def read_data():
    return pd.read_excel('data.xlsx')

# Function to save data to Excel
def save_data(df):
    df.to_excel('data.xlsx', index=False)

@app.route('/data')
def data():
    df = read_data()
    return df.to_html(classes='table table-striped', index=False)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        # Update data in Excel file
        file_path = "data.xlsx"
        df = pd.read_excel(file_path)
        # Check if the form is submitted for updating a single row or multiple rows
        if 'row_id' in request.form:
            # Update a single row
            row_id = int(request.form["row_id"])
            product_name = request.form["product_name"]
            quantity = int(request.form["quantity"])
            df.loc[row_id, "Product Name"] = product_name
            df.loc[row_id, "Quantity"] = quantity
        else:
            # Update multiple rows
            for index, _ in enumerate(df.index):
                df.loc[index, "Product Name"] = request.form[f"product_name_{index}"]
                df.loc[index, "Quantity"] = int(request.form[f"quantity_{index}"])
        save_data(df)
        return redirect(url_for('data'))
    df = read_data()
    return render_template('edit.html', data=df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
