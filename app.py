from flask import Flask, jsonify
from datetime import datetime
import time

app = Flask(__name__)

# Store the start time for uptime calculation
start_time = time.time()

# Sample data
reviews_data = [
    {"book": "1984", "review": "A chilling dystopia", "rating": 5},
    {"book": "The Hobbit", "review": "A delightful adventure", "rating": 4}
]

@app.route('/')
def welcome():
    """Welcome endpoint"""
    return jsonify({
        "service": "BookReview API",
        "version": "1.0",
        "message": "Welcome to the BookReview service!"
    })

@app.route('/reviews', methods=['GET'])
def get_reviews():
    """Get all reviews"""
    return jsonify({
        "reviews": reviews_data,
        "count": len(reviews_data)
    })

@app.route('/status')
def health_check():
    """Health check endpoint"""
    uptime_seconds = time.time() - start_time
    hours = int(uptime_seconds // 3600)
    minutes = int((uptime_seconds % 3600) // 60)
    
    return jsonify({
        "status": "healthy",
        "uptime": f"{hours} hours {minutes} minutes",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)