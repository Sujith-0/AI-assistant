
from flask import Flask, request, jsonify
from rag import get_rag_response

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get("message", "")
    response = get_rag_response(query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
