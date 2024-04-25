import React, { useState } from 'react';
import axios from 'axios';

const TextRandom = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [processedText, setProcessedText] = useState('');
    const [error, setError] = useState('');

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleSubmit = async () => {
        const formData = new FormData();
        setProcessedText('');
        formData.append('file', selectedFile);
        try {
            const response = await axios.post('http://localhost:8000/api/process_text/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            setProcessedText(response.data.processed_text);
            setError('');
        } catch (error) {
            console.error('Error uploading file: ', error);
            if (error.response) {
                setError(error.response.data['0'] || 'Server error occurred');
            } else {
                setError('Network error occurred');
            }
        }
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleSubmit}>Upload</button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {processedText && (
                <div style={{ whiteSpace: 'pre-line'}}>
                    <h3>Processed text</h3>
                    <p>{processedText}</p>
                </div>
            )}
        </div>
    );
};
        

export default TextRandom;