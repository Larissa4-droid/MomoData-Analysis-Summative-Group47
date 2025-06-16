from flask import Flask, render_template, request
import sqlite3
import plotly.graph_objs as go

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect("transactions.db")
    c = conn.cursor()

    # Get filters
    type_filter = request.args.get('type')
    date_filter = request.args.get('date')
    year_filter = request.args.get('year')
    month_year_filter = request.args.get('month_year')
    min_amt = request.args.get('min_amount')
    max_amt = request.args.get('max_amount')
    page = int(request.args.get('page', 1))
    per_page = 20
    offset = (page - 1) * per_page  # how many items to skip (based on current page).

    # Build dynamic query
    base_query = "FROM messages m JOIN categories c ON m.category_id = c.id"
    where_clause = []  # collect SQL filter conditions as strings.
    params = []  # collect the actual values to safely insert into the query (used with ? placeholders to prevent SQL injection).

    if type_filter:
        where_clause.append("c.category = ?")
        params.append(type_filter)
    if date_filter:
        where_clause.append("DATE(m.date) = ?")
        params.append(date_filter)  # Matches a specific date. The DATE() ensures the time portion is removed.
    if month_year_filter:
        where_clause.append("strftime('%Y-%m', m.date) = ?")
        params.append(month_year_filter)  # Matches something like "2025-06"
    if year_filter:
        where_clause.append("strftime('%Y', m.date) = ?")
        params.append(year_filter)
    if min_amt:
        where_clause.append("m.amount >= ?")
        params.append(min_amt)  # Filters messages with amount greater than or equal to min_amt
    if max_amt:
        where_clause.append("m.amount <= ?")
        params.append(max_amt)

    where_sql = " WHERE " + " AND ".join(where_clause) if where_clause else ""
    # Example of where_sql: WHERE c.category = ? AND m.amount >= ? AND strftime('%Y', m.date) = ?

    # Count total messages for pagination
    count_query = f"SELECT COUNT(*) {base_query} {where_sql}"
    c.execute(count_query, params)
    total_messages = c.fetchone()[0]  # fetchone() returns a tuple like (42,), so [0] extracts the number 42.
    total_pages = (total_messages + per_page - 1) // per_page

    # Retrieve paginated messages
    query = f'''SELECT m.*, c.category 
                {base_query} {where_sql} 
                ORDER BY m.date DESC 
                LIMIT ? OFFSET ?'''
    paginated_params = params + [per_page, offset]
    c.execute(query, paginated_params)
    messages = c.fetchall()

    # Chart data
    chart_query = f'''SELECT c.category, COUNT(*) 
                  {base_query} {where_sql}
                  GROUP BY c.category'''
    c.execute(chart_query, params)
    chart_data = c.fetchall()
    
    conn.close() # Close the connection to the database.

    categories = [r[0] for r in chart_data]  # Recuparate the list of categories.
    counts = [r[1] for r in chart_data]  # Recuparate the list counts of each category.
    selected_category = type_filter or None  # This is used to highlight the selected category in the chart.

    colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880']
    highlight_color = '#FFD700'

    # Create a pie chart
    pie = go.Figure(data=[go.Pie(
        labels=categories,
        values=counts,
        marker=dict(colors=[
            highlight_color if cat == selected_category else colors[i % len(colors)]
            for i, cat in enumerate(categories)
        ])
    )])

    pie.update_layout(
    title="Transactions by Type",
    height=300,
    margin=dict(t=40, b=20, l=20, r=20)
    )

    # Create a bar chart
    bar = go.Figure(data=[go.Bar(
        x=categories,
        y=counts,
        marker=dict(color=[
            highlight_color if cat == selected_category else colors[i % len(colors)]
            for i, cat in enumerate(categories)
        ])
    )])

    bar.update_layout(
    title="Transaction Volume per Category",
    xaxis_title="Category",
    yaxis_title="Count",
    height=300,
    margin=dict(t=40, b=40, l=40, r=20)
    )

    return render_template("index.html",
                           messages=messages,
                           total_messages=total_messages,
                           current_page=page,
                           total_pages=total_pages,
                           pie_chart=pie.to_html(full_html=False, include_plotlyjs=False),
                           bar_chart=bar.to_html(full_html=False, include_plotlyjs=False))
    
if __name__ == '__main__':
    app.run(debug=True)
