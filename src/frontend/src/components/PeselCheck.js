import React, { useState } from 'react';
import axios from 'axios';

const PeselValidator = () => {
    const [pesel, setPesel] = useState('');
    const [validationResult, setValidationResult] = useState('');

    const handlePeselChange = (event) => {
        setPesel(event.target.value);
    };

    const handleSubmit = async () => {
        try {
            const response = await axios.post('http://localhost:8000/api/validate-pesel/', { pesel });
            setValidationResult(response.data);
        } catch (error) {
            console.log('Error validating PESEL: ', error);
        }
    };

    return (
        <div>
            <input type="text" value={pesel} onChange={handlePeselChange} />
            <button onClick={handleSubmit}>Validate</button>
            {validationResult && (
                <div>
                <p>{validationResult.message}</p>
                {validationResult.gender && (
                    <p>Pleć: {validationResult.gender}</p>
                )}
                {validationResult.birth_date && (
                    <p>Data urodzenia: {validationResult.birth_date}</p>
                )}
                </div>
            )}
        </div>
    );
};

export default PeselValidator;