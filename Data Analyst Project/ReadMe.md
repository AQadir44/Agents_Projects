# Data Insights Bot: Your AI-Driven Analytics Assistant

Welcome to **Data Insights Bot**, an interactive tool powered by Streamlit that helps users quickly analyze datasets and derive insights through various statistical measures and visualizations. The bot is designed to be user-friendly, allowing you to upload your data and get immediate insights with minimal effort.

## Features

- **File Upload**: Upload your CSV dataset and let the bot handle the rest.
- **Data Preview**: View the first few rows of your dataset to understand its structure.
- **Basic Statistics**: Get a quick summary of your data with key statistics like mean, median, and standard deviation.
- **Visualizations**: Select columns to generate visualizations such as bar charts, and view a correlation heatmap.
- **AI-driven Insights**: The bot offers recommendations for further analysis or steps based on the data type.

## Prerequisites

Before running the **Data Insights Bot**, make sure you have the following dependencies installed:

- Python 3.7 or later
- Streamlit
- Pandas
- Seaborn (for the heatmap visualization)
- Matplotlib (for plotting)
- Langchain
- Gemini



## How to Use

1. **Clone the Repository**:
   Clone this repository to your local machine using:
   
   ```bash
   git clone https://github.com/yourusername/data-insights-bot.git
   ```
2. **Create a Virtual Environment**:
   Create a virtual environment
   ```bash
    python -m venv venv
    ```
   Activate the virtual environment
    ```bash
    venv\Scripts\activate
    ```
4. **Install Dependencies**
    To install the necessary dependencies, run the following command:
    
    ```bash
    pip install -r requirements.txt
    ```



5. **Run the Application**:
   Navigate to the project directory and run the Streamlit app with the following command:
   
   ```bash
   streamlit run app.py
   ```

3. **Interact with the Bot**:
   Once the app is running, open your browser and go to `http://localhost:8501`. You can:
   - Upload a CSV file for analysis.
   - View the data preview.
   - Generate basic statistics.
   - Visualize columns and view correlations.
   - Ask questions

## Customizing the Bot

Feel free to customize the bot by modifying the following sections:

- **Data Analysis**: Extend the bot to support more types of analyses, like regression, clustering, or time-series forecasting.
- **Visualizations**: Add more plot options, like histograms, line charts, or scatter plots.
- **Insights**: Implement AI-based recommendations based on data patterns.

## Example

### Upload a CSV:
1. Click on the **Upload CSV file** button.
2. Choose your CSV file, for example, `sales_data.csv`.

### View Basic Statistics:
Once uploaded, the bot will generate a summary of the dataset, showing statistics like:

- Mean
- Median
- Min & Max values
- Standard Deviation

### Visualize the Data:
Select a column from your dataset, and the bot will generate a bar chart showing the frequency of different values.

If you'd like, you can also view a correlation heatmap to better understand relationships between numeric columns.

## Contributing

If you'd like to contribute to this project, feel free to fork this repository and create a pull request with your improvements. You can improve the bot's capabilities by:

- Adding more statistical analysis methods.
- Improving the visualizations.
- Enhancing the user interface.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or need further assistance, please feel free to reach out:

- Email: [aqsamoizlakhani@gmail.com](mailto:aqsamoizlakhani@gmail.com)

---

Thank you for using **Data Insights Bot**! We hope it helps you gain valuable insights from your data with ease.


