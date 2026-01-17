from app import create_app

# Create the Flask app using factory pattern
app = create_app()

if __name__ == "__main__":
    # Run locally (Render will just use `app`)
    app.run(debug=True)
