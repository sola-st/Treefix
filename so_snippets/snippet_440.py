# Extracted from https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
    @app.route("/summary")
    def summary():
        responseBody = { "message": "bla bla bla", "summary": make_summary() }
        return make_response(jsonify(responseBody), 200)

