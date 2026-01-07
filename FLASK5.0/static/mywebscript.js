document.getElementById('analyzeBtn').addEventListener('click', async () => {
    const text = document.getElementById('textInput').value.trim();
    const resultDiv = document.getElementById('result');
    const loadingSpinner = document.getElementById('loading');

    resultDiv.innerHTML = '';
    loadingSpinner.style.display = 'block';

    if (!text) {
        loadingSpinner.style.display = 'none';
        resultDiv.innerHTML = '<div class="alert alert-warning">Please enter some text to analyze.</div>';
        return;
    }

    try {
        const response = await fetch('/emotion', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        });

        loadingSpinner.style.display = 'none';

        if (!response.ok) {
            throw new Error('Server error');
        }

        const data = await response.json();

        const emojiMap = {
            'SENT_POSITIVE': '😊',
            'SENT_NEGATIVE': '😠',
            'SENT_NEUTRAL': '😐'
        };

        const emoji = emojiMap[data.label] || '🤔';

        resultDiv.innerHTML = `
            <div class="alert alert-info">
                <strong>Emotion:</strong> ${data.label} ${emoji}<br>
                <strong>Confidence:</strong> ${data.score.toFixed(2)}
            </div>
        `;
    } catch (error) {
        loadingSpinner.style.display = 'none';
        resultDiv.innerHTML = '<div class="alert alert-danger">Error analyzing emotion. Please try again.</div>';
        console.error(error);
    }
});