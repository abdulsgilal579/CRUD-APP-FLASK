from website import create_app

app = create_app()
if __name__ == "__main__":
    # Run this block only when this file is executed directly, not when imported
    app.run(debug=False, port=5001)
    # You’re telling Flask to run in debug mode — and it enables two powerful features that are extremely helpful during development:
    # Auto-Reload on File Changes |  Interactive Error Pages (Debugger)
    # Keep deubg=False in production
