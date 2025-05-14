from flask import Flask, render_template, Response
import io
import seaborn as sns
import matplotlib.pyplot as plt
from mpg import df


app = Flask(__name__)

# Load the Auto MPG dataset
mpg_data = df

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to generate a bar chart
@app.route('/bar_chart.png')
def bar_chart():
    fig = plt.figure(figsize = (12, 4))
    sns.barplot(x='origin', y='horsepower', data=mpg_data, hue = "origin", estimator='mean', palette="Blues")
    plt.title("Average Horsepower by Origin")
    
    # Save the plot to a BytesIO object
    output = io.BytesIO()
    fig.savefig(output, format='png')
    plt.close(fig)
    output.seek(0)
    return Response(output.getvalue(), mimetype='image/png')

# Route to generate a scatter plot
@app.route('/scatter_plot.png')
def scatter_plot():
    fig = plt.figure(figsize = (12, 4))
    sns.scatterplot(x='weight', y='mpg', hue='origin', data=mpg_data,  palette="viridis")
    plt.title("MPG vs. Weight by Origin")
    
    output = io.BytesIO()
    fig.savefig(output, format='png')
    plt.close(fig)
    output.seek(0)
    return Response(output.getvalue(), mimetype='image/png')

# Route to generate a box plot
@app.route('/box_plot.png')
def box_plot():
    fig = plt.figure(figsize = (12, 4))
    sns.boxplot(x='origin', y='mpg', data=mpg_data, hue = "origin", palette="pastel")
    plt.title("MPG Distribution by Origin")
    
    output = io.BytesIO()
    fig.savefig(output, format='png')
    plt.close(fig)
    output.seek(0)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
